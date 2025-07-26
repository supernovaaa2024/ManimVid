
from manim import *

# Instagram Reels configuration - 9:16 aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0




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

