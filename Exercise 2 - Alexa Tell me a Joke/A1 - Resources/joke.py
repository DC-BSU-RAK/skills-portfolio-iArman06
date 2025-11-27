#Exercise 2 - Alexa tell me a Joke!

#Importing tkinter library 
import tkinter as tk
from tkinter import messagebox  #for showing error message
import random   #for showing random emojis

root=tk.Tk()

#adding a function to load jokes from the txt file of Random Jokes
def load_jokes():
    jokes=[]    #adding a empty list to store all the jokes
    try:
        
        #Linking the txt file
        with open(r"C:\Users\DELL\OneDrive\Documents\GitHub\skills-portfolio-iArman06\Assessment 1 - Skills Portfolio\Exercise 2 - Alexa Tell me a Joke\A1 - Resources\randomJokes.txt","r") as file:
            content= file.read().strip().split("\n\n")
            
            #the program splits the joke into lines and makes sure whether each joke has 2line or not and then adds the joke to the list
            for block in content:
                lines= block.strip().split("\n")
                if len(lines)>= 2:
                    jokes.append((lines[0], lines[1]))
                    
    #if the txt file is not found, it will show a error through the message box
    except FileNotFoundError:
        messagebox.showerror("Sorry!", "The file randomeJokes.txt was not found")
    return jokes

#making the interface GUI
class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa, Tell me a Joke!")   #adding a title
        self.root.geometry("1000x1000")     #adding the sreen size 
        self.root.configure(bg="#20232a")
        
        
        self.jokes = load_jokes()   #loads the joke from the file
        self.index=0
        
#adding the emoji animation at the main menu
        self.emoji_label = tk.Label(root, text="💀 🤣 😒 😂 😍 👌 😭", font=("Arial",30), bg="#20232a", fg="white")
        self.emoji_label.pack(pady=45)
        
#adding the intro text
        self.title_label = tk.Label(root, text="Alexa, Tell me a Joke!", font=("Ärial", 25, "bold" ),bg="#20232a", fg="cyan")
        self.title_label.pack()
        
#adding the button to start the joke section 
        self.root.after(2000, self.show_start_button)
        
        self.joke_label = tk.Label(root, text="", font=("Arial", 20), bg="#20232a", fg="white", wraplength=500)
        self.punchline_button = None
        self.next_button = None
        
        self.animate_emojis()

#adding the emojis for animation 
    def animate_emojis(self):
        emojis = ["💀", "🤣", "😒", "😂", "😍", "👌", "😭"]
        text = " ".join(random.choices(emojis, k=5))
        self.emoji_label.config(text=text)
        self.root.after(300, self.animate_emojis)
        
    def show_start_button(self):
        self.start_button = tk.Button(self.root, text="Alexa, Tell Me a Joke", font=("Arial", 15 , "bold"), bg="cyan", fg="black", command=self.show_joke)
        self.start_button.pack(pady=20)
        
        
#adding function to show the first part of the joke
    def show_joke(self):
        if not self.jokes:
            return
        
        self.start_button.destroy()
        setup = self.jokes[self.index][0]
        self.joke_label.config(text=setup)
        self.joke_label.pack(pady=30)
        
    #adding button to reveal the puncline of the respective joke 
        self.punchline_button = tk.Button(self.root, text="Show Punchline", font=("Arial", 14), bg="#61dafb", command=self.show_punchline)
        self.punchline_button.pack()
        
#adding function to show the punchline of each respective joke
    def show_punchline(self):
        punchline = self.jokes[self.index][1]
        self.joke_label.config(text=f"{self.jokes[self.index][0]}\n\n --> {punchline}")

        self.punchline_button.destroy()

        #adding next button and quit button down below
        self.next_button = tk.Button(self.root, text="Next Joke", font=("Arial", 15), bg="#32acd1", fg="white", width=12, height=1, command=self.next_joke)
        self.next_button.pack(side="right", padx=40, pady=20)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 15),bg="#32acd1", fg="white", width=12, height=1, command=self.root.quit)
        self.quit_button.pack(side="left", padx=40, pady=20)
        
#adding function to load the next joke after one joke is done
    def next_joke(self):
        self.index = (self.index + 1) % len(self.jokes)
        self.joke_label.config(text=self.jokes[self.index][0])

        #to remove the puncline which was already revealed 
        if self.punchline_button:
            self.punchline_button.destroy()
        if self.next_button:
            self.next_button.destroy()
        if self.quit_button:
            self.quit_button.destroy()
            
#new punchline button
        self.punchline_button = tk.Button(self.root, text="Show Punchline", font=("Arial", 14), bg="#61dafb", command=self.show_punchline)
        self.punchline_button.pack()



app=JokeApp(root)
root.mainloop() #to run the window in loop 
