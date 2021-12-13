from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        red_wrong = PhotoImage(file="images/false.png")
        self.red_button = Button(image=red_wrong, highlightthickness=0, borderwidth=0, command=self.wrong_answer)
        self.red_button.grid(column=1, row=2)

        green_right = PhotoImage(file="images/true.png")
        self.green_button = Button(image=green_right, highlightthickness=0, borderwidth=0, command=self.true_answer)
        self.green_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The quiz over.")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def true_answer(self):
        is_answer_check = self.quiz.check_answer("True")
        self.feedback_to_user(is_answer_check)

    def wrong_answer(self):
        is_answer_check = self.quiz.check_answer("False")
        self.feedback_to_user(is_answer_check)

    def feedback_to_user(self, is_answer_check):
        if is_answer_check:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



