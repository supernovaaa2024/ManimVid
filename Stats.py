# --- Animated Normal Curve: Mean and SD Changes ---
from manim import *
import numpy as np
import scipy.stats as stats

# manim -pqh Stats.py NormalDistributionReel
from manim import *
import numpy as np
from scipy import stats
from manim import *
import numpy as np
from scipy import stats

class NormalDistributionReel(Scene):
    def construct(self):
        # Configure for Instagram Reels (9:16 aspect ratio)
        self.camera.frame_height = 14
        self.camera.frame_width = 14 * 9/16
        
        # Title
        title = Text("Normal Distribution", font_size=48, weight=BOLD)
        title.set_color_by_gradient(BLUE, TEAL)
        title.to_edge(UP, buff=1.2)
        
        # Mathematical formula
        formula = MathTex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}")
        formula.set_color(WHITE).scale(0.8)
        formula.next_to(title, DOWN, buff=0.3)
        
        # Create axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 0.6, 0.1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2}
        )
        axes.shift(DOWN * 1)
        
        # Labels
        x_label = axes.get_x_axis_label("x", direction=RIGHT)
        y_label = axes.get_y_axis_label("f(x)", direction=UP)
        
        # Create the initial bell curve (μ=0, σ=1)
        bell_curve = axes.plot(
            lambda x: stats.norm.pdf(x, 0, 1),
            x_range=[-6, 6],
            color=BLUE,
            stroke_width=4
        )
        
        # Area under curve
        area = axes.get_area(
            bell_curve,
            x_range=[-6, 6],
            color=BLUE,
            opacity=0.3
        )
        
        # 68-95-99.7 rule visualization
        std_areas = []
        colors = [YELLOW, ORANGE, RED]
        ranges = [1, 2, 3]
        
        for i, (r, color) in enumerate(zip(ranges, colors)):
            std_area = axes.get_area(
                bell_curve,
                x_range=[-r, r],
                color=color,
                opacity=0.6
            )
            std_areas.append(std_area)
        
        # Percentage labels
        percentages = ["68%", "95%", "99.7%"]
        percent_labels = VGroup()
        for i, (pct, color) in enumerate(zip(percentages, colors)):
            label = Text(pct, font_size=24, weight=BOLD, color=color)
            label.move_to(axes.c2p(0, 0.45 - i*0.08))
            percent_labels.add(label)
        
        # Parameter display
        param_text = MathTex(r"\mu = 0, \sigma = 1", font_size=32, color=WHITE)
        param_text.next_to(axes, DOWN, buff=0.5)
        
        # Animation sequence - Initial setup
        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=1.5)
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1)
        self.play(Create(bell_curve), run_time=1.5)
        self.play(FadeIn(area), Write(param_text), run_time=1)
        
        # Show standard deviations
        for i, (std_area, label) in enumerate(zip(std_areas, percent_labels)):
            self.play(
                Transform(area, std_area),
                Write(label),
                run_time=1
            )
            self.wait(0.5)
        
        # Clear the percentage labels to focus on parameter changes
        self.play(
            FadeOut(percent_labels),
            Transform(area, axes.get_area(bell_curve, x_range=[-6, 6], 
                                        color=BLUE, opacity=0.3)),
            run_time=1
        )
        
        # Section 1: Changing Mean (μ)
        mean_title = Text("Changing Mean (μ)", font_size=36, weight=BOLD, color=GREEN)
        mean_title.move_to(param_text.get_center() + DOWN * 0.5)
        
        self.play(Write(mean_title), run_time=1)
        
        # Show different means
        means = [0, 2, -2, 0]
        mean_colors = [BLUE, GREEN, RED, BLUE]
        
        for i, (mu, color) in enumerate(zip(means[1:], mean_colors[1:]), 1):
            # Create new curve with different mean
            new_curve = axes.plot(
                lambda x: stats.norm.pdf(x, mu, 1),
                x_range=[-6, 6],
                color=color,
                stroke_width=4
            )
            
            new_area = axes.get_area(
                new_curve,
                x_range=[-6, 6],
                color=color,
                opacity=0.3
            )
            
            new_param_text = MathTex(f"\\mu = {mu}, \\sigma = 1", 
                                   font_size=32, color=color)
            new_param_text.next_to(axes, DOWN, buff=0.5)
            
            # Animate transformation
            self.play(
                Transform(bell_curve, new_curve),
                Transform(area, new_area),
                Transform(param_text, new_param_text),
                run_time=1.5
            )
            self.wait(0.8)
        
        self.play(FadeOut(mean_title), run_time=0.5)
        
        # Section 2: Changing Standard Deviation (σ)
        std_title = Text("Changing Std Dev (σ)", font_size=36, weight=BOLD, color=PURPLE)
        std_title.move_to(mean_title.get_center())
        
        self.play(Write(std_title), run_time=1)
        
        # Show different standard deviations (keep mean at 0)
        stds = [1, 0.5, 2, 1.5, 1]
        std_colors = [BLUE, PURPLE, ORANGE, PINK, BLUE]
        
        for i, (sigma, color) in enumerate(zip(stds[1:], std_colors[1:]), 1):
            # Create new curve with different std dev
            new_curve = axes.plot(
                lambda x: stats.norm.pdf(x, 0, sigma),
                x_range=[-6, 6],
                color=color,
                stroke_width=4
            )
            
            new_area = axes.get_area(
                new_curve,
                x_range=[-6, 6],
                color=color,
                opacity=0.3
            )
            
            new_param_text = MathTex(f"\\mu = 0, \\sigma = {sigma}", 
                                   font_size=32, color=color)
            new_param_text.next_to(axes, DOWN, buff=0.5)
            
            # Add descriptive text
            if sigma < 1:
                desc_text = Text("Narrower & Taller", font_size=24, color=color)
            elif sigma > 1:
                desc_text = Text("Wider & Shorter", font_size=24, color=color)
            else:
                desc_text = Text("Standard Normal", font_size=24, color=color)
            
            desc_text.next_to(new_param_text, DOWN, buff=0.8)
            
            # Animate transformation
            self.play(
                Transform(bell_curve, new_curve),
                Transform(area, new_area),
                Transform(param_text, new_param_text),
                run_time=1.5
            )
            self.play(Write(desc_text), run_time=0.5)
            self.wait(0.8)
            self.play(FadeOut(desc_text), run_time=0.3)
        
        self.play(FadeOut(std_title), run_time=0.5)
        
        # Section 3: Changing Both Parameters
        both_title = Text("Both μ and σ", font_size=36, weight=BOLD, color=GOLD)
        both_title.move_to(std_title.get_center())
        
        self.play(Write(both_title), run_time=1)
        
        # Show combinations of mean and std dev
        params = [(0, 1), (2, 0.8), (-1, 1.5), (1, 0.6), (0, 1)]
        combo_colors = [BLUE, GOLD, MAROON, TEAL, BLUE]
        
        for i, ((mu, sigma), color) in enumerate(zip(params[1:], combo_colors[1:]), 1):
            # Create new curve
            new_curve = axes.plot(
                lambda x: stats.norm.pdf(x, mu, sigma),
                x_range=[-6, 6],
                color=color,
                stroke_width=4
            )
            
            new_area = axes.get_area(
                new_curve,
                x_range=[-6, 6],
                color=color,
                opacity=0.3
            )
            
            new_param_text = MathTex(f"\\mu = {mu}, \\sigma = {sigma}", 
                                   font_size=32, color=color)
            new_param_text.next_to(axes, DOWN, buff=0.5)
            
            # Animate transformation
            self.play(
                Transform(bell_curve, new_curve),
                Transform(area, new_area),
                Transform(param_text, new_param_text),
                run_time=1.5
            )
            self.wait(0.8)
        
        # Final message
        self.play(FadeOut(both_title), run_time=0.5)
        
        final_message = Text("μ shifts, σ shapes!", font_size=32, weight=BOLD, color=WHITE)
        final_message.set_color_by_gradient(GREEN, PURPLE)
        final_message.next_to(param_text, DOWN, buff=0.3)
        
        self.play(Write(final_message), run_time=1)
        
        # Add sparkle effects for finale
        sparkles = VGroup()
        for _ in range(12):
            sparkle = Dot(color=GOLD, radius=0.05)
            sparkle.move_to([np.random.uniform(-2, 2), np.random.uniform(-1, 1), 0])
            sparkles.add(sparkle)
        
        self.play(
            LaggedStart(*[FadeIn(sparkle) for sparkle in sparkles]),
            lag_ratio=0.1,
            run_time=1.2
        )
        
        self.play(
            LaggedStart(*[FadeOut(sparkle) for sparkle in sparkles]),
            lag_ratio=0.05,
            run_time=0.8
        )
        
        self.wait(1.5)


# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# manim -pqh Stats.py DoubleExponentialLRT
from manim import *
import numpy as np

from manim import *
import numpy as np
from scipy import stats

