import json


def newline_tweak_str(v):
    if isinstance(v,str):
        return v.replace("\n","<br/>")
    return v

def newline_tweak(dct):
    for k,v in dct.items():
        if isinstance(v,str):
            dct[k] = v.replace("\n","<br/>")


def escape_str(str): 
    return f"```\n{str}\n```"

def escape_col(col):
    str = json.dumps(col, indent=2)+"\n"
    return escape_str(str)


def make_red(msg):
    return f'**_<font color="red" size="+1">{msg}</font>_**'


def is_primitive(thing):
    _primitives = (int, float, str, bool)
    return isinstance(thing, _primitives)
