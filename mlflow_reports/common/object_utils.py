import json

def obj_to_dict(obj):
    """ Recursively convert an object to a dict. """
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )   


def dict_to_json(dct):
    return json.dumps(json.dumps(dct))


def dump_as_json(dct, sort_keys=None):
    print(json.dumps(dct, sort_keys=sort_keys, indent=2))
