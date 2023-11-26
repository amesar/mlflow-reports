from mlflow.exceptions import RestException
from mlflow_reports.common import MlflowReportsException

def to_dict(e, msg, error_category="error"):
    if isinstance(e, MlflowReportsException):
        return to_MlflowReportsException(e, msg, error_category)
    elif isinstance(e, RestException):
        return to_RestException_dict(e, msg, error_category)
    else:
        return to_Exception_dict(e, msg, error_category)


def to_MlflowReportsException(e, msg, error_category):
    return {
        error_category: {
            "message": msg,
            "MlflowReportsException": e.error
        }
    }

def to_RestException_dict(e, msg, error_category):
    return {
        error_category: {
            "message": msg,
            "RestException": {
                **{ "http_status_code": e.get_http_status_code() },
                **e.json
            }
        }
    }

def to_Exception_dict(e, msg, error_category):
    return {
        error_category: {
            "message": msg,
            "exception_type": str(type(e)),
            "exception": str(e)
        }
    }
