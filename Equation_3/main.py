from manim import *

class Solve_3 (Scene):
    def construct(self):
        equation = MathTex(r'\sqrt{3x + \sqrt{3x + \sqrt{3x + \sqrt{3x + \ldots}}}} = 15',  r'&=> \sqrt{3x + 15} = 15', r'\\ &=> (\sqrt{3x + 15})^{2} = 15^{2}', r'\\ &=> 3x + 15 = 225', r'\\ &=> 3x = 225 - 15',  r'\\ &=> 3x = 210', r'\\ &=>x = 70', font_size=36)
        equation.shift(UP * 1)

        self.play(Write(equation[0]))
        self.wait(1.5)

        Concluse = MathTex(r'&Because', r'\\&\sqrt{3x + \sqrt{3x + \sqrt{3x + \sqrt{3x + \ldots}}}} = 15', r'\\&So', r'\\ &\sqrt{3x + \sqrt{3x + \sqrt{3x + \sqrt{3x + \ldots}}}} = 15', r' => \sqrt{3x + 15} = 15',  font_size=36)
        Concluse.shift(DOWN * 1)
        self.play(Write(Concluse[0]))
        self.wait(.5)
        self.play(Write(Concluse[1]))
        self.play(Circumscribe(Concluse[1][:20]))
        self.play(Circumscribe(Concluse[1][24:27]))
        self.wait(.5)
        self.play(Write(Concluse[2]))
        self.wait(1.5)
        self.play(Write(Concluse[3]))
        self.wait(1.5)
        self.play(Write(Concluse[4]))
        self.wait(1.5)
        self.remove(Concluse[0])
        self.remove(Concluse[1])
        self.remove(Concluse[2])
        self.remove(Concluse[3])
        self.remove(Concluse[4])

        self.play(Write(equation[1]))
        self.wait(1.5)

        for i in range(2, len(equation)):
            self.play(Write(equation[i]))
            self.wait(1.5)
