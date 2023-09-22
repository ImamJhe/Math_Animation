from manim import *

class Trigon(Scene):
    def construct(self):
        ax = Axes(x_range=[-2, 2], y_range=[-2, 2], y_length=12, x_length=12)
        circle = Circle(radius=2)
        t = ValueTracker(0)

        dot = Dot().move_to(circle.point_from_proportion((t.get_value()/100) % 1))

        line = Line(ax.coords_to_point(0, 0), dot.get_center())
        line1 = Line(np.array((dot.get_x(), 0, 0)), dot.get_center())
        line2 = Line(np.array((0, 0, 0)), np.array((2, 0, 0)))

        def dot_updater(obj, dt):
            obj.move_to(circle.point_from_proportion((t.get_value()/100) % 1))
        def update_line(obj):
            obj.become(Line(ax.coords_to_point(0, 0), dot.get_center()))
        def update_line1(obj):
            obj.become(Line(np.array((dot.get_x(), 0, 0)), dot.get_center()))
        def update_line2(obj):
            obj.become(Line(np.array((0, 0, 0)), np.array((2, 0, 0))))

        def getAngle(theta):
            global angle
            global thetaLabel
            if theta == 0:
                angle = VectorizedPoint()
            elif theta == 360:
                angle = VectorizedPoint()
            else:
                if theta > 0:
                    angle = Angle(line2, line, radius=0.6, quadrant=(1, 1))
                else:
                    angle = Angle(line2, line, radius=0.6, quadrant=(1, 1))
            return angle

        dot.add_updater(dot_updater)

        line.add_updater(update_line)
        line1.add_updater(update_line1)
        line2.add_updater(update_line2)

        angle = always_redraw(lambda: getAngle(t.get_value() * 360/100))

        def update_text():
            text = MathTex(r"\theta={:.2f}".format(t.get_value() * 360 / 100)).next_to(circle.point_from_proportion(0.15), buff=0.6)
            return text

        text = always_redraw(update_text)

        def update_all():
            sin = np.sin(t.get_value() * 360 * DEGREES / 100)
            cos = np.cos(t.get_value() * 360 * DEGREES / 100)
            tan = np.tan(t.get_value() * 360 * DEGREES / 100)

            if abs(tan) > 1000:
                tan = "{:.3e}".format(tan)
            else:
                tan = "{:.3f}".format(tan)

            all = MathTex(r"&sin(\theta)={:.3f}".format(sin),
                          r"\\ &cos(\theta)={:.3f}".format(cos),
                          r"\\ &tan(\theta)={}".format(tan)).next_to(7 * LEFT + 2 * UP)
            return all


        all = always_redraw(update_all)

        self.add(ax, circle, always_redraw(lambda: dot), line, line1, angle, text, all)
        self.play(t.animate.set_value(50), run_time=6)
        self.play(t.animate.set_value(100), run_time=6)
        self.wait()
