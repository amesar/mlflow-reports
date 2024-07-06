"""
Based upon: https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
"""

header = ""
elbow = "└──"
pipe = "│  "
tee = "├──"
blank = "   "


class Node(object):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f"( value={self.value} #children={len(self.children)})"


def to_string(node, header="", last=True):
    content = header + (elbow if last else tee) + node.value
    for j, child in enumerate(node.children):
        _content = to_string(child, header + (blank if last else pipe), j == len(node.children)-1)
        content += "\n" + _content
    return content
