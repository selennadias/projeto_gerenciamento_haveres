
import operator
try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk


root = tk.Tk()
root.title("listbox")
root["bg"] = "LightSteelBlue"
root.geometry('1180x600')

class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        container = ttk.Frame()
        container.place(x=400, y=300, width=500)

        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=titulos_listbox, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in titulos_listbox:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in banco_dados:
            self.tree.insert('', 'end', values=item)


def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]



    if col == "Código":
        print("Código")
        # bd = sorted(banco_dados, key=operator.itemgetter(1))# sem alterar a lista
        bd = banco_dados.sort(key=operator.itemgetter(1)) # alterando a lista
        print(banco_dados)

    elif col == "Produto":
        print("Item")
        # bd = sorted(banco_dados, key=operator.itemgetter(2))# sem alterar a lista
        bd = banco_dados.sort(key=operator.itemgetter(2)) # alterando a lista
        print(banco_dados)

    elif col == "Quantidade":
        print("Quantidade")
        # bd = sorted(banco_dados, key=operator.itemgetter(3))# sem alterar a lista
        bd = banco_dados.sort(key=operator.itemgetter(3)) # alterando a lista
        print(banco_dados)



titulos_listbox = [ 'Código', 'Produto', 'Quantidade']
banco_dados = [( 000, 'item 000', 555),
               ( 111, 'item 111', 111),
                (333, 'item 333', 222),
               ( 777, 'item 777', 333),
               ( 444, 'item 444', 4444),
               ( 222, 'item 222', 5555),
               ( 888, 'item 888', 6666)]

listbox = MultiColumnListbox()

root.mainloop()
   