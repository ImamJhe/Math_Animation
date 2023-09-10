from manim import *

class Lissajous_curve(Scene):
    def construct(self):
        # Create the first circle
        circle1 = Circle(radius=1, color=RED).shift(LEFT * 3 + UP)
        dot1 = Dot(circle1.point_from_proportion(0))

        # Create the second circle
        circle2 = Circle(radius=1, color=BLUE).shift(DOWN * 2)
        dot2 = Dot(circle2.point_from_proportion(0))

        # Create the central dot at the initial position
        central_dot = Dot([dot1.get_center()[1], dot2.get_center()[0], 0], color=GREEN)

        # Create lines connecting the central dot to dot1 and dot2
        line1 = Line(central_dot.get_center(), dot1.get_center(), color=RED)
        line2 = Line(central_dot.get_center(), dot2.get_center(), color=BLUE)

        round1 = 4
        round2 = 5

        text1 = Text(f"{round1}", font_size=16).scale(2).move_to(circle1, aligned_edge=ORIGIN)
        text2 = Text(f"{round2}", font_size=16).scale(2).move_to(circle2, aligned_edge=ORIGIN)

        trace = TracedPath(central_dot.get_start)

        self.play(Create(circle1), Create(circle2), Create(text1), Create(text2))
        self.play(Create(dot1), Create(dot2))
        self.play(Create(central_dot), Create(trace))
        self.play(Create(line1), Create(line2))

        def update_dot(dot, circle, rounds, alpha):
            dot.move_to(circle.point_from_proportion((alpha * rounds) % 1))

        def update_line1(obj):
            obj.become(Line(central_dot.get_center(), dot1.get_center(), color=RED))

        def update_line2(obj):
            obj.become(Line(central_dot.get_center(), dot2.get_center(), color=BLUE))

        anim1 = UpdateFromAlphaFunc(dot1, lambda x, alpha: update_dot(x, circle1, round1, alpha))
        anim2 = UpdateFromAlphaFunc(dot2, lambda x, alpha: update_dot(x, circle2, round2, alpha))

        anim_line1 = UpdateFromFunc(line1, update_line1)
        anim_line2 = UpdateFromFunc(line2, update_line2)

        def update_central_dot(dot):
            dot.move_to([dot2.get_center()[0], dot1.get_center()[1], 0])

        anim_central_dot = UpdateFromFunc(central_dot, update_central_dot)

        self.play(anim1, anim2, anim_central_dot, anim_line1, anim_line2, run_time=4, rate_func=linear)
        self.wait(1)