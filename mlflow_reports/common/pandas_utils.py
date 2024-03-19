
def move_column(df, column_name, index=1):
    column_names = list(df.columns)
    if column_name in column_names:
        col = df.pop(column_name)
        df.insert(index, column_name, col)
    return df
