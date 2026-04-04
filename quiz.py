# quiz.py
# A general knowledge quiz game with a tkinter UI

import tkinter as tk
from tkinter import messagebox    # for the popup at the end

# ══════════════════════════════════════════
# QUESTIONS — list of dictionaries
# each question has: question, options, answer, fun fact
# ══════════════════════════════════════════

questions = [
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra",
        "fact": "Canberra became the capital in 1913!"
    },
    {
        "question": "How many planets are in our solar system?",
        "options": ["7", "8", "9", "10"],
        "answer": "8",
        "fact": "Pluto was reclassified as a dwarf planet in 2006."
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific",
        "fact": "The Pacific Ocean covers more than 30% of Earth's surface!"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Van Gogh", "Picasso", "Da Vinci", "Michelangelo"],
        "answer": "Da Vinci",
        "fact": "Leonardo da Vinci painted it between 1503 and 1519."
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "answer": "Au",
        "fact": "Au comes from the Latin word Aurum meaning gold."
    },
    {
        "question": "Which country has the largest population?",
        "options": ["USA", "India", "China", "Russia"],
        "answer": "India",
        "fact": "India surpassed China as the most populous country in 2023!"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6",
        "fact": "Honeycombs are made of hexagons — the most efficient shape!"
    },
    {
        "question": "What is the fastest animal on land?",
        "options": ["Lion", "Horse", "Cheetah", "Leopard"],
        "answer": "Cheetah",
        "fact": "Cheetahs can reach 112 km/h in just 3 seconds!"
    },
    {
        "question": "In which year did World War 2 end?",
        "options": ["1943", "1944", "1945", "1946"],
        "answer": "1945",
        "fact": "WW2 ended on September 2, 1945 with Japan's surrender."
    },
    {
        "question": "What is the square root of 144?",
        "options": ["11", "12", "13", "14"],
        "answer": "12",
        "fact": "12 x 12 = 144. You can verify on your calculator project!"
    },
]

# ══════════════════════════════════════════
# QUIZ LOGIC
# ══════════════════════════════════════════

current_question = 0    # tracks which question we're on
score = 0               # tracks correct answers
answered = False        # stops user clicking twice on same question

def load_question():
    """Load the current question onto the screen"""
    global answered
    answered = False

    q = questions[current_question]   # get current question dictionary

    # update question number and score labels
    progress_label.config(text=f"Question {current_question + 1} of {len(questions)}")
    score_label.config(text=f"Score: {score}")

    # update the question text
    question_label.config(text=q["question"])

    # update each button with the 4 options
    for i, btn in enumerate(option_buttons):
        btn.config(
            text=q["options"][i],
            bg="#2c2c2e",           # reset to default dark color
            fg="white",
            state="normal"          # make clickable again
        )

    # hide the fact and next button
    fact_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(selected):
    """Called when user clicks an answer button"""
    global score, answered

    if answered:        # ignore clicks if already answered
        return

    answered = True     # mark as answered so user can't click again

    correct = questions[current_question]["answer"]
    fact    = questions[current_question]["fact"]

    if selected == correct:
        score += 1
        score_label.config(text=f"Score: {score}")
        fact_label.config(
            text=f"Correct!  {fact}",
            fg="#30d158"            # green for correct
        )
    else:
        fact_label.config(
            text=f"Wrong! Correct answer: {correct}\n{fact}",
            fg="#ff453a"            # red for wrong
        )

    # highlight correct answer green, wrong answer red
    for btn in option_buttons:
        if btn.cget("text") == correct:
            btn.config(bg="#1a3a2a", fg="#30d158")   # green highlight
        elif btn.cget("text") == selected:
            btn.config(bg="#3a1a1a", fg="#ff453a")   # red highlight
        btn.config(state="disabled")                  # disable all buttons

    next_btn.config(state="normal")    # now allow moving to next question

def next_question():
    """Move to the next question or show final score"""
    global current_question

    current_question += 1

    if current_question < len(questions):
        load_question()           # load next question
    else:
        show_final_score()        # quiz is done!

def show_final_score():
    """Show a popup with the final result"""
    total = len(questions)
    percentage = (score / total) * 100

    if percentage == 100:
        message = "Perfect score! You're a genius!"
    elif percentage >= 70:
        message = "Great job! Well done!"
    elif percentage >= 50:
        message = "Not bad! Keep learning!"
    else:
        message = "Keep practicing, you'll get better!"

    messagebox.showinfo(
        "Quiz Complete!",
        f"Your score: {score} / {total}\n{percentage:.0f}%\n\n{message}"
    )
    window.destroy()    # close the window after popup


# ══════════════════════════════════════════
# THE UI — building the window
# ══════════════════════════════════════════

window = tk.Tk()
window.title("General Knowledge Quiz")
window.resizable(False, False)
window.configure(bg="#1c1c1e")

# ── Top bar: progress + score ──────────────
top_frame = tk.Frame(window, bg="#1c1c1e")
top_frame.pack(fill="x", padx=20, pady=(20, 10))

progress_label = tk.Label(
    top_frame, text="Question 1 of 10",
    font=("Arial", 13), bg="#1c1c1e", fg="#888888"
)
progress_label.pack(side="left")

score_label = tk.Label(
    top_frame, text="Score: 0",
    font=("Arial", 13, "bold"), bg="#1c1c1e", fg="#378ADD"
)
score_label.pack(side="right")

# ── Question box ──────────────────────────
q_frame = tk.Frame(window, bg="#2c2c2e", padx=20, pady=20)
q_frame.pack(fill="x", padx=20, pady=10)

question_label = tk.Label(
    q_frame, text="", font=("Arial", 15, "bold"),
    bg="#2c2c2e", fg="white",
    wraplength=380,        # wraplength wraps long text onto next line
    justify="left"
)
question_label.pack(anchor="w")

# ── Answer buttons (2x2 grid) ─────────────
options_frame = tk.Frame(window, bg="#1c1c1e")
options_frame.pack(padx=20, pady=10)

option_buttons = []
labels = ["A", "B", "C", "D"]

for i in range(4):
    btn = tk.Button(
        options_frame,
        text="",
        font=("Arial", 13),
        bg="#2c2c2e", fg="white",
        activebackground="#3a3a3c",
        relief="flat", bd=0,
        cursor="hand2",
        width=22, height=2,
        anchor="w",             # left-align text inside button
        padx=10,
        wraplength=180,
        command=lambda b=i: check_answer(option_buttons[b].cget("text"))
    )
    # place in 2x2 grid
    row = i // 2      # 0,0,1,1
    col = i % 2       # 0,1,0,1
    btn.grid(row=row, column=col, padx=5, pady=5)
    option_buttons.append(btn)

# ── Fact / feedback label ─────────────────
fact_label = tk.Label(
    window, text="",
    font=("Arial", 12), bg="#1c1c1e", fg="#30d158",
    wraplength=400, justify="left"
)
fact_label.pack(padx=20, pady=(0, 10))

# ── Next button ───────────────────────────
next_btn = tk.Button(
    window, text="Next Question →",
    font=("Arial", 14, "bold"),
    bg="#378ADD", fg="white",
    activebackground="#185FA5",
    relief="flat", bd=0,
    cursor="hand2",
    width=28, height=2,
    command=next_question,
    state="disabled"         # disabled until user answers
)
next_btn.pack(pady=(0, 20))

# ── Start the quiz ────────────────────────
load_question()       # load the first question
window.mainloop()     # keep window open