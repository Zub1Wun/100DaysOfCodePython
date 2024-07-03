from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 8)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler (by Zub1Wun)")

        self.window.configure(bg=THEME_COLOR, pady=20, padx=20)
        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}",
            font=SCORE_FONT,
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        width = 300
        height = 250
        self.canvas = Canvas(width=width, height=height, bg="white")
        self.question_text = self.canvas.create_text(
            width / 2,
            height / 2,
            width=290,
            text="q_text",
            fill=THEME_COLOR,
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.check_true)  # if use parenthesis
        # for method call in command, then it will call method before it is clicked
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.configure(bg="Green")
        else:
            self.canvas.configure(bg="Red")
        self.window.after(1000, self.get_next_question)  # Cant use time.sleep as it's outside mainloop