# manim -pql Stats.py UniformDistributionReel
# 2. Uniform Distribution
class UniformDistributionReel(Scene):
    def construct(self):
        self.camera.frame_height = 14
        self.camera.frame_width = 14 * 9/16
        
        # Simple title without hook
        main_title = Text("Visualizing Uniform Distribution", 
                         font_size=28, color=YELLOW, weight=BOLD, font="Arial")
        main_title.move_to(ORIGIN)
        
        self.play(Write(main_title), run_time=2)
        self.wait(1)
        
        # Clear title for main content
        self.play(FadeOut(main_title), run_time=1)
        
        # Start with uniform distribution concepts FIRST
        title = Text("Uniform Distribution", font_size=32, weight=BOLD)
        title.set_color_by_gradient(GREEN, BLUE)
        title.to_edge(UP, buff=1.8)
        
        # Key concept text - introduce first
        concept_text = Text("Continuous Uniform Distribution", font_size=20, color=YELLOW, weight=BOLD, font="Arial")
        concept_text.next_to(title, DOWN, buff=0.3)
        
        # PDF integrates to 1 text - fundamental concept
        area_text = Text("PDF integrates to 1, Probability ∝ Area", font_size=16, color=WHITE, font="Arial")
        area_text.next_to(concept_text, DOWN, buff=0.3)
        
        # Mathematical definition - show early
        formula = MathTex(
            r"f(x) = \begin{cases} \frac{1}{b-a} & a \leq x \leq b \\ 0 & \text{otherwise} \end{cases}",
            font_size=18
        )
        formula.set_color(WHITE)
        formula.next_to(area_text, DOWN, buff=0.3)
        
        # Mean and variance formulas
        mean_var = MathTex(
            r"\mu = \frac{a+b}{2}, \quad \sigma^2 = \frac{(b-a)^2}{12}",
            font_size=16
        )
        mean_var.set_color(BLUE)
        mean_var.next_to(formula, DOWN, buff=0.3)
        
        # Animate core concepts first
        self.play(Write(title), run_time=1)
        self.play(Write(concept_text), run_time=1)
        self.play(Write(area_text), run_time=1)
        self.play(Write(formula), run_time=1.5)
        self.play(Write(mean_var), run_time=1.2)
        self.wait(0.8)
        
        # Now show different geometric shapes to demonstrate the concept
        shapes_group = VGroup()
        
        # Rectangle (classic uniform distribution)
        rect = Rectangle(
            width=1.8, height=0.9,
            color=GREEN, fill_opacity=0.7,
            stroke_width=3
        )
        rect.shift(LEFT * 2.8)
        rect_label = Text("Rectangle", font_size=18, color=GREEN).next_to(rect, DOWN, buff=0.3)
        
        # Circle
        circle = Circle(
            radius=0.5,  # Area = π * 0.5² ≈ 0.78
            color=BLUE, fill_opacity=0.7,
            stroke_width=3
        )
        circle.shift(UP * 0)
        circle_label = Text("Circle", font_size=18, color=BLUE).next_to(circle, DOWN, buff=0.3)
        
        # Triangle
        triangle = Polygon(
            [-0.45, -0.6, 0], [0.45, -0.6, 0], [0, 0.6, 0],  # Smaller triangle
            color=RED, fill_opacity=0.7,
            stroke_width=3
        )
        triangle.shift(RIGHT * 2.8)
        triangle_label = Text("Triangle", font_size=18, color=RED).next_to(triangle, DOWN, buff=0.3)
        
        shapes_group.add(rect, rect_label, circle, circle_label, triangle, triangle_label)
        shapes_group.next_to(mean_var, DOWN, buff=0.4)
        
        # Animate shapes appearing
        self.play(
            LaggedStart(
                Create(rect), Write(rect_label),
                Create(circle), Write(circle_label),
                Create(triangle), Write(triangle_label),
                lag_ratio=0.3
            ),
            run_time=3
        )
        
        # Probability explanation
        prob_text = Text("Equal area regions have equal probability", 
                        font_size=14, color=WHITE, font="Arial")
        prob_text.next_to(shapes_group, DOWN, buff=0.4)
        self.play(Write(prob_text), run_time=1.5)
        
        # Show uniform sampling points
        sample_points = VGroup()
        
        # Add sample points to each shape
        for shape, color in [(rect, GREEN), (circle, BLUE), (triangle, RED)]:
            for _ in range(6):  # Reduced number of points
                if shape == rect:
                    point_x = np.random.uniform(-0.9, 0.9)
                    point_y = np.random.uniform(-0.45, 0.45)
                    point = Dot([point_x, point_y, 0], color=color, radius=0.05)
                    point.shift(shape.get_center())
                elif shape == circle:
                    # Sample uniformly inside circle
                    r = np.sqrt(np.random.uniform(0, 1)) * 0.5
                    theta = np.random.uniform(0, 2*np.pi)
                    point_x = r * np.cos(theta)
                    point_y = r * np.sin(theta)
                    point = Dot([point_x, point_y, 0], color=color, radius=0.05)
                    point.shift(shape.get_center())
                else:  # triangle
                    # Sample uniformly inside triangle using barycentric coordinates
                    u, v = np.random.uniform(0, 1, 2)
                    if u + v > 1:
                        u, v = 1 - u, 1 - v
                    w = 1 - u - v
                    vertices = [[-0.45, -0.6, 0], [0.45, -0.6, 0], [0, 0.6, 0]]
                    point_pos = u * np.array(vertices[0]) + v * np.array(vertices[1]) + w * np.array(vertices[2])
                    point = Dot(point_pos, color=color, radius=0.05)
                    point.shift(shape.get_center())
                
                sample_points.add(point)
        
        self.play(
            LaggedStart(*[Create(point) for point in sample_points], lag_ratio=0.1),
            run_time=2
        )
        
        # Clear some space and add detailed explanation
        self.wait(0.5)
        
        # Key principle with formula
        principle_text = Text("Probability ∝ Area", font_size=16, color=YELLOW, weight=BOLD, font="Arial")
        principle_text.next_to(prob_text, DOWN, buff=0.3)
        self.play(Write(principle_text), run_time=1)
        
        # Probability formula for regions
        prob_formula = MathTex(
            r"P(A) = \frac{\text{Area}(A)}{\text{Area}(\text{whole shape})}",
            font_size=14
        )
        prob_formula.set_color(WHITE)
        prob_formula.next_to(principle_text, DOWN, buff=0.2)
        self.play(Write(prob_formula), run_time=1.5)
        
        # Equal area = equal probability
        equal_area_text = Text("Equal area regions → Equal probability", 
                             font_size=12, color=BLUE, font="Arial")
        equal_area_text.next_to(prob_formula, DOWN, buff=0.2)
        self.play(Write(equal_area_text), run_time=1)
        
        # Critical insight about points
        point_zero_text = Text("Single points have ZERO probability!", 
                             font_size=14, color=RED, weight=BOLD, font="Arial")
        point_zero_text.next_to(equal_area_text, DOWN, buff=0.3)
        self.play(Write(point_zero_text), run_time=1.5)
        
        # Explanation of dots
        dots_explanation = Text("Dots = finite sampling for visualization only", 
                              font_size=10, color=GRAY, font="Arial")
        dots_explanation.next_to(point_zero_text, DOWN, buff=0.2)
        self.play(Write(dots_explanation), run_time=1)
        
        # Continuous vs discrete summary
        continuous_summary = Text("Continuous: Density per unit area constant", 
                                font_size=12, color=GREEN, font="Arial")
        continuous_summary.next_to(dots_explanation, DOWN, buff=0.2)
        self.play(Write(continuous_summary), run_time=1)
        
        discrete_summary = Text("Discrete: Each dot equally likely", 
                               font_size=12, color=ORANGE, font="Arial")
        discrete_summary.next_to(continuous_summary, DOWN, buff=0.15)
        self.play(Write(discrete_summary), run_time=1)
        
        self.wait(1)
        
        # Clear explanations and show use cases
        self.play(
            FadeOut(principle_text), FadeOut(prob_formula), 
            FadeOut(equal_area_text), FadeOut(point_zero_text),
            FadeOut(dots_explanation), FadeOut(continuous_summary),
            FadeOut(discrete_summary), run_time=1
        )
        
        # USE CASES SECTION
        use_cases_title = Text("Real-World Applications", font_size=20, color=GOLD, weight=BOLD, font="Arial")
        use_cases_title.next_to(prob_text, DOWN, buff=0.4)
        self.play(Write(use_cases_title), run_time=1)
        
        # Use case 1: Random number generation
        use_case_1 = Text("🎲 Random Number Generators", font_size=14, color=BLUE, font="Arial")
        use_case_1.next_to(use_cases_title, DOWN, buff=0.2)
        self.play(Write(use_case_1), run_time=1)
        
        # Use case 2: Simulation
        use_case_2 = Text("⚡ Monte Carlo Simulations", font_size=14, color=GREEN, font="Arial")
        use_case_2.next_to(use_case_1, DOWN, buff=0.15)
        self.play(Write(use_case_2), run_time=1)
        
        # Use case 3: Modeling
        use_case_3 = Text("📊 Modeling Unknown Systems", font_size=14, color=PURPLE, font="Arial")
        use_case_3.next_to(use_case_2, DOWN, buff=0.15)
        self.play(Write(use_case_3), run_time=1)
        
        # Use case 4: Gaming
        use_case_4 = Text("🎮 Fair Gaming & Lottery Systems", font_size=14, color=RED, font="Arial")
        use_case_4.next_to(use_case_3, DOWN, buff=0.15)
        self.play(Write(use_case_4), run_time=1)
        
        # Use case 5: Statistics
        use_case_5 = Text("📈 Statistical Testing & Sampling", font_size=14, color=ORANGE, font="Arial")
        use_case_5.next_to(use_case_4, DOWN, buff=0.15)
        self.play(Write(use_case_5), run_time=1)
        
        self.wait(2)

