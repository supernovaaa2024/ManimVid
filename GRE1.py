from manim import *

class GREProblemSolve(Scene):
    def construct(self):
        # Title
        title = Text("GRE Problem: Factors and Powers", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Problem Statement
        problem_text_lines = [
            r"Let a be the greatest integer such that $5^a$ is a factor of 1,500,",
            r"and let b be the greatest integer such that $3^b$ is a factor of 33,333,333.",
            r"Which of the following statements are true?",
            r"Indicate all such statements."""
        ]
        problem_mobjects = VGroup(*[Text(line, font_size=24) for line in problem_text_lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem_mobjects.next_to(title, DOWN, buff=0.3)
        self.play(Write(problem_mobjects))
        self.wait(2)

        options_text = VGroup(
            Text("A.  ab = 3", font_size=28),
            Text("B.  a = 3b", font_size=28),
            Text("C.  2a > 5b", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(problem_mobjects, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(options_text))
        self.wait(3)

        # Clear problem statement for calculation space
        self.play(FadeOut(problem_mobjects), FadeOut(options_text))

        # --- Solve for 'a' ---
        solve_a_title = Text("Step 1: Solve for 'a'", font_size=30, color=YELLOW)
        solve_a_title.to_edge(UP).shift(DOWN*0.2) # Adjusted position
        self.play(Transform(title, solve_a_title))
        
        text_a_def = MathTex(r"\text{Find the greatest integer 'a' such that } 5^a \text{ is a factor of 1,500.}", font_size=28)
        text_a_def.next_to(title, DOWN, buff=0.4)
        self.play(Write(text_a_def))
        self.wait(1)

        factor_1500_steps = VGroup(
            MathTex(r"1500 = 15 \times 100"),
            MathTex(r"= (3 \times 5) \times 10^2"),
            MathTex(r"= 3 \times 5 \times (2 \times 5)^2"),
            MathTex(r"= 3 \times 5 \times 2^2 \times 5^2"),
            MathTex(r"= 2^2 \times 3^1 \times 5^3")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.9)
        factor_1500_steps.next_to(text_a_def, DOWN, buff=0.3)
        
        for i, step in enumerate(factor_1500_steps):
            self.play(Write(step))
            self.wait(1 if i < len(factor_1500_steps) -1 else 2)

        highlight_5_3 = SurroundingRectangle(factor_1500_steps[-1].get_parts_by_tex("5^3"), color=GREEN, buff=0.1)
        text_a_val_explain = MathTex(r"\text{The highest power of 5 is } 5^3.", font_size=28).next_to(factor_1500_steps, DOWN, buff=0.3)
        self.play(Create(highlight_5_3), Write(text_a_val_explain))
        self.wait(1)
        
        a_value = MathTex(r"a = 3", font_size=32, color=GREEN)
        a_value.next_to(text_a_val_explain, DOWN, buff=0.3)
        self.play(Write(a_value))
        self.wait(2)

        # Group objects for 'a' to fade them out together
        group_a_calc = VGroup(text_a_def, factor_1500_steps, highlight_5_3, text_a_val_explain)
        self.play(FadeOut(group_a_calc))
        
        # --- Solve for 'b' ---
        solve_b_title = Text("Step 2: Solve for 'b'", font_size=30, color=YELLOW)
        solve_b_title.to_edge(UP).shift(DOWN*0.2) # Adjusted position
        self.play(Transform(title, solve_b_title))
        
        a_value_on_screen = a_value.copy() # Keep a_value displayed
        a_value_on_screen.generate_target()
        a_value_on_screen.target.scale(0.8).to_corner(UP + LEFT, buff=0.5)
        self.play(MoveToTarget(a_value_on_screen))


        text_b_def = MathTex(r"\text{Find the greatest integer 'b' such that } 3^b \text{ is a factor of 33,333,333.}", font_size=28)
        text_b_def.next_to(title, DOWN, buff=0.4)
        self.play(Write(text_b_def))
        self.wait(1)

        factor_33m_step1 = MathTex(r"33,333,333 = 3 \times 11,111,111", font_size=32)
        factor_33m_step1.next_to(text_b_def, DOWN, buff=0.3)
        self.play(Write(factor_33m_step1))
        self.wait(2)

        sum_digits_11m = MathTex(r"\text{For } 11,111,111: \text{ sum of digits} = 1+1+1+1+1+1+1+1 = 8", font_size=28)
        sum_digits_11m.next_to(factor_33m_step1, DOWN, buff=0.3)
        self.play(Write(sum_digits_11m))
        self.wait(1.5)
        
        div_by_3_check = MathTex(r"8 \text{ is not divisible by 3, so } 11,111,111 \text{ is not divisible by 3.}", font_size=28)
        div_by_3_check.next_to(sum_digits_11m, DOWN, buff=0.3)
        self.play(Write(div_by_3_check))
        self.wait(2)

        text_b_val_explain = MathTex(r"\text{So, the highest power of 3 in } 33,333,333 \text{ is } 3^1.", font_size=28).next_to(div_by_3_check, DOWN, buff=0.3)
        self.play(Write(text_b_val_explain))
        self.wait(1)

        b_value = MathTex(r"b = 1", font_size=32, color=GREEN)
        b_value.next_to(text_b_val_explain, DOWN, buff=0.3)
        self.play(Write(b_value))
        self.wait(2)
        
        b_value_on_screen = b_value.copy() # Keep b_value displayed
        b_value_on_screen.generate_target()
        b_value_on_screen.target.scale(0.8).next_to(a_value_on_screen, RIGHT, buff=0.5)
        self.play(MoveToTarget(b_value_on_screen))

        group_b_calc = VGroup(text_b_def, factor_33m_step1, sum_digits_11m, div_by_3_check, text_b_val_explain)
        self.play(FadeOut(group_b_calc))

        # --- Evaluate Statements ---
        eval_title = Text("Step 3: Evaluate Statements", font_size=30, color=YELLOW)
        eval_title.to_edge(UP).shift(DOWN*0.2) # Adjusted position
        self.play(Transform(title, eval_title))
        
        # Display a=3 and b=1 clearly
        current_values_display = VGroup(
            MathTex(r"a = 3", font_size=30, color=GREEN),
            MathTex(r"b = 1", font_size=30, color=GREEN)
        ).arrange(RIGHT, buff=1).next_to(title, DOWN, buff=0.4)
        self.play(FadeOut(a_value_on_screen), FadeOut(b_value_on_screen), Write(current_values_display))
        self.wait(1)

        # Statement A
        st_A_text = MathTex(r"\text{A. } a \cdot b = 3", font_size=30)
        st_A_text.next_to(current_values_display, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(st_A_text))
        
        st_A_eval = MathTex(r"3 \cdot 1 = 3", font_size=30).next_to(st_A_text, RIGHT, buff=0.5)
        self.play(Write(st_A_eval))
        st_A_res = MathTex(r"3 = 3 \quad (\text{TRUE})", font_size=30, color=GREEN).next_to(st_A_eval, RIGHT, buff=0.5)
        self.play(Write(st_A_res))
        self.wait(1.5)

        # Statement B
        st_B_text = MathTex(r"\text{B. } a = 3b", font_size=30)
        st_B_text.next_to(st_A_text, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(st_B_text))

        st_B_eval = MathTex(r"3 = 3 \cdot 1", font_size=30).next_to(st_B_text, RIGHT, buff=0.5)
        self.play(Write(st_B_eval))
        st_B_res = MathTex(r"3 = 3 \quad (\text{TRUE})", font_size=30, color=GREEN).next_to(st_B_eval, RIGHT, buff=0.5)
        self.play(Write(st_B_res))
        self.wait(1.5)

        # Statement C
        st_C_text = MathTex(r"\text{C. } 2a > 5b", font_size=30)
        st_C_text.next_to(st_B_text, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(st_C_text))

        st_C_eval = MathTex(r"2 \cdot 3 > 5 \cdot 1", font_size=30).next_to(st_C_text, RIGHT, buff=0.5)
        self.play(Write(st_C_eval))
        st_C_res = MathTex(r"6 > 5 \quad (\text{TRUE})", font_size=30, color=GREEN).next_to(st_C_eval, RIGHT, buff=0.5)
        self.play(Write(st_C_res))
        self.wait(1.5)

        # --- Conclusion ---
        conclusion_title = Text("Conclusion", font_size=30, color=YELLOW)
        conclusion_title.to_edge(UP).shift(DOWN*0.2) # Adjusted position
        
        statements_group = VGroup(st_A_text, st_A_eval, st_A_res, st_B_text, st_B_eval, st_B_res, st_C_text, st_C_eval, st_C_res)
        self.play(FadeOut(current_values_display), Transform(title, conclusion_title))
        
        final_answer_text = Text("All statements A, B, and C are true.", font_size=32, color=BLUE)
        final_answer_text.next_to(title, DOWN, buff=0.7)
        
        self.play(
            statements_group.animate.scale(0.9).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(final_answer_text, DOWN, buff=0.4)
        )
        self.play(Write(final_answer_text))
        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(statements_group), FadeOut(final_answer_text))
        end_text = Text("End of Explanation", font_size=36)
        self.play(Write(end_text))
        self.wait(2)
        self.play(FadeOut(end_text))

# manim -pqh GRE1.py GREProblemSolve
