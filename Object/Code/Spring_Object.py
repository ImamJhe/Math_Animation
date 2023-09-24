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
                [self.empty + self.step, 0, 0],
                *[
                    [
                        (t / 12 + np.cos(t / 4 - np.pi)) / 10,
                        np.sin(-t / 4) / 2,
                        0,
                    ]
                    for t in range(76, 314)
                ],
                [self.empty + self.step * 3 * bumps, 0, 0],
                [self.empty * 2 + self.step * 3 * bumps, 0, 0],
            ]
        )
        vertices = vertices * [self.length /
                               (1 + 0.2 * bumps), 1, 0] + np.array(start)

        self.start_new_path(np.array(start))
        self.add_points_as_corners(
            [*(np.array(vertex) for vertex in vertices)])

class Test(ThreeDScene):
    def construct(self):
        t = ValueTracker(0)
        dot = Dot().set_color(YELLOW).move_to(3*LEFT + 0.45*DOWN)
        dot1 = Dot()
        square = Square(side_length=1)

        spring = Spring(dot.get_center())

        def springupdater(m: Spring):
            # Modified Mobject.put_start_and_end_on
            curr_start, curr_end = m.get_start_and_end()
            curr_vect = curr_end - curr_start
            target_vect = (
                dot1.get_start()
                + (dot1.get_end() - dot1.get_start())
                - dot.get_start()
                - (dot.get_end() - dot.get_start())
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
        dot1.add_updater(lambda m: m.move_to(square.get_center() + 0.5 * LEFT))
        spring.add_updater(springupdater)

        self.play(Create(VGroup(square, dot, dot1), run_time=2))
        self.play(Create(spring, run_time=2))
        self.play(
            t.animate.set_value(2),
            rate_functions=linear,
            run_time=3
        )
        self.play(
            t.animate.set_value(1),
            rate_functions=linear,
            run_time=2
        )
        self.play(
            t.animate.set_value(4),
            rate_functions=linear,
            run_time=3
        )