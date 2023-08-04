# Samples

## MLflow Model Reports

[model_reports](model_reports)

### Non-Unity Catalog Reports

* [credit_adjudication](model_reports/credit_adjudication) - Canonical credit model
* [Sklearn_Wine_ONNX_ws](model_reports/Sklearn_Wine_ONNX_ws) - Two models (Sklearn and ONNX) in one run
* [Sklearn_Wine_FS_ws](model_reports/Sklearn_Wine_FS_ws) - Feature Store model
* [AutoML_Wine_2023_05_21](model_reports/AutoML_Wine_2023_05_21) - AutoML model
* [cv_pytorch_final](model_reports/cv_pytorch_final) - PyTorch job

**LLMs**
  * [dolly3b](model_reports/dolly3b) - Dolly
  * [hugging-face-transformers-batch-nlp](model_reports/hugging-face-transformers-batch-nlp) - HugginFace
  * [Conversational_Task](model_reports/transformers/Conversational_Task)

### Unity Catalog Reports

* [andre.ml_models.credit_adjudication](model_reports/credit_adjudication)
* [andre.ml_models2.sklearn_wine_best](model_reports/sklearn_wine_best/uc)
* [andre.ml_models2.dolly3b](model_reports/unity_catalog/dolly3b)
* [andre.transformer_models.Conversational_Task](model_reports/transformers/Conversational_Task/uc)

## MLflow Objects

[mlflow_objects](mlflow_objects)

### Basic

**MLflow objects**
* [registered_models](mlflow_objects/registered_models)
* [model_versions](mlflow_objects/model_versions)
* [experiments](mlflow_objects/experiments)
* [runs](mlflow_objects/runs)

**MLflow models**
* [mlflow_models](mlflow_objects/mlflow_models)
* [mlflow_models_wide](mlflow_objects/mlflow_models_wide)

### Unity Catalog

* [registered_models](mlflow_objects/registered_models/uc/Sklearn_Wine_best.json)


### Raw JSON

* [registered_models](mlflow_objects/registered_models/raw)
* [model_versions](mlflow_objects/model_versions/raw)
* [experiments](mlflow_objects/experiments/raw)
* [mlflow_objects](mlflow_objects/runs/raw)


## Featured MLflow Models

### Model: credit_adjudication 

_**MLflow Model Report**_

| Model Report | Markdown | JSON |
|-----|-------|---|
| non-UC| [report.md](model_reports/credit_adjudication/report.md) | [report.json](model_reports/credit_adjudication/report.json) |
| UC | [report.md](model_reports/credit_adjudication/uc/report.md) | [report.json](model_reports/credit_adjudication/uc/report.json) |
| MLmodel | | [MLmodel](model_reports/credit_adjudication/MLmodel) |


_**MLflow Objects**_
| Object | Enriched | Original |
|-----|-------|---|
| Run | [enriched json](mlflow_objects/runs/credit_adjudication/run.json) | [raw json](mlflow_objects/runs/credit_adjudication/run_raw.json) |
| Experiment | [enriched json](mlflow_objects/experiments/credit_adjudication.json) | [raw json](mlflow_objects/experiments/raw/credit_adjudication.json) |
| Registered Model | [enriched json](mlflow_objects/registered_models/credit_adjudication.json) | [raw json](mlflow_objects/registered_models/raw/credit_adjudication.json) |
| Model Version| [enriched json](mlflow_objects/model_versions/credit_adjudication.json) | [raw json](mlflow_objects/model_versions/raw/credit_adjudication.json) |
| UC Model Version| [enriched json](mlflow_objects/model_versions/uc/credit_adjudication.json) | [raw json](mlflow_objects/model_versions/raw/uc_credit_adjudication.json) |


### Model: Sklearn_Wine_best

_**MLflow Model Report**_

| Model Report | Markdown | JSON |
|-----|-------|---|
| non-UC| [report.md](model_reports/Sklearn_Wine_best/report.md) | [report.json](model_reports/Sklearn_Wine_best/report.json) |
| UC | [report.md](model_reports/Sklearn_Wine_best/uc/report.md) | [report.json](model_reports/Sklearn_Wine_best/uc/report.json) |
| MLmodel | | [MLmodel](mlflow_objects/runs/Sklearn_Wine_best/MLmodel) |

_**MLflow Objects**_
| Object | Enriched | Original |
|-----|-------|---|
| Run | [enriched json](mlflow_objects/runs/Sklearn_Wine_best/run.json) | [raw json](mlflow_objects/runs/Sklearn_Wine_best/run_raw.json) |
| Experiment | [enriched json](mlflow_objects/experiments/Sklearn_Wine_best.json) | [raw json](mlflow_objects/experiments/raw/Sklearn_Wine_best.json) |
| Registered Model | [enriched json](mlflow_objects/registered_models/Sklearn_Wine_best.json) | [raw json](mlflow_objects/registered_models/raw/Sklearn_Wine_best.json) |
| Model Version | [enriched json](mlflow_objects/model_versions/Sklearn_Wine_best/model_version.json) | [raw json](mlflow_objects/model_versions/Sklearn_Wine_best/raw/model_version.json) |
| UC Model Version | [enriched json](mlflow_objects/model_versions/Sklearn_Wine_best/uc_model_version.json) | [raw json](mlflow_objects/model_versions/Sklearn_Wine_best/raw/uc_model_version.json) |

