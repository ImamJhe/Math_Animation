from manim import *
import numpy as np

class Text3D2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45*DEGREES)

        text_x = Text("X_label", font_size=12).scale(2).set_shade_in_3d(True)
        text_y = Text("Y_label", font_size=12).scale(2).set_shade_in_3d(True)
        text_z = Text("Z_label", font_size=12).scale(2).set_shade_in_3d(True)

        text_x.rotate(0, axis=RIGHT)
        text_y.rotate(-PI/2, axis=OUT)
        text_z.rotate(PI / 2, axis=RIGHT)

        text_x.shift(5*UP + RIGHT)
        text_y.shift(5*RIGHT + DOWN)
        text_z.shift(3*OUT + RIGHT)

        play = [text_x, text_y, text_z]
        j = [0, 0, 90]
        k = [0, 0, -90]
        l = [0, 90, 0]

        self.play(Create(axes))
        self.wait()

        for i, j, k, l in zip(play, j, k, l):
            self.move_camera(phi=j * DEGREES, theta=k * DEGREES, gamma=l * DEGREES)
            self.wait()
            self.play(Create(i))
            self.wait()
