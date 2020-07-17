from datetime import date, datetime, timedelta
from tkinter import *


def grid(self, columns, headers, combolist, ordlist, height, row, col, colspan=1, rowspan=1, cmd=None, order=True):
       

    def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            indice = columns
            if 'format' in headers[indice[col]]:
                if headers[indice[col]]['format'] == 'float':
                    l.sort(key=lambda t: float(num_usa(t[0])), reverse=reverse)
                if headers[indice[col]]['format'] == 'int':
                    l.sort(key=lambda t: int(num_usa(t[0])), reverse=reverse)
                if headers[indice[col]]['format'] == 'date/time':
                    try:
                        l.sort(key=lambda t: datetime.strptime(t[0], '%d/%m/%Y %H:%M:%S'), reverse=reverse)
                    except:
                        l.sort(key=lambda t: datetime.strptime(t[0], '%d/%m/%Y %H:%M'), reverse=reverse)
                if headers[indice[col]]['format'] == 'date':
                    l.sort(key=lambda t: datetime.strptime(t[0], '%d/%m/%Y'), reverse=reverse)
            else:
                l.sort(key=lambda t: t[0].lower(), reverse=reverse)
                # l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda: \
                    treeview_sort_column(tv, col, not reverse))
def num_usa(val):
        valorfill = val.replace('.', ';')
        valorfill = valorfill.replace(',', ';')
        valorfill = valorfill.split(';')
        if len(valorfill) == 1:
            valorfill.append('0')
        valorfill = ''.join(valorfill[:-1]) + '.' + valorfill[-1:][0]
        return valorfill       
              

                    
        
            