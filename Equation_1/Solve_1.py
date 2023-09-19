from manim import *

class solve_1(Scene):
    def construct(self):
        Circ = Circle(2, color=RED, fill_opacity=0.2)

        self.play(DrawBorderThenFill(Circ), run_time=1.2)

        title = Text("Math", font_size=72, slant="ITALIC").shift(UP * 0.3)
        subtitle = Text("Class", slant="ITALIC").shift(DOWN * 0.6)
        self.play(Write(title), Write(subtitle))

        Logo = Arc(2.3, TAU * 1 / 3, -TAU * 3 / 4, color=BLUE, stroke_width=15)
        self.play(Create(Logo))

        self.wait(1)
        self.remove(Circ, Logo, title, subtitle)
        self.wait(1)

        # Equation
        equation = MathTex(r"\frac{3^{2021} - 3^{2019}}{3^{2018} - 3^{2016}}",                                  #0
                            r"= \frac{3^{(2019 + 2)} - 3^{2019}}{3^{(2016 + 2)} - 3^{2016}} \\&",               #1
                            r"= \frac{3^{2} \cdot 3^{2019} - 3^{2019}}{3^{2} \cdot 3^{2016} - 3^{2016}} \\&",   #2
                            r"= \frac{3^{2019} \cdot (3^2 - 1)}{3^{2016} \cdot (3^2 - 1)} \\&",                 #3
                            r"= \frac{3^{2019}}{3^{2016}}", r"\cdot", r"\frac{(3^2 - 1)}{(3^2 - 1)} \\&",       #4
                            r"= \frac{3^{2019}}{3^{2016}} \\&",                                                 #5
                            r"= 3^{2019 - 2016} \\&",                                                           #6
                            r"= 3^{3} = 27 \\&")                                                                        #8

        equation[0].shift(1.325*DOWN)
        equation[1].shift(1.325 * DOWN)

        for i in range(len(equation)):
            self.play(Write(equation[i]))
            self.wait(1)