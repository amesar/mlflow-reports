
import pandas as pd

def move_column(df, column_name, index=1):
    column_names = list(df.columns)
    if column_name in column_names:
        col = df.pop(column_name)
        df.insert(index, column_name, col)
    return df


def as_pandas(list_of_dicts, normalize_pandas_df=False):
    df = pd.json_normalize(list_of_dicts) if normalize_pandas_df else pd.DataFrame(list_of_dicts)
    return df
    #if reorder_columns:
        #df = reorder_columns(df)
    #print(f"Columns: {list(df.columns)}")
    #list_utils.to_datetime(df, ts_columns)
    #list_utils.show_and_write(df, columns, csv_file)
