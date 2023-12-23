## Model Version `Sklearn_Wine_best` notes

#### Unity Catalog Model Registry
* [uc_model_version.json](uc_model_version.json) - workspace experiment
* [uc_model_version_notebook_experiment.json](uc_model_version_notebook_experiment.json) - notebook experiment permission fails with 400
* [raw/uc_model_version.json](raw/uc_model_version.json) - as returned by API with no enrichments

#### Workspace Model Registry
* [ws_model_version.json](ws_model_version.json) - bug with (MLflow 2.8.1): no stage transitions as `transition-requests/list` incorrectly returns an empty list
* [ws_model_version_with_transitions.json](ws_model_version_with_transitions.json) - has transitions as expected
* [raw/ws_model_version.json](raw/ws_model_version.json) - as returned by API with no enrichments

Last updated: 2023-12-22
