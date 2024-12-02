# README  - Databricks notebooks

## Overview

These notebooks correspond to command line scripts described here:
* [MLflow model reports](../README_model_reports.md)
* [MLflow object retrieval](../README_objects.md)

MLflow Model reports notebooks
* [Detailed_Model_Report](reports/Detailed_Model_Report.py)
* [Summary_Report](reports/Summary_Report.py) - WIP

MLflow object dump notebooks
* [MLflow_Model_Manager](objects/MLflow_Model_Manager.py)
* [Get_MLflow_Model](objects/Get_MLflow_Model.py)
* [Get_Registered_Model](objects/Get_Registered_Model.py)
* [Get_Model_Version](objects/Get_Model_Version.py)
* [Get_Experiment](objects/Get_Experiment.py)
* [Get_Run](objects/Get_Run.py)

## Installing notebooks into Databricks workspace

You can import the notebooks into Databricks in two ways:
* As a workspace folder 
* As a Git Repo folder

### Import directory as Databricks workspace folder

See the [Workspace CLI](https://docs.databricks.com/dev-tools/cli/workspace-cli.html).
```
git clone https://github.com/amesar/mlflow-reports

databricks workspace import_dir \
  databricks_notebooks \
  /Users/me@mycompany.com/mlflow-reports
```

### Clone directory as Databricks Git Repo

You can load a Git Repo either through the Databricks UI or via the command line.

#### 1. Load through Databricks UI

See [Clone a Git Repo & other common Git operations](https://docs.databricks.com/repos/git-operations-with-repos.html).

#### 2. Load from command line with cUrl

Note it's best to use the curl version since the CLI doesn't appear to support the sparse checkout option.

```
curl \
  https://my.company.com/api/2.0/repos \
  -H "Authorization: Bearer MY_TOKEN" \
  -X POST \
  -d ' {
    "url": "https://github.com/amesar/mlflow-reports",
    "provider": "gitHub",
    "path": "/Repos/me@my.company.com/mlflow-reports",
    "sparse_checkout": {
      "patterns": [ "databricks_notebooks" ]
      }
    }'
```

