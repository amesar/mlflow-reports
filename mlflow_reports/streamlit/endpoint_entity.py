import copy
import streamlit as st
from mlflow_reports.model_serving import get_endpoint
from mlflow_reports.data import get_model_version
from mlflow_reports.mlflow_model.mlflow_model_utils import get_model_artifact
from mlflow_reports.common.timestamp_utils import now
from mlflow_reports.common import explode_utils


def do_model_serving_endpoint_entity():
    def refresh(endpoint_name, entity_name):
        if not endpoint_name:
            return { "error": "Missing model serving endpoint name" }, None, None, None
        endpoint = get_endpoint.get(endpoint_name)
        entity = get_entity(endpoint, entity_name)
        entity_name = entity.get("name")
        st.write(f"Retrieved entity _{endpoint_name}/{entity_name}_ at {now()}")
        st.session_state.entity = entity
        if entity:
            vr, signature, mlmodel = _get_model_version(entity)
            return entity, vr, signature, mlmodel
        else:
            msg = { "error": "Cannot find entity", "endpoint_name": endpoint_name, "entity_name": entity_name, "endpoint": endpoint }
            return msg, None, None, None

    entity = st.session_state.entity if "entity" in st.session_state else None
    vr, signature, mlmodel = None, None, None
    #help = "Custom model entity"
    #st.subheader("_Endpoint entity (model) details_", help=help)

    endpoint_name = st.text_input("Endpoint", key="endpoint_name_2", help="Model serving endpoint")
    entity_name = st.text_input("Entity (model)", key="entity_name", help="Model serving endpoint entity. If empty will return the first entity.")

    if st.button("Refresh", key="refresh_entity"):
        entity, vr, signature, mlmodel = refresh(endpoint_name, entity_name)

    tab_entity, tab_version, tab_signature, tab_mlmodel  = st.tabs(["Entity", "Model version", "Model signature", "MLmodel"])

    if entity:
        with tab_entity:
            st.write(entity)
        with tab_version:
            st.write(vr)
        with tab_signature:
            st.write(signature)
        with tab_mlmodel:
            st.write(mlmodel)

def get_entity(endpoint, entity_name=None):
    config = endpoint.get("config", {})
    entities = config.get("served_entities", [])

    if entity_name:
        for ent in entities:
            if entity_name == ent["name"]:
                return ent
        return None
    else:
        return entities[0] if entities else None


def _get_model_version(entity):
    name =  entity.get("entity_name")
    version =  entity.get("entity_version")
    if not version:
        return None
    vr = get_model_version.get(name,version)

    model_uri = f"models:/{name}/{version}"
    mlmodel = get_model_artifact(model_uri, "MLmodel", file_type="yaml", explode_json=False)

    signature = copy.deepcopy(mlmodel.get("signature"))
    explode_utils.explode_json(signature)

    return vr, signature, mlmodel
