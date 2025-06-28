import tkinter as tk

class WheelCanvas:
    def __init__(self, root, participant_data):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.participant_data = participant_data
        self.current_angle = 0
        self.spin_speed = 10
        self.colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
        self.draw_wheel()

        self.root.after(1000, self.spin)

    def draw_wheel(self):
        self.canvas.delete('all')
        total = sum(self.participant_data.values())
        start_angle = self.current_angle % 360
        for i, (name, weight) in enumerate(self.participant_data.items()):
            extent = 360 * weight / total
            color = self.colors[i % len(self.colors)]
            self.canvas.create_arc(50, 50, 350, 350, start=start_angle, extent=extent, fill=color)
            start_angle += extent
        self.canvas.create_polygon(195, 10, 205, 10, 200, 30, fill='black')

    def spin(self):
        if self.spin_speed > 0:
            self.current_angle += self.spin_speed
            self.spin_speed *= 0.97  # slow down gradually
            self.draw_wheel()
            self.root.after(50, self.spin)