# manim -pqh Stats.py CentralLimitTheoremMagic
class CentralLimitTheoremMagic(Scene):
    def construct(self):
        # Configure for Instagram Reels (9:16 aspect ratio)
        self.camera.frame_height = 14
        self.camera.frame_width = 14 * 9/16
        
        # Title with Dynamic Island spacing
        main_title = Text("Central Limit Theorem", font_size=32, weight=BOLD, font="Arial")
        main_title.set_color_by_gradient(PURPLE, PINK)
        main_title.to_edge(UP, buff=1.8)  # Extra buff for Dynamic Island
        
        subtitle = Text("The Magic of Statistics", font_size=24, color=YELLOW, weight=BOLD, font="Arial")
        subtitle.next_to(main_title, DOWN, buff=0.3)
        
        # Add assumptions - critical for mathematical accuracy
        assumptions = Text(
            "For i.i.d. samples with finite variance",
            font="Arial",
            font_size=14,
            color=GRAY,
            slant=ITALIC
        ).next_to(subtitle, DOWN, buff=0.2)
        
        self.play(Write(main_title), run_time=1.5)
        self.play(Write(subtitle), run_time=1)
        self.play(FadeIn(assumptions), run_time=0.8)
        self.wait(1)
        
        # Hook: Start with a weird distribution
        hook_text = Text("Start with ANY* weird distribution...", font_size=20, color=WHITE, font="Arial")
        hook_text.next_to(assumptions, DOWN, buff=0.4)
        
        # Add asterisk clarification
        asterisk_note = Text("*with finite variance", font_size=12, color=GRAY, font="Arial")
        asterisk_note.next_to(hook_text, RIGHT, buff=0.2)
        
        self.play(Write(hook_text), run_time=1.5)
        self.play(FadeIn(asterisk_note), run_time=0.8)
        self.wait(0.5)
        
        # Create original distribution (bimodal for maximum "weirdness")
        original_axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.4, 0.1],
            x_length=5,
            y_length=2.5,
            axis_config={"color": WHITE, "stroke_width": 2}
        ).scale(0.8)
        original_axes.next_to(hook_text, DOWN, buff=0.3)
        
        # Bimodal distribution (mixture of two normals)
        def bimodal_dist(x):
            return 0.3 * (np.exp(-(x+1.5)**2/0.5) + np.exp(-(x-1.5)**2/0.5))
        
        original_curve = original_axes.plot(
            bimodal_dist,
            x_range=[-4, 4],
            color=RED,
            stroke_width=4
        )
        
        original_area = original_axes.get_area(
            original_curve,
            x_range=[-4, 4],
            color=RED,
            opacity=0.3
        )
        
        original_label = Text("Weird Bimodal Distribution", font_size=16, color=RED, font="Arial")
        original_label.next_to(original_axes, DOWN, buff=0.2)
        
        self.play(Create(original_axes), run_time=1)
        self.play(Create(original_curve), FadeIn(original_area), run_time=1.5)
        self.play(Write(original_label), run_time=1)
        
        # Add some sample points to show the original distribution
        sample_dots = VGroup()
        np.random.seed(42)  # For reproducibility
        for _ in range(20):
            # Generate bimodal samples
            if np.random.random() < 0.5:
                x_val = np.random.normal(-1.5, 0.7)
            else:
                x_val = np.random.normal(1.5, 0.7)
            
            if -4 <= x_val <= 4:
                y_val = bimodal_dist(x_val) + np.random.uniform(-0.02, 0.02)
                dot = Dot(original_axes.c2p(x_val, y_val), color=RED, radius=0.03)
                sample_dots.add(dot)
        
        self.play(
            LaggedStart(*[Create(dot) for dot in sample_dots], lag_ratio=0.1),
            run_time=2
        )
        self.wait(1)
        
        # Magic announcement
        magic_text = Text("✨ Watch the MAGIC happen! ✨", font_size=22, color=GOLD, weight=BOLD, font="Arial")
        magic_text.next_to(original_label, DOWN, buff=0.4)
        self.play(Write(magic_text), run_time=1.5)
        self.wait(0.5)
        
        # Clear for CLT demonstration
        self.play(
            FadeOut(VGroup(hook_text, asterisk_note, original_axes, original_curve, original_area, 
                          original_label, sample_dots, magic_text)),
            run_time=1
        )
        
        # CLT Explanation - Simple hook for the visual demonstration
        # Position below assumptions to avoid overlap
        clt_explanation = Text(
            "Watch how ANY distribution becomes normal \nwhen we look at sample means!", 
            font_size=14, color=WHITE, font="Arial"
        )
        clt_explanation.next_to(assumptions, DOWN, buff=0.8)
        self.play(Write(clt_explanation), run_time=1.5)
        
        # Set up side-by-side comparison
        # Left: Original distribution, Right: Sample means distribution
        left_title = Text("Original Distribution", font_size=16, color=RED, font="Arial")
        left_title.move_to([-1.5, 1.5, 0])
        
        right_title = Text("Sample Means", font_size=16, color=BLUE, font="Arial")
        right_title.move_to([1.5, 1.5, 0])
        
        self.play(Write(left_title), Write(right_title), run_time=1)
        
        # Create axes for both distributions
        left_axes = Axes(
            x_range=[-4, 4, 2],
            y_range=[0, 0.4, 0.2],
            x_length=3,
            y_length=2,
            axis_config={"color": WHITE, "stroke_width": 1}
        )
        left_axes.move_to([-1.5, -0.5, 0])
        
        right_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[0, 1.5, 0.5],
            x_length=3,
            y_length=2,
            axis_config={"color": WHITE, "stroke_width": 1}
        )
        right_axes.move_to([1.5, -0.5, 0])
        
        self.play(Create(left_axes), Create(right_axes), run_time=1)
        
        # Show original distribution on left
        left_curve = left_axes.plot(bimodal_dist, x_range=[-4, 4], color=RED, stroke_width=3)
        left_area = left_axes.get_area(left_curve, x_range=[-4, 4], color=RED, opacity=0.3)
        
        self.play(Create(left_curve), FadeIn(left_area), run_time=1)
        
        # Animate sampling process with increasing sample sizes
        sample_sizes = [1, 2, 5, 10, 30]
        colors = [ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        
        sample_means_data = []
        
        for i, (n, color) in enumerate(zip(sample_sizes, colors)):
            # Generate sample means
            np.random.seed(42 + i)  # Different seed for each sample size
            means = []
            
            for _ in range(1000):  # 1000 sample means
                # Generate n samples from bimodal distribution
                samples = []
                for _ in range(n):
                    if np.random.random() < 0.5:
                        sample = np.random.normal(-1.5, 0.7)
                    else:
                        sample = np.random.normal(1.5, 0.7)
                    samples.append(sample)
                
                sample_mean = np.mean(samples)
                if -2 <= sample_mean <= 2:  # Keep within range
                    means.append(sample_mean)
            
            sample_means_data.append((means, color, n))
            
            # Show sample size with convergence information
            n_text = Text(f"Sample Size: n = {n}", font_size=18, color=color, weight=BOLD, font="Arial")
            
            # Add convergence quality indicator
            if n >= 30:
                convergence_note = Text("✓ Good approximation", font_size=12, color=GREEN, font="Arial")
            elif n >= 10:
                convergence_note = Text("~ Fair approximation", font_size=12, color=YELLOW, font="Arial") 
            else:
                convergence_note = Text("⚠ Poor approximation", font_size=12, color=ORANGE, font="Arial")
            
            n_group = VGroup(n_text, convergence_note)
            n_group.arrange(DOWN, buff=0.1)
            n_group.next_to(clt_explanation, DOWN, buff=0.3)
            
            if i > 0:
                self.play(Transform(prev_n_group, n_group), run_time=0.5)
            else:
                self.play(Write(n_group), run_time=0.5)
                prev_n_group = n_group
            
            # Create histogram of sample means
            hist_bars = VGroup()
            
            # Calculate histogram
            hist, bin_edges = np.histogram(means, bins=20, range=(-2, 2), density=True)
            bin_width = bin_edges[1] - bin_edges[0]
            
            for j, (height, edge) in enumerate(zip(hist, bin_edges[:-1])):
                if height > 0:
                    bar_height = height * 0.8  # Scale for visibility
                    bar = Rectangle(
                        width=bin_width * right_axes.x_length / 4,  # Scale to axes
                        height=bar_height * right_axes.y_length / 1.5,
                        color=color,
                        fill_opacity=0.7,
                        stroke_width=1
                    )
                    bar_center_x = edge + bin_width/2
                    bar.move_to(right_axes.c2p(bar_center_x, bar_height/2))
                    hist_bars.add(bar)
            
            # Calculate theoretical normal curve for comparison
            theoretical_mean = 0  # Population mean of bimodal distribution
            theoretical_std = 1.68 / np.sqrt(n)  # Approximate standard error
            
            x_vals = np.linspace(-2, 2, 100)
            y_vals = (1 / (theoretical_std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_vals - theoretical_mean) / theoretical_std) ** 2)
            
            # Scale to match histogram scale
            y_vals = y_vals * 0.8
            
            normal_curve = right_axes.plot_line_graph(
                x_values=x_vals,
                y_values=y_vals,
                line_color=RED,
                stroke_width=3,
                add_vertex_dots=False
            )
            
            # Animate the histogram
            if i == 0:
                self.play(
                    LaggedStart(*[Create(bar) for bar in hist_bars], lag_ratio=0.02),
                    run_time=1.5
                )
                prev_hist = hist_bars
                
                # Add theoretical curve for comparison (starts faint)
                normal_curve.set_stroke(opacity=0.3)
                self.play(Create(normal_curve), run_time=1)
                prev_curve = normal_curve
                
            else:
                # Increase opacity of normal curve as n increases
                curve_opacity = min(0.9, 0.3 + (i * 0.15))
                normal_curve.set_stroke(opacity=curve_opacity)
                
                self.play(
                    Transform(prev_hist, hist_bars),
                    Transform(prev_curve, normal_curve),
                    run_time=1.2
                )
            
            # Add normal curve overlay for larger sample sizes
            if n >= 10:
                # Calculate sample mean and standard error
                sample_mean = np.mean(means)
                sample_std = np.std(means)
                
                def normal_overlay(x):
                    return (1/(sample_std * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-sample_mean)/sample_std)**2)
                
                normal_curve = right_axes.plot(
                    normal_overlay,
                    x_range=[-2, 2],
                    color=WHITE,
                    stroke_width=3
                )
                
                if n == 10:
                    self.play(Create(normal_curve), run_time=1)
                    prev_normal = normal_curve
                else:
                    self.play(Transform(prev_normal, normal_curve), run_time=1)
            
            self.wait(0.8)
        
        # Final revelation
        self.play(FadeOut(prev_n_group), run_time=0.5)
        
        # Add all persistent text elements to clear list  
        elements_to_clear = [main_title, subtitle, left_title, right_title, left_axes, right_axes, 
                           left_curve, left_area, prev_hist, prev_curve, clt_explanation, assumptions]
        
        # Add prev_normal if it exists (for n >= 10)
        try:
            elements_to_clear.append(prev_normal)
        except:
            pass
            
        self.play(
            FadeOut(VGroup(*elements_to_clear)),
            run_time=1
        )
        
        # Position revelation text at very top after clearing everything
        revelation_text = Text("NORMAL DISTRIBUTION!", font_size=22, color=GOLD, weight=BOLD, font="Arial")
        revelation_text.move_to([0, 5.5, 0])  # Higher position since we cleared titles
        self.play(Write(revelation_text), run_time=1.5)
        
        # Key insights - mathematically precise, smaller font
        insights = [
            "• Exact: X̄ ~ N(μ, σ²/n) if Xi ~ N(μ, σ²)",
            "• Asymptotic: √n(X̄ - μ) →d N(0, σ²)", 
            "• Unbiased: E[X̄] = μ, Var(X̄) = σ²/n",
            "• Convergence rate: O(n^(-1/2)) by Berry-Esseen"
        ]
        
        insight_group = VGroup()
        for insight in insights:
            insight_text = Text(insight, font_size=11, color=WHITE, font="Arial")  # Smaller font
            insight_group.add(insight_text)
        
        insight_group.arrange(DOWN, buff=0.08, aligned_edge=LEFT)  # Tighter spacing
        insight_group.next_to(revelation_text, DOWN, buff=0.25)  # Reduced spacing
        
        for insight in insight_group:
            self.play(Write(insight), run_time=0.8)
        
        # Final formula with asymptotic notation - larger and bolder
        formula_title = Text("Asymptotic Result:", font_size=18, color=GRAY, font="Arial", weight=BOLD)
        clt_formula = MathTex(
            r"\bar{X} \xrightarrow{d} N\left(\mu, \frac{\sigma}{\sqrt{n}}\right) \text{ as } n \to \infty",
            font_size=24, color=YELLOW
        )
        
        # Add approximation note
        approx_note = Text("≈ Normal for large n", font_size=16, color=GRAY, font="Arial", weight=BOLD, slant=ITALIC)
        
        formula_group = VGroup(formula_title, clt_formula, approx_note)
        formula_group.arrange(DOWN, buff=0.1)  # Adjusted spacing
        formula_group.next_to(insight_group, DOWN, buff=0.3)  # Increased spacing
        
        self.play(Write(formula_title), run_time=0.8)
        self.play(Write(clt_formula), run_time=1.5)
        self.play(Write(approx_note), run_time=0.8)
        
        # Sparkle finale - smaller and more controlled
        sparkles = VGroup()
        for _ in range(12):
            sparkle = Dot(color=GOLD, radius=0.05)
            sparkle.move_to([np.random.uniform(-2, 2), np.random.uniform(-1, 1), 0])
            sparkles.add(sparkle)
        
        self.play(
            LaggedStart(*[FadeIn(sparkle) for sparkle in sparkles]),
            lag_ratio=0.1,
            run_time=1.2
        )
        
        self.play(
            LaggedStart(*[FadeOut(sparkle) for sparkle in sparkles]),
            lag_ratio=0.05,
            run_time=0.8
        )
        
        self.wait(1)
        
        # Clear everything for rigorous mathematical formulation
        self.play(
            FadeOut(VGroup(revelation_text, insight_group, formula_group)),
            run_time=1
        )
        
        # Now present the rigorous mathematical formulation
        # Title for the rigorous section
        sampling_title = Text("Rigorous Mathematical Framework", font_size=28, color=YELLOW, weight=BOLD, font="Arial")
        sampling_title.move_to([0, 5, 0])
        
        # Setup conditions
        setup_conditions = MathTex(
            r"X_1,\ldots,X_n \text{ i.i.d. with } \mu = \mathbb{E}[X_i], \; 0 < \sigma^2 = \mathrm{Var}(X_i) < \infty",
            font_size=18
        )
        setup_conditions.next_to(sampling_title, DOWN, buff=0.4)
        
        # 1. Unbiasedness
        unbiasedness_title = Text("1. Unbiasedness", font_size=20, color=GREEN, weight=BOLD, font="Arial")
        unbiasedness_formula = MathTex(
            r"\mathbb{E}[\bar{X}] = \mu, \quad \mathrm{Var}(\bar{X}) = \frac{\sigma^2}{n} \Longrightarrow \mathrm{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}}",
            font_size=16
        )
        
        # 2. Exact Normality
        exact_title = Text("2. Exact Normality (Gaussian case)", font_size=20, color=BLUE, weight=BOLD, font="Arial")
        exact_formula = MathTex(
            r"\text{If } X_i \sim N(\mu,\sigma^2), \text{ then for every } n: \quad \bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)",
            font_size=16
        )
        
        # 3. Central Limit Theorem
        clt_title = Text("3. Central Limit Theorem (general case)", font_size=20, color=PURPLE, weight=BOLD, font="Arial")
        clt_formula1 = MathTex(
            r"\text{As } n \to \infty: \quad \sqrt{n}(\bar{X} - \mu) \xrightarrow{d} N(0, \sigma^2)",
            font_size=16
        )
        clt_equiv = MathTex(
            r"\text{equivalent to: } \bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right) \text{ for large } n",
            font_size=16
        )
        
        # 4. Rate of convergence
        rate_title = Text("4. Rate of convergence (Berry–Esseen)", font_size=20, color=ORANGE, weight=BOLD, font="Arial")
        rate_formula = MathTex(
            r"\text{If } \mathbb{E}[|X_i-\mu|^3] < \infty: \quad \sup_x |F_{\sqrt{n}(\bar{X}-\mu)/\sigma}(x) - \Phi(x)| = O(n^{-1/2})",
            font_size=14
        )
        
        # Arrange all components
        rigorous_content = VGroup(
            sampling_title,
            setup_conditions,
            unbiasedness_title,
            unbiasedness_formula,
            exact_title,
            exact_formula,
            clt_title,
            clt_formula1,
            clt_equiv,
            rate_title,
            rate_formula
        )
        rigorous_content.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        rigorous_content.move_to([0, 1, 0])
        
        # Animate the rigorous formulation
        self.play(Write(sampling_title), run_time=1.5)
        self.play(Write(setup_conditions), run_time=2)
        self.play(Write(unbiasedness_title), run_time=1)
        self.play(Write(unbiasedness_formula), run_time=1.5)
        self.play(Write(exact_title), run_time=1)
        self.play(Write(exact_formula), run_time=1.5)
        self.play(Write(clt_title), run_time=1)
        self.play(Write(clt_formula1), run_time=1.5)
        self.play(Write(clt_equiv), run_time=1.2)
        self.play(Write(rate_title), run_time=1)
        self.play(Write(rate_formula), run_time=2)
        
        self.wait(3)

