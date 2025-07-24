from manim import *

# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

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


class BinomialProofSteps(Scene):
    def construct(self):
        # Step-by-step breakdown for better understanding
        
        title = Text("Binomial Proof: Step by Step", font_size=36, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)

        # Step 1: Setup
        step1_title = Text("Step 1: Definition", font_size=28, weight=BOLD, color=YELLOW)
        step1_title.next_to(title, DOWN, buff=1)
        
        step1_content = VGroup(
            MathTex(r"X \sim \text{Binomial}(n, p)", font_size=24, color=GREEN),
            MathTex(r"P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}", font_size=22, color=WHITE),
            MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = \sum_{k=0}^{n} \frac{1}{k+1} P(X = k)", font_size=20, color=BLUE)
        ).arrange(DOWN, buff=0.3)
        step1_content.next_to(step1_title, DOWN, buff=0.5)
        
        self.play(Write(step1_title), run_time=0.8)
        for item in step1_content:
            self.play(Write(item), run_time=1)
        self.wait(2)

        # Clear and show Step 2
        self.play(FadeOut(VGroup(step1_title, step1_content)), run_time=0.5)

        step2_title = Text("Step 2: The Key Transformation", font_size=28, weight=BOLD, color=YELLOW)
        step2_title.next_to(title, DOWN, buff=1)
        
        step2_content = VGroup(
            Text("Transform using factorial identity:", font_size=22, color=WHITE),
            MathTex(r"\frac{1}{k+1} \binom{n}{k} = \frac{n!}{(k+1)!(n-k)!}", font_size=20, color=GREEN),
            MathTex(r"= \frac{1}{n+1} \cdot \frac{(n+1)!}{(k+1)!(n-k)!}", font_size=20, color=BLUE),
            MathTex(r"= \frac{1}{n+1} \binom{n+1}{k+1}", font_size=22, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        step2_content.next_to(step2_title, DOWN, buff=0.5)
        
        self.play(Write(step2_title), run_time=0.8)
        for item in step2_content:
            self.play(Write(item), run_time=1.2)
        self.wait(2)

        # Clear and show Step 3
        self.play(FadeOut(VGroup(step2_title, step2_content)), run_time=0.5)

        step3_title = Text("Step 3: Apply Binomial Theorem", font_size=28, weight=BOLD, color=YELLOW)
        step3_title.next_to(title, DOWN, buff=1)
        
        step3_content = VGroup(
            Text("After reindexing and factoring:", font_size=22, color=WHITE),
            MathTex(r"\sum_{k=0}^{n+1} \binom{n+1}{k} p^k (1-p)^{n+1-k} = (p + (1-p))^{n+1} = 1", 
                   font_size=18, color=GREEN),
            Text("Therefore:", font_size=22, color=WHITE),
            MathTex(r"\mathbb{E}\left(\frac{1}{X+1}\right) = \frac{1 - (1-p)^{n+1}}{(n+1)p}", 
                   font_size=24, color=YELLOW)
        ).arrange(DOWN, buff=0.4)
        step3_content.next_to(step3_title, DOWN, buff=0.5)
        
        self.play(Write(step3_title), run_time=0.8)
        for item in step3_content:
            self.play(Write(item), run_time=1.5)
        self.wait(3)

# manim -pqh BinomialProofReel.py BinomialProofReel
# manim -pqh ExactBinomialProof.py ExactBinomialProof
# manim -pqh BinomialProof.py BinomialProof

# For detailed algebraic steps
# manim -pqh BinomialProofReel.py BinomialProofSteps
# manim -pqh ExactBinomialProof.py BinomialProofKeyStep