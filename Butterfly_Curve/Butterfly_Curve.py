from manim import *

class Butterfly1(Scene):
    def construct(self):
        plane = PolarPlane(radius_max=3)
        ax = Axes()

        t = ValueTracker(0)

        graph = always_redraw(lambda: ParametricFunction(
            lambda t: plane.polar_to_point((np.e**np.sin(t) - 2*np.cos(4*t) + np.sin((t - np.pi/2)/12)**5), t),
            t_range=[0, t.get_value()], color=GREEN)
                              )

        self.add(ax, graph)
        self.play(t.animate.set_value(24*np.pi), run_time=24)
        self.wait()
