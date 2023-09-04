from manim import *
import numpy as np
class cosine_curve_circle(Scene):
    def construct(self):
        # define axis and create
        ax = Axes(x_range=[-90, 390, 45], y_range=[-2, 2], axis_config={"include_numbers": False, "color": "#77c5f4"},
                  y_length=4.5, x_length=12)

        x_val = [x for x in range(0, 390, 45)]
        y_val = [x for x in range(-2, 2)]

        ax.add_coordinates(x_val, y_val)
        self.play(Create(ax))

        # define circle on axis
        circle = Circle(radius=ax.coords_to_point(-45, 0)[0] - ax.coords_to_point(0, 0)[0]).move_to(
            ax.coords_to_point(-45, 0))
        self.play(Create(circle))

        # define dot
        dot = Dot(radius=0.1).move_to(ax.coords_to_point(-45, 1))

        def radial_line():
            return Line(circle.get_center(), dot.get_center(), color=YELLOW)

        radius_constant = radial_line()
        self.play(Create(radius_constant))
        self.play(Create(dot))

        # define graph
        cosine = ax.plot(lambda x: np.cos(x), x_range=[0, 0], color=RED)

        # updaters!
        self.displacement = 0
        self.rate = 10

        def update_dot(obj, dt):
            self.displacement += (self.rate * dt)
            if np.radians(self.displacement * 180) <= 360:
                obj.move_to(circle.point_from_proportion((self.displacement / 115 + 0.75) % 1))
            else:
                self.displacement = 0  # Reset the displacement to 0 when it exceeds 360 degrees
                obj.move_to(circle.point_from_proportion((self.displacement / 115 + 0.75) % 1))

        def update_graph(obj, dt):
            self.displacement += self.rate * dt
            if np.radians(self.displacement * 180) <= 360:
                obj.become(ax.plot(lambda x: np.cos(np.radians(x)), x_range=[0, np.radians(self.displacement * 180)],
                                   color=YELLOW))
            else:
                self.displacement = 0  # Reset the displacement to 0 when it exceeds 360 degrees
                obj.become(ax.plot(lambda x: np.cos(np.radians(x)), x_range=[0, np.radians(self.displacement * 180)],
                                   color=YELLOW))

        dot.add_updater(update_dot)
        cosine.add_updater(update_graph)
        radius = always_redraw(radial_line)

        # horizontal line
        horizontal_line = Line(dot.get_center(), np.array([0, 0, 0]), color=PURPLE)

        def update_horizontal_line(obj, dt):
            obj.become(Line(dot.get_center(), np.array([15, dot.get_center()[1], 0]), color=PURPLE))

        horizontal_line.add_updater(update_horizontal_line)

        self.add(always_redraw(lambda: dot), always_redraw(lambda: cosine), radius, horizontal_line)
        self.remove(radius_constant)


        self.wait(20)
