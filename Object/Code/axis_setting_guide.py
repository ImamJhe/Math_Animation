from manim import *
class axis_setting_guide(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(x_range=[-2, 2],
                        y_range=[-2, 2],
                        z_range=[0, 5],
                        x_length=6,
                        y_length=6,
                        z_length=6,
                        x_axis_config={"include_numbers": False},
                        y_axis_config={"include_numbers": False},
                        z_axis_config={"include_numbers": True}
                        )

        text_x = Text("x", font_size=10).scale(2).set_shade_in_3d(True)
        text_y = Text("y", font_size=10).scale(2).set_shade_in_3d(True)
        text_z = Text("z", font_size=10).scale(2).set_shade_in_3d(True)

        text_z.rotate(PI/2, axis=UP)
        text_z.rotate(PI/2, axis=OUT)

        text_x.shift(3*RIGHT + 0.5*UP)
        text_y.shift(3*UP + 0.5*LEFT)
        text_z.shift(6*OUT + 0.5*RIGHT)

        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, gamma=0 * DEGREES,
                                    focal_distance=1000,
                                    run_time=1, frame_center=ax)

        self.play(Create(ax))
        self.add(text_x, text_y, text_z)

        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, gamma=0 * DEGREES,
                         focal_distance=1000,
                         run_time=2, frame_center=ax)

        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, gamma=-45 * DEGREES,
                         focal_distance=1000,
                         run_time=2, frame_center=ax)

        self.move_camera(phi=90 * DEGREES, theta=90 * DEGREES, gamma=-90 * DEGREES,
                         focal_distance=1000,
                         run_time=3, frame_center=ax)

