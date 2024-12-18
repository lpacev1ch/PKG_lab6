import tkinter as tk
from tkinter import Canvas, Button, Entry, Label
from three_d_object import create_letter_A, plot_3d
from transformations import translate, scale, rotate

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Transformations")
        
        self.vertices, self.edges = create_letter_A()

        self.canvas = Canvas(root, width=400, height=400)
        self.canvas.pack()

        Label(root, text="Translation (tx, ty, tz)").pack()
        self.tx = Entry(root)
        self.tx.pack()
        self.ty = Entry(root)
        self.ty.pack()
        self.tz = Entry(root)
        self.tz.pack()

        Button(root, text="Translate", command=self.apply_translation).pack()

        Label(root, text="Scale (sx, sy, sz)").pack()
        self.sx = Entry(root)
        self.sx.pack()
        self.sy = Entry(root)
        self.sy.pack()
        self.sz = Entry(root)
        self.sz.pack()

        Button(root, text="Scale", command=self.apply_scaling).pack()

        Label(root, text="Rotation (angle, axis)").pack()
        self.angle = Entry(root)
        self.angle.pack()
        self.axis = Entry(root)
        self.axis.pack()

        Button(root, text="Rotate", command=self.apply_rotation).pack()

        Button(root, text="Plot 3D", command=self.plot_3d).pack()

    def apply_translation(self):
        tx = float(self.tx.get())
        ty = float(self.ty.get())
        tz = float(self.tz.get())
        self.vertices = translate(self.vertices, tx, ty, tz)

    def apply_scaling(self):
        sx = float(self.sx.get())
        sy = float(self.sy.get())
        sz = float(self.sz.get())
        self.vertices = scale(self.vertices, sx, sy, sz)

    def apply_rotation(self):
        angle = float(self.angle.get())
        axis = self.axis.get()
        self.vertices = rotate(self.vertices, angle, axis)

    def plot_3d(self):
        plot_3d(self.vertices, self.edges)

root = tk.Tk()
app = App(root)
root.mainloop()
