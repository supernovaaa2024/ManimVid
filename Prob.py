from manim import *
# --- Binomial Identity Proof Animation ---
from manim import *

# manim -pqh Prob.py CombinatoriaIdentity
# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

from manim import *
import numpy as np

class CombinatoriaIdentity(Scene):
    PRIMARY_COLOR = "#FF6B6B"
    SECONDARY_COLOR = "#4ECDC4"
    ACCENT_COLOR = "#45B7D1"
    SUCCESS_COLOR = "#98D8C8"
    WARNING_COLOR = "#FFD93D"
    WOMEN_COLOR = "#FF69B4"  # Pink for women
    MEN_COLOR = "#4169E1"    # Blue for men
    TEXT_COLOR = WHITE

    def construct(self):
        # Set up vertical format for Instagram reels
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        # Main title
        main_title = Text("Vandermonde's Identity", font_size=44, color=self.PRIMARY_COLOR, weight=BOLD)
        main_title.to_edge(UP, buff=0.8)

        self.play(Write(main_title), run_time=1.5)

        # Problem statement
        problem_title = Text("Problem 3", font_size=36, color=self.SECONDARY_COLOR, weight=BOLD)
        problem_title.next_to(main_title, DOWN, buff=0.5)

        self.play(Write(problem_title), run_time=1)

        # Given conditions
        conditions = MathTex(
            r"m, n, r \geq 1",
            font_size=28,
            color=self.TEXT_COLOR
        )
        conditions.next_to(problem_title, DOWN, buff=0.6)

        self.play(Write(conditions), run_time=1)

        # Part A statement
        part_a_text = Text("Part A: Prove that", font_size=28, color=self.ACCENT_COLOR)
        part_a_text.next_to(conditions, DOWN, buff=0.6)

        self.play(Write(part_a_text), run_time=1.2)

        # The identity to prove
        identity_a = MathTex(
            r"\binom{m+n}{r} = \sum_{k=0}^{r} \binom{n}{r-k}\binom{m}{k}",
            font_size=30,
            color=self.WARNING_COLOR
        )
        identity_a.next_to(part_a_text, DOWN, buff=0.5)

        self.play(Write(identity_a), run_time=2.5)

        # Part B statement
        part_b_text = Text("Part B: Conclude that", font_size=28, color=self.ACCENT_COLOR)
        part_b_text.next_to(identity_a, DOWN, buff=0.6)

        self.play(Write(part_b_text), run_time=1.2)

        # The identity for part B
        identity_b = MathTex(
            r"\binom{2n}{n} = \sum_{k=0}^{n} \binom{n}{k}^2",
            font_size=32,
            color=self.WARNING_COLOR
        )
        identity_b.next_to(part_b_text, DOWN, buff=0.5)

        self.play(Write(identity_b), run_time=2)
        self.wait(2)

        # Clear screen for solutions
        self.play(FadeOut(VGroup(conditions, part_a_text, identity_a, part_b_text, identity_b)), run_time=1)

        # Solution Part A
        self.solve_part_a(main_title, problem_title)

        # Solution Part B
        self.solve_part_b(main_title, problem_title)

        # Final summary
        self.show_summary(main_title)

    def solve_part_a(self, main_title, problem_title):
        # Part A title
        part_a_title = Text("Part A: Combinatorial Interpretation", font_size=32, color=self.PRIMARY_COLOR, weight=BOLD)
        part_a_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_a_title), run_time=1.5)
        
        # Visual representation setup
        group_text = Text("Group: m women + n men", font_size=26, color=self.TEXT_COLOR)
        group_text.next_to(part_a_title, DOWN, buff=0.6)
        
        self.play(Write(group_text), run_time=1.5)
        
        # Visual representation
        women_circles = VGroup(*[Circle(radius=0.15, color=self.WOMEN_COLOR, fill_opacity=0.7) for _ in range(4)])
        women_circles.arrange(RIGHT, buff=0.1)
        women_label = Text("m women", font_size=20, color=self.WOMEN_COLOR)
        women_group = VGroup(women_circles, women_label).arrange(DOWN, buff=0.2)
        
        men_circles = VGroup(*[Circle(radius=0.15, color=self.MEN_COLOR, fill_opacity=0.7) for _ in range(3)])
        men_circles.arrange(RIGHT, buff=0.1)
        men_label = Text("n men", font_size=20, color=self.MEN_COLOR)
        men_group = VGroup(men_circles, men_label).arrange(DOWN, buff=0.2)
        
        visual_group = VGroup(women_group, men_group).arrange(RIGHT, buff=1)
        visual_group.next_to(group_text, DOWN, buff=0.5)
        visual_group.scale(0.8)
        
        self.play(Create(women_circles), Write(women_label), run_time=1.5)
        self.play(Create(men_circles), Write(men_label), run_time=1.5)
        
        # Question
        question_text = Text("How many ways to choose r people?", font_size=24, color=self.ACCENT_COLOR)
        question_text.next_to(visual_group, DOWN, buff=0.6)
        
        self.play(Write(question_text), run_time=1.5)
        
        # Method 1
        method1_title = Text("Method 1: Direct", font_size=24, color=self.SUCCESS_COLOR, weight=BOLD)
        method1_title.next_to(question_text, DOWN, buff=0.6)
        
        method1_formula = MathTex(
            r"\binom{m+n}{r} \text{ ways}",
            font_size=28,
            color=self.SUCCESS_COLOR
        )
        method1_formula.next_to(method1_title, DOWN, buff=0.3)
        
        self.play(Write(method1_title), run_time=1)
        self.play(Write(method1_formula), run_time=1.5)
        self.wait(1)
        
        # Clear visual for method 2
        self.play(FadeOut(VGroup(visual_group, question_text)), run_time=1)
        
        # Method 2
        method2_title = Text("Method 2: Choose by categories", font_size=24, color=self.SECONDARY_COLOR, weight=BOLD)
        method2_title.next_to(method1_formula, DOWN, buff=0.6)
        
        self.play(Write(method2_title), run_time=1.2)
        
        # Explanation of method 2
        explanation = Text("Choose k men, then (r-k) women", font_size=22, color=self.TEXT_COLOR)
        explanation.next_to(method2_title, DOWN, buff=0.4)
        
        self.play(Write(explanation), run_time=1.5)
        
        # Sum over all possible k values
        sum_explanation = MathTex(
            r"k \text{ can be } 0, 1, 2, \ldots, r",
            font_size=24,
            color=self.TEXT_COLOR
        )
        sum_explanation.next_to(explanation, DOWN, buff=0.4)
        
        self.play(Write(sum_explanation), run_time=1.5)
        
        # Method 2 formula
        method2_formula = MathTex(
            r"\sum_{k=0}^{r} \binom{m}{k} \binom{n}{r-k} \text{ ways}",
            font_size=26,
            color=self.SECONDARY_COLOR
        )
        method2_formula.next_to(sum_explanation, DOWN, buff=0.5)
        
        self.play(Write(method2_formula), run_time=2)
        
        # Conclusion
        conclusion = MathTex(
            r"\binom{m+n}{r} = \sum_{k=0}^{r} \binom{m}{k} \binom{n}{r-k}",
            font_size=28,
            color=self.WARNING_COLOR
        )
        conclusion.next_to(method2_formula, DOWN, buff=0.6)
        
        conclusion_box = SurroundingRectangle(
            conclusion, 
            color=self.WARNING_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(conclusion), run_time=2)
        self.play(Create(conclusion_box), run_time=1)
        self.wait(1.5)
        
        # Clear for next part
        self.play(FadeOut(VGroup(part_a_title, group_text, method1_title, method1_formula,
                                method2_title, explanation, sum_explanation, method2_formula,
                                conclusion, conclusion_box)), run_time=1)

    def solve_part_b(self, main_title, problem_title):
        # Part B title
        part_b_title = Text("Part B: Special Case (m = n)", font_size=32, color=self.PRIMARY_COLOR, weight=BOLD)
        part_b_title.next_to(problem_title, DOWN, buff=0.8)
        
        self.play(Write(part_b_title), run_time=1.5)
        
        # Setting m = n in the identity
        substitution = MathTex(
            r"\text{Let } m = n \text{ in Part A:}",
            font_size=26,
            color=self.ACCENT_COLOR
        )
        substitution.next_to(part_b_title, DOWN, buff=0.6)
        
        self.play(Write(substitution), run_time=1.5)
        
        # Substituted formula
        substituted = MathTex(
            r"\binom{2n}{n} = \sum_{k=0}^{n} \binom{n}{k} \binom{n}{n-k}",
            font_size=28,
            color=self.TEXT_COLOR
        )
        substituted.next_to(substitution, DOWN, buff=0.5)
        
        self.play(Write(substituted), run_time=2)
        
        # Key insight
        insight_text = Text("Key insight:", font_size=24, color=self.SECONDARY_COLOR, weight=BOLD)
        insight_text.next_to(substituted, DOWN, buff=0.6)
        
        self.play(Write(insight_text), run_time=1)
        
        # Symmetry property
        symmetry = MathTex(
            r"\binom{n}{n-k} = \binom{n}{k}",
            font_size=28,
            color=self.SECONDARY_COLOR
        )
        symmetry.next_to(insight_text, DOWN, buff=0.4)
        
        self.play(Write(symmetry), run_time=1.5)
        
        # Therefore
        therefore_text = Text("Therefore:", font_size=24, color=self.TEXT_COLOR)
        therefore_text.next_to(symmetry, DOWN, buff=0.5)
        
        self.play(Write(therefore_text), run_time=1)
        
        # Simplified formula
        simplified = MathTex(
            r"\binom{n}{k} \binom{n}{n-k} = \binom{n}{k} \binom{n}{k} = \binom{n}{k}^2",
            font_size=24,
            color=self.TEXT_COLOR
        )
        simplified.next_to(therefore_text, DOWN, buff=0.4)
        
        self.play(Write(simplified), run_time=2)
        
        # Final result
        final_result = MathTex(
            r"\binom{2n}{n} = \sum_{k=0}^{n} \binom{n}{k}^2",
            font_size=32,
            color=self.SUCCESS_COLOR
        )
        final_result.next_to(simplified, DOWN, buff=0.6)
        
        result_box_b = SurroundingRectangle(
            final_result, 
            color=self.SUCCESS_COLOR, 
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Write(final_result), run_time=2)
        self.play(Create(result_box_b), run_time=1)
        
        # Expanded form
        expanded_text = Text("Expanded:", font_size=22, color=self.TEXT_COLOR)
        expanded_text.next_to(result_box_b, DOWN, buff=0.5)
        
        expanded_form = MathTex(
            r"= \binom{n}{0}^2 + \binom{n}{1}^2 + \binom{n}{2}^2 + \cdots + \binom{n}{n}^2",
            font_size=22,
            color=self.TEXT_COLOR
        )
        expanded_form.next_to(expanded_text, DOWN, buff=0.3)
        
        self.play(Write(expanded_text), run_time=1)
        self.play(Write(expanded_form), run_time=2)
        self.wait(1.5)
        
        # Clear for summary
        self.play(FadeOut(VGroup(part_b_title, substitution, substituted, insight_text,
                                symmetry, therefore_text, simplified, final_result,
                                result_box_b, expanded_text, expanded_form)), run_time=1)

    def show_summary(self, main_title):
        # Summary title
        summary_title = Text("Vandermonde's Identity", font_size=38, color=self.PRIMARY_COLOR, weight=BOLD)
        summary_title.next_to(main_title, DOWN, buff=1)
        
        self.play(Write(summary_title), run_time=1.5)
        
        # General form
        general_title = Text("General Form:", font_size=26, color=self.ACCENT_COLOR, weight=BOLD)
        general_title.next_to(summary_title, DOWN, buff=0.6)
        
        general_identity = MathTex(
            r"\binom{m+n}{r} = \sum_{k=0}^{r} \binom{m}{k} \binom{n}{r-k}",
            font_size=28,
            color=self.ACCENT_COLOR
        )
        general_identity.next_to(general_title, DOWN, buff=0.4)
        
        self.play(Write(general_title), run_time=1)
        self.play(Write(general_identity), run_time=2)
        
        # Special case
        special_title = Text("Special Case (m = n):", font_size=26, color=self.SECONDARY_COLOR, weight=BOLD)
        special_title.next_to(general_identity, DOWN, buff=0.6)
        
        special_identity = MathTex(
            r"\binom{2n}{n} = \sum_{k=0}^{n} \binom{n}{k}^2",
            font_size=28,
            color=self.SECONDARY_COLOR
        )
        special_identity.next_to(special_title, DOWN, buff=0.4)
        
        self.play(Write(special_title), run_time=1)
        self.play(Write(special_identity), run_time=2)
        
        # Interpretation
        interpretation_title = Text("Combinatorial Interpretation:", font_size=24, color=self.WARNING_COLOR, weight=BOLD)
        interpretation_title.next_to(special_identity, DOWN, buff=0.4)
        
        interpretation_text = Text("Ways to form committees = Sum of products", font_size=22, color=self.TEXT_COLOR)
        interpretation_text.next_to(interpretation_title, DOWN, buff=0.3)
        
        self.play(Write(interpretation_title), run_time=1)
        self.play(Write(interpretation_text), run_time=1.5)
        
        # Final emphasis box
        final_box = SurroundingRectangle(
            VGroup(general_identity, special_identity), 
            color=self.WARNING_COLOR, 
            buff=0.8,
            corner_radius=0.3,
            stroke_width=3
        )
        
        self.play(Create(final_box), run_time=1.5)
        
        # Final fade out
        self.play(FadeOut(VGroup(summary_title, general_title, general_identity,
                                special_title, special_identity, interpretation_title,
                                interpretation_text, final_box)), run_time=2)
        

