from manim import *
from manim.mobject.geometry.line import TangentLine

class DerivativeIntegralConnection(Scene):
    def construct(self):

        # ===============================
        # DISTANCE GRAPH
        # ===============================

        axes1 = Axes(
            x_range=[0,5],
            y_range=[0,13],
            x_length=5,
            y_length=4,
            tips=False
        ).to_edge(LEFT)

        labels1 = axes1.get_axis_labels("t","s(t)")
        dist_graph = axes1.plot(lambda x: 0.5*x**2, color=BLUE)

        self.play(Create(axes1), Write(labels1))
        self.play(Create(dist_graph))

        tracker = ValueTracker(0.1)

        dot = always_redraw(
            lambda: Dot(
                axes1.c2p(tracker.get_value(),0.5*tracker.get_value()**2),
                color=YELLOW
            )
        )

        tangent = always_redraw(
            lambda: TangentLine(
                dist_graph,
                alpha=(tracker.get_value() - dist_graph.t_min) / (dist_graph.t_max - dist_graph.t_min),
                length=3,
                color=RED
            )
        )

        self.add(dot, tangent)

        # ===============================
        # VELOCITY GRAPH
        # ===============================

        axes2 = Axes(
            x_range=[0,5],
            y_range=[0,5],
            x_length=5,
            y_length=4,
            tips=False
        ).to_edge(RIGHT)

        labels2 = axes2.get_axis_labels("t","v(t)")
        vel_graph = axes2.plot(lambda x: x, color=GREEN)

        self.play(Create(axes2), Write(labels2))
        self.play(Create(vel_graph))

        vel_dot = always_redraw(
            lambda: Dot(
                axes2.c2p(tracker.get_value(),tracker.get_value()),
                color=GREEN
            )
        )

        self.add(vel_dot)

        # Move time
        self.play(tracker.animate.set_value(4), run_time=5, rate_func=linear)

        self.wait()

        # ===============================
        # AREA = DISTANCE
        # ===============================

        rects = axes2.get_riemann_rectangles(
            vel_graph,
            x_range=[0,4],
            dx=0.25,
            fill_opacity=0.6
        )

        self.play(Create(rects))

        explanation = Text(
            "Each rectangle = small distance",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))

        area = axes2.get_area(vel_graph,[0,4],color=GREEN,opacity=0.5)

        self.play(Transform(rects,area))

        final = Text(
            "Area under velocity = Total distance",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(final))

        # Visual match
        vline1 = axes1.get_vertical_line(
            axes1.c2p(4,8),
            color=YELLOW
        )

        vline2 = axes2.get_vertical_line(
            axes2.c2p(4,4),
            color=YELLOW
        )

        self.play(Create(vline1),Create(vline2))

        self.wait(3)
