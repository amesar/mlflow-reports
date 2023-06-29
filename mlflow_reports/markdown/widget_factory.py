from mlflow_reports.markdown.local_utils import newline_tweak

_TAG_COLUMNS = ["Key","Value"]
_NAME_COLUMNS = ["Name","Value"]

TAG_COLUMNS = { "columns": _TAG_COLUMNS }
NAME_COLUMNS = { "columns": _NAME_COLUMNS }

NOT_FOUND = '**_<font color="red" size="+1">None found</font>_**'

class WidgetFactory:
    def __init__(self, card):
        self.card = card

    # =====
    # table widgets

    def mk_table(self, columns, data, title, level):
        self.card.new_header(level=level, title=title)
        if len(data) == 0:
            return
        table = columns.copy()
        for row in data:
            table.extend(row)
        self.card.new_line()
        self.card.new_table(columns=len(columns), rows=len(data)+1, text=table, text_align="left")

    def build_table(self, obj, title=None, level=2, columns=None):
        columns = columns or _NAME_COLUMNS
        if not obj:
            self.mk_not_present_header(title, level)
            return 
        if title:
            self._mk_header(level, title)
        if obj is None or len(obj) == 0:
            self.card.new_line(NOT_FOUND)
            return
        if isinstance(obj,dict):
            self._build_table_from_dict(obj, columns)
        elif isinstance(obj,list):
            self._build_table_from_list(obj, columns=columns)

    def _mk_header(self, level, title):
        if level < 1:
            title = f'<b><font size="+1">{title}</font></b>'
            self.card.new_line(title)
        else:
            self.card.new_header(level=level, title=title)

    def _build_table_from_dict(self, dct, columns=None):
        table = columns.copy() if columns else ["", "" ]
        newline_tweak(dct)
        for k,v in dct.items():
            table.extend([k,v])
        self.card.new_line()
        self.card.new_table(columns=2, rows=len(dct)+1, text=table, text_align="left")

    def _build_table_from_list(self, lst, columns=None):
        columns = columns.copy() if columns else ["", "" ]
        table = columns.copy() 
        for row in lst:
            table.extend(row)
        self.card.new_line()
        self.card.new_table(columns=len(columns), rows=len(lst)+1, text=table, text_align="left")


    # =====
    # Helper

    def mk_list_as_table(self, dct, title=None, level=None, keys=None):
        def _add_item(dct_dst, dct_src, k):
            dct_dst[k] = dct_src.get(k)
        keys = keys if keys else dct.keys()
        dct2 = {}  
        for k in keys:
            _add_item(dct2, dct, k)
        self.build_table(dct2, title, level)

    def mk_not_present_header(self, title, level):
        if title:
            self._mk_header(level, title)
        self.card.new_line(NOT_FOUND)

    def mk_not_present(self):
        self.card.new_line(NOT_FOUND)