# manim -pql Stats.py 
# 3. Exponential Distribution
class ExponentialDistributionReel(Scene):
    def construct(self):
        self.camera.frame_height = 14
        self.camera.frame_width = 14 * 9/16
        
        title = Text("Exponential Distribution", font_size=48, weight=BOLD)
        title.set_color_by_gradient(RED, ORANGE)
        title.to_edge(UP, buff=1.2)
        
        formula = MathTex(r"f(x) = \lambda e^{-\lambda x}, \quad x \geq 0")
        formula.set_color(WHITE).scale(0.8)
        formula.next_to(title, DOWN, buff=0.3)
        
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 2, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2}
        )
        axes.shift(DOWN * 1)
        
        # Different lambda values
        lambdas = [0.5, 1, 2]
        colors = [RED, ORANGE, YELLOW]
        
        curves = VGroup()
        areas = VGroup()
        labels = VGroup()
        
        for i, (lam, color) in enumerate(zip(lambdas, colors)):
            curve = axes.plot(
                lambda x: lam * np.exp(-lam * x),
                x_range=[0, 5],
                color=color,
                stroke_width=4
            )
            
            area = axes.get_area(
                curve,
                x_range=[0, 5],
                color=color,
                opacity=0.3
            )
            
            label = MathTex(f"\\lambda = {lam}", color=color)
            label.move_to(axes.c2p(3.5, 1.5 - i*0.3))
            
            curves.add(curve)
            areas.add(area)
            labels.add(label)
        
        # Animation
        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=1.5)
        self.play(Create(axes), run_time=1)
        
        # Show curves one by one
        for curve, area, label in zip(curves, areas, labels):
            self.play(
                Create(curve),
                FadeIn(area),
                Write(label),
                run_time=1.2
            )
            self.wait(0.5)
        
        # Highlight "memoryless" property
        memoryless_text = Text("Memoryless Property", font_size=28, color=WHITE)
        memoryless_text.next_to(axes, DOWN, buff=0.5)
        self.play(Write(memoryless_text), run_time=1)
        
        self.wait(1.5)

# manim -pql Stats.py
# 4. Beta Distribution
class BetaDistributionReel(Scene):
    def construct(self):
        self.camera.frame_height = 14
        self.camera.frame_width = 14 * 9/16
        
        title = Text("Beta Distribution", font_size=48, weight=BOLD)
        title.set_color_by_gradient(PURPLE, PINK)
        title.to_edge(UP, buff=1.2)
        
        formula = MathTex(r"f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, \quad 0 \leq x \leq 1")
        formula.set_color(WHITE).scale(0.7)
        formula.next_to(title, DOWN, buff=0.3)
        
        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 3, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2}
        )
        axes.shift(DOWN * 1)
        
        # Different parameter combinations
        params = [(1, 1), (2, 5), (5, 2), (2, 2)]
        colors = [PURPLE, PINK, BLUE, GREEN]
        
        curves = VGroup()
        labels = VGroup()
        
        for i, ((alpha, beta), color) in enumerate(zip(params, colors)):
            curve = axes.plot(
                lambda x: stats.beta.pdf(x, alpha, beta),
                x_range=[0.01, 0.99],
                color=color,
                stroke_width=4
            )
            
            label = MathTex(f"\\alpha={alpha}, \\beta={beta}", color=color, font_size=24)
            label.move_to(axes.c2p(0.7, 2.5 - i*0.4))
            
            curves.add(curve)
            labels.add(label)
        
        # Animation
        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=2)
        self.play(Create(axes), run_time=1)
        
        # Show different shapes
        for curve, label in zip(curves, labels):
            self.play(Create(curve), Write(label), run_time=1)
            self.wait(0.5)
        
        # Highlight bounded [0,1]
        bounded_text = Text("Bounded: [0, 1]", font_size=28, color=WHITE)
        bounded_text.next_to(axes, DOWN, buff=0.5)
        self.play(Write(bounded_text), run_time=1)
        
        self.wait(1.5)

# 5. Poisson Distribution (Discrete)
class PoissonDistributionReel(Scene):
    def construct(self):
        self.camera.frame_height = 14
        self.camera.frame_width = 14 * 9/16
        
        title = Text("Poisson Distribution", font_size=48, weight=BOLD)
        title.set_color_by_gradient(TEAL, BLUE)
        title.to_edge(UP, buff=1.2)
        
        formula = MathTex(r"P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}")
        formula.set_color(WHITE).scale(0.8)
        formula.next_to(title, DOWN, buff=0.3)
        
        axes = Axes(
            x_range=[0, 15, 1],
            y_range=[0, 0.4, 0.1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2}
        )
        axes.shift(DOWN * 1)
        
        # Different lambda values
        lambdas = [2, 5, 8]
        colors = [TEAL, BLUE, PURPLE]
        
        # Animation
        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=1.5)
        self.play(Create(axes), run_time=1)
        
        for lam, color in zip(lambdas, colors):
            # Create bar chart
            bars = VGroup()
            for k in range(15):
                prob = stats.poisson.pmf(k, lam)
                if prob > 0.01:  # Only show significant probabilities
                    bar = Rectangle(
                        width=0.08,
                        height=axes.y_length * prob / 0.4,
                        color=color,
                        fill_opacity=0.8,
                        stroke_width=2
                    )
                    bar.move_to(axes.c2p(k, prob/2))
                    bars.add(bar)
            
            # Lambda label
            lambda_label = MathTex(f"\\lambda = {lam}", color=color, font_size=32)
            lambda_label.next_to(axes, RIGHT, buff=0.5)
            
            self.play(
                LaggedStart(*[Create(bar) for bar in bars]),
                Write(lambda_label),
                lag_ratio=0.05,
                run_time=2
            )
            self.wait(1)
            
            if lam != lambdas[-1]:  # Don't fade out the last one
                self.play(FadeOut(bars), FadeOut(lambda_label), run_time=0.5)
        
        # Add context
        context_text = Text("Events per time period", font_size=24, color=WHITE)
        context_text.next_to(axes, DOWN, buff=0.5)
        self.play(Write(context_text), run_time=1)
        
        self.wait(1.5)

# 6. Gamma Distribution
class GammaDistributionReel(Scene):
    def construct(self):
        self.camera.frame_height = 14
        self.camera.frame_width = 14 * 9/16
        
        title = Text("Gamma Distribution", font_size=48, weight=BOLD)
        title.set_color_by_gradient(ORANGE, RED)
        title.to_edge(UP, buff=1.2)
        
        formula = MathTex(r"f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}")
        formula.set_color(WHITE).scale(0.7)
        formula.next_to(title, DOWN, buff=0.3)
        
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 0.5, 0.1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2}
        )
        axes.shift(DOWN * 1)
        
        # Different parameter combinations
        params = [(1, 1), (2, 1), (3, 1), (2, 2)]
        colors = [ORANGE, RED, PURPLE, YELLOW]
        
        curves = VGroup()
        areas = VGroup()
        labels = VGroup()
        
        for i, ((alpha, beta), color) in enumerate(zip(params, colors)):
            curve = axes.plot(
                lambda x: stats.gamma.pdf(x, alpha, scale=1/beta),
                x_range=[0.01, 10],
                color=color,
                stroke_width=4
            )
            
            area = axes.get_area(
                curve,
                x_range=[0.01, 10],
                color=color,
                opacity=0.2
            )
            
            label = MathTex(f"\\alpha={alpha}, \\beta={beta}", color=color, font_size=24)
            label.move_to(axes.c2p(7, 0.4 - i*0.06))
            
            curves.add(curve)
            areas.add(area)
            labels.add(label)
        
        # Animation
        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=2)
        self.play(Create(axes), run_time=1)
        
        # Show all curves together with staggered animation
        self.play(
            LaggedStart(*[Create(curve) for curve in curves]),
            LaggedStart(*[FadeIn(area) for area in areas]),
            LaggedStart(*[Write(label) for label in labels]),
            lag_ratio=0.3,
            run_time=3
        )
        
        # Add relationship note
        relation_text = Text("Generalizes Exponential", font_size=24, color=WHITE)
        relation_text.next_to(axes, DOWN, buff=0.5)
        self.play(Write(relation_text), run_time=1)
        
        self.wait(1.5)












