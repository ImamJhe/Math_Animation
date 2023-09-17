from manim import *

class Bubble_Sort(Scene):
    def construct(self):
        number = [11, 19, 3, 8, 13, 5, 1]
        arrow_end = [DOWN, UP, UP]
        colour = [YELLOW, RED, RED]

        tracker_i = ValueTracker(0)
        tracker_j = ValueTracker(0)
        tracker_j1 = ValueTracker(0)

        arrows_group = VGroup(
            *[Arrow(start=np.array((0, 0, 0)), end=end)
            .set_color(colour) for end, colour in zip(arrow_end, colour)]
                            )

        squares_group = VGroup(
            *[Square(side_length=0.8).add(Text(str(number[i]), font_size=16).scale(2)) for i in range(len(number))]
        ).arrange(buff=0.2)

        self.play(Create(squares_group, run_time=2))

        def bubble_sort():
            value = number
            self.add(arrows_group)

            for i in range(len(value)-1):
                tracker_i.set_value(i)
                arrows_group[0].next_to(squares_group[i], UP)

                for j in range(0, len(value)-i-1):
                    tracker_j.set_value(j)
                    tracker_j1.set_value(j + 1)

                    arrows_group[1].next_to(squares_group[j], DOWN)
                    arrows_group[2].next_to(squares_group[j + 1], DOWN)

                    def update_i():
                        texti = Text(f'i={tracker_i.get_value():.0f}', font_size=14).scale(2).set_color(YELLOW).next_to(
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

                    self.play(Create(VGroup(texti, textj, textj1)))
                    self.wait(1)

                    if value[j] > value[j+1]:
                        squares_group[j], squares_group[j + 1] = squares_group[j + 1], squares_group[j]
                        value[j], value[j + 1] = value[j + 1], value[j]

                        self.play(
                            Swap(squares_group[j],
                                squares_group[j+1],
                                run_time=1)
                            )
                        self.wait()

        bubble_sort()
        self.wait()