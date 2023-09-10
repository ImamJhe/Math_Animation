from manim import *
class Free_Fall_Motion(Scene):
    def construct(self):
        ax = Axes(y_range=[0, 10], x_range=[0, 4], y_axis_config={"include_numbers": True})
        self.t = 0
        self.v = 0
        self.h = 10
        self.g = 9.8
        self.rate = 1

        def update_dot(dot, dt):
            self.t += self.rate * dt
            self.h += self.v * self.t * dt
            self.v -= self.g * self.t * dt

            if self.h <= 0:
                self.h = 0
                dot.move_to(ax.c2p(1, self.h))
            else:
                dot.move_to(ax.c2p(1, self.h))

        def update_text():
            if self.h <= 0:
                self.h = 0

            text = Text(f'h = {self.h:.2f}', font_size=12).scale(2).next_to(dot, RIGHT)
            return text

        dot = Dot(ax.coords_to_point(1, self.h))
        dot_to = TracedPath(dot.get_center, dissipating_time=0.8, stroke_opacity=[1, 0])

        text = always_redraw(update_text)
        dot.add_updater(update_dot)

        self.play(Create(ax))
        self.add(always_redraw(lambda: dot), text, dot_to)
        self.wait(3)  # Wait for a moment at the end of the animation




