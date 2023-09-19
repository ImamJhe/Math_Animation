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

        equation = [
        MathTex(r"8^x = \frac{2^{56} - 4^{26}}{30}"),
        MathTex(r"8^x = \frac{2^{56} - 2^{52}}{30}"),
        MathTex(r"8^x = \frac{2^{52}(2^4 - 1)}{30}"),
        MathTex(r"8^x = \frac{2^{52}(16 - 1)}{30}"),
        MathTex(r"8^x = \frac{2^{52} \cdot 15}{30}"),
        MathTex(r"8^x = 2^{52} \cdot \frac{15}{30}"),
        MathTex(r"8^x = 2^{52} \cdot \frac{1}{2}"),
        MathTex(r"8^x = 2^{52} \cdot 2^{-1}"),
        MathTex(r"8^x = 2^{52 - 1}"),
        MathTex(r"8^x = 2^{51}"),
        MathTex(r"2^{3x} = 2^{51}"),
        MathTex(r"3x = 51"),
        MathTex(r"x = 17") ]

        self.play(Create(equation[0], run_time=3))
        self.wait()
        self.remove(equation[0])
        for i in range(0, len(equation)-1):
            self.play(Transform(equation[i], equation[i+1], run_time=2))
            self.wait()
            self.remove(equation[i])