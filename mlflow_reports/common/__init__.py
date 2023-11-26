import json

class MlflowReportsException(Exception):
    def __init__(self, http_status_code=None, uri=None, params=None, response=None, message=None):
        def _add(dct, k, v):
            if v: dct[k] = v
        self.http_status_code = http_status_code
        self.uri = uri
        self.params = params
        self.error = {}
        _add(self.error, "http_status_code", http_status_code)
        _add(self.error, "uri", uri)
        _add(self.error, "params", params)
        _add(self.error, "response", _to_dict(response))
        _add(self.error, "message", message)


    def __str__(self):
        return json.dumps(self.args_dict)


def _to_dict(msg):
    if not msg:
        return None
    try:
        return json.loads(msg)
    except json.decoder.JSONDecodeError:
        return msg
