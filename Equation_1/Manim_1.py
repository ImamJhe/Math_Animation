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
        original_equation = MathTex(r"\frac{3^{2021} - 3^{2019}}{3^{2018} - 3^{2016}}")
        explanation_1 = MathTex(r"= \frac{3^{(2019 + 2)} - 3^{2019}}{3^{(2016 + 2)} - 3^{2016}}")
        explanation_2 = MathTex(r"= \frac{3^{2} \cdot 3^{2019} - 3^{2019}}{3^{2} \cdot 3^{2016} - 3^{2016}}")
        explanation_3 = MathTex(r"= \frac{3^{2019} \cdot (3^2 - 1)}{3^{2016} \cdot (3^2 - 1)}")
        explanation_3_1 = MathTex(r"= \frac{3^{2019}}{3^{2016}}", r"\cdot", r"\frac{(3^2 - 1)}{(3^2 - 1)}")
        explanation_4 = MathTex(r"= \frac{3^{2019}}{3^{2016}}")
        explanation_5 = MathTex(r"= 3^{2019 - 2016}")
        explanation_6 = MathTex(r"= 3^{3}")
        final_result  = MathTex(r"= 27")

        # Move Equation
        equation_copy = original_equation.copy()
        equation_copy.shift(UP * 3.3 + LEFT * 5)
        explanation_1.shift(UP * 3.3 + LEFT * 1.4)
        explanation_2.shift(UP * 2. + LEFT * 1.4)
        explanation_3.shift(UP * .6 + LEFT * 1.6)
        explanation_3_1.shift(UP * .6 + LEFT * 1.55)
        explanation_4.shift(DOWN * .7 + LEFT * 2.65)
        explanation_5.shift(DOWN * 1.8 + LEFT * 2.15)
        explanation_6.shift(DOWN * 2.5 + LEFT * 3)
        final_result.shift(DOWN * 3.1 + LEFT * 2.97)

        self.play(Write(original_equation))
        self.wait(1.5)
        self.play(Indicate(original_equation))
        self.play(Transform(original_equation, equation_copy))
        self.wait(1.5)

        self.play(Write(explanation_1))
        self.wait(1.5)

        self.play(Write(explanation_2))
        self.wait(1.5)

        self.play(Write(explanation_3))
        self.wait(.5)
        self.remove(explanation_3)
        self.play(Transform(explanation_3, explanation_3_1))
        self.wait(.5)
        self.play(Circumscribe(explanation_3_1[2]))
        self.wait(1.5)

        self.play(Write(explanation_4))
        self.wait(1.5)

        self.play(Write(explanation_5))
        self.wait(1.5)

        self.play(Write(explanation_6))
        self.wait(1.5)

        self.play(Write(final_result))
        self.wait(1.5)