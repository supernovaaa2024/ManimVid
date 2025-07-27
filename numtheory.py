from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class divisibility11(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())
        title = Text("Divisibility Rule of 11 Proof", font_size=24, color=BLUE)
        self.play(Write(title))
        with self.voiceover(
            text="How do we proof that a number is divisible by 11? We take the difference between the sum of all odd and even digits. Sounds like magic, right? Here's how it works."
        ):
            self.wait(1)
        self.play(title.animate.to_edge(UP))

        eq1 = MathTex(
            r"Let\; n \;=\; a_n a_{n-1} \dots a_2 a_1 a_0", color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(eq1))
        with self.voiceover(text="Here, the various A  sub  N are different digits."):
            self.wait(1)
        with self.voiceover(text="Then, we write the equation in summation form."):
            self.wait(1)
        eq2 = MathTex(
            r"n \;=\; a_n \, 10^n + a_{n-1}\,10^{\,n-1} + \dots + a_1\,10 + a_0",
            color=YELLOW,
        ).next_to(eq1, DOWN, buff=0.5)
        self.play(Write(eq2))
        self.wait(1)

        text1 = MathTex(
            r"Rewrite \;10^k\; in\; the\; form: ", font_size=36, color=GREEN
        ).next_to(eq2, DOWN, buff=0.5)
        self.play(Write(text1))
        eq3 = MathTex(r"10^k \;=\; (11 - 1)^k", color=GREEN).next_to(
            text1, DOWN, buff=0.5
        )
        self.play(Write(eq3))
        with self.voiceover(
            text="We rewrite (10) to the power of k and then expand using binomial theorem, which is the algebraic expansion of a binomial expression."
        ):
            self.wait(1)

        self.play(FadeOut(eq1), FadeOut(eq2), FadeOut(text1), FadeOut(eq3))
        self.wait(1)

        text2 = Text(
            "Now we use the binomial theorem to expand:", font_size=36, color=GREEN
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(text2))
        eq4 = MathTex(
            r"(11 - 1)^k = \underbrace{ \binom{k}{1} 11^{k-1} (-1)^1 + \binom{k}{2} 11^{k-2}(-1)^2 + \cdots + 11^1(-1)^{\,k-1} }_{\text{all terms are multiples of } 11} + (-1)^k",
            font_size=36,
            color=GREEN,
        ).next_to(text2, DOWN, buff=0.5)
        self.play(Write(eq4))
        self.wait(2)
        self.play(FadeOut(text2), FadeOut(eq4))

        eq5 = MathTex(
            r"10^k = (11 - 1)^k = 11\bigl(\text{some integer}\bigr) + (-1)^k",
            color=YELLOW,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(eq5))
        with self.voiceover(
            text="This expansion of (11) to the power of k is equal to 11 times some integer plus (-1) to the power of k."
        ):
            self.wait(1)
        with self.voiceover(
            text="We substitute (11) to the power of k back into the equation n."
        ):
            self.wait(1)
        self.wait(1)

        eq6 = MathTex(
            r"n = a_n \,10^n + a_{n-1}\,10^{\,n-1} + \dots + a_1\,10 + a_0",
            color=YELLOW,
        ).next_to(eq5, DOWN, buff=0.5)
        self.play(Write(eq6))
        eq7 = MathTex(
            r"a_k\,10^k = a_k \Bigl[\,11(\text{some value}) + (-1)^k\Bigr]",
            color=YELLOW,
        ).next_to(eq6, DOWN, buff=0.5)
        self.play(Write(eq7))
        eq8 = MathTex(
            r"n = 11(\text{some bigger integer}) + \bigl[\,a_n(-1)^n + a_{n-1}(-1)^{n-1} + \cdots + a_1(-1)^1 + a_0(-1)^0\bigr]",
            font_size=30,
            color=YELLOW,
        ).next_to(eq7, DOWN, buff=0.5)

        self.play(FadeOut(eq5))
        self.wait(1)

        eq9 = MathTex(
            r"n = 11(\text{an integer}) + \bigl(a_0 - a_1 + a_2 - a_3 + \cdots + (-1)^n\,a_n\bigr)",
            color=YELLOW,
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(eq8))
        with self.voiceover(
            text="We simplify the equation to get the final result where the first term is divisible by 11 and the latter term is the difference between the sum of odd and sum of even terms which needs to be divisible by 11 for the whole number to be divisible by 11."
        ):
            self.wait(1)

        self.play(FadeOut(eq6))
        self.play(FadeOut(eq7))
        self.play(FadeOut(eq8))

        self.play(Write(eq9))
        self.wait(1)

        eq10 = MathTex(
            r"n \;\equiv\; \bigl(a_0 - a_1 + a_2 - a_3 + \dots + (-1)^n\,a_n\bigr) \pmod{11}",
            color=YELLOW,
        ).next_to(eq9, DOWN, buff=0.5)
        eq11 = MathTex(
            r"a_0 - a_1 + a_2 - a_3 + \cdots + (-1)^n\,a_n \;=\;0 \quad(\text{or a multiple of } 11)",
            color=YELLOW,
        ).next_to(eq10, DOWN, buff=0.5)
        self.play(Write(eq10))
        self.wait(3)
        self.play(Write(eq11))
        self.wait(3)
        self.play(FadeOut(eq9), FadeOut(eq10), FadeOut(eq11))

        conclusion = Text(
            "A number is divisible by 11 if and only if the difference between\n"
            "the sum of its digits in the odd positions and the sum of its digits\n"
            "in the even positions is a multiple of 11 (including 0).",
            font_size=34,
            color=BLUE,
            line_spacing=1.5,
        ).next_to(eq10, DOWN, buff=0.5)
        self.play(Write(conclusion))
        with self.voiceover(
            text="A number is divisible by 11 if and only if the difference between\n"
            "the sum of its digits in the odd positions and the sum of its digits\n"
            "in the even positions is a multiple of 11 (including 0)."
        ):
            self.wait(2)

        self.play(FadeOut(title), FadeOut(conclusion))

        example1 = Text(r"Example: Let N = abc = 121", color=PURPLE)
        example1.shift(UP * 3)
        example2 = Text(r"such that N = 100a + 10b + c", color=PURPLE)
        example2.next_to(example1, DOWN, buff=0.5)
        self.play(Write(example1), Write(example2))
        with self.voiceover(text="Now, this is an example."):
            self.wait(1)
        with self.voiceover(text="Let N = ABC = 121 such that N = 100A + 10B + C"):
            self.wait(1)
        self.play(FadeOut(example1))
        self.play(example2.animate.shift(UP * 1.5))
        with self.voiceover(
            text="We rewrite the 100 and 10 and rewrite the equation as 11 times some integer plus the difference between the sum of odd and sum of even terms."
        ):
            self.wait(1)
        text7 = Text(r"= (99 + 1)a + (11 - 1)b + c", color=PURPLE).scale(0.8)
        text7.next_to(example2, DOWN, buff=0.5)
        self.play(Write(text7))
        text8 = Text(r"= 99a + 11b + a - b + c", color=PURPLE).scale(0.8)
        text8.next_to(text7, DOWN, buff=0.5)
        self.play(Write(text8))
        text9 = Text(r"= 11(9a + b) + a - b + c", color=PURPLE).scale(0.8)
        text9.next_to(text8, DOWN, buff=0.5)
        self.play(Write(text9))
        with self.voiceover(
            text="The difference between the sum of odd and sum of even terms is 1 - 2 + 1 = 0."
        ):
            self.wait(1)
        text10 = MathTex(
            r"a - b + c = 1 - 2 + 1 \equiv 0 (mod 11)", color=PURPLE
        ).scale(0.8)
        text10.next_to(text9, DOWN, buff=0.5)
        self.play(Write(text10))
        text11 = Text(r"121 / 11 = 11", color=PURPLE).scale(0.8)
        text11.next_to(text10, DOWN, buff=0.5)
        self.play(Write(text11))
        with self.voiceover(text="Therefore, 121 is divisible by 11."):
            self.wait(1)


# manim -pql divisibility11proof.py divisibility11

