from setuptools import setup, find_packages

setup(
    name="mlflow_reports",
    version="1.0.0",
    author="Andre Mesarovic",
    description="MLflow Report Tools",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/amesar/mlflow-reports",
    project_urls={
        "Bug Tracker": "https://github.com/amesar/mlflow-reports/issues",
        "Documentation": "https://github.com/amesar/mlflow-reports/",
        "Source Code": "https://github.com/amesar/mlflow-reports/"
    },
    python_requires = ">=3.8",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    install_requires=[
        "mlflow-skinny[databricks]>=2.12.2",
        "mlflow[genai]",
        "databricks-vectorsearch",
        "databricks-cli",
        "pandas>=2.0.3",
        "mdutils",
        "wheel"
    ],
    extras_require= { 
        "tests": [ "mlflow", "pytest","pytest-html>=3.2.0", "shortuuid>=1.0.11" ],
        "streamlit": [ "streamlit" ]
    },
    license = "Apache License 2.0",
    keywords = "mlflow ml ai",
    classifiers = [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    entry_points = {
        "console_scripts": [
            "mlflow-model-report = mlflow_reports.markdown.detailed_report:main",
            "get-run = mlflow_reports.data.get_run:main",
            "get-experiment = mlflow_reports.data.get_experiment:main",
            "get-model-version = mlflow_reports.data.get_model_version:main",
            "get-registered-model = mlflow_reports.data.get_registered_model:main",
            "get-mlflow-model = mlflow_reports.data.get_mlflow_model:main",
            "get-mlflow-model-wide = mlflow_reports.mlflow_model.mlflow_model_manager:main",
            "list-registered-models = mlflow_reports.list.list_registered_models:main",
            "list-model-versions = mlflow_reports.list.list_model_versions:main",
            "list-model-serving-endpoints = mlflow_reports.model_serving.list_endpoints:main",
            "list-artifacts= mlflow_reports.tools.list_artifacts:main",
            "list-vector-search-endpoints = mlflow_reports.vector_search.list_endpoints:main",
            "list-feature-tables = mlflow_reports.feature_store.list_feature_tables:main",
            "get-list-model-serving-endpoint = mlflow_reports.model_serving.get_endpoint:main"
        ]
    }
)
