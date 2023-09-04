from manim import *
import numpy as np
class tangen(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 390, 45],
                  y_range=[-5, 5],
                  axis_config={"include_numbers": False, "color": "#77c5f4"},
                  y_length=8, x_length=12)

        x_val = [x for x in range(0, 390, 45)]
        y_val = [x for x in range(-5, 5)]

        ax.add_coordinates(x_val, y_val)
        self.play(Create(ax))

        self.displacement1 = 0
        self.displacement2 = 0
        self.displacement3 = 0

        self.rate = 10

        self.approx_factor_Low = 0.934
        self.approx_factor_Up = 1.066

        self.min = 90*self.approx_factor_Low
        self.max = 90 *self.approx_factor_Up

        tangen1 = ax.plot(lambda x: np.tan(np.radians(x)),
                         x_range=[0, 0],
                         color=YELLOW)

        tangen2 = ax.plot(lambda x: np.tan(np.radians(x)),
                          x_range=[0, 0],
                          color=YELLOW)

        tangen3 = ax.plot(lambda x: np.tan(np.radians(x)),
                          x_range=[0, 0],
                          color=YELLOW)

        def update_graph1(obj, dt):
            self.displacement1 += self.rate * dt
            if np.radians(self.displacement1 * 180) <= self.min:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)),
                                   x_range=[0, np.radians(self.displacement1*180)],
                                   color=YELLOW))

        def update_graph2(obj, dt):
            self.displacement2 += self.rate * dt
            if self.max <= np.radians(self.displacement2 * 180) <= self.min + 1*180:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)),
                                   x_range=[self.max, np.radians(self.displacement2*180)],
                                   color=YELLOW))

        def update_graph3(obj, dt):
            self.displacement3 += self.rate * dt
            if self.max + 1*180 <= np.radians(self.displacement3 * 180) <= 2*180:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)),
                                   x_range=[self.max + 1*180, np.radians(self.displacement3*180)],
                                   color=YELLOW))

        tangen1.add_updater(update_graph1)
        tangen2.add_updater(update_graph2)
        tangen3.add_updater(update_graph3)


        self.add(always_redraw(lambda: tangen1),
                 always_redraw(lambda: tangen2),
                 always_redraw(lambda: tangen3),
                 )

        self.wait(20)