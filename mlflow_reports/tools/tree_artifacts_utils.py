"""
Tree artifacts utilities.
"""

from mlflow_reports.common.tree_utils import Node, to_string


def artifacts_to_string(artifacts_dct, root_name="artifacts"):
    """
    Return
    param: artifacts_dct: Dict with "artifacts" key as returned by artifact_utils.list_artifacts
    """
    artifacts = artifacts_dct.get("artifacts")
    tree = _to_tree(artifacts, root_name)
    return to_string(tree)


def _to_tree(artifacts_lst, root_name):
    tree = Node(root_name)
    for art in artifacts_lst:
        if "artifacts" in art:
            node = _to_tree(art["artifacts"], art["path"])
        else:
            node = Node(art.get("path"))
        tree.children.append(node)
    return tree
