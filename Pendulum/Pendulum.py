from manim import *
from manim.utils.rate_functions import ease_out_sine
class Pendulum(Scene):
    def construct(self):
        line1 = Line(np.array([4, 3, 0]), np.array([-4, 3, 0]))
        time = ValueTracker(0)
        initThetaS = PI / 4
        initTheta = Variable(initThetaS, r'\theta')
        l = 5
        g = 9.8
        w = np.sqrt(g / l)
        p = 2 * PI / w

        originX = 0
        originY = 3
        startPoint = Dot([originX, originY, 0], radius=0.1, color=BLUE_B)
        originShft = originX * RIGHT + originY * UP

        theta = DecimalNumber().shift(10 * UP)
        theta.add_updater(lambda m: m.set_value(initTheta.tracker.get_value() * np.sin(w * time.get_value())))

        self.add(theta)

        def getAngle(theta):
            global angle
            global thetaLabel
            if theta == 0:
                angle = VectorizedPoint().move_to(10 * UP)
                thetaLabel = VectorizedPoint().move_to(10 * UP)
            else:
                if theta > 0:
                    angle = Angle(line, verticalLine, radius=1, quadrant=(1, 1), other_angle=True, color=YELLOW_B,
                                  fill_opacity=0.5)
                else:
                    angle = Angle(line, verticalLine, radius=1, quadrant=(1, 1), other_angle=False, color=YELLOW_B,
                                  fill_opacity=0.5)
            return angle

        def getEndBall(x, y):
            endBall = Dot(fill_color=BLUE_B, fill_opacity=1).move_to(x * RIGHT + y * UP + originShft).scale(l)
            return endBall

        def getLine():
            line = Line(np.array([0, 3, 0]), ball.get_center())
            global verticalLine
            verticalLine = DashedLine(start=line.get_start(), end=line.get_start() + l * DOWN, color=WHITE)
            return line

        ball = always_redraw(lambda: getEndBall(l * np.sin(theta.get_value()), -l * np.cos(theta.get_value())))
        line = always_redraw(getLine)
        angle = always_redraw(lambda: getAngle(theta.get_value()))

        theta_value = DecimalNumber(0, num_decimal_places=1).next_to(angle, DOWN)

        theta_value.add_updater(lambda d: d.next_to(angle, DOWN))
        theta_value.add_updater(lambda d: d.set_value(np.abs(theta.get_value()*180/3.14)))

        self.play(Create(line1), Create(startPoint), Create(ball), Create(line), Create(angle), Create(verticalLine), run_time=3)
        self.play(Create(theta_value))

        self.play(time.animate.set_value(2 * p), rate_func=ease_out_sine, run_time=5)
        self.play(time.animate.set_value(4 * p), rate_func=ease_out_sine, run_time=5)

        normal = always_redraw(
            lambda: Arrow(start=[l * np.sin(theta.get_value()) + originX, -l * np.cos(theta.get_value()) + originY, 0],
                          end=[l * np.sin(theta.get_value()) + 2 * np.cos(theta.get_value()) + originX,
                               -l * np.cos(theta.get_value()) + 2 * np.sin(theta.get_value()) + originY, 0]))

        normalLabel = always_redraw(
            lambda: MathTex(r'\mid \vec{v} \mid = mg \sin(\theta)').next_to(
                ball, 0.5 * DOWN, buff=0.5).scale(1))

        self.play(Create(VGroup(normal, normalLabel)))

        self.play(time.animate.set_value(6 * p), rate_func=ease_out_sine, run_time=5)
        self.play(FadeOut(normalLabel))