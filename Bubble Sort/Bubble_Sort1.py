from manim import *

class Bubble_Sort(Scene):
    def construct(self):
        tracker_i = ValueTracker(0)
        tracker_j = ValueTracker(0)
        tracker_j1 = ValueTracker(0)

        number = [11, 19, 3, 8, 13, 5, 1]
        arrow_end = [DOWN, UP, UP]
        colour = [YELLOW, RED, RED]

        squares_group = VGroup(
            *[Square(side_length=0.8).add(Text(str(number[i]), font_size=16).scale(2)) for i in range(len(number))]
        ).arrange(buff=0.2)

        arrows_group = VGroup(
            *[Arrow(start=np.array((0, 0, 0)), end=end)
              .set_color(colour) for end, colour in zip(arrow_end, colour)]
        )

        squares_group.shift(UP)

        Sq1 = Rectangle(width=2, height=0.5).add(MathTex(r"V[j] > V[j+1]", font_size=14).scale(2).set_color(WHITE)).shift(LEFT + 2*DOWN)
        Sq2 = Rectangle(width=1, height=0.5).add(Tex("Swap", font_size=16).scale(2).set_color(WHITE)).shift(1.5 * RIGHT + 1.5 * DOWN)
        Sq3 = Rectangle(width=1, height=0.5).add(Tex("Pass", font_size=16).scale(2).set_color(WHITE)).shift(1.5 * RIGHT + 2.5 * DOWN)

        line = Line(Sq1.get_right(), Sq2.get_left())
        line1 = Line(Sq1.get_right(), Sq3.get_left())
        def Gr1():
            Gr1 = VGroup(Sq1.set_opacity(0.6),
                   line.set_opacity(0.6),
                   Sq2.set_opacity(0.6),
                   Sq3.set_opacity(0.2),
                   line1.set_opacity(0.2))
            return Gr1

        def Gr2():
            Gr2 = VGroup(Sq1.set_opacity(0.6),
                   line.set_opacity(0.2),
                   Sq2.set_opacity(0.2),
                   Sq3.set_opacity(0.6),
                   line1.set_opacity(0.6))
            return Gr2

        def Gr3():
            Gr3 = VGroup(Sq1.set_opacity(0.6),
                   line.set_opacity(0.2),
                   Sq2.set_opacity(0.2),
                   Sq3.set_opacity(0.2),
                   line1.set_opacity(0.2))
            return Gr3

        Gr1 = always_redraw(Gr1)
        Gr2 = always_redraw(Gr2)
        Gr3 = always_redraw(Gr3)

        self.play(Create(squares_group, run_time=2))
        self.play(Create(VGroup(Sq1, Sq2, Sq3)), Create(VGroup(line, line1)))

        def bubble_sort():
            value = number
            self.add(arrows_group)

            for i in range(len(value)-1):
                tracker_i.set_value(i)
                arrows_group[0].next_to(squares_group[len(number) - 1 - i], UP)
                self.add(Gr3)

                for j in range(0, len(value)-i-1):
                    tracker_j.set_value(j)
                    tracker_j1.set_value(j + 1)

                    arrows_group[1].next_to(squares_group[j], DOWN)
                    arrows_group[2].next_to(squares_group[j + 1], DOWN)

                    def update_i():
                        texti = Text(f'i={len(number) - 1 - tracker_i.get_value():.0f}', font_size=14).scale(2).set_color(YELLOW).next_to(
                            arrows_group[0], UP)
                        return texti

                    def update_j():
                        textj = Text(f'j={tracker_j.get_value():.0f}', font_size=14).scale(2).set_color(RED).next_to(
                            arrows_group[1], DOWN)
                        return textj

                    def update_j1():
                        textj1 = Text(f'j={tracker_j1.get_value():.0f}', font_size=14).scale(2).set_color(RED).next_to(
                            arrows_group[2], DOWN)
                        return textj1

                    texti = always_redraw(update_i)
                    textj = always_redraw(update_j)
                    textj1 = always_redraw(update_j1)

                    self.add(VGroup(texti, textj, textj1))
                    if value[j] > value[j+1]:
                        squares_group[j], squares_group[j + 1] = squares_group[j + 1], squares_group[j]
                        value[j], value[j + 1] = value[j + 1], value[j]
                        self.play(Transform(Gr1, Gr2))
                        self.play(
                            Swap(squares_group[j],
                                squares_group[j+1],
                                run_time=1)
                            )
                        self.play(Transform(Gr3, Gr3))
                        self.wait()
                    else:
                        self.add(VGroup(texti, textj, textj1))
                        self.play(Transform(Gr2, Gr1))
                        self.wait(1)
                        self.play(Transform(Gr3, Gr3))
                        self.wait()

        bubble_sort()
        self.wait(2)
