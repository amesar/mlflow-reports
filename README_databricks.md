# Databricks Object Tools

## Overview

Python scripts and [Databricks notebooks](databricks_notebooks/README.md) to display and list some Databricks objects.

Last updated: _2024-05-20.

## Summary

#### Model Serving Endpoints
*  [get-model-serving-endpoint](#get-model-serving-endpoint) - get model serving endpoint
*  [list-model-serving-endpoints](#list-model-serving-endpoints) - list model serving endpoints

#### Vector Search - TODO
*  [list-vector-search-endpoints](#list-model-serving-endpoints) - list vector search endpoints
*  [get-vector-search-endpoint](#get-vector-search-endpoint)

#### Feature Store
*  [list-feature-tables](#list-feature-tables) - list feature tables (non-UC "Feature Store" instead of UC "Feature Engineering")


## Model Serving Endpoints

### Get Model Serving Endpoint 

Get Databricks model serving endpoint details.

```
get-model-serving-endpoint \
  --endpoint sklearn_wine_best \
  --openapi True \
  --output-file sklearn_wine_best.json
```
```
{
  "name": "sklearn_wine_best",
  "creator": "andre@my-company.com",
  "creation_timestamp": 1706467706000,
  "last_updated_timestamp": 1706467706000,
  "state": {
    "ready": "READY",
    "config_update": "NOT_UPDATING"
  },
  "config": {
    "served_entities": [
      {
        "name": "Sklearn_Wine_best-2",
        "entity_name": "Sklearn_Wine_best",
        "entity_version": "2",
        "workload_size": "Small",
        "scale_to_zero_enabled": true,
        "workload_type": "CPU",
        "state": {
          "deployment": "DEPLOYMENT_READY",
          "deployment_state_message": "Scaled to zero"
        },
        "creator": "andre@my-company.com",
        "creation_timestamp": 1706467706000,
        "_creation_timestamp": "2024-01-28 18:48:26"
      }
    ],
    "traffic_config": {
      "routes": [
        {
          "served_model_name": "Sklearn_Wine_best-2",
```

##### Usage

```
get-model-serving-endpoint --help

Options:
  --endpoint TEXT                 Model serving endpoint name.
  --openapi BOOLEAN               Get endpoint OpenAPI schema and append it to
                                  the output JSON.
  --use-deployment-client BOOLEAN
                                  Databricks only. Use
                                  DatabricksDeploymentClient. Otherwise, make
                                  direct calls to 'api/2.0/serving-endpoints'.
  --get-raw BOOLEAN               Preserve raw JSON as received from API call.
                                  [default: False]
  --output-file TEXT              JSON output file.
  --silent BOOLEAN                Do not display to stdout.  [default: False]
  --expand-model-version [none|version|version-and-signature|version-all]
                                  Model type: version|version-and-
                                  signature|version-all
```

### List Model Serving Endpoints

List Databricks model serving endpoints.

```
list-model-serving-endpoints \
  --columns name,endpoint_type,task,creator,creation_timestamp \
  --output-base endpoints
```

```
| name                             | endpoint_type        | task               | creator                 | creation_timestamp   |
|----------------------------------|----------------------|--------------------|-------------------------|----------------------|
| embeddings_proxy_eo              |                      |                    | amelia@mycompany.com    | 2023-11-22 18:36:33  |
| eo_rfp_rag                       |                      |                    | amelia@mycompany.com    | 2023-11-22 19:00:33  |
| databricks-llama-2-70b-chat      | FOUNDATION_MODEL_API | llm/v1/chat        |                         | 2023-11-10 09:53:20  |
| databricks-mixtral-8x7b-instruct | FOUNDATION_MODEL_API | llm/v1/chat        |                         | 2023-11-10 09:53:20  |
| databricks-bge-large-en          | FOUNDATION_MODEL_API | llm/v1/embeddings  |                         | 2023-11-10 09:53:20  |
| databricks-mpt-30b-instruct      | FOUNDATION_MODEL_API | llm/v1/completions |                         | 2023-11-10 09:53:20  |
| databricks-mpt-7b-instruct       | FOUNDATION_MODEL_API | llm/v1/completions |                         | 2023-11-10 09:53:20  |
| openai-completions-endpoint      | EXERNAL_MODEL        | llm/v1/completions | k1.denali@mycompany.com | 2024-05-10 19:03:00  |
```

##### Usage
```
Options:
  --model-type [all|custom|foundation|external]
                                  Model type: all|custom|foundation|external
  --openapi BOOLEAN               Write OpenAPI schema for all endpoints to
                                  file '{output-file-base}_opena[i.json'.
  --columns TEXT                  Columns to display. Comma delimited.
  --output-file-base TEXT         File base for JSON and CSV output files. For
                                  example, 'out' will result in 'out.csv' and
                                  'out.json.'  [default: out]
  --use-deployment-client BOOLEAN
                                  Databricks only. Use
                                  DatabricksDeploymentClient. Otherwise, make
                                  direct calls to 'api/2.0/serving-endpoints'.
  --get-raw BOOLEAN               Preserve raw JSON as received from API call.
                                  [default: False]
  --get-details BOOLEAN           Get details of each listed object.
  --normalize-pandas-df BOOLEAN   Convert JSON list with pd.json_normalize,
                                  otherwise use pd.DataFrame.
```


# =========== OLD XXX

## Feature Store 

### List Feature Store Tables

List feature tables (non-UC "Feature Store" instead of UC "Feature Engineering").

```
list-feature-tables \
  --columns name,primary_keys,features,creation_timestamp,creator_id
```

```
| name                                                              | primary_keys                       | features                                                                                                                                                                               | creation_timestamp   | creator_id                  |
|-------------------------------------------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------|
| andre_fs_wine.wine_features                                       | ['wine_id']                        | ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity', 'wine_id'] | 2023-11-16 11:22:54  | amelia.singer@mycompany.com |
| andre_fs_wine.wine_static_features                                | ['wine_id']                        | ['chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity', 'wine_id']            | 2023-05-29 02:49:42  | amelia.singer@mycompany.com |
| dbdemos_fs_travel_shared.destination_features_advanced            | ['destination_id']                 | ['destination_id', 'sum_clicks_7d', 'sum_impressions_7d', 'ts']                                                                                                                        | 2023-08-14 16:58:07  | amelia.singer@mycompany.com |
| travel_recommendations_realtime.destination_availability_features | ['destination_id', 'booking_date'] | ['availability', 'booking_date', 'destination_id', 'event_ts', 'name', 'price']                                                                                                        | 2022-10-31 18:42:57  | samaim.amisam@mycompany.com |
| travel_recommendations_realtime.destination_location_features     | ['destination_id']                 | ['destination_id', 'latitude', 'longitude', 'name']                                                                                                                                    | 2022-10-31 18:18:19  | samaim.amisam@mycompany.com |
| travel_recommendations_realtime.destination_popularity_features   | ['destination_id']                 | ['destination_id', 'sum_clicks_7d', 'sum_impressions_7d', 'ts']                                                                                                                        | 2022-10-31 20:09:12  | samaim.amisam@mycompany.com |
```

```
Options:
  --columns TEXT          Columns to display. Comma delimited.
  --output-csv-file TEXT  Output CSV file.
```



