from mlflow_reports.markdown.local_utils import escape_dict
from mlflow_reports.markdown.widget_factory import (
     WidgetFactory,
     TAG_COLUMNS,
     NOT_FOUND
)


class ReportFactory:
    def __init__(self, card):
        self.card = card
        self.wf = WidgetFactory(card)

    # =====
    # ModelInfo widgets

    def build_signature(self, sig, level=2):
        def _mk_inputs(sig):
            inputs = sig.get("inputs")
            columns = [ "Column", "Type" ]
            data = [ [ x.get("name"), x.get("type") ] for  x in inputs ]
            self.wf.mk_table(columns, data, "Inputs", level=level+1)

        def _mk_outputs(sig):
            outputs = sig.get("outputs")
            columns = [ "Type name", "Type value" ]
            data = [ [ x.get("type"), x.get("tensor-spec") ] for  x in outputs ]
            self.wf.mk_table(columns, data, "Outputs", level=level+1)

        self.card.new_header(level=level, title="Signature")
        if not sig:
            self.card.new_line(NOT_FOUND)
            return False
        _mk_inputs(sig)
        _mk_outputs(sig)
        return True

    def build_saved_input_example_info(self, example, level):
        title = "Saved input example info"
        if example:
            self.wf.build_table(example, title, level)
        else:
            self.wf.mk_not_present_header(title, level)
        return example is not None

    def build_flavors(self, flavors, level, show_as_json=False):
        self.card.new_header(level=level, title="Flavors")
        if show_as_json:
            for k,v in flavors.items():
                self.card.new_header(level=level+1, title=f"Flavor '{k}'")
                self.card.new_line(escape_dict(v))
        else:
            for k,v in flavors.items():
                self.wf.build_table(v, f"Flavor '{k}'", level+1)


    # ====
    # Run widgets

    def build_sparkDatasourceInfo(self, ds_info, level):
        title = "Spark Datasources"
        if not ds_info:
            self.wf.mk_not_present_header(title, level)
            return
        data = []
        for x in ds_info:
            data.append([ x.get("format"), x.get("version",""), x.get("path") ])
        columns = ["Format", "Version", "Path" ]
        self.wf.mk_table(columns, data, "Spark Datasources", level=level)

    def build_inputs(self, run, level):
        inputs = run.get("inputs")
        self.card.new_header(level=level, title="Inputs")
        if not inputs:
            self.mk_not_present()
            return False

        dataset_inputs = inputs.get("dataset_inputs")
        for x in dataset_inputs:
            self._build_dataset_input(x, level+1)
        return True

    def _build_dataset_input(self, dataset_input, level):
        dataset = dataset_input.get("dataset")
        name = dataset.get("name")
        self.card.new_header(level=level, title=f"Dataset Input '{name}'")

        schema = dataset.pop("schema",None)
        profile = dataset.pop("profile")
        dataset["profile_num_rows"] = profile["num_rows"]
        dataset["profile_num_elements"] = profile["num_elements"]

        self.wf.build_table(dataset, "Dataset Info", level=level+1)

        colspec = schema.get("mlflow_colspec")
        columns = [ "Column", "Type" ]
        data = [ [ x.get("name"), x.get("type") ] for  x in colspec ]
        self.wf.mk_table(columns, data, "Schema", level=level+1)


    # =====
    # Cluster tag widgets

    def build_cluster_stuff(self, tags, level):

        def build_cluster_info(tags, level):
            cluster_id = tags.get("mlflow.databricks.cluster.id")
            if cluster_id:
                dct = tags.get("mlflow.databricks.cluster.info")
                dct = { **{"cluster_id": cluster_id}, **dct }
                self.wf.build_table(dct, "Cluster Info", level=level, **TAG_COLUMNS)

        def build_cluster_libraries(tags, level):
            def _parse_libs(libs):
                dct = {}
                for x in libs:
                    k = list(x.keys())[0]
                    v = x.get(k)
                    dct[k] = v
                return dct
            def _build_libs(cluster_libs, lib_name):
                libs = cluster_libs.get(lib_name)
                if libs:
                    dct = _parse_libs(libs)
                    self.wf.build_table(dct, f"{lib_name.capitalize()} Libraries", level+1)

            self.card.new_header(level=level, title="Cluster Libraries")
            cluster_libs = tags.get("mlflow.databricks.cluster.libraries")
            if cluster_libs:
                _build_libs(cluster_libs, "installable")
                _build_libs(cluster_libs, "redacted")
            cluster_libs_error = tags.get("mlflow.databricks.cluster.libraries.error")
            if cluster_libs_error:
                self.card.new_line(escape_dict(cluster_libs_error))


        if tags.get("mlflow.databricks.cluster.id"):
            build_cluster_info(tags, level)
            build_cluster_libraries(tags, level)


    # =====
    # Permission widgets

    def build_permissions(self, permissions, level):
        if permissions:
            self.card.new_header(level=level, title="Permissions")
            self.card.new_line(escape_dict(permissions))
        else:
            #pass
            self.wf.mk_not_present_header("Permissions", level)

