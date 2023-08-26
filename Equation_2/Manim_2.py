from manim import *

class solve_2(Scene):
    def construct(self):
        # Intro
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
        # plane = NumberPlane()
        # self.add(plane)

        original_equation = MathTex(r"8^x = \frac{2^{56} - 4^{26}}{30}")
        Arrow = MathTex(r"=>")
        explanation_1 = MathTex(r" 8^x = \frac{2^{56} - 2^{52}}{30}")
        explanation_2 = MathTex(r" 8^x = \frac{2^{52}(2^4 - 1)}{30}")
        explanation_2_1 = MathTex(r"8^x = \frac{2^{52}(16 - 1)}{30}")
        explanation_2_2 = MathTex(r"8^x = \frac{2^{52} \cdot 15}{30}")
        explanation_2_3 = MathTex(r"8^x = 2^{52} \cdot \frac{15}{30}")
        explanation_2_4 = MathTex(r"8^x = 2^{52} \cdot \frac{1}{2}")
        explanation_3 = MathTex(r"8^x = 2^{52} \cdot 2^{-1}")
        explanation_3_1 = MathTex(r"8^x = 2^{52 - 1}")
        explanation_3_2 = MathTex(r"8^x = 2^{51}")
        explanation_4 = MathTex(r"2^{3x}",  r"=", r"2^{51}")
        explanation_5 = MathTex(r"3x = 51")
        final_result = MathTex(r"x = 17")

        # Move Equation
        equation_copy = original_equation.copy()
        left_side = 2
        equation_copy.shift(UP * 2.1 + LEFT * (5 - left_side))
        Arrow.shift(UP * 2 + LEFT * (2.6 - left_side))

        explanation_1.shift(UP * 2.1 + LEFT * (.4- left_side))

        explanation_2.shift(UP * .7 + LEFT * (.2 - left_side))
        explanation_2_1.shift(UP * .7 + LEFT * (.2 - left_side))

        explanation_2_2.shift(UP * .7 + LEFT * (.6 - left_side))
        explanation_2_3.shift(UP * .65 + LEFT * (.6 - left_side))
        explanation_2_4.shift(UP * .65 + LEFT * (.75 - left_side))

        explanation_3.shift(DOWN * .75 + LEFT * (.45 - left_side))
        explanation_3_1.shift(DOWN * .7 + LEFT * (.8 - left_side))
        explanation_3_2.shift(DOWN * .75 + LEFT * (1.1 - left_side))

        explanation_4.shift(DOWN * 1.8 + LEFT * (1.0 - left_side))
        explanation_5.shift(DOWN * 2.8 + LEFT * (1.2 - left_side))
        final_result.shift(DOWN * 2.8 + LEFT * (1.25 - left_side))

        self.play(Write(original_equation))
        self.wait(1.5)
        self.play(Indicate(original_equation))
        self.play(Transform(original_equation, equation_copy))
        self.wait(.5)

        self.play(Write(Arrow))
        self.wait(.5)
        self.play(Write(explanation_1))
        self.wait(1.5)

        self.play(Write(explanation_2))
        self.wait(1.5)
        self.remove(explanation_2)

        self.play(Transform(explanation_2, explanation_2_1))
        self.wait(1.5)
        self.remove(explanation_2)

        self.play(Transform(explanation_2_1, explanation_2_2))
        self.wait(1.5)
        self.remove(explanation_2_1)

        self.play(Transform(explanation_2_2, explanation_2_3))
        self.wait(1.5)

        self.remove(explanation_2_2)
        self.play(Transform(explanation_2_3, explanation_2_4))
        self.wait(1.5)


        self.play(Transform(explanation_2_4, explanation_3))
        self.wait(1.5)
        self.remove(explanation_2_4)

        self.play(Transform(explanation_3, explanation_3_1))
        self.wait(.5)
        self.remove(explanation_3)

        self.play(Transform(explanation_3_1, explanation_3_2))
        self.wait(.5)

        self.play(Transform(explanation_3_2, explanation_4))
        self.wait(.5)

        self.play(Circumscribe(explanation_4[0]))
        self.play(Circumscribe(explanation_4[2]))
        self.wait(.5)

        self.play(Circumscribe(explanation_4[0][1:5]))
        self.play(Circumscribe(explanation_4[2][1:5]))

        self.play(Transform(explanation_4, explanation_5))
        self.wait(.5)
        self.remove(explanation_4)
        self.play(Transform(explanation_5, final_result))
        self.wait(3)