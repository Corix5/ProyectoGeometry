import tkinter as tk
from tkinter import ttk
from tri import graph

root = tk.Tk()
root.config(width=300, height=200)
style = ttk.Style()
style.configure(
    "MyEntry.TEntry",
    # Espacio entre los márgenes de la caja de texto
    # y el texto (en píxeles).
    padding=10
)
entry = ttk.Entry(style="MyEntry.TEntry")
entry.place(x=50, y=50)

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

array = [[19.459836, -99.122448], [19.442675, -99.123055], [19.404388, -99.125812], [19.404358, -99.156808], [19.399934, -99.170592], [19.407860, -99.184260], 
[19.423629, -99.177524], [19.464074, -99.158410], [19.464691, -99.133004], [19.4518039,-99.1410253], [19.4286819,-99.1458219], [19.3381141,-99.1696988], [19.3449362,-99.1948387], [19.4220411,-99.1269733], [19.4307821,-99.1513346]]
coordenada = [19.423659, -99.159024]
text_disp= tk.Button(frame, 
                   text="Agregar coordenada", 
                   command= lambda: array.append(entry.get())
                   )

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                   text="Graficar",
                   fg="green",
                   command= lambda: graph(array, coordenada))
exit_button.pack(side=tk.RIGHT)


root.mainloop()
print(array)

