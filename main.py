import tkinter as tk
from functions import dimension, create_sweep_line, simulate_blips

root = tk.Tk()
root.title("Radar")
root.state('zoomed')
w=tk.Canvas(root)
w.pack(fill=tk.BOTH, expand = True)
w.config(background="green")

sweep_line_created = False

def resize(event):
    global sweep_line_created
    center_x, center_y, radius = dimension(event, w)

    if not sweep_line_created:
        create_sweep_line(w, center_x, center_y, radius)
        sweep_line_created = True

    simulate_blips(w, center_x, center_y, radius)

w.bind("<Configure>", resize)
root.mainloop()