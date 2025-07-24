from manim import *

# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class QuadrilateralPerimeter(Scene):
    def construct(self):
        # Title - larger and more prominent for mobile
        title = Text("GRE Problem", font_size=48, weight=BOLD)
        subtitle = Text("Quadrilateral Perimeter", font_size=36, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        self.play(Write(subtitle), run_time=0.8)
        self.wait(0.5)

        # Problem Statement - more compact for mobile
        problem_text = VGroup(
            Text("Compare:", font_size=32, weight=BOLD, color=BLUE),
            Text("Quantity A: Perimeter of RSTW", font_size=28),
            Text("Quantity B: 34", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem_text.next_to(title_group, DOWN, buff=0.8)
        
        # Answer choices for quantitative comparison
        choices = VGroup(
            Text("(A) Quantity A is greater", font_size=24, color=WHITE),
            Text("(B) Quantity B is greater", font_size=24, color=GREEN, weight=BOLD), # Correct answer
            Text("(C) The two quantities are equal", font_size=24, color=WHITE),
            Text("(D) Cannot be determined", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        choices.next_to(problem_text, DOWN, buff=0.6)
        
        self.play(FadeIn(problem_text), run_time=1)
        self.wait(0.5)
        
        # Show answer choices
        for choice in choices:
            self.play(Write(choice), run_time=0.4)
        self.wait(1)

        # Clear and show coordinate system - centered for mobile
        self.play(FadeOut(VGroup(problem_text, choices)), run_time=0.5)

        # Coordinate system - larger for mobile viewing
        axes = Axes(
            x_range=[-7, 8, 2],
            y_range=[-2, 7, 2],
            x_length=6,  # Slightly smaller to give more room
            y_length=4,  # Slightly smaller to give more room
            axis_config={"color": GRAY, "stroke_width": 2}
        ).move_to(ORIGIN).shift(UP * 1)  # Move coordinate system up more
        
        # Define points
        R = axes.coords_to_point(-4, 6)
        S = axes.coords_to_point(5, 6)
        T = axes.coords_to_point(6, 1)
        W = axes.coords_to_point(-6, 1)
        
        # Create quadrilateral with animation
        quad = Polygon(R, S, T, W, color=BLUE, fill_opacity=0.3, stroke_width=4)
        
        # Point labels - larger for mobile
        R_label = MathTex("R(-4, 6)", font_size=24, color=WHITE).next_to(R, UP, buff=0.2)
        S_label = MathTex("S(5, 6)", font_size=24, color=WHITE).next_to(S, UP, buff=0.2)
        T_label = MathTex("T(6, 1)", font_size=24, color=WHITE).next_to(T, DOWN, buff=0.2)
        W_label = MathTex("W(-6, 1)", font_size=24, color=WHITE).next_to(W, DOWN, buff=0.2)
        
        self.play(Create(axes), run_time=1)
        self.play(Create(quad), run_time=1)
        self.play(Write(VGroup(R_label, S_label, T_label, W_label)), run_time=1)
        self.wait(0.5)

        # Calculate each side with highlighting - faster pacing
        calculations = []
        sides_data = [
            (Line(R, S, color=RED, stroke_width=6), MathTex(r"|RS| = 9", font_size=32, color=RED)),
            (Line(S, T, color=GREEN, stroke_width=6), MathTex(r"|ST| = \sqrt{26} \approx 5.1", font_size=32, color=GREEN)),
            (Line(T, W, color=ORANGE, stroke_width=6), MathTex(r"|TW| = 12", font_size=32, color=ORANGE)),
            (Line(W, R, color=PURPLE, stroke_width=6), MathTex(r"|WR| = \sqrt{29} \approx 5.4", font_size=32, color=PURPLE))
        ]
        
        calc_group = VGroup()
        for line, calc in sides_data:
            calc.move_to(ORIGIN).shift(DOWN * 2.5)  # Position calculation text with better spacing
            self.play(Create(line), Write(calc), run_time=0.8)
            calc_group.add(calc)
            calculations.append(calc)
            self.wait(0.3)
            self.play(FadeOut(line), FadeOut(calc), run_time=0.3)  # Fade out both line and calc

        # Show final calculation
        # No need to fade out calc_group since we're fading out each calc individually now
        
        final_calc = VGroup(
            MathTex(r"\text{Perimeter} = 9 + 5.1 + 12 + 5.4", font_size=28),
            MathTex(r"= 31.5", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.3)
        final_calc.move_to(ORIGIN).shift(DOWN * 2.5)  # Better positioning to avoid overlap
        
        self.play(Write(final_calc), run_time=1)
        self.wait(1)

        # Clear everything for conclusion
        self.play(FadeOut(VGroup(axes, quad, R_label, S_label, T_label, W_label, final_calc)), run_time=0.8)

        # Big conclusion - Instagram-friendly
        conclusion = VGroup(
            Text("31.5 < 34", font_size=48, color=GREEN, weight=BOLD),
            Text("Quantity B is greater!", font_size=36, color=BLUE),
            Text("Answer: B", font_size=44, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        conclusion.move_to(ORIGIN)
        
        for item in conclusion:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)
        
        self.wait(1.5)


class MerchantPricing(Scene):
    def construct(self):
        # Title optimized for Instagram
        title = Text("GRE Problem", font_size=48, weight=BOLD)
        subtitle = Text("Merchant Pricing", font_size=36, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), Write(subtitle), run_time=1)
        self.wait(0.5)

        # Problem Statement - simplified for mobile
        problem_text = VGroup(
            Text("A merchant bought an item for $15", font_size=28, color=WHITE),
            Text("Sold for 20% above wholesale", font_size=28, color=GREEN),
            Text("20% below suggested retail price", font_size=28, color=RED),
            Text("What was the suggested retail price?", font_size=28, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem_text.next_to(title_group, DOWN, buff=0.8)
        
        # Answer choices
        choices = VGroup(
            Text("(A) $18.00", font_size=26, color=WHITE),
            Text("(B) $20.00", font_size=26, color=WHITE),
            Text("(C) $21.50", font_size=26, color=WHITE),
            Text("(D) $22.50", font_size=26, color=GREEN, weight=BOLD), # Correct answer
            Text("(E) $24.00", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        choices.next_to(problem_text, DOWN, buff=0.6)
        
        for line in problem_text:
            self.play(Write(line), run_time=0.6)
        self.wait(0.5)
        
        # Show answer choices
        for choice in choices:
            self.play(Write(choice), run_time=0.4)
        self.wait(1)

        # Clear and show solution
        self.play(FadeOut(VGroup(problem_text, choices)), run_time=0.5)

        # Variables setup - visual and simple
        variables = VGroup(
            MathTex(r"\text{Wholesale} = \$15.00", font_size=32, color=BLUE),
            MathTex(r"\text{Selling Price} = S", font_size=32, color=GREEN),
            MathTex(r"\text{Retail Price} = R", font_size=32, color=RED)
        ).arrange(DOWN, buff=0.5)
        variables.move_to(ORIGIN).shift(UP * 2)
        
        self.play(Write(variables), run_time=1.5)
        self.wait(1)

        # Equations - step by step
        eq1 = MathTex(r"S = 15.00 \times 1.20 = \$18.00", font_size=36, color=GREEN)
        eq1.next_to(variables, DOWN, buff=0.8)
        self.play(Write(eq1), run_time=1)
        self.wait(0.8)

        eq2 = MathTex(r"S = R \times 0.80", font_size=36, color=RED)
        eq2.next_to(eq1, DOWN, buff=0.5)
        self.play(Write(eq2), run_time=1)
        self.wait(0.8)

        # Solution
        solution = VGroup(
            MathTex(r"18.00 = R \times 0.80", font_size=32),
            MathTex(r"R = \frac{18.00}{0.80}", font_size=32),
            MathTex(r"R = \$22.50", font_size=44, color=YELLOW)
        ).arrange(DOWN, buff=0.4)
        solution.next_to(eq2, DOWN, buff=0.8)
        
        for step in solution:
            self.play(Write(step), run_time=0.8)
            self.wait(0.5)

        # Clear for final answer
        self.play(FadeOut(VGroup(variables, eq1, eq2, solution[:2])), run_time=0.8)
        
        # Big final answer
        final_answer = VGroup(
            Text("Answer: D", font_size=44, color=YELLOW, weight=BOLD),
            Text("$22.50", font_size=56, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        final_answer.move_to(ORIGIN)
        
        self.play(Transform(solution[2], final_answer), run_time=1)
        self.wait(1.5)


class HotelGuests(Scene):
    def construct(self):
        # Title for Instagram
        title = Text("GRE Problem", font_size=48, weight=BOLD)
        subtitle = Text("Hotel Guests Venn Diagram", font_size=32, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), Write(subtitle), run_time=1)
        self.wait(0.5)

        # Problem - simplified for mobile
        problem = VGroup(
            Text("66 hotel guests total", font_size=32, color=WHITE),
            Text("40 enjoy dancing", font_size=32, color=BLUE),
            Text("25 enjoy swimming", font_size=32, color=RED),
            Text("6 enjoy neither", font_size=32, color=GRAY),
            Text("How many dance but don't swim?", font_size=28, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        problem.next_to(title_group, DOWN, buff=0.8)
        
        # Answer choices
        choices = VGroup(
            Text("(A) 29", font_size=26, color=WHITE),
            Text("(B) 31", font_size=26, color=WHITE),
            Text("(C) 34", font_size=26, color=WHITE),
            Text("(D) 35", font_size=26, color=GREEN, weight=BOLD), # Correct answer
            Text("(E) 40", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        choices.next_to(problem, DOWN, buff=0.6)
        
        for line in problem:
            self.play(Write(line), run_time=0.5)
        self.wait(0.5)
        
        # Show answer choices
        for choice in choices:
            self.play(Write(choice), run_time=0.4)
        self.wait(1)

        # Clear and show Venn diagram
        self.play(FadeOut(VGroup(problem, choices)), run_time=0.5)

        # Large Venn diagram for mobile - adjusted positioning
        dancing_circle = Circle(radius=1.8, color=BLUE, stroke_width=4).shift(LEFT * 0.8)
        swimming_circle = Circle(radius=1.8, color=RED, stroke_width=4).shift(RIGHT * 0.8)
        
        dancing_label = Text("Dancing", font_size=26, color=BLUE, weight=BOLD).next_to(dancing_circle, UP, buff=0.2).shift(LEFT * 0.5)
        swimming_label = Text("Swimming", font_size=26, color=RED, weight=BOLD).next_to(swimming_circle, UP, buff=0.2).shift(RIGHT * 0.5)
        
        circles_group = VGroup(dancing_circle, swimming_circle).move_to(ORIGIN).shift(UP * 0.8)
        labels_group = VGroup(dancing_label, swimming_label)
        
        self.play(Create(circles_group), Write(labels_group), run_time=1.5)
        self.wait(0.5)

        # Show equation setup
        equation_text = Text("Let x = guests who enjoy both", font_size=24, color=YELLOW)
        equation_text.next_to(circles_group, DOWN, buff=1)
        self.play(Write(equation_text), run_time=0.8)

        # Label regions with variables - adjusted for smaller circles
        dancing_only = MathTex("40-x", font_size=30, color=BLUE).move_to(dancing_circle.get_center() + LEFT * 0.8)
        both = MathTex("x", font_size=30, color=PURPLE).move_to(ORIGIN).shift(UP * 0.8)
        swimming_only = MathTex("25-x", font_size=30, color=RED).move_to(swimming_circle.get_center() + RIGHT * 0.8)
        
        self.play(Write(VGroup(dancing_only, both, swimming_only)), run_time=1)
        self.wait(0.5)

        # Show equation
        equation = MathTex(r"(40-x) + x + (25-x) = 60", font_size=32)
        equation.next_to(equation_text, DOWN, buff=0.5)
        self.play(Write(equation), run_time=1)
        self.wait(0.5)

        # Solve step by step
        solution_steps = VGroup(
            MathTex(r"65 - x = 60", font_size=32),
            MathTex(r"x = 5", font_size=40, color=GREEN)
        ).arrange(DOWN, buff=0.3)
        solution_steps.next_to(equation, DOWN, buff=0.5)
        
        for step in solution_steps:
            self.play(Write(step), run_time=0.8)
            self.wait(0.3)

        # Update diagram with solution - adjusted positions
        self.play(
            Transform(dancing_only, MathTex("35", font_size=36, color=GREEN).move_to(dancing_only)),
            Transform(both, MathTex("5", font_size=36, color=GREEN).move_to(both)),
            Transform(swimming_only, MathTex("20", font_size=36, color=GREEN).move_to(swimming_only)),
            run_time=1
        )
        self.wait(1)

        # Clear for final answer
        self.play(FadeOut(VGroup(circles_group, labels_group, equation_text, equation, solution_steps)), run_time=0.8)

        # Big final answer
        final_answer = VGroup(
            Text("Dancing but not swimming:", font_size=32, color=WHITE),
            Text("35 guests", font_size=56, color=GREEN, weight=BOLD),
            Text("Answer: D", font_size=44, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        final_answer.move_to(ORIGIN)
        
        for item in final_answer:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)
        
        self.wait(1.5)


class EquationIntercepts(Scene):
    def construct(self):
        # Title for Instagram
        title = Text("GRE Problem", font_size=48, weight=BOLD)
        subtitle = Text("Hyperbola Intercepts", font_size=32, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), Write(subtitle), run_time=1)
        self.wait(0.5)

        # Problem statement - mobile optimized
        problem = VGroup(
            Text("How many intercepts does", font_size=32, color=WHITE),
            MathTex("4x^2 - 9y^2 = 1", font_size=40, color=YELLOW),
            Text("have?", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.4)
        problem.next_to(title_group, DOWN, buff=1)
        
        # Answer choices
        choices = VGroup(
            Text("(A) 0", font_size=28, color=WHITE),
            Text("(B) 1", font_size=28, color=WHITE),
            Text("(C) 2", font_size=28, color=GREEN, weight=BOLD), # Correct answer highlighted
            Text("(D) 3", font_size=28, color=WHITE),
            Text("(E) 4", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        choices.next_to(problem, DOWN, buff=0.8)
        
        for item in problem:
            self.play(Write(item), run_time=0.8)
        self.wait(0.5)
        
        # Show answer choices
        for choice in choices:
            self.play(Write(choice), run_time=0.4)
        self.wait(1)

        # Clear and show analysis
        self.play(FadeOut(VGroup(problem, choices)), run_time=0.5)

        # Show it's a hyperbola
        hyperbola_text = Text("This is a HYPERBOLA!", font_size=36, color=BLUE, weight=BOLD)
        hyperbola_text.next_to(title_group, DOWN, buff=1)
        self.play(Write(hyperbola_text), run_time=1)
        self.wait(0.8)

        # Find x-intercepts
        x_section = VGroup(
            Text("X-intercepts (set y = 0):", font_size=28, color=BLUE, weight=BOLD),
            MathTex(r"4x^2 - 9(0)^2 = 1", font_size=32),
            MathTex(r"4x^2 = 1", font_size=32),
            MathTex(r"x = \pm \frac{1}{2}", font_size=36, color=GREEN),
            Text("✓ TWO x-intercepts", font_size=32, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        x_section.next_to(hyperbola_text, DOWN, buff=1)
        
        for item in x_section:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)

        # Find y-intercepts
        y_section = VGroup(
            Text("Y-intercepts (set x = 0):", font_size=28, color=RED, weight=BOLD),
            MathTex(r"4(0)^2 - 9y^2 = 1", font_size=32),
            MathTex(r"-9y^2 = 1", font_size=32),
            MathTex(r"y^2 = -\frac{1}{9}", font_size=32, color=RED),
            Text("✗ NO real solutions", font_size=32, color=RED, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        y_section.next_to(x_section, DOWN, buff=0.8)
        
        for item in y_section:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)

        self.wait(0.8)

        # Clear for visual
        self.play(FadeOut(VGroup(hyperbola_text, x_section, y_section)), run_time=0.8)

        # Show simple visual of hyperbola
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 3}
        ).move_to(ORIGIN).shift(UP * 0.5)
        
        # Mark x-intercepts clearly
        x_int_left = Dot(axes.coords_to_point(-0.5, 0), color=GREEN, radius=0.15)
        x_int_right = Dot(axes.coords_to_point(0.5, 0), color=GREEN, radius=0.15)
        x_labels = VGroup(
            MathTex(r"-\frac{1}{2}", font_size=24, color=GREEN).next_to(x_int_left, DOWN, buff=0.3),
            MathTex(r"\frac{1}{2}", font_size=24, color=GREEN).next_to(x_int_right, DOWN, buff=0.3)
        )
        
        # No y-intercepts indication
        no_y_text = Text("No y-intercepts", font_size=28, color=RED).next_to(axes, UP, buff=0.5)
        
        self.play(Create(axes), run_time=1)
        self.play(Create(x_int_left), Create(x_int_right), Write(x_labels), run_time=1)
        self.play(Write(no_y_text), run_time=0.8)
        self.wait(1)

        # Clear for final answer
        self.play(FadeOut(VGroup(axes, x_int_left, x_int_right, x_labels, no_y_text)), run_time=0.8)

        # Big final answer
        final_answer = VGroup(
            Text("2 x-intercepts", font_size=40, color=GREEN, weight=BOLD),
            Text("0 y-intercepts", font_size=40, color=RED, weight=BOLD),
            Text("Answer: C", font_size=48, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        final_answer.move_to(ORIGIN)
        
        for item in final_answer:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)
        
        self.wait(1.5)


class PalindromeOdometer(Scene):
    def construct(self):
        # Title for Instagram
        title = Text("GRE Problem", font_size=48, weight=BOLD)
        subtitle = Text("Palindrome Odometer", font_size=32, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), Write(subtitle), run_time=1)
        self.wait(0.5)

        # Problem - simplified for mobile
        problem = VGroup(
            Text("Car odometer starts at 2882", font_size=32, color=WHITE),
            Text("(a palindrome)", font_size=28, color=GRAY),
            Text("Travels at 55 mph", font_size=32, color=GREEN),
            Text("When is the next palindrome?", font_size=28, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        problem.next_to(title_group, DOWN, buff=1)
        
        # Answer choices
        choices = VGroup(
            Text("(A) 1.5 hours", font_size=26, color=WHITE),
            Text("(B) 2.0 hours", font_size=26, color=GREEN, weight=BOLD), # Correct answer
            Text("(C) 2.5 hours", font_size=26, color=WHITE),
            Text("(D) 3.0 hours", font_size=26, color=WHITE),
            Text("(E) 3.5 hours", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        choices.next_to(problem, DOWN, buff=0.6)
        
        for line in problem:
            self.play(Write(line), run_time=0.6)
        self.wait(0.5)
        
        # Show answer choices
        for choice in choices:
            self.play(Write(choice), run_time=0.4)
        self.wait(1)

        # Clear and show palindrome explanation
        self.play(FadeOut(VGroup(problem, choices)), run_time=0.5)

        # Palindrome explanation
        palindrome_demo = VGroup(
            Text("Palindrome = same forwards & backwards", font_size=28, color=BLUE),
            MathTex("2882 \\rightarrow 2882", font_size=36, color=GREEN),
            Text("Next palindrome: 2992", font_size=32, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        palindrome_demo.next_to(title_group, DOWN, buff=1)
        
        for item in palindrome_demo:
            self.play(Write(item), run_time=0.8)
            self.wait(0.5)

        # Show calculation
        calculation = VGroup(
            Text("Distance traveled:", font_size=28, color=WHITE),
            MathTex("2992 - 2882 = 110 \\text{ miles}", font_size=36, color=GREEN),
            Text("Time calculation:", font_size=28, color=WHITE),
            MathTex("\\text{Time} = \\frac{110 \\text{ miles}}{55 \\text{ mph}} = 2 \\text{ hours}", font_size=32, color=BLUE)
        ).arrange(DOWN, buff=0.4)
        calculation.next_to(palindrome_demo, DOWN, buff=1)
        
        for item in calculation:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)

        # Clear for visual representation
        self.play(FadeOut(VGroup(palindrome_demo, calculation)), run_time=0.8)

        # Visual odometer
        odometer_visual = VGroup(
            Text("2882", font_size=56, color=WHITE, font="monospace"),
            Text("↓", font_size=40, color=YELLOW),
            Text("110 miles", font_size=32, color=GREEN),
            Text("↓", font_size=40, color=YELLOW),
            Text("2992", font_size=56, color=GREEN, font="monospace")
        ).arrange(DOWN, buff=0.3)
        odometer_visual.move_to(ORIGIN).shift(UP * 0.5)
        
        for item in odometer_visual:
            self.play(Write(item), run_time=0.6)
            self.wait(0.2)

        # Final answer
        final_answer = VGroup(
            Text("Answer: B", font_size=44, color=YELLOW, weight=BOLD),
            Text("2.0 hours", font_size=56, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        final_answer.next_to(odometer_visual, DOWN, buff=1)
        
        for item in final_answer:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)
        
        self.wait(1.5)


class HeightStatistics(Scene):
    def construct(self):
        # Title for Instagram
        title = Text("GRE Problem", font_size=48, weight=BOLD)
        subtitle = Text("Height Statistics", font_size=32, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), Write(subtitle), run_time=1)
        self.wait(0.5)

        # Problem - simplified for mobile
        problem = VGroup(
            Text("10 people, height stats:", font_size=32, color=WHITE),
            Text("Median = 70 inches", font_size=28, color=BLUE),
            Text("Mean = 70.5 inches", font_size=28, color=GREEN),
            Text("Range = 12 inches", font_size=28, color=RED),
            Text("Add person: 74 inches tall", font_size=28, color=YELLOW),
            Text("Which statistic MUST change?", font_size=26, color=WHITE, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        problem.next_to(title_group, DOWN, buff=0.8)
        
        # Answer choices
        choices = VGroup(
            Text("(A) Mean only", font_size=26, color=GREEN, weight=BOLD), # Correct answer
            Text("(B) Median only", font_size=26, color=WHITE),
            Text("(C) Range only", font_size=26, color=WHITE),
            Text("(D) Mean and median", font_size=26, color=WHITE),
            Text("(E) All three statistics", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        choices.next_to(problem, DOWN, buff=0.6)
        
        for line in problem:
            self.play(Write(line), run_time=0.5)
        self.wait(0.5)
        
        # Show answer choices
        for choice in choices:
            self.play(Write(choice), run_time=0.4)
        self.wait(1)

        # Clear and analyze each statistic
        self.play(FadeOut(VGroup(problem, choices)), run_time=0.5)

        # Mean analysis
        mean_section = VGroup(
            Text("MEAN (Average):", font_size=36, color=GREEN, weight=BOLD),
            MathTex("\\text{Old sum} = 10 \\times 70.5 = 705", font_size=28),
            MathTex("\\text{New sum} = 705 + 74 = 779", font_size=28),
            MathTex("\\text{New mean} = \\frac{779}{11} = 70.82", font_size=32, color=GREEN),
            Text("✓ MEAN CHANGES!", font_size=32, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        mean_section.next_to(title_group, DOWN, buff=0.8)
        
        for item in mean_section:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)

        # Other statistics
        other_stats = VGroup(
            Text("MEDIAN & RANGE:", font_size=32, color=BLUE, weight=BOLD),
            Text("Median = 6th value (might not change)", font_size=24, color=BLUE),
            Text("Range might not change", font_size=24, color=RED),
            Text("✗ Don't necessarily change", font_size=28, color=GRAY)
        ).arrange(DOWN, buff=0.3)
        other_stats.next_to(mean_section, DOWN, buff=0.8)
        
        for item in other_stats:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)

        self.wait(0.8)

        # Clear for final answer
        self.play(FadeOut(VGroup(mean_section, other_stats)), run_time=0.8)

        # Big final answer
        final_answer = VGroup(
            Text("Only the MEAN", font_size=44, color=GREEN, weight=BOLD),
            Text("must change!", font_size=44, color=GREEN, weight=BOLD),
            Text("Answer: A", font_size=56, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        final_answer.move_to(ORIGIN)
        
        for item in final_answer:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)
        
        self.wait(1.5)


# To run all scenes for Instagram Reels (9:16 aspect ratio):
# manim -pqh GRE_Problems_Collection.py QuadrilateralPerimeter
# manim -pqh GRE_Problems_Collection.py MerchantPricing  
# manim -pqh GRE_Problems_Collection.py HotelGuests
# manim -pqh GRE_Problems_Collection.py EquationIntercepts
# manim -pqh GRE_Problems_Collection.py PalindromeOdometer
# manim -pqh GRE_Problems_Collection.py HeightStatistics

# Note: These animations are optimized for Instagram Reels with:
# - 9:16 aspect ratio (1080x1920 resolution)
# - Larger fonts for mobile viewing
# - Faster pacing and shorter wait times
# - Centered content for vertical format
# - Bold, eye-catching visual elements
