"""
Create and show a Pandas dataframe and text table fromt the JSON response for all endpoints.
TODO
"""

import click

from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from . click_options import opt_call_databricks_model_serving
from . import get_endpoints


def show(output_file_base, call_databricks_model_serving=False):
    endpoints = get_endpoints(call_databricks_model_serving)

    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(f"{output_file_base}_endpoints", endpoints, [], ts_columns)

    ts_columns = [ "ep_creation_timestamp", "ep_last_updated_timestamp" ]
    for mdef in _model_defs:
        models = mdef["func"](endpoints)
        base = f"{output_file_base}_{mdef['prefix']}"
        io_utils.write_csv_and_json_files(base, models, [], ts_columns)


def mk_all_entities(endpoints):
    def mk_models(ep):
        config = ep.get("config", {})
        served_entities = config.get("served_entities", [])
        return [ { **_mk_ep(ep),  **ent} for ent in served_entities ]
    return _mk_models(endpoints, mk_models)


def mk_custom_models(endpoints):
    def mk_models(ep):
        config = ep.get("config", {})
        served_models = config.get("served_models", [])
        return [ { **_mk_ep(ep),  **mdl} for mdl in served_models if "FEATURE_SPEC" != mdl.get("type") ]
    return _mk_models(endpoints, mk_models)

def mk_feature_spec_models(endpoints):
    def mk_models(ep):
        config = ep.get("config", {})
        served_models = config.get("served_models", [])
        return [ { **_mk_ep(ep),  **mdl} for mdl in served_models if "FEATURE_SPEC" == mdl.get("type") ]
    return _mk_models(endpoints, mk_models)

def mk_foundation_models(endpoints):
    def mk_models(ep):
        config = ep.get("config", {})
        keys = [ "entity_name", "name", "display_name", "price" ]
        served_entities = config.get("served_entities", [])
        def mk_row(ep, ent, keys):
            return { **_mk_ep(ep), **_rename(ent.get("foundation_model"), keys, "fm")}
        return [ mk_row(ep, ent, keys) for ent in served_entities if "FOUNDATION_MODEL" == ent.get("type")]
    return _mk_models(endpoints, mk_models)

def mk_external_models(endpoints):
    def mk_models(ep):
        config = ep.get("config", {})
        served_entities = config.get("served_entities", [])
        def mk_row(ep, ent):
            dct = { "entity_name": ent["name"] }
            em = ent.get("external_model")
            return { **_mk_ep(ep),  **dct, **em }
        return [ mk_row(ep, ent) for ent in served_entities if "EXTERNAL_MODEL" == ent.get("type")]
    return _mk_models(endpoints, mk_models)

def mk_pending_models(endpoints):
    def mk_models(ep):
        pending_config = ep.get("pending_config", {})
        served_models = pending_config.get("served_models",[])
        return [ { **_mk_ep(ep),  **dct} for dct in served_models]
    return _mk_models(endpoints, mk_models)


def _mk_models(endpoints, func):
    return [x for ep in endpoints for x in func(ep)]


def _rename(dct, keys, prefix):
    def rename(k, prefix):
        return f"{prefix}_{k}"
    return { rename(k,prefix):v for k,v in dct.items() if k in keys }

def _mk_ep(ep):
    keys = ["name", "creator", "creation_timestamp", "last_updated_timestamp", "state" ]
    return _rename(ep, keys, "ep")


_model_defs = [
    { "func": mk_all_entities, "prefix": "entities" },
    { "func": mk_custom_models, "prefix": "custom" },
    { "func": mk_feature_spec_models, "prefix": "feature_spec" },
    { "func": mk_foundation_models, "prefix": "foundation" },
    { "func": mk_external_models, "prefix": "external" },
    { "func": mk_pending_models, "prefix": "pending" }
]


@click.command()
@opt_output_file_base
@opt_call_databricks_model_serving
def main(output_file_base, call_databricks_model_serving):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    show(output_file_base, call_databricks_model_serving)

if __name__ == "__main__":
    main()
