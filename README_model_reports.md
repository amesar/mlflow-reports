# MLflow Model Reports


## Overview

**TLDR**
* Commands to generate MLflow model reports based upon the [MLmodel](https://www.mlflow.org/docs/latest/models.html#fields-in-the-mlmodel-format) file.
* Keywords: model cards, model governance, model lineage, model auditing, regualted industries.
* This work was inspired by a similar effort from the Databricks Industry Solutions - Financial Services project:
  * [Model Risk Management, a true accelerator to corporate AI](https://www.databricks.com/blog/model-risk-management-true-accelerator-corporate-ai) - blog - 2023-05-23
  * https://github.com/databricks-industry-solutions/fsi-mrm-generation

**Features**
* Provides a comprehensive view of an entire MLflow model.
* Handles all standard MLflow model schemes such as `models:/`, `runs:/` or `dbfs:/`.
* Generates a markdown model report file
* Saves (optional) a JSON file representing all the data used to build the report.
* Handles varying kinds of MLflow models - feature store models, AutoML models, both notebook and workspace experiments and models run as jobs.

**Future enhancements**
* Create an executive summary report as well as other views for different stakeholders (C-suite, ML data scientists, MLOps staff, 3rd party regulators).
* Generate other representations of a model report such as PDF and HTML.
* Develop abstraction of higher-level data structure to represent the entire model graph so rendering can work from this instead of raw API calls to lower-level objects.
* Persist model reports and the accompanying JSON data files. This creates a point-in-time snapshot for model governance purposes.
* Integrate better with Databricks Feature Store data lineage. Dependent upon a public Feature Store API.
* Integrate fully with Databricks Unity Catalog model features.
* Integrate with Databricks Unity Catalog data lineage features.

## Model Report Samples 

| Model | Markdown | JSON | MLmodel |  Note
|-------|----------|------|---|--|
| credit_adjudication | [link](samples/databricks/model_reports/credit_adjudication/report.md) | [link](samples/databricks/model_reports/credit_adjudication/report.json) | [link](samples/databricks/model_reports/credit_adjudication/MLmodel) | Git Repo notebook experiment |
| credit_adjudication (UC)| [link](samples/databricks/model_reports/credit_adjudication/uc_report.md) | [link](samples/databricks/model_reports/credit_adjudication/uc_report.json) |  | Unity Catalog model
| dolly3b | [link](samples/databricks/model_reports/dolly3b/report.md) | [link](samples/databricks/model_reports/dolly3b/report.json) | [link](samples/databricks/model_reports/dolly3b/MLmodel) | LLM, Notebook experiment
| hugging-face-transformers-batch-nlp | [link](samples/databricks/model_reports/hugging-face-transformers-batch-nlp/report.md) | [link](samples/databricks/model_reports/hugging-face-transformers-batch-nlp/report.json) | [link](samples/databricks/model_reports/hugging-face-transformers-batch-nlp/MLmodel) | LLM, Notebook experiment
| Sklearn_Wine_ONNX_ws | [link](samples/databricks/model_reports/Sklearn_Wine_ONNX_ws/report.md) | [link](samples/databricks/model_reports/Sklearn_Wine_ONNX_ws/report.json) | [link](samples/databricks/model_reports/Sklearn_Wine_ONNX_ws/MLmodel) | Workspace experiment  
| Sklearn_Wine_AutoML | [link](samples/databricks/model_reports/AutoML_Wine_2023_05_21/report.md) | [link](samples/databricks/model_reports/AutoML_Wine_2023_05_21/report.json) | [link](samples/databricks/model_reports/AutoML_Wine_2023_05_21/MLmodel) | AutoML experiment
| Sklearn_Wine_Feature_Store | [link](samples/databricks/model_reports/Sklearn_Wine_FS_ws/report.md) | [link](samples/databricks/model_reports/Sklearn_Wine_FS_ws/report.json) | [link](samples/databricks/model_reports/Sklearn_Wine_FS_ws) | Feature Store model
| cv_pytorch_final | [link](samples/databricks/model_reports/cv_pytorch_final/report.md) | [link](samples/databricks/model_reports/cv_pytorch_final/report.json) | [link](samples/databricks/model_reports/cv_pytorch_final/MLmodel) | Job experiment

## Report structure

* Model Overview
* MLflow Model
  * Details
  * Signature
* Saved input example info
* Registered Model
  * Details
  * Tags
  * Permissions
* Registered Model Version
  * Details
  * Tags
* Run
  * Info
  * Params
  * Metrics
  * Inputs
  * Tags
* Experiment
  * Details
  * Tags
  * Permissions

## MLflow Model Report Command

Builds a detailed report of an MLflow model and all its related object in markdown format.

The `model-uri` can be any legal MLflow scheme:
* models:/credit_adjudication/3
* models:/credit_adjudication/production
* runs:/76031d22c5464dd99431e426b939e800/model

Download URIs:
* run model - dbfs:/databricks/mlflow-registry/417e414731e74e03b731fb3a63a3b4e4/models/model
* registry model - dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model

In addition a customer data scheme is available to load from a JSON file:
* data:/credit_adjudication.json

**Example**

_Standard_
```
mlflow-model-report \
  --model-uri models:/credit_adjudication/3
  --output-file credit_adjudication.md \
  --output-data-file credit_adjudication.json
```
```
wc -l credit_adjudication.*

541 credit_adjudication.json
403 credit_adjudication.md
```

_Load from file_
```
mlflow-model-report \
  --model-uri data:/dbfs:/model_archives/2023-05-04/credit_adjudication/prod/data.json \
  --output-file credit_adjudication.md
```

**Usage**

```
mlflow-model-report --help

Options:
Options:
  --model-uri TEXT           Model URI such as 'models:/my-model/123' or
                             'runs:/123/my-model'.  [required]
  --show-as-json BOOLEAN     Show as JSON selected fields  [default: False]
  --show-manifest BOOLEAN    Show manifest stanza  [default: False]
  --output-file TEXT         JSON output file.
  --output-data-file TEXT    Output JSON data file
  --get-permissions BOOLEAN  Get Databricks permissions.  [default: False]
```
