from mlflow.exceptions import RestException, MlflowException
from mlflow_reports.common import MlflowReportsException

def to_dict(e, msg, error_category="error"):
    if isinstance(e, MlflowReportsException):
        return to_MlflowReportsException(e, msg, error_category)
    elif isinstance(e, MlflowException):
        return to_MlflowException_dict(e, msg, error_category)
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

def to_MlflowException_dict(e, msg, error_category):
    return {
        error_category: {
            "message": msg,
            "MlflowException": {
                **{  "http_status_code": e.get_http_status_code(),
                     "error_code": e.error_code,
                      "message": e.message
                }, **e.json_kwargs }
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


# == Dump exception functions

def mk_msg_RestException(e):
    return { "RestException": { **e.json,  **{ "http_status_code": e.get_http_status_code()} } }


def dump_exception(ex, msg=""):
    if issubclass(ex.__class__,MlflowException):
        _dump_MlflowException(ex, msg)
    else:
        _dump_exception(ex, msg)
    print(f"==== dump_exception.end")


def _dump_exception(ex, msg=""):
    print(f"==== {ex.__class__.__name__}: {msg} =====")
    print(f"  type: {type(ex)}")
    print(f"  ex:   '{ex}'")
    print("  attrs:")
    for k,v in ex.__dict__.items():
        if isinstance(v,dict):
            print(f"    {k}:")
            for k2,v2 in v.items():
                print(f"      {k2}: {v2}")
        else:
            if k == "src_exception" and v:
                print(f"    {k}: {type(v)}")
            print(f"    {k}: {v}")


def _dump_MlflowException(ex, msg=""):
    _dump_exception(ex, msg)
    print(f"  get_http_status_code(): {ex.get_http_status_code()}")
    print(f"  serialize_as_json():    {ex.serialize_as_json()}")
