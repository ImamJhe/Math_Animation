from manim import *
class Euler_Graph(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(x_range=[-2, 2],
                        y_range=[-2, 2],
                        z_range=[0, 5],
                        x_length=6,
                        y_length=6,
                        z_length=6,
                        x_axis_config={"include_numbers": False},
                        y_axis_config={"include_numbers": False},
                        z_axis_config={"include_numbers": False}
                        )

        curve_euler = ParametricFunction(
            lambda u: np.array([
                1.5 * np.sin(np.pi * u),
                1.5 * np.cos(np.pi * u),
                u * 0.8
            ]), color=WHITE, t_range=np.array([0, 3])
        ).set_shade_in_3d(True)

        curve_sin_cos = ParametricFunction(
            lambda u: np.array([
                1.5 * np.sin(np.pi * u),
                1.5 * np.cos(np.pi * u),
                u * 0.8
            ]), color=WHITE, t_range=np.array([3, 6])
        ).set_shade_in_3d(True)

        Euler = MathTex(r'z = e^{i \cdot \pi \cdot t},\, t \in [0,1]', font_size=16).scale(2).set_shade_in_3d(True)
        text_x = MathTex("x = Re(z)", font_size=16).scale(2).set_shade_in_3d(True)
        text_y = MathTex("y = Im(z)", font_size=16).scale(2).set_shade_in_3d(True)

        Euler.rotate(0, axis=OUT)
        text_x.rotate(-PI / 2, axis=UP)
        text_x.rotate(-PI / 2, axis=OUT)
        text_y.rotate(-PI/2, axis=UP)

        text_x.shift(3 * RIGHT + OUT)
        text_y.shift(3*UP + OUT)
        Euler.shift(UP + RIGHT * 3)

        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, gamma=0, focal_distance=1000,
                                    frame_center=ax)

        self.play(Create(ax))
        self.play(Create(curve_euler))

        self.play(Create(Euler))
        self.add(text_x, text_y)

        sin = MathTex(r'x = sin(\pi t),\, t \in [0,2]', font_size=16).scale(2).set_shade_in_3d(True)
        sin_2 = MathTex(r'x = sin(\pi t),\, t \in [0,4]', font_size=16).scale(2).set_shade_in_3d(True)
        cos = MathTex(r'y = cos(\pi t),\, t \in [0,4]', font_size=16).scale(2).set_shade_in_3d(True)

        sin.rotate(-PI / 2, axis=UP)
        sin.rotate(-PI / 2, axis=OUT)
        sin.shift(2 * RIGHT + 3*OUT)

        sin_2.rotate(-PI / 2, axis=UP)
        sin_2.rotate(-PI / 2, axis=OUT)
        sin_2.shift(2 * RIGHT + 3 * OUT)

        cos.rotate(-PI / 2, axis=UP)
        cos.shift(2 * UP + 3*OUT)

        self.move_camera(phi=45 * DEGREES, theta=-135 * DEGREES, gamma=-45 * DEGREES, focal_distance=1000,
                         run_time=3,
                         frame_center=ax)

        self.move_camera(phi=90 * DEGREES, theta=-270 * DEGREES, gamma=-90 * DEGREES, focal_distance=1000,
                         run_time=1,
                         frame_center=ax)

        self.play(Create(sin, run_time=2))
        self.wait(1)
        self.play(Create(curve_sin_cos, run_time=2))
        self.play(Transform(sin, sin_2, run_time=2))

        self.move_camera(phi=45 * DEGREES, theta=-135 * DEGREES, gamma=-45 * DEGREES, focal_distance=1000,
                         run_time=3,
                         frame_center=ax)

        self.move_camera(phi=90 * DEGREES, theta=-180 * DEGREES, gamma=-90 * DEGREES, focal_distance=1000,
                         run_time=1,
                         frame_center=ax)

        self.play(Create(cos, run_time=2))
        self.wait(2)