"""
List objects
"""

import pandas as pd
import numpy as np
from . import list_utils


def search_registered_models(filter=None, prefix=None, max_description=None):
    models = list_utils.search_registered_models(filter, prefix)
    if len(models) == 0:
        return

    df = pd.DataFrame.from_dict(models)
    columns = ["name", "user_id", "creation_timestamp", "last_updated_timestamp" ]
    if not "user_id" in df:
        columns.remove("user_id")

    if "description" in df:
        columns.append("description")

    df = df.replace(np.nan, "", regex=True)
    df = df[columns]
    list_utils.mk_nice_timestamp(df, "creation_timestamp")
    list_utils.mk_nice_timestamp(df, "last_updated_timestamp")

    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]
    return df
