def dimension(event, w):
    
        w.delete("all")
        width=event.width
        height=event.height
        radius = min(width, height) / 2
        x1 = width/2 - radius
        y1 = height/2 - radius
        x2 = width/2 + radius
        y2 = height/2 + radius
        w.create_oval(x1, y1, x2, y2, outline = "white", width = 3)
        center_x = width/2
        center_y = height/2
        return center_x, center_y, radius

def create_sweep_line(canvas, center_x, center_y, radius):
        
        import math
        angle = 0
        line_id = canvas.create_line(center_x, center_y, center_x+radius, center_y+radius, fill = "white", width = 2)

        def update():
                nonlocal angle
                end_x = center_x + radius * math.cos(angle)
                end_y = center_y + radius * math.sin(angle)

                canvas.coords(line_id, center_x, center_y, end_x, end_y)

                angle += 0.05
                if angle >= 2 * math.pi:
                        angle = 0
                
                canvas.after(20, update)

        update()