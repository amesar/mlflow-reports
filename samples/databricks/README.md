# Samples

## MLflow Model Reports

Top-level directory of [model_reports](model_reports).

### Non-Unity Catalog Reports

* [credit_adjudication](model_reports/credit_adjudication) - Canonical credit model
* [Sklearn_Wine_ONNX_ws](model_reports/Sklearn_Wine_ONNX_ws) - Two models (Sklearn and ONNX) in one run
* [Sklearn_Wine_FS_ws](model_reports/Sklearn_Wine_FS_ws) - Feature Store model
* [AutoML_Wine_2023_05_21](model_reports/AutoML_Wine_2023_05_21) - AutoML model
* [cv_pytorch_final](model_reports/cv_pytorch_final) - PyTorch job


### Unity Catalog Reports

* [andre.ml_models.credit_adjudication](model_reports/credit_adjudication)
* [andre.ml_models2.sklearn_wine_best](model_reports/sklearn_wine_best/uc)
* [andre.ml_models2.dolly3b](model_reports/unity_catalog/dolly3b)
* [andre.transformer_models.Conversational_Task](model_reports/transformers/Conversational_Task/uc)

### Transformer Model Reports

Hugging Face model reports (non-UC).

| Model JSON sample | Hugging Face Task | Hugging Face Model | Model GB|
|-----|-----|-------|---|
| [Text_to_Text_Generation_Task](model_reports/transformers/Text_to_Text_Generation_Task) | [text2text-generation](https://huggingface.co/tasks/text-generation) | [declare-lab/flan-alpaca-base](https://huggingface.co/declare-lab/flan-alpaca-base) | 1.092 |
| [Translation_Task](model_reports/transformers/Translation_Task) | [translation_en_to_fr](https://huggingface.co/tasks/translation) | [t5-small](https://huggingface.co/t5-small) |  0.245 |
| [Conversational_Task](model_reports/transformers/Conversational_Task) | [conversational](https://huggingface.co/tasks/conversational) | [microsoft/DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium) | 1.654 |
| [Feature_Extraction_Task](model_reports/transformers/Feature_Extraction_Task) | [feature-extraction](https://huggingface.co/tasks/feature-extraction) | [sentence-transformers/all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) | 0.134 |
| [Speech_Recognition_Task](model_reports/transformers/Speech_Recognition_Task) | [automatic-speech-recognition](https://huggingface.co/tasks/automatic-speech-recognition) | [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) |  0.154 |
| [hugging-face-transformers-batch-nlp](model_reports/transformers/hugging-face-transformers-batch-nlp) | [summarization](https://huggingface.co/tasks/summarization) | [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | 1.636 |
| [dolly3b](model_reports/transformers/dolly3b) | [text-generation](https://huggingface.co/tasks/text-generation) | [databricks/dolly-v2-3b](https://huggingface.co/databricks/dolly-v2-3b) |  11.239 |
| [dbdemos_pcb_classification](dbdemos_pcb_classification) | [image-classification](https://huggingface.co/tasks/image-classification) | [vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) | .343 |


## MLflow Objects

Top-level directory of [mlflow_objects](mlflow_objects).

### Basic

**MLflow objects**
* [registered_models](mlflow_objects/registered_models)
* [experiments](mlflow_objects/experiments)
* [runs](mlflow_objects/runs)

**Model Versions**
* [model_versions](mlflow_objects/model_versions)
* [Llama2-7B](mlflow_objects/model_versions/llama2_7b.json)

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
| UC Model Version| [enriched json](mlflow_objects/model_versions/credit_adjudication/uc_model_version.json) | [raw json](mlflow_objects/model_versions/credit_adjudication/raw/uc_model_version.json) 
| Non-UC Model Version| [enriched json](mlflow_objects/model_versions/credit_adjudication/ws_model_version.json) | [raw json](mlflow_objects/model_versions/credit_adjudication/raw/ws_model_version.json)
| Non-UC Registered Model | [enriched json](mlflow_objects/registered_models/credit_adjudication.json) | [raw json](mlflow_objects/registered_models/raw/credit_adjudication.json) |
| Run | [enriched json](mlflow_objects/runs/credit_adjudication/run.json) | [raw json](mlflow_objects/runs/credit_adjudication/run_raw.json) |
| Experiment | [enriched json](mlflow_objects/experiments/credit_adjudication.json) | [raw json](mlflow_objects/experiments/raw/credit_adjudication.json) |


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