class DoubleExponentialLRT(Scene):
    def construct(self):
        # Set up for vertical (reels) format
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        
        # Title
        title = Text("Likelihood Ratio Test", font_size=36, color=BLUE)
        subtitle = Text("Double Exponential Distribution", font_size=24)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=1.2)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(0.3)
        
        # Problem setup
        setup_title = Text("Problem Setup", font_size=30, color=GREEN)
        setup_title.next_to(title_group, DOWN, buff=0.8)
        
        # Distribution definition
        dist_eq = MathTex(
            r"f(x) = \frac{1}{2}\lambda e^{-\lambda|x|}",
            font_size=32
        )
        
        # Hypotheses
        h0 = MathTex(r"H_0: \lambda = \lambda_0", font_size=28)
        h1 = MathTex(r"H_1: \lambda = \lambda_1", font_size=28)
        condition = MathTex(r"\lambda_1 > \lambda_0", font_size=24, color=YELLOW)
        
        setup_group = VGroup(setup_title, dist_eq, h0, h1, condition)
        setup_group.arrange(DOWN, buff=0.4)
        setup_group.next_to(title_group, DOWN, buff=0.5)
        
        self.play(Write(setup_title))
        self.play(Write(dist_eq))
        self.play(Write(h0))
        self.play(Write(h1))
        self.play(Write(condition))
        self.wait(2)
        
        # Clear setup for likelihood derivation
        self.play(FadeOut(setup_group))
        
        # Likelihood ratio derivation
        lr_title = Text("Likelihood Ratio", font_size=30, color=GREEN)
        lr_title.next_to(title_group, DOWN, buff=0.5)
        
        # Likelihood under H0 and H1
        l0 = MathTex(
            r"\text{lik}(\lambda_0) = \left(\frac{1}{2}\lambda_0\right)^n e^{-\lambda_0\sum_{i=1}^n|x_i|}",
            font_size=24
        )
        
        l1 = MathTex(
            r"\text{lik}(\lambda_1) = \left(\frac{1}{2}\lambda_1\right)^n e^{-\lambda_1\sum_{i=1}^n|x_i|}",
            font_size=24
        )
        
        # Likelihood ratio
        lambda_ratio = MathTex(
            r"\Lambda = \frac{\text{lik}(\lambda_0)}{\text{lik}(\lambda_1)}",
            font_size=28
        )
        
        # Simplified ratio
        simplified_ratio = MathTex(
            r"\Lambda = \left(\frac{\lambda_0}{\lambda_1}\right)^n e^{(\lambda_1-\lambda_0)\sum_{i=1}^n|x_i|}",
            font_size=38
        )
        
        lr_group = VGroup(lr_title, lambda_ratio, l0, l1, simplified_ratio)
        lr_group.arrange(DOWN, buff=0.3)
        lr_group.next_to(title_group, DOWN, buff=0.3)
        
        self.play(Write(lr_title))
        self.play(Write(lambda_ratio))
        self.play(Write(l0))
        self.play(Write(l1))
        self.wait(1)
        self.play(Transform(VGroup(lambda_ratio, l0, l1), simplified_ratio))
        self.wait(2)
        
        # Clear for test derivation
        self.play(FadeOut(lr_group))
        
        # Test statistic derivation
        test_title = Text("Test Statistic", font_size=30, color=GREEN)
        test_title.next_to(title_group, DOWN, buff=0.5)
        
        # Since λ₁ > λ₀, reject H₀ when Λ ≤ c₀
        reject_condition = MathTex(
            r"\text{Since } \lambda_1 > \lambda_0, \text{ reject } H_0 \text{ when } \Lambda \leq c_0",
            font_size=22
        )
        
        # This is equivalent to
        equiv_arrow = MathTex(r"\Updownarrow", font_size=30, color=YELLOW)
        
        # Test statistic condition
        test_condition = MathTex(
            r"\sum_{i=1}^n |x_i| \leq \frac{\ln\left[\left(\frac{\lambda_1}{\lambda_0}\right)^n c_0\right]}{\lambda_1 - \lambda_0} = c",
            font_size=20
        )
        
        test_group = VGroup(test_title, reject_condition, equiv_arrow, test_condition)
        test_group.arrange(DOWN, buff=0.3)
        test_group.next_to(title_group, DOWN, buff=0.3)
        
        self.play(Write(test_title))
        self.play(Write(reject_condition))
        self.play(Write(equiv_arrow))
        self.play(Write(test_condition))
        self.wait(2)
        
        # Clear for UMP explanation
        self.play(FadeOut(test_group))
        
        # UMP explanation (Text for titles/explanations, MathTex for math)
        ump_title = Text("Most Powerful", font_size=28, color=GREEN, weight=BOLD)
        ump_title.next_to(title_group, DOWN, buff=0.5)

        # Neyman-Pearson lemma
        np_text = Text("By Neyman-Pearson Lemma:", font_size=24, color=BLUE, weight=BOLD)

        # Monotonic ratio explanation
        monotonic_text = Text("Since the likelihood ratio is monotonic in the sufficient statistic", font_size=20, color=WHITE)
        monotone_math = MathTex(r"\sum |x_i|", font_size=22, color=WHITE)
        monotonic_group = VGroup(monotonic_text, monotone_math).arrange(RIGHT, buff=0.3)

        # UMP conclusion
        ump_conclusion_text = Text("This test is UMP for", font_size=22, color=YELLOW, weight=BOLD)
        ump_conclusion_math = MathTex(r"H_1: \lambda > \lambda_0", font_size=22, color=YELLOW)
        ump_conclusion_theorem = Text("by Karlin-Rubin theorem", font_size=20, color=YELLOW)
        ump_conclusion_group = VGroup(ump_conclusion_text, ump_conclusion_math, ump_conclusion_theorem).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # Final test
        final_test = MathTex(r"\text{Reject } H_0 \text{ if } \sum_{i=1}^n |X_i| \leq c", font_size=24, color=RED)

        ump_group = VGroup(ump_title, np_text, monotonic_group, ump_conclusion_group, final_test)
        ump_group.arrange(DOWN, buff=0.4)
        ump_group.next_to(title_group, DOWN, buff=0.3)

        self.play(Write(ump_title))
        self.play(Write(np_text))
        self.play(Write(monotonic_text), Write(monotone_math))
        self.play(Write(ump_conclusion_text), Write(ump_conclusion_math), Write(ump_conclusion_theorem))
        self.wait(1)

        # Highlight final test
        final_box = SurroundingRectangle(final_test, color=RED, buff=0.2)
        self.play(Write(final_test))
        self.play(Create(final_box))
        self.wait(2)
        
        # Visual representation of the test
        self.play(FadeOut(ump_group), FadeOut(final_box))
        
        # Create a visual representation
        visual_title = Text("Test Visualization", font_size=28, color=GREEN)
        visual_title.next_to(title_group, DOWN, buff=0.5)
        
        # Create axes for the test statistic distribution
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 0.8, 0.2],
            x_length=6,
            y_length=3,
            axis_config={"color": BLUE},
        ).scale(0.7)
        
        # Exponential-like curve for the distribution of sum of |Xi|
        def dist_func(x):
            return 0.6 * np.exp(-x/2) if x >= 0 else 0
        
        curve = axes.plot(dist_func, color=WHITE, x_range=[0, 6])
        
        # Critical value line
        c_line = axes.get_vertical_line(axes.c2p(2, 0), color=RED, stroke_width=3)
        c_label = MathTex("c", color=RED).next_to(c_line, UP)
        
        # Rejection region
        rejection_area = axes.get_area(
            curve, x_range=[0, 2], color=RED, opacity=0.3
        )
        
        # Labels
        x_label = axes.get_x_axis_label(r"\sum |X_i|")
        reject_label = Text("Reject H₀", font_size=16, color=RED).next_to(rejection_area, DOWN)
        
        visual_group = VGroup(visual_title, axes, curve, c_line, c_label, 
                            rejection_area, x_label, reject_label)
        visual_group.next_to(title_group, DOWN, buff=0.2)
        
        self.play(Write(visual_title))
        self.play(Create(axes))
        self.play(Create(curve))
        self.play(Create(c_line), Write(c_label))
        self.play(FadeIn(rejection_area))
        self.play(Write(x_label), Write(reject_label))

        # Final summary
        self.play(FadeOut(visual_group))

        summary_title = Text("Summary", font_size=44, color=GREEN, weight=BOLD)
        summary_title.next_to(title_group, DOWN, buff=0.5)

        summary_points = VGroup(
            MathTex(r"\text{• Likelihood ratio test derived}", font_size=24),
            MathTex(r"\text{• Test statistic: } \sum |X_i|", font_size=24),
            MathTex(r"\text{• Reject } H_0 \text{ if } \sum |X_i| \leq c", font_size=24),
            MathTex(r"\text{• UMP test for } \lambda > \lambda_0", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        summary_group = VGroup(summary_title, summary_points)
        summary_group.arrange(DOWN, buff=0.5)
        summary_group.next_to(title_group, DOWN, buff=0.3)

        self.play(Write(summary_title))
        for point in summary_points:
            self.play(Write(point))
            self.wait(0.5)

        self.wait(1)

        # Add explanation about c and false positive rate (after summary)
        c_expl_line1 = Text(
            "c is chosen so the probability of false positive (Type I error)",
            font_size=18, color=WHITE
        )
        c_expl_line2 = VGroup(
            Text("is less than or equal to the significance level", font_size=18, color=WHITE),
            MathTex(r"\alpha", font_size=22, color=YELLOW)
        ).arrange(RIGHT, buff=0.08)
        c_expl_group = VGroup(c_expl_line1, c_expl_line2).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        c_expl_box = SurroundingRectangle(c_expl_group, color=TEAL_A, buff=0.12)
        c_expl_vgroup = VGroup(c_expl_group, c_expl_box)
        c_expl_vgroup.next_to(summary_group, DOWN, buff=0.12)

        self.play(FadeIn(c_expl_vgroup), run_time=1.2)
        self.wait(2)



class CoinFlipHypothesisTest(Scene):
    PRIMARY_COLOR = "#FF6B6B"
    SECONDARY_COLOR = "#4ECDC4"
    ACCENT_COLOR = "#45B7D1"
    SUCCESS_COLOR = "#98D8C8"
    WARNING_COLOR = "#FFD93D"
    REJECT_COLOR = "#FF4757"
    TEXT_COLOR = WHITE

    def construct(self):
        # Set up vertical format for Instagram reels
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        
        # Main title
        main_title = Text("Hypothesis Testing", font_size=48, color=self.PRIMARY_COLOR, weight=BOLD)
        main_title.to_edge(UP, buff=0.8)

        self.play(Write(main_title), run_time=1.5)

        # Problem statement
        problem_title = Text("Problem 1", font_size=36, color=self.SECONDARY_COLOR, weight=BOLD)
        problem_title.next_to(main_title, DOWN, buff=0.5)

        self.play(Write(problem_title), run_time=1)

        # Problem setup
        setup_text = Text("Coin thrown 10 times independently", font_size=28, color=self.TEXT_COLOR)
        setup_text.next_to(problem_title, DOWN, buff=0.6)

        self.play(Write(setup_text), run_time=1.5)

        # Hypotheses
        hypothesis_h0 = MathTex(
            r"H_0: p = \frac{1}{2}",
            font_size=32,
            color=self.ACCENT_COLOR
        )
        hypothesis_h1 = MathTex(
            r"H_1: p \neq \frac{1}{2}",
            font_size=32,
            color=self.ACCENT_COLOR
        )

        hypotheses_group = VGroup(hypothesis_h0, hypothesis_h1).arrange(RIGHT, buff=1.5)
        hypotheses_group.next_to(setup_text, DOWN, buff=0.6)

        self.play(Write(hypothesis_h0), run_time=1.5)
        self.play(Write(hypothesis_h1), run_time=1.5)

        # Rejection rule
        rejection_text = Text("Reject H₀ if 0 or 10 heads observed", font_size=26, color=self.REJECT_COLOR)
        rejection_text.next_to(hypotheses_group, DOWN, buff=0.6)

        self.play(Write(rejection_text), run_time=1.5)
        self.wait(1)

        # Questions
        questions = [
            "a. What is the significance level?",
            "b. If p = 0.1, what is the power?"
        ]

        question_objects = []
        for i, q in enumerate(questions):
            q_text = Text(q, font_size=28, color=self.TEXT_COLOR)
            question_objects.append(q_text)

        questions_group = VGroup(*question_objects).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        questions_group.next_to(rejection_text, DOWN, buff=0.8)

        for q in question_objects:
            self.play(Write(q), run_time=1.2)

        self.wait(2)

        # Clear screen for solutions
        self.play(FadeOut(VGroup(setup_text, hypotheses_group, rejection_text, questions_group)), run_time=1)

        # Solution Part A: Significance Level
        self.solve_part_a(main_title, problem_title)

        # Solution Part B: Power
        self.solve_part_b(main_title, problem_title)

        # Final summary
        self.show_summary(main_title)

    def solve_part_a(self, main_title, problem_title):
        # Part A title
        part_a_title = Text("Part A: Significance Level (α)", font_size=36, color=self.PRIMARY_COLOR, weight=BOLD)
        part_a_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_a_title), run_time=1.5)
        
        # Definition of significance level
        alpha_def = MathTex(
            r"\alpha = P(\text{rejecting } H_0 | H_0 \text{ is true})",
            font_size=28,
            color=self.ACCENT_COLOR
        )
        alpha_def.next_to(part_a_title, DOWN, buff=0.6)
        
        self.play(Write(alpha_def), run_time=2)
        
        # Breaking it down
        breakdown = MathTex(
            r"= P(0 \text{ heads} | H_0) + P(10 \text{ heads} | H_0)",
            font_size=26,
            color=self.TEXT_COLOR
        )
        breakdown.next_to(alpha_def, DOWN, buff=0.5)
        
        self.play(Write(breakdown), run_time=1.8)
        
        # Binomial calculation
        binomial_calc = MathTex(
            r"= \binom{10}{0}\left(\frac{1}{2}\right)^{10} + \binom{10}{10}\left(\frac{1}{2}\right)^{10}",
            font_size=24,
            color=self.TEXT_COLOR
        )
        binomial_calc.next_to(breakdown, DOWN, buff=0.5)
        
        self.play(Write(binomial_calc), run_time=2.5)
        
        # Simplification
        simplification = MathTex(
            r"= \left(\frac{1}{2}\right)^{10} + \left(\frac{1}{2}\right)^{10} = 2\left(\frac{1}{2}\right)^{10}",
            font_size=26,
            color=self.TEXT_COLOR
        )
        simplification.next_to(binomial_calc, DOWN, buff=0.5)
        
        self.play(Write(simplification), run_time=2)
        
        # Final calculation
        final_calc = MathTex(
            r"= \left(\frac{1}{2}\right)^9 = \frac{1}{512} \approx 0.00195",
            font_size=28,
            color=self.TEXT_COLOR
        )
        final_calc.next_to(simplification, DOWN, buff=0.5)
        
        self.play(Write(final_calc), run_time=2)
        
        # Final result for part A
        result_a = MathTex(
            r"\alpha = 0.00195",
            font_size=36,
            color=self.SUCCESS_COLOR
        )
        result_a.next_to(final_calc, DOWN, buff=0.6)
        
        result_box_a = SurroundingRectangle(
            result_a, 
            color=self.SUCCESS_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(result_a), run_time=2)
        self.play(Create(result_box_a), run_time=1)
        self.wait(1.5)
        
        # Clear for next part
        self.play(FadeOut(VGroup(part_a_title, alpha_def, breakdown, binomial_calc, 
                                simplification, final_calc, result_a, result_box_a)), run_time=1)

    def solve_part_b(self, main_title, problem_title):
        # Part B title
        part_b_title = Text("Part B: Power (when p = 0.1)", font_size=36, color=self.PRIMARY_COLOR, weight=BOLD)
        part_b_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_b_title), run_time=1.5)
        
        # Definition of power
        power_def = MathTex(
            r"\text{Power} = 1 - \beta = P(\text{reject } H_0 | H_1 \text{ is true})",
            font_size=26,
            color=self.ACCENT_COLOR
        )
        power_def.next_to(part_b_title, DOWN, buff=0.6)
        
        self.play(Write(power_def), run_time=2)
        
        # Concept explanation
        concept_text = Text("β = False negative, Power = True positive", font_size=24, color=self.SECONDARY_COLOR)
        concept_text.next_to(power_def, DOWN, buff=0.4)
        
        self.play(Write(concept_text), run_time=1.5)
        
        # Breaking down the power calculation
        power_breakdown = MathTex(
            r"= P(0 \text{ heads} | p=0.1) + P(10 \text{ heads} | p=0.1)",
            font_size=26,
            color=self.TEXT_COLOR
        )
        power_breakdown.next_to(concept_text, DOWN, buff=0.5)
        
        self.play(Write(power_breakdown), run_time=1.8)
        
        # Binomial calculation with p = 0.1
        binomial_calc_b = MathTex(
            r"= \binom{10}{0}(0.1)^0(0.9)^{10} + \binom{10}{10}(0.1)^{10}(0.9)^0",
            font_size=22,
            color=self.TEXT_COLOR
        )
        binomial_calc_b.next_to(power_breakdown, DOWN, buff=0.5)
        
        self.play(Write(binomial_calc_b), run_time=2.5)
        
        # Simplification
        simplification_b = MathTex(
            r"= (0.9)^{10} + (0.1)^{10}",
            font_size=28,
            color=self.TEXT_COLOR
        )
        simplification_b.next_to(binomial_calc_b, DOWN, buff=0.5)
        
        self.play(Write(simplification_b), run_time=2)
        
        # Numerical calculation
        numerical_calc = MathTex(
            r"= 0.3487 + 0.0000000001 \approx 0.3487",
            font_size=26,
            color=self.TEXT_COLOR
        )
        numerical_calc.next_to(simplification_b, DOWN, buff=0.5)
        
        self.play(Write(numerical_calc), run_time=2)
        
        # Final result for part B
        result_b = MathTex(
            r"\text{Power} = 0.3487",
            font_size=36,
            color=self.SUCCESS_COLOR
        )
        result_b.next_to(numerical_calc, DOWN, buff=0.6)
        
        result_box_b = SurroundingRectangle(
            result_b, 
            color=self.SUCCESS_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(result_b), run_time=2)
        self.play(Create(result_box_b), run_time=1)
        self.wait(1.5)
        
        # Clear for summary
        self.play(FadeOut(VGroup(part_b_title, power_def, concept_text, power_breakdown, 
                                binomial_calc_b, simplification_b, numerical_calc, result_b, result_box_b)), run_time=1)

    def show_summary(self, main_title):
        # Summary title
        summary_title = Text("Summary", font_size=42, color=self.PRIMARY_COLOR, weight=BOLD)
        summary_title.next_to(main_title, DOWN, buff=1)
        
        self.play(Write(summary_title), run_time=1.5)
        
        # Hypothesis testing visual
        hypothesis_visual = VGroup(
            MathTex(r"H_0: p = \frac{1}{2}", font_size=28, color=self.ACCENT_COLOR),
            MathTex(r"H_1: p \neq \frac{1}{2}", font_size=28, color=self.ACCENT_COLOR)
        ).arrange(RIGHT, buff=1)
        hypothesis_visual.next_to(summary_title, DOWN, buff=0.6)
        
        self.play(Write(hypothesis_visual), run_time=1.5)
        
        # Rejection rule
        rejection_rule = Text("Reject if 0 or 10 heads", font_size=26, color=self.REJECT_COLOR)
        rejection_rule.next_to(hypothesis_visual, DOWN, buff=0.5)
        
        self.play(Write(rejection_rule), run_time=1.2)
        
        # Results
        results = [
            (r"a) \text{ Significance Level: } \alpha = 0.00195", self.PRIMARY_COLOR),
                       (r"b) \text{ Power (p=0.1): } 0.3487", self.SECONDARY_COLOR)
               ]
        
        result_objects = []
        for i, (result, color) in enumerate(results):
            result_math = MathTex(result, font_size=30, color=color)
            result_objects.append(result_math)
        
        results_group = VGroup(*result_objects).arrange(DOWN, buff=0.8)
        results_group.next_to(rejection_rule, DOWN, buff=0.8)
        
        # Animate each result
        for result in result_objects:
            self.play(Write(result), run_time=1.5)
            self.wait(0.5)
        
        # Add interpretation
        interpretation = Text("Very low α (strict test), moderate power", 
                            font_size=24, color=self.WARNING_COLOR)
        interpretation.next_to(results_group, DOWN, buff=0.6)
        
        self.play(Write(interpretation), run_time=1.5)
        
        # Final emphasis box
        final_box = SurroundingRectangle(
            VGroup(results_group, interpretation), 
            color=self.WARNING_COLOR, 
            buff=0.4,
            corner_radius=0.3,
            stroke_width=3
        )
        
        self.play(Create(final_box), run_time=1.5)
        
        # Closing text
        closing_text = Text("Hypothesis Test Complete!", 
                           font_size=32, color=self.WARNING_COLOR, weight=BOLD)
        closing_text.next_to(final_box, DOWN, buff=0.8)
        
        self.play(Write(closing_text), run_time=2)
        self.wait(3)
        
        # Final fade out
        self.play(FadeOut(VGroup(summary_title, hypothesis_visual, rejection_rule, 
                                results_group, interpretation, final_box, closing_text)), run_time=2)


