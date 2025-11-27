import tkinter as tk    #importing tkinter library 
from tkinter import messagebox, simpledialog

root = tk.Tk()  #creating the window
root.title("Student Manager App")
root.geometry("1000x1000")  #describing the window size 
root.configure(bg="#69B680")    #putting bg color to the window

#adding a title at top
title_label = tk.Label(root, text="Student Manager", font=("Arial", 24, "bold"), bg="#69B680", fg="white")
title_label.pack(pady=20)


#adding a function that will read the txt file and load the data from the file 
def load_students():
    students = []   #adding a empty list to store all student data
    try:
        
        #linking the txt file location
        with open(r"C:\Users\DELL\OneDrive\Documents\GitHub\skills-portfolio-iArman06\Assessment 1 - Skills Portfolio\Exercise 3 - Student Manager\A1 - Resources\studentMarks.txt", "r") as file:
            count = int(file.readline().strip())
            for _ in range(count):
                
                #reading each line at a time and separating them using commas
                line = file.readline().strip().split(",")
                
                #we created a dictionary to store the mark of the student 
                student = {
                    "id": line[0],      #student ID
                    "name": line[1],    #name of student
                    "c1": int(line[2]), #mark 1
                    "c2": int(line[3]), #mark 2
                    "c3": int(line[4]), #mark 3
                    "exam": int(line[5])    #final exam mark
                }
                students.append(student)
    except FileNotFoundError:
        
        #if the txt file is missing, it will show a error 
        messagebox.showerror("Error", "studentMarks.txt file was not found!")
    return students

#loading all the student data when the program starts 
students = load_students()

#adding a function to calculate the total marks i.e, mark1 + mark2 + mark3
def calc_coursework(s):
    return s["c1"] + s["c2"] + s["c3"]

#adding function to calculate the overall percentage of the class
def calc_percentage(s):
    total = calc_coursework(s) + s["exam"]
    return round((total / 160) * 100, 2)

#adding function that will determine the grade of a student based on the percentage
def calc_grade(percent):
    #using if else statment to add the grade to a respective mark range
    if percent >= 70:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"

def clear_output():
    output.delete("1.0", tk.END)

def write(text):
    output.insert(tk.END, text + "\n")

#No: 1 - to show all the data record one by one 
def view_all():
    clear_output()
    if not students:
        write("Student data is not loaded") #if there are no students, this message will load
        return

    total_percent = 0
    
    #adding loop for each student
    for s in students:
        cw = calc_coursework(s)         #mark total
        percent = calc_percentage(s)    #percentage
        grade = calc_grade(percent)     #grade 
        total_percent += percent        #class total percentage

        write(f"Name: {s['name']}")
        write(f"ID: {s['id']}")
        write(f"Coursework Total: {cw} / 60")
        write(f"Exam Mark: {s['exam']} / 100")
        write(f"Overall Percent: {percent}%")
        write(f"Grade: {grade}")
        write("-" * 40)

        #to show summary 
    avg = round(total_percent / len(students), 2)
    write(f"\nTotal Students: {len(students)}")
    write(f"Class Average: {avg}%")

#No: 2- for showing individual details of each student
def view_individual():
    
    #upon clicking the button, it will ask either the student name or their ID in order to show the info of that student
    sid = simpledialog.askstring("Student Search", "Enter the Name of the student or Student ID:")
    if not sid:
        return

    sid = sid.lower()   #to eliminate the problem of uppercase and lowercase
    clear_output()

    #then the program will look for the student
    for s in students:
        if sid == s["id"] or sid in s["name"].lower():
            cw = calc_coursework(s)
            percent = calc_percentage(s)
            grade = calc_grade(percent)

            #student details will be displayed in this format upon finding
            write(f"Name: {s['name']}")
            write(f"ID: {s['id']}")
            write(f"Coursework Total: {cw} / 60")
            write(f"Exam Mark: {s['exam']}")
            write(f"Overall Percent: {percent}%")
            write(f"Grade: {grade}")
            return
    #if the entered student name or ID is wrong, the message below will be shown to the user
    write("Sorry!, Student not found")


# No: 3 - to show the student with Highest marks
def highest_score():
    clear_output()
    if not students:
        write("No Data found")
        return

    #the program will find the student with highest percentage and then display it to the user
    top_student = max(students, key=lambda s: calc_percentage(s))
    show_one_student(top_student)

# No: 4- To show the student with the lowest mark
def lowest_score():
    clear_output()
    if not students:
        write("No Dats found")
        return

    #same process as finding in highest percentage, except here its for lower percentage
    low_student = min(students, key=lambda s: calc_percentage(s))
    show_one_student(low_student)

def show_one_student(s):
    cw = calc_coursework(s)
    percent = calc_percentage(s)
    grade = calc_grade(percent)

    write(f"Name: {s['name']}")
    write(f"ID: {s['id']}")
    write(f"Coursework Total: {cw} / 60")
    write(f"Exam Mark: {s['exam']}")
    write(f"Overall Percent: {percent}%")
    write(f"Grade: {grade}")

#creating a frame to hold all the buttons 
frame = tk.Frame(root, bg="#000000")
frame.pack(pady=10)

#adding color and styling to the buttons
button_style = {"bg": "#69B680", "fg": "white", "width": 30, "height": 2}

#creating the buttons for all four functionality mentioned in the exercise document
tk.Button(frame, text="All student records", command=view_all, **button_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Individual student record", command=view_individual, **button_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Student with highest total score", command=highest_score, **button_style).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Student with lowest total score", command=lowest_score, **button_style).grid(row=3, column=0, padx=5, pady=5)

#adding the output mox where all the output will be shown
output = tk.Text(root, width=80, height=20, borderwidth=2, relief="sunken", bg="#9ED6AF", fg="black")
output.pack(pady=10)

#used to keep the window open
root.mainloop()
