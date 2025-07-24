from manim import *

# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class ExactBinomialProof(Scene):
    def construct(self):
        # Title
        title = Text("Binomial Expected Value Proof", font_size=36, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.4)
        
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Given statement
        given = MathTex(r"\text{Let } X \text{ be a binomial random variable with parameters } n \text{ and } p.", 
                       font_size=20, color=WHITE)
        given.next_to(title, DOWN, buff=0.5)
        
        show_that = MathTex(r"\text{Show that: } \mathbb{E}\left(\frac{1}{X+1}\right) = \frac{1 - (1-p)^{n+1}}{(n+1)p}", 
                           font_size=24, color=YELLOW)
        show_that.next_to(given, DOWN, buff=0.4)
        
        self.play(Write(given), run_time=1.5)
        self.play(Write(show_that), run_time=2)
        self.wait(1.5)

        # Clear and start with the exact steps from the image
        self.play(FadeOut(VGroup(given, show_that)), run_time=0.5)

        # Step 1: X ~ Bin(n, p)
        step1 = MathTex(r"X \sim \text{Bin}(n, p)", font_size=32, color=GREEN)
        step1.next_to(title, DOWN, buff=0.8)
        self.play(Write(step1), run_time=1)

        # Step 2: P(X = k)
        step2 = MathTex(r"P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}", font_size=28, color=WHITE)
        step2.next_to(step1, DOWN, buff=0.4)
        self.play(Write(step2), run_time=1.5)

        # Step 3: E(X) formula
        step3 = MathTex(r"\mathbb{E}(X) = \sum_{k=0}^{n} k \binom{n}{k} p^k (1-p)^{n-k}", font_size=24, color=BLUE)
        step3.next_to(step2, DOWN, buff=0.4)
        self.play(Write(step3), run_time=2)
        self.wait(1)

        # Clear and start main proof
        self.play(FadeOut(VGroup(step1, step2, step3)), run_time=0.5)

        # Following the exact handwritten steps
        # Line 1: E(1/(X+1)) = sum...
        line1 = MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = \sum_{k=0}^{n} \frac{1}{k+1} \binom{n}{k} p^k (1-p)^{n-k}", 
                       font_size=20, color=WHITE)
        line1.next_to(title, DOWN, buff=0.8)
        self.play(Write(line1), run_time=2.5)
        self.wait(1)

        # Line 2: Factorial expansion
        line2 = MathTex(r"= \sum_{k=0}^{n} \frac{1}{k+1} \cdot \frac{n!}{(n-k)! \, k!} \cdot p^k (1-p)^{n-k}", 
                       font_size=20, color=GREEN)
        line2.next_to(line1, DOWN, buff=0.3)
        self.play(Write(line2), run_time=2.5)
        self.wait(1)

        # Line 3: Combine fractions
        line3 = MathTex(r"= \sum_{k=0}^{n} \frac{n!}{(k+1)!(n-k)!} p^k (1-p)^{n-k}", 
                       font_size=22, color=BLUE)
        line3.next_to(line2, DOWN, buff=0.3)
        self.play(Write(line3), run_time=2)
        self.wait(1)

        # Line 4: Factor out 1/((n+1)p)
        line4 = MathTex(r"= \frac{1}{(n+1)p} \sum_{k=0}^{n} \frac{(n+1)!}{(k+1)!(n-k)!} \cdot p^{k+1} (1-p)^{n-k}", 
                       font_size=18, color=WHITE)
        line4.next_to(line3, DOWN, buff=0.3)
        self.play(Write(line4), run_time=3)
        self.wait(1.5)

        # Clear some lines to make room
        self.play(FadeOut(VGroup(line1, line2)), run_time=0.5)

        # Line 5: Recognize binomial coefficient
        line5 = MathTex(r"= \frac{1}{(n+1)p} \sum_{k=0}^{n} \binom{n+1}{k+1} p^{k+1} (1-p)^{n-k}", 
                       font_size=20, color=GREEN)
        line5.next_to(line3, DOWN, buff=0.3)
        self.play(Write(line5), run_time=2.5)
        self.wait(1)

        # Line 6: Reindex sum
        line6 = MathTex(r"= \frac{1}{(n+1)p} \sum_{k=1}^{n+1} \binom{n+1}{k} p^k (1-p)^{n+1-k}", 
                       font_size=20, color=BLUE)
        line6.next_to(line5, DOWN, buff=0.3)
        self.play(Write(line6), run_time=2.5)
        self.wait(1)

        # Clear more lines
        self.play(FadeOut(VGroup(line3, line4, line5)), run_time=0.5)

        # Line 7: Use binomial theorem
        line7 = MathTex(r"= \frac{1}{(n+1)p} \left[1 - \binom{n+1}{0} p^0 (1-p)^{n+1}\right]", 
                       font_size=20, color=WHITE)
        line7.next_to(line6, DOWN, buff=0.3)
        self.play(Write(line7), run_time=2.5)
        self.wait(1)

        # Line 8: Simplify
        line8 = MathTex(r"= \frac{1}{(n+1)p} \left[1 - (1-p)^{n+1}\right]", 
                       font_size=24, color=GREEN)
        line8.next_to(line7, DOWN, buff=0.3)
        self.play(Write(line8), run_time=2)
        self.wait(1)

        # Final result
        final = MathTex(r"= \frac{1 - (1-p)^{n+1}}{(n+1)p}", 
                       font_size=32, color=YELLOW)
        final.next_to(line8, DOWN, buff=0.5)
        self.play(Write(final), run_time=2)
        self.wait(1.5)

        # QED
        qed = Text("∎", font_size=40, color=GREEN)
        qed.next_to(final, RIGHT, buff=0.5)
        self.play(Write(qed), run_time=1)
        self.wait(2)

        # Summary
        self.play(FadeOut(VGroup(line6, line7, line8, final, qed)), run_time=0.8)
        
        summary = VGroup(
            Text("Key Steps:", font_size=28, weight=BOLD, color=BLUE),
            Text("1. Use factorial identity for binomial coefficients", font_size=20, color=WHITE),
            Text("2. Factor and reindex the sum", font_size=20, color=WHITE),
            Text("3. Apply binomial theorem: Σ C(n+1,k) p^k (1-p)^(n+1-k) = 1", font_size=18, color=GREEN),
            Text("4. Simplify to get the final result", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.move_to(ORIGIN)
        
        for item in summary:
            self.play(Write(item), run_time=1)
            self.wait(0.5)
        
        self.wait(3)


# Create a scene that shows the key algebraic manipulation step by step
class BinomialProofKeyStep(Scene):
    def construct(self):
        # Title
        title = Text("Key Algebraic Manipulation", font_size=36, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=1)

        # Show the critical step in detail
        step_title = Text("Transforming the binomial coefficient:", font_size=24, color=YELLOW)
        step_title.next_to(title, DOWN, buff=1)
        self.play(Write(step_title), run_time=1)

        # Step by step transformation
        transform_steps = [
            MathTex(r"\frac{1}{k+1} \binom{n}{k}", font_size=32, color=WHITE),
            MathTex(r"= \frac{1}{k+1} \cdot \frac{n!}{k!(n-k)!}", font_size=28, color=GREEN),
            MathTex(r"= \frac{n!}{(k+1) \cdot k! \cdot (n-k)!}", font_size=28, color=BLUE),
            MathTex(r"= \frac{n!}{(k+1)!(n-k)!}", font_size=28, color=WHITE),
            MathTex(r"= \frac{n! \cdot (n+1)}{(n+1)(k+1)!(n-k)!}", font_size=26, color=GREEN),
            MathTex(r"= \frac{1}{n+1} \cdot \frac{(n+1)!}{(k+1)!(n-k)!}", font_size=26, color=BLUE),
            MathTex(r"= \frac{1}{n+1} \binom{n+1}{k+1}", font_size=32, color=YELLOW)
        ]

        current_pos = step_title.get_center() + DOWN * 1
        for i, step in enumerate(transform_steps):
            step.move_to(current_pos + DOWN * i * 0.8)
            self.play(Write(step), run_time=1.5)
            if i < len(transform_steps) - 1:
                # Add arrow
                arrow = MathTex(r"\downarrow", font_size=24, color=RED)
                arrow.move_to(current_pos + DOWN * (i + 0.5) * 0.8)
                self.play(Write(arrow), run_time=0.5)
            self.wait(0.8)

        self.wait(2)

        # Highlight the final result
        final_box = SurroundingRectangle(transform_steps[-1], color=YELLOW, buff=0.2)
        self.play(Create(final_box), run_time=1)
        self.wait(2)