# Version with visual distribution curves
class CoinFlipWithDistribution(Scene):
    def construct(self):
        # Set vertical format
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        
        # Title
        title = Text("Hypothesis Testing", font_size=48, weight=BOLD)
        title.set_color_by_gradient("#FF6B6B", "#4ECDC4")
        title.to_edge(UP, buff=1)
        
        self.play(Write(title), run_time=1.5)
        
        # Create distribution visualization
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 0.5, 0.1],
            x_length=6,
            y_length=3,
            axis_config={"color": WHITE, "stroke_width": 2},
        )
        axes.center().shift(UP * 2)
        
        # Normal distribution under H0
        def normal_h0(x):
            return 0.4 * np.exp(-0.5 * x**2)
        
        # Normal distribution under H1
        def normal_h1(x):
            return 0.35 * np.exp(-0.5 * (x - 1.5)**2)
        
        curve_h0 = axes.plot(normal_h0, x_range=[-3, 3], color="#4ECDC4", stroke_width=3)
        curve_h1 = axes.plot(normal_h1, x_range=[-3, 3], color="#FF6B6B", stroke_width=3)
        
        # Labels
        h0_label = MathTex("H_0", font_size=28, color="#4ECDC4")
        h0_label.next_to(curve_h0.get_center(), UP, buff=0.3)
        
        h1_label = MathTex("H_1", font_size=28, color="#FF6B6B")
        h1_label.next_to(curve_h1.get_center(), UP, buff=0.3)
        
        # Critical regions
        critical_left = axes.plot(normal_h0, x_range=[-3, -2], color="#FF4757", stroke_width=4)
        critical_right = axes.plot(normal_h0, x_range=[2, 3], color="#FF4757", stroke_width=4)
        
        self.play(Create(axes), run_time=1.5)
        self.play(Create(curve_h0), Write(h0_label), run_time=2)
        self.play(Create(curve_h1), Write(h1_label), run_time=2)
        self.play(Create(critical_left), Create(critical_right), run_time=1.5)
        
        # Add significance level annotation
        alpha_text = MathTex(r"\alpha = 0.00195", font_size=24, color="#FF4757")
        alpha_text.next_to(axes, DOWN, buff=0.5)
        
        power_text = MathTex(r"\text{Power} = 0.3487", font_size=24, color="#FF6B6B")
        power_text.next_to(alpha_text, DOWN, buff=0.3)
        
        self.play(Write(alpha_text), run_time=1)
        self.play(Write(power_text), run_time=1)
        
        self.wait(3)


