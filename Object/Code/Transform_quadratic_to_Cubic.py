from manim import *

class Transform_quadratic_to_Cubic(Scene):
    def construct(self):
        ax = Axes(x_range=[-3, 3],
                  y_range=[-3, 3],
                  x_length=8, y_length=8,)

        x_2 = ax.plot(lambda x: x ** 2, x_range=[-2, 2], color=BLUE)
        x_3 = ax.plot(lambda x: x ** 3, x_range=[-2, 2], color=RED)

        label_2 = ax.get_graph_label(x_2, "f(x): x^2", x_val=1.5, direction=DR)
        label_3 = ax.get_graph_label(x_3, "f(x): x^3", x_val=-1.5, direction=DL)

        ax_2 = VGroup(x_2, label_2)
        ax_3 = VGroup(x_3, label_3)

        self.play(Create(ax))
        self.wait()
        self.play(Create(ax_2))
        self.wait()
        self.play(Transform(ax_2, ax_3, run_time=3))
        self.wait()