#Exercise 1 - Maths Quiz
import tkinter as tk 
from tkinter import messagebox  #to show pop up messages in a message box.
import random   #to add random numbers and operators.

#declaring global variables
current_question = 0
score = 0
First_attempt = True
level = ''

#doing the setup for the main screen window
window = tk.Tk()
window.title( "Maths Quiz")
window.geometry("500x500") #adding the size of the window
window.attributes("-fullscreen", True) #to open the program in full screen
window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False)) #to exit the full screen using esc button


#adding animations before the quiz starts
def introAnimation():
    for widget in window.winfo_children():
        widget.destroy()

    window.config ( bg="black")

    #to show a a text which will welcome the user.
    intro_label = tk.Label(window,
                           text="Welcome to MATHS QUIZ!",font=("Arial", 40,"bold"), fg="white", bg="black")
    
    x_start = -500  #the text will start from left side and come to the main screen sliding in 
    y_pos = window.winfo_screenheight()//2
    intro_label.place(x=x_start, y=y_pos)

    def slideText(current_x):
        if current_x < window.winfo_screenwidth()//2 - 300:
            current_x += 10  #setting the speed of the slide in 
            intro_label.place(x=current_x, y=y_pos)
            window.after(  20, lambda: slideText(current_x))
        else:
            #adding a delay when moving on to start the quiz
            window.after(1000, displayMenu)

    slideText(x_start)

#adding functions for the 1st displau menu i.e, difficulty screen from which the users will select the quiz difficulty
def displayMenu():
    for widget in window.winfo_children():
        widget.destroy()
        #the above line will return a list of all the widgets which will be in the window
        #and call ".destroy()" to remove it from the window so that when we move to another screen, the previous buttons won't stay

    #to place the content at the center of the screen on full size
    center_Frame = tk.Frame(window)
    center_Frame.pack(expand=True)
    
        #Now we wil create label Widget
    title_label = tk.Label( window, text="Difficulty LEVEL", font=("Arial",30,"bold")) #adding text functions like fonts and font sizes
    title_label.pack(pady=15) #adding padding(spacing)

        #Now we will create a button

        #Button for Easy level
        # tk.Button will create a button which the user can click
    button_easy = tk.Button(window, text="1.Easy", font=("Arial", 20), command=lambda: start_quiz('easy'))
    button_easy.pack(pady=10)

        #Button for Moderate level
    button_moderate = tk.Button(window, text="2.Moderate", font=("Arial",20), command=lambda: start_quiz('moderate'))
    button_moderate.pack(pady=10)

        #Button for Advanced Level
    button_advanced = tk.Button(window, text="3.Advanced", font=("Arial",20), command=lambda: start_quiz('advanced'))
    button_advanced.pack(pady=10)
    #There are 3 buttons above and each button represents a difficulty level i.e, Easy, Moderate and Advanced
    #we also added a padding of 10 in all the buttons to add some spacing.

#now we will add a function to generate random integers based on the level of difficulty
def randomInt( level ):
    if level == 'easy':
        return random.randint(1,9), random.randint(1,9)
    elif level == 'moderate':
        return random.randint(10,99), random.randint(10,99)
    else:
        return random.randint(1000,9999), random.randint(1000,9999)

#now we will add function which will decide the operators for the quiz questions
def decideOperation():
    return random.choice(['+','-']) #adding and subtraction

#now we will add function to start the maths quiz
def start_quiz(chosen_level):
    global level, current_question, score 
    level = chosen_level
    current_question = 0
    score = 0
    displayProblem()

def displayProblem():
    global numb1, numb2, operation, First_attempt

    #to clear the screen 
    for widget in window.winfo_children():
        widget.destroy()
    #the attempt chances will reset after each question
    First_attempt = True
    
     #to place the content at the center of the screen on full size
    center_Frame = tk.Frame(window, highlightbackground="red", highlightthickness=5)
    center_Frame.pack(expand=True)

    numb1, numb2 = randomInt( level)
    operation = decideOperation()

    #to display the questions box and also adding a thick border line around it 
    question_label = tk.Label(center_Frame, text=f"Question {current_question + 1} of 10", font=("Arial", 15,"bold"), bd=5, relief="solid", highlightbackground="red", highlightthickness=5)
    question_label.pack(pady=15)

    #to display the question in the box
    problem_label = tk.Label(center_Frame, text=f"{numb1}{operation}{numb2}= ", font=("Arial",20,"bold"))
    problem_label.pack(pady=15)

    #to have a input box to put the answer and also adding a thick border line around it 
    answer_entry = tk.Entry(center_Frame, font=("Arial", 14,"italic"), bd=5, relief="solid")
    answer_entry.pack(pady=15)
    answer_entry.focus()

    #function for the submit button
    submit_button = tk.Button(center_Frame, text="Submit", font=("Arial", 15), command=lambda: isCorrect(answer_entry.get()))
    submit_button.pack(pady=15 )
    
    #adding a function so we can submit answers by clicking enter key
    window.bind("<Return>", lambda event: isCorrect(answer_entry.get()))

#now we will add a fuction to check whether the answer given by the user is correct or not
def isCorrect(answer):
    global current_question, score, First_attempt

    try:
        user_answer = int( answer)
    except ValueError:
        messagebox.showerror("Error", "Please enter a Number which is Valid")
        return

    #adding if else statement to calculate the answer using addition or subtraction operation 
    if operation == '+':
        correct_answer = numb1 + numb2
    else:
        correct_answer = numb1 - numb2

    #checking whether the answer is correct or not
    if user_answer == correct_answer:
        current_question += 1
        if First_attempt:       #if the answer is given in 1st attempt
            score += 10         #score will be 10
            messagebox.showinfo("Correct", "Correct answer on 1st try! Well Done (+10 Points added)")
        else:
            score += 5     
            messagebox.showinfo("Correct", "Correct answer but on 2nd try (+5 points added)")
        if current_question < 10:
            displayProblem()
        else:
            displayResults()  
    else: 
        if First_attempt:
            First_attempt = False
            messagebox.showwarning("Incorrect", "Incorrect answer, Please Try again!")
        else:
            current_question += 1
            messagebox.showinfo("Incorrect", f"You have entered a wrong answer again, The correct answer is {correct_answer}.")
            if current_question < 10:
                displayProblem()
            else: 
                displayResults()

#now we will add a function which will show the users their respective final scores
def displayResults():
    for widget in window.winfo_children():
        widget.destroy()
        
     #to place the content at the center of the screen on full size
    center_Frame = tk.Frame( window)
    center_Frame.pack( expand=True)

    #using else if statements to decide the grade based on the score which the user scores.
    grade = '' 
    if score >= 90:
        grade = 'A+'
    elif score >=  80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    else: 
        grade = 'F'

    result_label = tk.Label(center_Frame, text=f"Your Final SCORE will be: {score}/100", font=("Arial", 15, "bold"))
    result_label.pack(pady=15)

    grade_label = tk.Label(center_Frame, text=f"Your Grade is: {grade}" ,font=("Arial", 15, "bold"))
    grade_label.pack(pady=15)

    play_again = tk.Button(center_Frame, text="Please Play again", font=("Arial", 15), command=displayMenu, highlightbackground="red", highlightthickness=5)
    play_again.pack(pady=15)

    quit_button = tk.Button(center_Frame, text="Please QUIT!", font=("Arial", 15), command=window.destroy, highlightbackground="red", highlightthickness=5)
    quit_button.pack(pady=15)

introAnimation()
window.mainloop()