# Quick version for shorter reels
class CoinFlipQuick(Scene):
    def construct(self):
        # Set vertical format
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        
        # Title
        title = Text("Coin Flip Test", font_size=48, weight=BOLD)
        title.set_color_by_gradient("#FF6B6B", "#4ECDC4")
        title.to_edge(UP, buff=1)
        
        # Quick setup
        setup = Text("10 flips, reject if 0 or 10 heads", font_size=26, color=WHITE)
        setup.next_to(title, DOWN, buff=0.5)
        
        hypotheses = MathTex(r"H_0: p = \frac{1}{2} \text{ vs } H_1: p \neq \frac{1}{2}", 
                           font_size=28, color="#45B7D1")
        hypotheses.next_to(setup, DOWN, buff=0.5)
        
        self.play(Write(title), Write(setup), Write(hypotheses), run_time=2.5)
        self.wait(1)
        
        # Quick solutions
        solutions = [
            (r"\text{Significance Level: } \alpha = \left(\frac{1}{2}\right)^9 = 0.00195", "#FF6B6B"),
            (r"\text{Power (p=0.1): } (0.9)^{10} + (0.1)^{10} = 0.3487", "#4ECDC4")
        ]
        
        y_pos = 1
        for solution, color in solutions:
            sol_math = MathTex(solution, font_size=26, color=color)
            sol_math.move_to([0, y_pos, 0])
            
            self.play(Write(sol_math), run_time=2)
            self.wait(1)
            y_pos -= 2
        
        self.wait(2)

class ParetoDistributionComplete(Scene):
    # Colors for visual appeal (class attributes)
    PRIMARY_COLOR = "#FF6B6B"
    SECONDARY_COLOR = "#4ECDC4"
    ACCENT_COLOR = "#45B7D1"
    SUCCESS_COLOR = "#98D8C8"
    WARNING_COLOR = "#FFD93D"
    TEXT_COLOR = WHITE

    def construct(self):
        # Set up vertical format for Instagram reels
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        # Main title
        main_title = Text("Pareto Distribution", font_size=48, color=self.PRIMARY_COLOR, weight=BOLD)
        main_title.to_edge(UP, buff=0.8)

        self.play(Write(main_title), run_time=1.5)

        # Problem statement
        problem_title = Text("Problem 47", font_size=36, color=self.SECONDARY_COLOR, weight=BOLD)
        problem_title.next_to(main_title, DOWN, buff=0.5)

        self.play(Write(problem_title), run_time=1)

        # PDF formula
        pdf_text = Text("Pareto PDF:", font_size=28, color=self.TEXT_COLOR)
        pdf_formula = MathTex(
            r"f(x|x_0,\theta) = \theta x_0^\theta x^{-\theta-1}",
            font_size=32,
            color=self.ACCENT_COLOR
        )
        conditions = MathTex(
            r"x \geq x_0, \quad \theta > 1",
            font_size=24,
            color=self.SECONDARY_COLOR
        )

        pdf_group = VGroup(pdf_text, pdf_formula, conditions).arrange(DOWN, buff=0.3)
        pdf_group.next_to(problem_title, DOWN, buff=0.6)

        self.play(Write(pdf_text), run_time=1)
        self.play(Write(pdf_formula), run_time=1.5)
        self.play(Write(conditions), run_time=1)
        self.wait(1)

        # Sample assumption
        sample_text = MathTex(
            r"X_1, X_2, \ldots, X_n \text{ is an i.i.d. sample}",
            font_size=28,
            color=self.TEXT_COLOR
        )
        sample_text.next_to(pdf_group, DOWN, buff=0.5)

        self.play(Write(sample_text), run_time=1.5)
        self.wait(1)

        # Questions list
        questions = [
            "a. Find the method of moments estimate of θ",
            "b. Find the MLE of θ",
            "c. Find the asymptotic variance of the MLE",
            "d. Find a sufficient statistic for θ"
        ]

        question_objects = []
        for i, q in enumerate(questions):
            q_text = Text(q, font_size=24, color=self.TEXT_COLOR)
            question_objects.append(q_text)

        questions_group = VGroup(*question_objects).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        questions_group.next_to(sample_text, DOWN, buff=0.8)

        for q in question_objects:
            self.play(Write(q), run_time=1)

        self.wait(2)

        # Clear screen for solutions
        self.play(FadeOut(VGroup(pdf_group, sample_text, questions_group)), run_time=1)

        # Solution Part A: Method of Moments
        self.solve_part_a(main_title, problem_title)

        # Solution Part B: MLE
        self.solve_part_b(main_title, problem_title)

        # Solution Part C: Asymptotic Variance
        self.solve_part_c(main_title, problem_title)

        # Solution Part D: Sufficient Statistic
        self.solve_part_d(main_title, problem_title)

        # Final summary
        self.show_summary(main_title)

    def solve_part_a(self, main_title, problem_title):
        # Part A title
        part_a_title = Text("Part A: Method of Moments", font_size=36, color=self.PRIMARY_COLOR, weight=BOLD)
        part_a_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_a_title), run_time=1.5)
        
        # Expected value calculation
        expected_value = MathTex(
            r"E(X) = \frac{\theta x_0}{\theta - 1}",
            font_size=32,
            color=self.ACCENT_COLOR
        )
        expected_value.next_to(part_a_title, DOWN, buff=0.6)
        
        self.play(Write(expected_value), run_time=1.5)
        
        # Setting equal to sample mean
        equation = MathTex(
            r"\bar{X}(\theta - 1) = \theta x_0",
            font_size=32,
            color=self.TEXT_COLOR
        )
        equation.next_to(expected_value, DOWN, buff=0.5)
        
        self.play(Write(equation), run_time=1.5)
        
        # Solving for theta
        solving = MathTex(
            r"\theta(\bar{X} - x_0) = \bar{X}",
            font_size=32,
            color=self.TEXT_COLOR
        )
        solving.next_to(equation, DOWN, buff=0.5)
        
        self.play(Write(solving), run_time=1.5)
        
        # Final result for part A
        result_a = MathTex(
            r"\hat{\theta}_{MM} = \frac{\bar{X}}{\bar{X} - x_0}",
            font_size=36,
            color=self.SUCCESS_COLOR
        )
        result_a.next_to(solving, DOWN, buff=0.6)
        
        result_box_a = SurroundingRectangle(
            result_a, 
            color=self.SUCCESS_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(result_a), run_time=2)
        self.play(Create(result_box_a), run_time=1)
        self.wait(1.5)
        
        # Clear for next part
        self.play(FadeOut(VGroup(part_a_title, expected_value, equation, solving, result_a, result_box_a)), run_time=1)

    def solve_part_b(self, main_title, problem_title):
        # Part B title
        part_b_title = Text("Part B: Maximum Likelihood", font_size=36, color=self.PRIMARY_COLOR, weight=BOLD)
        part_b_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_b_title), run_time=1.5)
        
        # Likelihood function
        likelihood = MathTex(
            r"L(\theta) = \frac{(\theta x_0^\theta)^n}{\prod_{i=1}^n x_i^{\theta+1}}",
            font_size=28,
            color=self.ACCENT_COLOR
        )
        likelihood.next_to(part_b_title, DOWN, buff=0.6)
        
        self.play(Write(likelihood), run_time=2)
        
        # Log-likelihood
        log_likelihood = MathTex(
            r"\ell(\theta) = n\log\theta + n\theta\log x_0 - (\theta+1)\sum_{i=1}^n \log x_i",
            font_size=24,
            color=self.TEXT_COLOR
        )
        log_likelihood.next_to(likelihood, DOWN, buff=0.5)
        
        self.play(Write(log_likelihood), run_time=2.5)
        
        # First derivative
        first_derivative = MathTex(
            r"\ell'(\theta) = \frac{n}{\theta} + n\log x_0 - \sum_{i=1}^n \log x_i = 0",
            font_size=26,
            color=self.TEXT_COLOR
        )
        first_derivative.next_to(log_likelihood, DOWN, buff=0.5)
        
        self.play(Write(first_derivative), run_time=2)
        
        # Solving
        solving_step = MathTex(
            r"\frac{n}{\theta} = \sum_{i=1}^n \log x_i - n\log x_0",
            font_size=28,
            color=self.TEXT_COLOR
        )
        solving_step.next_to(first_derivative, DOWN, buff=0.5)
        
        self.play(Write(solving_step), run_time=1.5)
        
        # Final MLE result
        result_b = MathTex(
            r"\hat{\theta}_{MLE} = \frac{n}{\sum_{i=1}^n \log x_i - n\log x_0}",
            font_size=32,
            color=self.SUCCESS_COLOR
        )
        result_b.next_to(solving_step, DOWN, buff=0.6)
        
        result_box_b = SurroundingRectangle(
            result_b, 
            color=self.SUCCESS_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(result_b), run_time=2)
        self.play(Create(result_box_b), run_time=1)
        self.wait(1.5)
        
        # Clear for next part
        self.play(FadeOut(VGroup(part_b_title, likelihood, log_likelihood, 
                                first_derivative, solving_step, result_b, result_box_b)), run_time=1)

    def solve_part_c(self, main_title, problem_title):
        # Part C title
        part_c_title = Text("Part C: Asymptotic Variance", font_size=36, color=self.PRIMARY_COLOR, weight=BOLD)
        part_c_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_c_title), run_time=1.5)
        
        # Explanation of asymptotic efficiency
        efficiency_text = Text("MLE is asymptotically efficient", font_size=28, color=self.SECONDARY_COLOR)
        efficiency_text.next_to(part_c_title, DOWN, buff=0.6)
        
        self.play(Write(efficiency_text), run_time=1.5)
        
        # Variance formula
        variance_formula = MathTex(
            r"\text{Var}(\hat{\theta}) \approx \frac{1}{nI(\theta)}",
            font_size=32,
            color=self.ACCENT_COLOR
        )
        variance_formula.next_to(efficiency_text, DOWN, buff=0.5)
        
        self.play(Write(variance_formula), run_time=1.5)
        
        # Fisher Information calculation
        fisher_info = MathTex(
            r"nI(\theta) = E\left[-\ell''(\theta)\right]",
            font_size=28,
            color=self.TEXT_COLOR
        )
        fisher_info.next_to(variance_formula, DOWN, buff=0.5)
        
        self.play(Write(fisher_info), run_time=1.5)
        
        # Second derivative
        second_derivative = MathTex(
            r"\ell''(\theta) = -\frac{n}{\theta^2}",
            font_size=32,
            color=self.TEXT_COLOR
        )
        second_derivative.next_to(fisher_info, DOWN, buff=0.5)
        
        self.play(Write(second_derivative), run_time=1.5)
        
        # Final variance result
        result_c = MathTex(
            r"\text{Var}(\hat{\theta}) = \frac{\theta^2}{n}",
            font_size=36,
            color=self.SUCCESS_COLOR
        )
        result_c.next_to(second_derivative, DOWN, buff=0.6)
        
        result_box_c = SurroundingRectangle(
            result_c, 
            color=self.SUCCESS_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(result_c), run_time=2)
        self.play(Create(result_box_c), run_time=1)
        self.wait(1.5)
        
        # Clear for next part
        self.play(FadeOut(VGroup(part_c_title, efficiency_text, variance_formula, 
                                fisher_info, second_derivative, result_c, result_box_c)), run_time=1)

    def solve_part_d(self, main_title, problem_title):
        # Part D title
        part_d_title = Text("Part D: Sufficient Statistic", font_size=36, color=self.PRIMARY_COLOR, weight=BOLD)
        part_d_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_d_title), run_time=1.5)
        
        # Explanation
        sufficient_text = Text("By factorization theorem:", font_size=28, color=self.SECONDARY_COLOR)
        sufficient_text.next_to(part_d_title, DOWN, buff=0.6)
        
        self.play(Write(sufficient_text), run_time=1.5)
        
        # The sufficient statistic from the MLE derivation
        statistic_explanation = MathTex(
            r"T(X_1, \ldots, X_n) = \sum_{i=1}^n \log X_i",
            font_size=32,
            color=self.ACCENT_COLOR
        )
        statistic_explanation.next_to(sufficient_text, DOWN, buff=0.6)
        
        self.play(Write(statistic_explanation), run_time=2)
        
        # Alternative form
        alternative_form = Text("or equivalently:", font_size=24, color=self.TEXT_COLOR)
        alternative_form.next_to(statistic_explanation, DOWN, buff=0.4)
        
        alternative_statistic = MathTex(
            r"T = \sum_{i=1}^n X_i",
            font_size=32,
            color=self.TEXT_COLOR
        )
        alternative_statistic.next_to(alternative_form, DOWN, buff=0.3)
        
        self.play(Write(alternative_form), run_time=1)
        self.play(Write(alternative_statistic), run_time=1.5)
        
        # Final result for part D
        result_d = MathTex(
            r"T = \sum_{i=1}^n \log X_i \text{ is sufficient for } \theta",
            font_size=28,
            color=self.SUCCESS_COLOR
        )
        result_d.next_to(alternative_statistic, DOWN, buff=0.6)
        
        result_box_d = SurroundingRectangle(
            result_d, 
            color=self.SUCCESS_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(result_d), run_time=2)
        self.play(Create(result_box_d), run_time=1)
        self.wait(1.5)
        
        # Clear for summary
        self.play(FadeOut(VGroup(part_d_title, sufficient_text, statistic_explanation, 
                                alternative_form, alternative_statistic, result_d, result_box_d)), run_time=1)

    def show_summary(self, main_title):
        # Summary title
        summary_title = Text("Summary", font_size=42, color=self.PRIMARY_COLOR, weight=BOLD)
        summary_title.next_to(main_title, DOWN, buff=1)
        
        self.play(Write(summary_title), run_time=1.5)
        
        # All results together
        results = [
            (r"a) \hat{\theta}_{MM} = \frac{\bar{X}}{\bar{X} - x_0}", self.PRIMARY_COLOR),
            (r"b) \hat{\theta}_{MLE} = \frac{n}{\sum \log x_i - n\log x_0}", self.SECONDARY_COLOR),
            (r"c) \text{Var}(\hat{\theta}) = \frac{\theta^2}{n}", self.ACCENT_COLOR),
            (r"d) T = \sum \log X_i \text{ is sufficient}", self.SUCCESS_COLOR)
        ]
        
        result_objects = []
        for i, (result, color) in enumerate(results):
            result_math = MathTex(result, font_size=26, color=color)
            result_objects.append(result_math)
        
        results_group = VGroup(*result_objects).arrange(DOWN, buff=0.6)
        results_group.next_to(summary_title, DOWN, buff=0.8)
        
        # Animate each result
        for result in result_objects:
            self.play(Write(result), run_time=1.5)
            self.wait(0.5)
        
        # Final emphasis
        final_box = SurroundingRectangle(
            results_group, 
            color=self.WARNING_COLOR, 
            buff=0.4,
            corner_radius=0.3,
            stroke_width=3
        )
        
        self.play(Create(final_box), run_time=1.5)
        
        # Closing text
        closing_text = Text("Pareto Distribution Analysis Complete!", 
                           font_size=32, color=self.WARNING_COLOR, weight=BOLD)
        closing_text.next_to(results_group, DOWN, buff=1)
        
        self.play(Write(closing_text), run_time=2)
        self.wait(3)
        
        # Final fade out
        self.play(FadeOut(VGroup(summary_title, results_group, final_box, closing_text)), run_time=2)


