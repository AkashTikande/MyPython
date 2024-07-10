# Creating a white workspace for drawing using python programming #
import tkinter as tk

class DrawingWorkspace(tk.Canvas):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height)

        self.bind("<Button-1>", self.start_drawing)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.end_drawing)

        self.x1 = None
        self.y1 = None

    def start_drawing(self, event):
        self.x1 = event.x
        self.y1 = event.y

    def draw(self, event):
        x2 = event.x
        y2 = event.y

        self.create_line(self.x1, self.y1, x2, y2, width=3)

        self.x1 = x2
        self.y1 = y2

    def end_drawing(self, event):
        self.x1 = None
        self.y1 = None


root = tk.Tk()

workspace = DrawingWorkspace(root,  1920, 1080)
workspace.pack()

root.mainloop()