class BinomialProofReel(Scene):
    def construct(self):
        # Title - Instagram friendly
        title = Text("Binomial Expected Value", font_size=40, weight=BOLD, color=BLUE)
        subtitle = Text("Mathematical Proof", font_size=32, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.3)
        
        self.play(Write(title), run_time=0.8)
        self.play(Write(subtitle), run_time=0.8)
        self.wait(0.5)

        # Problem setup - quick and visual
        problem = VGroup(
            Text("Given: X ~ Binomial(n, p)", font_size=28, color=GREEN),
            Text("Find:", font_size=24, color=WHITE),
            MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = ?", font_size=32, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        problem.next_to(title_group, DOWN, buff=0.8)
        
        for item in problem:
            self.play(Write(item), run_time=0.6)
        self.wait(1)

        # Clear and show key insight
        self.play(FadeOut(problem), run_time=0.5)

        insight_title = Text("💡 Key Insight", font_size=32, weight=BOLD, color=YELLOW)
        insight_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(insight_title), run_time=0.8)

        # Show the factorial trick
        trick = VGroup(
            MathTex(r"\frac{1}{k+1} \binom{n}{k} = \frac{1}{n+1} \binom{n+1}{k+1}", 
                   font_size=28, color=GREEN),
            Text("↓ This allows us to use binomial theorem!", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.4)
        trick.next_to(insight_title, DOWN, buff=0.6)
        
        self.play(Write(trick[0]), run_time=1.5)
        self.play(Write(trick[1]), run_time=1)
        self.wait(1.5)

        # Clear for main calculation
        self.play(FadeOut(VGroup(insight_title, trick)), run_time=0.5)

        # Show the calculation steps - fast paced for Instagram
        calc_title = Text("✨ The Magic Happens", font_size=28, weight=BOLD, color=BLUE)
        calc_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(calc_title), run_time=0.8)

        # Step 1
        step1 = MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = \sum_{k=0}^{n} \frac{1}{k+1} \binom{n}{k} p^k (1-p)^{n-k}", 
                       font_size=18, color=WHITE)
        step1.next_to(calc_title, DOWN, buff=0.5)
        self.play(Write(step1), run_time=1.5)

        # Step 2 - Apply the trick
        step2 = MathTex(r"= \frac{1}{(n+1)p} \sum_{k=1}^{n+1} \binom{n+1}{k} p^k (1-p)^{n+1-k}", 
                       font_size=18, color=GREEN)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2), run_time=1.5)

        # Step 3 - Binomial theorem
        step3 = MathTex(r"= \frac{1}{(n+1)p} \left[1 - (1-p)^{n+1}\right]", 
                       font_size=22, color=BLUE)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3), run_time=1.5)
        self.wait(1)

        # Final answer - highlighted
        final_box = Rectangle(height=1, width=6, color=YELLOW, stroke_width=3, fill_opacity=0.1, fill_color=YELLOW)
        final_answer = MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = \frac{1 - (1-p)^{n+1}}{(n+1)p}", 
                              font_size=28, color=YELLOW)
        final_group = VGroup(final_box, final_answer)
        final_group.next_to(step3, DOWN, buff=0.8)
        
        self.play(Create(final_box), run_time=0.8)
        self.play(Write(final_answer), run_time=1.5)
        self.wait(1.5)

        # Celebration effect
        self.play(FadeOut(VGroup(calc_title, step1, step2, step3)), run_time=0.5)
        
        celebration = VGroup(
            Text("🎉 PROVED! 🎉", font_size=36, color=GREEN, weight=BOLD),
            Text("The power of algebra!", font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.4)
        celebration.next_to(final_group, DOWN, buff=1)
        
        for item in celebration:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)

        # Final highlight animation
        self.play(
            final_box.animate.set_stroke(color=GREEN, width=5),
            final_answer.animate.set_color(GREEN),
            run_time=1
        )
        self.wait(2)