# --- Poisson Likelihood Ratio Test Animation for Reels ---
class PoissonLikelihoodRatioTestReel(Scene):
    def construct(self):

        # Title
        title = Text("Likelihood Ratio Test", font_size=46, weight=BOLD)
        subtitle = Text("Poisson Distribution", font_size=32, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18)
        title_group.to_edge(UP, buff=0.45)
        self.play(Write(title), Write(subtitle), run_time=0.8)
        self.wait(0.3)

        # Problem statement (corrected notation)
        problem = VGroup(
            MathTex(r"X_1, \ldots, X_n \sim \mathrm{Exp}(\theta)", font_size=28, color=WHITE),
            MathTex(r"f(x|\theta) = \theta e^{-\theta x}", font_size=30, color=BLUE),
            MathTex(r"\text{Test } H_0: \theta = \theta_0 \text{ vs } H_1: \theta \neq \theta_0", font_size=26, color=YELLOW),
            MathTex(r"\text{Show rejection region:}", font_size=22, color=WHITE),
            MathTex(r"\overline{X} e^{-\theta_0 \overline{X}} \leq c", font_size=32, color=GREEN)
        ).arrange(DOWN, buff=0.18)
        problem.next_to(title_group, DOWN, buff=0.45)
        self.play(FadeIn(problem), run_time=0.8)
        self.wait(0.5)

        # Likelihood function
        lik = MathTex(r"\text{Lik}(\theta) = \theta^n e^{-\theta \sum x_i}", font_size=28)
        lik.next_to(problem, DOWN, buff=0.35)
        self.play(Write(lik), run_time=0.7)
        self.wait(0.3)

        # Plug in θ₀ and θ₁ (MLE)
        lik_theta0 = MathTex(r"\text{Lik}(\theta_0) = \theta_0^n e^{-\theta_0 \sum x_i}", font_size=26)
        lik_theta1 = MathTex(r"\text{Lik}(\theta_1) = \theta_1^n e^{-\theta_1 \sum x_i}", font_size=26)
        lik_theta0.next_to(lik, DOWN, buff=0.22)
        lik_theta1.next_to(lik_theta0, DOWN, buff=0.18)
        self.play(Write(lik_theta0), Write(lik_theta1), run_time=0.8)
        self.wait(0.3)

        # Likelihood ratio
        ratio = MathTex(r"\Lambda = \frac{\text{Lik}(\theta_0)}{\text{Lik}(\theta_1)}", font_size=28, color=YELLOW)
        ratio.next_to(lik_theta1, DOWN, buff=0.32)
        self.play(Write(ratio), run_time=0.6)
        self.wait(0.2)

        # Substitute and simplify (split into two lines for layout)
        step1 = MathTex(r"= \frac{\theta_0^n e^{-\theta_0 \sum x_i}}{\theta_1^n e^{-\theta_1 \sum x_i}}", font_size=26)
        step2 = MathTex(r"= \left( \frac{\theta_0}{\theta_1} \right)^n e^{(\theta_1-\theta_0)\sum_{i=1}^n|x_i|}", font_size=26)
        step1.next_to(ratio, DOWN, buff=0.18)
        step2.next_to(step1, DOWN, buff=0.18)
        self.play(Write(step1), run_time=0.5)
        self.play(Write(step2), run_time=0.5)
        self.wait(0.2)

        # Use MLE: θ₁ = 1/\overline{X}, \sum x_i = n \overline{X}
        mle = MathTex(r"\theta_1 = \frac{1}{\overline{X}},\ \sum x_i = n\overline{X}", font_size=24, color=BLUE)
        mle.next_to(step2, DOWN, buff=0.18)
        self.play(Write(mle), run_time=0.5)
        self.wait(0.2)

        # Substitute MLE into ratio (split for layout)
        step3 = MathTex(r"= (\theta_0 \overline{X})^n e^{n(1-\theta_0 \overline{X})}", font_size=26, color=GREEN)
        step3.next_to(mle, DOWN, buff=0.18)
        self.play(Write(step3), run_time=0.6)
        self.wait(0.2)

        # Rejection region
        reject = MathTex(r"(\overline{X} e^{-\theta_0 \overline{X}})^n \leq c_1", font_size=28, color=YELLOW)
        reject.next_to(step3, DOWN, buff=0.22)
        self.play(Write(reject), run_time=0.5)
        self.wait(0.2)

        # Final boxed region
        final = MathTex(r"\overline{X} e^{-\theta_0 \overline{X}} \leq c", font_size=36, color=RED)
        final.next_to(reject, DOWN, buff=0.28)
        box = SurroundingRectangle(final, color=RED, buff=0.18)
        self.play(Write(final), Create(box), run_time=0.7)
        self.wait(1)

