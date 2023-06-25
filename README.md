# mlflow-reports

Reporting tools for MLflow.

Command line scripts to retrieve objects from the MLflow API.


## Setup 

##### Step 1. Create a virtual environment.
```
python -m venv mlflow-reports
source mlflow-reports/bin/activate
```

##### Step 2. pip install

pip install from github
```
pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports
```

or pip install in editable mode
```
git clone https://github.com/amesar/mlflow-reports
cd mlflow-reports
pip install -e .
```

## Commands

### Get run

Get run details.
* Source: [get_run.py](mlflow_reports/data/get_run.py).
* Shows info, params, metrics and tags of a run.
* Recursively lists run artifacts up to the specified level.

**Example**

```
get-run
  --run-id 4af184e8527a4f4a8fc563386807acb2 \
  --artifact-max-level 5
```

```
{
  "run": {
    "info": {
      "experiment_id": "2",
      "run_name": "all_options",
      "user_id": "andre",
      "status": "FINISHED",
      "start_time": 1687205142417,
      "end_time": 1687205147505,
      "_start_time": "2023-06-19 20:05:42",
      "_end_time": "2023-06-19 20:05:48",
      "_duration": 5.088
. . .
```

**Usage**

```
get-run --help

Options:
Options:
  --run-id TEXT                 Run ID  [required]
  --artifact-max-level INTEGER  Number of artifact levels to recurse for run
                                artifacts.  [default: 1]
  --dump-raw BOOLEAN            Show raw JSON as received from API call.
                                Ignore all other options.  [default: False]
  --silent BOOLEAN              Do not display to stdout.  [default: False]
  --output-file TEXT            JSON output file.
```

## Samples

Run samples:
 * [run.json](samples/open_source/run/run.json) and [run_raw.json](samples/open_source/run/run_raw.json)
