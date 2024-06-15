import json


def obj_to_dict(obj):
    """ Recursively convert an object to a dict. """
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )


def dict_to_json(dct, sort_keys=None, indent=2):
    return json.dumps(dct, sort_keys=sort_keys, indent=indent)


def dump_as_json(dct, title=None, sort_keys=None, indent=2):
    if title:
        print(f"{title}:")
    print(dict_to_json(dct, sort_keys, indent))


def dump_obj_as_json(obj, title=None):
    title = title if title else type(obj).__name__
    print(title)
    dump_as_json(obj_to_dict(obj))


def dump_object(obj, title=None):
    title = f"{title} - {type(obj)}" if title else f"{type(obj)}"
    print(f"{title}:")
    for k,v in obj.__dict__.items():
        print(f"  {k}: {v}")
