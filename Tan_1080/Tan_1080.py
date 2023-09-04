from manim import *
import numpy as np
class tangen(Scene):
    def construct(self):
        ax = Axes(x_range=[-300, 1160, 90], y_range=[-5, 5], axis_config={"include_numbers": False, "color": "#77c5f4"},
                  y_length=5, x_length=12)

        x_val1 = [x for x in range(0, 1090, 90)]
        y_val = [x for x in range(-5, 5)]

        ax.add_coordinates(x_val1, y_val)

        self.play(Create(ax))

        self.displacement = 0
        self.displacement1 = 0
        self.displacement2 = 0
        self.displacement3 = 0
        self.displacement4 = 0
        self.displacement5 = 0
        self.displacement6 = 0

        self.rate = 10
        self.approx_factor = 0.934
        self.approx_factor1 = 1.066
        self.min = 90*self.approx_factor
        self.max = 90 *self.approx_factor1

        tangen = ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, 0], color=YELLOW)
        tangen1 = ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, 0], color=YELLOW)
        tangen2 = ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, 0], color=YELLOW)
        tangen3 = ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, 0], color=YELLOW)
        tangen4 = ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, 0], color=YELLOW)
        tangen5 = ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, 0], color=YELLOW)
        tangen6 = ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, 0], color=YELLOW)

        def update_graph1(obj, dt):
            self.displacement += self.rate * dt
            if np.radians(self.displacement * 180) <= self.min:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)), x_range=[0, np.radians(self.displacement*180)],
                            color=YELLOW))

        def update_graph2(obj, dt):
            self.displacement1 += self.rate * dt
            if self.max <= np.radians(self.displacement1 * 180) <= self.min + 1*180:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)), x_range=[self.max, np.radians(self.displacement1*180)],
                            color=YELLOW))

        def update_graph3(obj, dt):
            self.displacement2 += self.rate * dt
            if self.max + 1*180 <= np.radians(self.displacement2 * 180) <= self.min + 2*180:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)), x_range=[self.max + 1*180, np.radians(self.displacement2*180)],
                            color=YELLOW))

        def update_graph4(obj, dt):
            self.displacement3 += self.rate * dt
            if self.max + 2*180 <= np.radians(self.displacement3 * 180) <= self.min + 3*180:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)), x_range=[self.max + 2*180, np.radians(self.displacement3*180)],
                            color=YELLOW))

        def update_graph5(obj, dt):
            self.displacement4 += self.rate * dt
            if self.max + 3*180 <= np.radians(self.displacement4 * 180) <= self.min + 4*180:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)), x_range=[self.max + 3*180, np.radians(self.displacement4*180)],
                            color=YELLOW))

        def update_graph6(obj, dt):
            self.displacement5 += self.rate * dt
            if self.max + 4*180 <= np.radians(self.displacement5 * 180) <= self.min + 5*180:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)), x_range=[self.max + 4*180, np.radians(self.displacement5*180)],
                            color=YELLOW))

        def update_graph7(obj, dt):
            self.displacement6 += self.rate * dt
            if self.max + 5*180 <= np.radians(self.displacement6 * 180) <= 1080:
                obj.become(ax.plot(lambda x: np.tan(np.radians(x)), x_range=[self.max + 5*180, np.radians(self.displacement6*180)],
                            color=YELLOW))


        tangen.add_updater(update_graph1)
        tangen1.add_updater(update_graph2)
        tangen2.add_updater(update_graph3)
        tangen3.add_updater(update_graph4)
        tangen4.add_updater(update_graph5)
        tangen5.add_updater(update_graph6)
        tangen6.add_updater(update_graph7)

        self.add(always_redraw(lambda: tangen),
                 always_redraw(lambda: tangen1),
                 always_redraw(lambda: tangen2),
                 always_redraw(lambda: tangen3),
                 always_redraw(lambda: tangen4),
                 always_redraw(lambda: tangen5),
                 always_redraw(lambda: tangen6))


        self.wait(40)