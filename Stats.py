from manim import *

import numpy as np

# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# manim -pqh Stats.py DoubleExponentialLRT
from manim import *
import numpy as np

class DoubleExponentialLRT(Scene):
    def construct(self):
        # Set up for vertical (reels) format
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        
        # Title
        title = Text("Likelihood Ratio Test", font_size=36, color=BLUE)
        subtitle = Text("Double Exponential Distribution", font_size=24)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)
        
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
        ump_title = Text("Uniformly Most Powerful", font_size=28, color=GREEN, weight=BOLD)
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
        title = Text("Likelihood Ratio Test", font_size=64, weight=BOLD)
        subtitle = Text("Poisson Distribution", font_size=40, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18)
        title_group.move_to(UP*5.5)
        self.play(Write(title), Write(subtitle), run_time=0.7)
        self.wait(0.5)

        # Problem statement
        problem = VGroup(
            MathTex(r"X_1, \ldots, X_n \sim \mathrm{Poisson}(\lambda)", font_size=32, color=WHITE),
            MathTex(r"P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}", font_size=36, color=BLUE),
            MathTex(r"\text{Test } H_0: \lambda = \lambda_0 \text{ vs } H_1: \lambda = \lambda_1 > \lambda_0", font_size=28, color=YELLOW),
            MathTex(r"\text{Find rejection region for level } \alpha", font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.13)
        problem.next_to(title_group, DOWN, buff=0.32)
        self.play(FadeIn(problem), run_time=1)
        self.wait(0.5)

        # Likelihoods
        lik_lambda0 = MathTex(r"\text{Lik}(\lambda_0) = \prod_{i=1}^n \frac{\lambda_0^{x_i} e^{-\lambda_0}}{x_i!}", font_size=28)
        lik_lambda1 = MathTex(r"\text{Lik}(\lambda_1) = \prod_{i=1}^n \frac{\lambda_1^{x_i} e^{-\lambda_1}}{x_i!}", font_size=28)
        lik_lambda0.next_to(problem, DOWN, buff=0.18)
        lik_lambda1.next_to(lik_lambda0, DOWN, buff=0.13)
        self.play(Write(lik_lambda0), Write(lik_lambda1), run_time=1)
        self.wait(0.5)

        # Likelihood ratio
        ratio = MathTex(r"\Lambda = \frac{\text{Lik}(\lambda_0)}{\text{Lik}(\lambda_1)}", font_size=32, color=YELLOW)
        ratio.next_to(lik_lambda1, DOWN, buff=0.18)
        self.play(Write(ratio), run_time=1)
        self.wait(0.5)

        # Substitute and simplify (split into two lines for layout)
        step1 = MathTex(r"= \frac{\lambda_0^{\sum x_i} e^{-n\lambda_0}}{\lambda_1^{\sum x_i} e^{-n\lambda_1}}", font_size=28)
        step2 = MathTex(r"= \left( \frac{\lambda_0}{\lambda_1} \right)^{\sum x_i} e^{n(\lambda_1-\lambda_0)}", font_size=28)
        step1.next_to(ratio, DOWN, buff=0.13)
        step2.next_to(step1, DOWN, buff=0.13)
        self.play(Write(step1), run_time=1)
        self.play(Write(step2), run_time=1)
        self.wait(0.5)

        # Monotonicity explanation
        mono = VGroup(
            MathTex(r"\Lambda \text{ is decreasing in } T = \sum x_i", font_size=22, color=BLUE),
            MathTex(r"\text{We want the critical value } c: \text{ such that }\ P(\sum x_i > c | H_0) \leq \alpha", font_size=22, color=YELLOW)
        ).arrange(DOWN, buff=0.13)
        mono.next_to(step2, DOWN, buff=0.18)
        self.play(Write(mono), run_time=1)
        self.wait(0.7)

        # Rejection region formula
        rej = MathTex(r"P\left(\sum x_i > c\mid H_0\right) \leq \alpha", font_size=28, color=GREEN)
        rej.next_to(mono, DOWN, buff=0.13)
        self.play(Write(rej), run_time=1)
        self.wait(0.7)

        # Poisson tail sum
        tail = MathTex(r"\sum_{t=0}^c \frac{e^{-n\lambda_0}(n\lambda_0)^t}{t!} \geq 1-\alpha", font_size=22, color=RED)
        tail.next_to(rej, DOWN, buff=0.16)
        box = SurroundingRectangle(tail, color=RED, buff=0.13)
        self.play(Write(tail), Create(box), run_time=1)
        self.wait(0.7)

        # Ending Notes (smaller font, tighter spacing)
        end_note1 = MathTex(r"\text{If exact equality isn't achievable,}", font_size=22)
        end_note2 = MathTex(r"\text{choose the smallest $c$ such that the inequality holds.}", font_size=22)
        end_note3 = MathTex(r"\text{This is the most powerful test under the Neyman-Pearson lemma.}", font_size=22)
        end_notes = VGroup(end_note1, end_note2, end_note3).arrange(DOWN, buff=0.07, aligned_edge=LEFT)
        end_notes.next_to(tail, DOWN, buff=0.5)
        self.play(Write(end_notes), run_time=0.9)
        self.wait(5)

# manim -pqh Stats.py PoissonLikelihoodRatioTestReel

# --- Exponential Likelihood Ratio Test Animation ---
class ExponentialLikelihoodRatioTest(Scene):
    def construct(self):

        # Title
        title = Text("Likelihood Ratio Test", font_size=46, weight=BOLD)
        subtitle = Text("Exponential Distribution", font_size=32, color=YELLOW)
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
        step2 = MathTex(r"= \left( \frac{\theta_0}{\theta_1} \right)^n e^{-(\theta_0-\theta_1)\sum x_i}", font_size=26)
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

