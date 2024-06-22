"""
Test get latest model version and get latest run.
"""

from mlflow_reports.common.model_version_utils import get_latest_model_version
from . test_http_iterators import _create_versions


def test_search_versions_order_by_version():
    model_names = _create_versions(1, 2)
    latest_vr = get_latest_model_version(model_names[0])
    assert latest_vr
    assert latest_vr["version"] == "2"

