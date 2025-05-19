import math
import random

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

        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            label_radius = radius - 20  # Slightly outside the ring
            text_x = center_x + label_radius * math.cos(rad)
            text_y = center_y + label_radius * math.sin(rad)
            w.create_text(text_x, text_y, text=str(angle), fill="white", font=("Helvetica", 10))

        return center_x, center_y, radius

def simulate_blips(canvas, center_x, center_y, radius, num_blips=5):

    canvas.delete("blips")  # Clear old blips

    for _ in range(num_blips):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0.1 * radius, radius)

        x = center_x + distance * math.cos(angle)
        y = center_y + distance * math.sin(angle)

        canvas.create_oval(x-3, y-3, x+3, y+3, fill="red", tags="blips")

def create_sweep_line(canvas, center_x, center_y, radius):
        
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