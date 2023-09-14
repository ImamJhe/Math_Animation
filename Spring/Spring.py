from manim import *

BLACK = "#343434"
SLATE = "#a2a2a2"
WHITE = "#ece6e2"

class Spring(VMobject):
    def __init__(self, start=ORIGIN, length=2, bumps=14):
        self.length = length
        self.empty = 0.4
        self.step = 0.07
        self.bump = 0.18
        super().__init__(color=WHITE)
        vertices = np.array(
            [
                [0, 0, 0],
                [0, self.empty, 0],
                [self.bump, self.empty + self.step, 0],
                *[
                    [
                        self.bump * (1 - (i % 2) * 2),
                        self.empty + self.step + self.step * 2 * i,
                        0,
                    ]
                    for i in range(1, bumps)
                ],
                [0, self.empty + self.step * 2 * bumps, 0],
                [0, self.empty * 2 + self.step * 2 * bumps, 0],
            ]
        )
        vertices = vertices * [1, -self.length /
                               (1 + 0.2 * bumps), 0] + np.array(start)

        self.start_new_path(np.array(start))
        self.add_points_as_corners(
            [*(np.array(vertex) for vertex in vertices)])

class Spring_vertical(Scene):
    def construct(self):

        circle = Circle(radius=0.4, fill_opacity=1).shift(DOWN)
        dot_circle = Dot(circle.point_from_proportion(25/100)%1)

        t = ValueTracker()

        ceil = VGroup(
            DashedLine(
                start=3 * LEFT,
                end= (3) * RIGHT,
                dashed_ratio=0.4,
                dash_length=0.2,
                color=WHITE,
            ).shift(3 * UP)
        )
        [i.rotate(PI / 4, about_point=i.get_start()) for i in ceil[0].submobjects]

        ceil.add(Line(3 * LEFT, 3 * RIGHT, color=WHITE).align_to(ceil, DOWN))
        line_up = Line(3 * LEFT, 3 * RIGHT, color=WHITE).align_to(ceil, DOWN)


        dot_line = Dot().move_to(line_up)
        spring = Spring(line_up.get_center(), 4)

        circle.add_updater(
            lambda m: m.move_to(np.array((0, t.get_value(), 0)))
        )
        dot_circle.add_updater(lambda m: m.move_to(circle.get_center()))

        def springupdater(m: Spring):
            # Modified Mobject.put_start_and_end_on
            curr_start, curr_end = m.get_start_and_end()
            curr_vect = curr_end - curr_start
            target_vect = (
                    dot_circle.get_end()
                    + (dot_circle.get_start() - dot_circle.get_end())
                    - dot_line.get_end()
                    - (dot_line.get_start() - dot_line.get_end())
            )
            axis = (
                normalize(np.cross(curr_vect, target_vect))
                if np.linalg.norm(np.cross(curr_vect, target_vect)) != 0
                else OUT
            )
            m.stretch(
                np.linalg.norm(target_vect) / np.linalg.norm(curr_vect),
                1,
                about_point=curr_start,
            )
            m.rotate(
                angle_between_vectors(curr_vect, target_vect),
                about_point=curr_start,
                axis=axis,
            )
            # m.move_to(
            #     line_down.get_start() + (line_down.get_end() - line_down.get_start()) * l / L,
            #     aligned_edge=LEFT,
            # )

        spring.add_updater(springupdater)
        self.add(ceil, dot_line, circle, dot_circle, spring)
        self.play(
            t.animate.set_value(-2),
            rate_func=there_and_back,
            run_time=3)
        self.play(
            t.animate.set_value(-3.5),
            rate_func=there_and_back,
            run_time=3)