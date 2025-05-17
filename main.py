import tkinter as tk

root = tk.Tk()
root.title("Radar")
root.state('zoomed')
w=tk.Canvas(root)
w.pack(fill=tk.BOTH, expand = True)
def dimension(event):
    
        width=event.width
        height=event.height
    
tk.canvas.bind("<Configure>", dimension)
radius = min(width, height) / 2
x1 = height/2 - radius
y1 = width/2 - radius
x2 = height/2 + radius
y2 = width/2 + radius
w.create_oval(x1, y1, x2, y2, fill = "white")
w.config(background="green")
root.mainloop()