"""
Write one set of JSON and CSV files for each of the different model serving endpoint entity types.

See: /api/2.0/serving-endpoints
https://docs.databricks.com/api/workspace/servingendpoints/list
"""

import os
import json
import click
import pandas as pd
from tabulate import tabulate

from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_dir, opt_silent
from . click_options import opt_call_databricks_model_serving, opt_input_file
from . import get_endpoints, get_entities, filter_entities
from . import FOUNDATION_MODEL, EXTERNAL_MODEL, FEATURE_SPEC


def show(output_dir, call_databricks_model_serving, input_file, silent):
    if input_file:
        print(f"Using file '{input_file}' instead of calling '/api/2.0/serving-endpoints'")
        with open(input_file, "r", encoding="utf-8") as f:
            endpoints = json.load(f)
    else:
        endpoints = get_endpoints(call_databricks_model_serving)

    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    base = os.path.join(output_dir, "all_endpoints")
    io_utils.write_csv_and_json_files(base, endpoints, [], ts_columns, silent=silent)

    ts_columns = [ "ep_creation_timestamp", "ep_last_updated_timestamp" ]
    for hdlr in _entity_type_handlers:
        entities = hdlr["func"](endpoints)
        base = os.path.join(output_dir, f"{hdlr['prefix']}_entities")
        if entities:
            io_utils.write_csv_and_json_files(base, entities, [], ts_columns, silent=silent)

    report(endpoints)


def mk_all_entities(endpoints):
    def mk_models(ep):
        return [ { **_mk_ep(ep),  **ent} for ent in get_entities(ep) ]
    return _mk_models(endpoints, mk_models)


def mk_custom_models(endpoints):
    def mk_models(ep):
        return [ { **_mk_ep(ep),  **ent} for ent in get_entities(ep) if not ent.get("type") ]
    return _mk_models(endpoints, mk_models)

def mk_feature_spec_models(endpoints):
    def mk_models(ep):
        return [ { **_mk_ep(ep),  **ent} for ent in filter_entities(get_entities(ep), FEATURE_SPEC) ]
    return _mk_models(endpoints, mk_models)

def mk_foundation_models(endpoints):
    def mk_models(ep):
        def mk_row(ep, ent, keys):
            return { **_mk_ep(ep), **_rename(ent.get("foundation_model"), keys, "fm")}
        keys = [ "entity_name", "name", "display_name", "price" ]
        return [ mk_row(ep, ent, keys) for ent in filter_entities(get_entities(ep), FOUNDATION_MODEL) ]
    return _mk_models(endpoints, mk_models)

def mk_external_models(endpoints):
    def mk_models(ep):
        def mk_row(ep, ent):
            dct = { "entity_name": ent["name"] }
            em = ent.get("external_model")
            return { **_mk_ep(ep),  **dct, **em }
        return [ mk_row(ep, ent) for ent in filter_entities(get_entities(ep), EXTERNAL_MODEL) ]
    return _mk_models(endpoints, mk_models)

def mk_pending_models(endpoints):
    def mk_models(ep):
        pending_config = ep.get("pending_config", {})
        entities = pending_config.get("served_entities",[])
        return [ { **_mk_ep(ep),  **dct} for dct in entities]
    return _mk_models(endpoints, mk_models)


def _mk_models(endpoints, func):
    return [x for ep in endpoints for x in func(ep)]


def _mk_ep(ep):
    keys = ["name", "creator", "creation_timestamp", "last_updated_timestamp", "state" ]
    return _rename(ep, keys, "ep")

def _rename(dct, keys, prefix):
    def rename(k, prefix):
        return f"{prefix}_{k}"
    return { rename(k,prefix):v for k,v in dct.items() if k in keys }


_entity_type_handlers = [
    { "func": mk_all_entities, "prefix": "all" },
    { "func": mk_custom_models, "prefix": "custom" },
    { "func": mk_feature_spec_models, "prefix": "feature_spec" },
    { "func": mk_foundation_models, "prefix": "foundation" },
    { "func": mk_external_models, "prefix": "external" },
    { "func": mk_pending_models, "prefix": "pending" }
]

def report(endpoints):
    print(f"\nFound {len(endpoints)} endpoints")
    entities, map = [], {}
    for ep in endpoints:
        config = ep.get("config", {})
        _entities = config.get("served_entities", [])
        num_entities = len(_entities)
        #if num_entities != 1:
            #print(f">> #entities {num_entities}: {ep['name']}")
        map[num_entities] = map.get(num_entities,0) + 1
        entities.extend(_entities)
    print(f"Found {len(entities)} entities")
    lst = [ (k,v)  for k,v in map.items() ]
    df = pd.DataFrame(lst, columns = ["Entity Count","Endpoints"])
    print(tabulate(df, headers="keys", tablefmt="psql", numalign="right", showindex=False))

    map = {}
    for ent in entities:
        etype = ent.get("type")
        map[etype] = map.get(etype,0) + 1
    print("\nEntity type count")
    lst = [ (k,v)  for k,v in map.items() ]
    df = pd.DataFrame(lst, columns = ["Type","Count"])
    df = df.sort_values(by=["Count"], ascending=False)
    print(tabulate(df, headers="keys", tablefmt="psql", numalign="right", showindex=False))


@click.command()
@opt_output_dir
@opt_call_databricks_model_serving
@opt_input_file
@opt_silent

def main(output_dir, call_databricks_model_serving, input_file, silent):
    """
Write a tuple of files (JSON and CSV) for each of the different model serving endpoint entity types.
Each file tuple (except 'all_endpoints.json/csv') is an 'opinionated' unrolling of select nested fields since
an entity is a polymorphic object (with some common fields) with different fields per entity/model type.
For example, a custom model has different fields from a foundation model.

\b
Output files are:

\b
  - all_endpoints.json - Original JSON from get endpoints API call
  - all_entities.json - Unrolled entities of all endpoints
  - custom_entities.json - Custom models
  - external_entities.json - External models
  - feature_spec_entities.json - Feature Spec 
  - foundation_entities.json - Foundation models
    """

    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    show(output_dir, call_databricks_model_serving, input_file, silent)

if __name__ == "__main__":
    main()
