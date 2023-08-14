import json

def obj_to_dict(obj):
    """ Recursively convert an object to a dict. """
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )   


def dict_to_json(dct):
    return json.dumps(dct)


def dump_as_json(dct, sort_keys=None):
    print(json.dumps(dct, sort_keys=sort_keys, indent=2))


def dump_object(obj):
    title = f"{type(obj)}.__name__"
    print(f"{title}:")
    for k,v in obj.__dict__.items():
        print(f"  {k}: {v}")
