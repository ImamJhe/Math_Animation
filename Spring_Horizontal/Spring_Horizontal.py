from manim import *

BLACK = "#343434"
SLATE = "#a2a2a2"
WHITE = "#ece6e2"

ceil_len = 3
w1 = 6
w2 = w1 * 1.1

L = 4
l = 1.5

class Spring(VMobject):
    def __init__(self, start=ORIGIN, length=2, bumps=10):
        self.length = length
        self.empty = 0.4
        self.step = 0.08
        self.bump = 0.15
        super().__init__(color=WHITE)
        vertices = np.array(
            [
                [0, 0, 0],
                [self.empty, 0, 0],
                [self.empty + self.step, self.bump, 0],
                *[
                    [
                        self.empty + self.step + self.step * 2 * i,
                        self.bump * (1 - (i % 2) * 2),
                        0,
                    ]
                    for i in range(1, bumps)
                ],
                [self.empty + self.step * 2 * bumps, 0, 0],
                [self.empty * 2 + self.step * 2 * bumps, 0, 0],
            ]
        )
        vertices = vertices * [self.length /
                               (1 + 0.2 * bumps), 1, 0] + np.array(start)

        self.start_new_path(np.array(start))
        self.add_points_as_corners(
            [*(np.array(vertex) for vertex in vertices)])

class Test(ThreeDScene):
    def construct(self):
        t = ValueTracker()

        text_spring = MathTex(r'k = 4', font_size=16).scale(2).set_color(YELLOW)
        text_equation = MathTex(f'F = -kx', font_size=16).scale(2).set_color(YELLOW)

        square = Square(side_length=1)
        dot_square = Dot()
        dot_line = Dot()

        ceil = VGroup(
            DashedLine(
                start=LEFT,
                end=RIGHT,
                dashed_ratio=0.8,
                dash_length=0.2,
            ).shift(3*LEFT + 2.05 *DOWN)

        )

        ceil_down = VGroup(
            DashedLine(
                start=3*RIGHT,
                end=3*LEFT,
                dashed_ratio=0.8,
                dash_length=0.2,
            ).shift(3 * DOWN)

        )
        [i.rotate(PI / 4, about_point=i.get_start()) for i in ceil_down[0].submobjects]
        [i.rotate(PI / 4, about_point=i.get_start()) for i in ceil[0].submobjects]

        ceil.rotate(PI/2).shift(2*UP)
        ceil_down.rotate(PI).shift(2*UP)

        line = Line(LEFT, RIGHT).move_to(ceil)
        line_down = Line(3 * RIGHT, 3 * LEFT).move_to(ceil_down)

        line.rotate(PI/2).shift(0.08*RIGHT)
        line_down.rotate(PI).shift(0.08*UP)

        dot_line.shift(line.get_center() + 0.45 * DOWN)
        text_equation.next_to(line, UP + RIGHT)
        spring = Spring(dot_line.get_center())

        def springupdater(m: Spring):
            # Modified Mobject.put_start_and_end_on
            curr_start, curr_end = m.get_start_and_end()
            curr_vect = curr_end - curr_start
            target_vect = (
                dot_square.get_start()
                + (dot_square.get_end() - dot_square.get_start())
                - dot_line.get_start()
                - (dot_line.get_end() - dot_line.get_start())
            )
            axis = (
                normalize(np.cross(curr_vect, target_vect))
                if np.linalg.norm(np.cross(curr_vect, target_vect)) != 0
                else OUT
            )
            m.stretch(
                np.linalg.norm(target_vect) / np.linalg.norm(curr_vect),
                0,
                about_point=curr_start,
            )
            m.rotate(
                angle_between_vectors(curr_vect, target_vect),
                about_point=curr_start,
                axis=axis,
            )

        square.add_updater(lambda m: m.move_to(np.array((t.get_value(), -0.45, 0))))
        dot_square.add_updater(lambda m: m.move_to(square.get_center() + 0.5*LEFT))

        spring.add_updater(springupdater)
        text_spring.add_updater(lambda m: m.next_to(spring, UP))
        def update_text():
            text = Text(f'F = {np.abs(4*t.get_value()):.2f}', font_size=12).scale(2).set_color(YELLOW).next_to(arrow_square, UP)
            return text
        def update_arrow():
            arrow_square = Arrow(buff=0.5, start=np.array((0, 0, 0)), end= -0.2 * np.array((t.get_value(), 0, 0)), color=YELLOW).scale(3).next_to(square, UP)
            return arrow_square

        arrow_square = always_redraw(update_arrow)
        text_square = always_redraw(update_text)

        self.play(Create(VGroup(line, line_down, ceil, ceil_down, dot_line), run_time=2))
        self.play(Create(VGroup(square, dot_square, arrow_square, text_square, text_equation), run_time=2))
        self.play(Create(VGroup(spring, text_spring)), run_time=2)
        self.play(
                t.animate.set_value(2),
                rate_functions=linear,
                run_time=3
                )
        self.play(
            t.animate.set_value(-1),
            rate_functions=linear,
            run_time=3
        )
        self.play(
            t.animate.set_value(0),
            rate_functions=linear,
            run_time=3
        )