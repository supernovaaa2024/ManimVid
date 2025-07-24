from manim import *

# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class BinomialProof(Scene):
    def construct(self):
        # Title
        title = Text("Binomial Random Variable", font_size=40, weight=BOLD, color=BLUE)
        subtitle = Text("Expected Value Proof", font_size=32, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=1)
        self.play(Write(subtitle), run_time=1)
        self.wait(1)

        # Problem statement
        problem = Text("Let X be a binomial random variable with parameters n and p.", 
                      font_size=24, color=WHITE)
        problem.next_to(title_group, DOWN, buff=0.8)
        
        goal = MathTex(r"\text{Show that: } \mathbb{E}\left(\frac{1}{X+1}\right) = \frac{1 - (1-p)^{n+1}}{(n+1)p}", 
                      font_size=30, color=GREEN)
        goal.next_to(problem, DOWN, buff=0.6)
        
        self.play(Write(problem), run_time=1.5)
        self.play(Write(goal), run_time=2)
        self.wait(2)

        # Clear and start proof
        self.play(FadeOut(VGroup(problem, goal)), run_time=0.8)

        # Step 1: Define X ~ Bin(n, p)
        step1 = VGroup(
            MathTex(r"X \sim \text{Bin}(n, p)", font_size=36, color=BLUE),
            MathTex(r"P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}", font_size=32, color=GREEN)
        ).arrange(DOWN, buff=0.4)
        step1.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(step1[0]), run_time=1)
        self.play(Write(step1[1]), run_time=1.5)
        self.wait(1.5)

        # Step 2: Expected value definition
        step2 = MathTex(r"\mathbb{E}(X) = \sum_{k=0}^{n} k \binom{n}{k} p^k (1-p)^{n-k}", 
                       font_size=28, color=WHITE)
        step2.next_to(step1, DOWN, buff=0.8)
        
        self.play(Write(step2), run_time=2)
        self.wait(1)

        # Clear for main proof
        self.play(FadeOut(VGroup(step1, step2)), run_time=0.8)

        # Main proof starts
        proof_title = Text("Proof:", font_size=32, weight=BOLD, color=YELLOW)
        proof_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(proof_title), run_time=0.8)

        # Step 3: E(1/(X+1)) definition
        step3 = MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = \sum_{k=0}^{n} \frac{1}{k+1} \binom{n}{k} p^k (1-p)^{n-k}", 
                       font_size=24, color=WHITE)
        step3.next_to(proof_title, DOWN, buff=0.6)
        
        self.play(Write(step3), run_time=2.5)
        self.wait(2)

        # Step 4: Rewrite using factorial identity
        step4 = MathTex(r"= \sum_{k=0}^{n} \frac{1}{k+1} \cdot \frac{n!}{(n-k)! k!} \cdot p^k (1-p)^{n-k}", 
                       font_size=22, color=GREEN)
        step4.next_to(step3, DOWN, buff=0.5)
        
        self.play(Write(step4), run_time=2)
        self.wait(1.5)

        # Step 5: Simplify factorial
        step5 = MathTex(r"= \sum_{k=0}^{n} \frac{n!}{(k+1)!(n-k)!} \cdot p^k (1-p)^{n-k}", 
                       font_size=24, color=BLUE)
        step5.next_to(step4, DOWN, buff=0.5)
        
        self.play(Write(step5), run_time=2)
        self.wait(1.5)

        # Clear for next steps
        self.play(FadeOut(VGroup(step3, step4, step5)), run_time=0.8)

        # Step 6: Factor out and reindex
        step6 = MathTex(r"= \frac{1}{(n+1)p} \sum_{k=0}^{n} \frac{(n+1)!}{(k+1)!(n-k)!} \cdot p^{k+1} (1-p)^{n-k}", 
                       font_size=20, color=WHITE)
        step6.next_to(proof_title, DOWN, buff=0.6)
        
        self.play(Write(step6), run_time=3)
        self.wait(2)

        # Step 7: Recognize binomial coefficient
        step7 = MathTex(r"= \frac{1}{(n+1)p} \sum_{k=0}^{n} \binom{n+1}{k+1} \cdot p^{k+1} (1-p)^{n-k}", 
                       font_size=22, color=GREEN)
        step7.next_to(step6, DOWN, buff=0.5)
        
        self.play(Write(step7), run_time=2.5)
        self.wait(2)

        # Step 8: Change of variables
        step8 = MathTex(r"= \frac{1}{(n+1)p} \sum_{k=1}^{n+1} \binom{n+1}{k} p^k (1-p)^{n+1-k}", 
                       font_size=24, color=BLUE)
        step8.next_to(step7, DOWN, buff=0.5)
        
        self.play(Write(step8), run_time=2.5)
        self.wait(2)

        # Clear for final steps
        self.play(FadeOut(VGroup(step6, step7, step8)), run_time=0.8)

        # Step 9: Use binomial theorem
        step9_text = Text("Using the binomial theorem:", font_size=24, color=YELLOW)
        step9_text.next_to(proof_title, DOWN, buff=0.6)
        
        step9 = MathTex(r"\sum_{k=0}^{n+1} \binom{n+1}{k} p^k (1-p)^{n+1-k} = (p + (1-p))^{n+1} = 1", 
                       font_size=22, color=GREEN)
        step9.next_to(step9_text, DOWN, buff=0.5)
        
        self.play(Write(step9_text), run_time=1)
        self.play(Write(step9), run_time=2.5)
        self.wait(2)

        # Step 10: Final manipulation
        step10 = MathTex(r"= \frac{1}{(n+1)p} \left[1 - \binom{n+1}{0} p^0 (1-p)^{n+1}\right]", 
                        font_size=22, color=WHITE)
        step10.next_to(step9, DOWN, buff=0.5)
        
        self.play(Write(step10), run_time=2.5)
        self.wait(1.5)

        # Step 11: Simplify
        step11 = MathTex(r"= \frac{1}{(n+1)p} \left[1 - (1-p)^{n+1}\right]", 
                        font_size=26, color=BLUE)
        step11.next_to(step10, DOWN, buff=0.5)
        
        self.play(Write(step11), run_time=2)
        self.wait(2)

        # Clear for final result
        self.play(FadeOut(VGroup(step9_text, step9, step10, step11)), run_time=0.8)

        # Final result - highlighted
        final_result = MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = \frac{1 - (1-p)^{n+1}}{(n+1)p}", 
                              font_size=36, color=YELLOW)
        final_result.next_to(proof_title, DOWN, buff=1)
        
        # QED
        qed = Text("Q.E.D.", font_size=32, weight=BOLD, color=GREEN)
        qed.next_to(final_result, DOWN, buff=0.8)
        
        self.play(Write(final_result), run_time=2.5)
        self.wait(1)
        self.play(Write(qed), run_time=1)
        self.wait(2)

        # Summary box
        summary_box = Rectangle(height=2, width=7, color=BLUE, stroke_width=3)
        summary_text = VGroup(
            Text("Key insight:", font_size=24, weight=BOLD, color=BLUE),
            Text("Transform expectation using", font_size=20, color=WHITE),
            Text("factorial identities and", font_size=20, color=WHITE),
            Text("binomial theorem", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        summary_group = VGroup(summary_box, summary_text).move_to(ORIGIN).shift(DOWN * 2)
        
        self.play(FadeOut(VGroup(proof_title, final_result, qed)), run_time=0.8)
        self.play(Create(summary_box), Write(summary_text), run_time=2)
        self.wait(3)


class BinomialProofDetailed(Scene):
    def construct(self):
        # More detailed version with step-by-step algebraic manipulations
        
        # Title
        title = Text("Detailed Binomial Proof", font_size=40, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Show the factorial manipulation in detail
        factorial_title = Text("Key Algebraic Step:", font_size=28, weight=BOLD, color=YELLOW)
        factorial_title.next_to(title, DOWN, buff=1)
        
        self.play(Write(factorial_title), run_time=1)

        # Step-by-step factorial manipulation
        steps = [
            MathTex(r"\frac{1}{k+1} \binom{n}{k} = \frac{1}{k+1} \cdot \frac{n!}{k!(n-k)!}", font_size=24),
            MathTex(r"= \frac{n!}{(k+1) \cdot k! \cdot (n-k)!}", font_size=24),
            MathTex(r"= \frac{n!}{(k+1)! \cdot (n-k)!}", font_size=24),
            MathTex(r"= \frac{n! \cdot (n+1)}{(n+1) \cdot (k+1)! \cdot (n-k)!}", font_size=24),
            MathTex(r"= \frac{1}{n+1} \cdot \frac{(n+1)!}{(k+1)!(n-k)!}", font_size=24),
            MathTex(r"= \frac{1}{n+1} \binom{n+1}{k+1}", font_size=24, color=GREEN)
        ]
        
        current_y = factorial_title.get_y() - 0.8
        for i, step in enumerate(steps):
            step.move_to([0, current_y - i * 0.6, 0])
            self.play(Write(step), run_time=1.5)
            self.wait(0.8)

        self.wait(2)
        
        # Clear and show final insight
        self.play(FadeOut(VGroup(factorial_title, *steps)), run_time=1)
        
        insight = VGroup(
            Text("This transformation allows us to use", font_size=26, color=WHITE),
            Text("the binomial theorem:", font_size=26, color=WHITE),
            MathTex(r"\sum_{k=0}^{n+1} \binom{n+1}{k} p^k (1-p)^{n+1-k} = 1", font_size=28, color=GREEN)
        ).arrange(DOWN, buff=0.4)
        insight.next_to(title, DOWN, buff=2)
        
        for item in insight:
            self.play(Write(item), run_time=1.5)
            self.wait(0.5)
        
        self.wait(3)
