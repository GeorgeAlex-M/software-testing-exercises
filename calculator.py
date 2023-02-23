import tkinter as tk
import random

class Calculator:
    """
    A simple calculator GUI that allows users to perform basic arithmetic calculations.
    """
    
    def __init__(self, master):
        """
        Initializes the calculator GUI.
        
        :param master: The parent window for the calculator.
        """
        self.master = master
        master.title("Calculator")
        master.iconbitmap('C:/Users/Alex/Desktop/nyancat.png')
        
        # Create a StringVar to store the calculator display
        self.result = tk.StringVar()
        self.result.set("")
        
        # Create a label to display the calculator result
        self.display = tk.Label(master, textvariable=self.result, font=("Arial", 18), width=12, height=2)
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Create buttons for the calculator
        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+", "="
        ]
        
        self.row = 1
        self.col = 0
        
        for button in self.buttons:
            command = lambda x=button: self.click(x)
            tk.Button(master, text=button, width=6, height=2, command=command).grid(row=self.row, column=self.col)
            self.col += 1
            if self.col > 3:
                self.col = 0
                self.row += 1
                
    def click(self, key):
        """
        Handles button clicks for the calculator.
        
        :param key: The button that was clicked.
        """
        if key == "C":
            # Clear the calculator display
            self.result.set("")
        elif key == "=":
            if self.result.get() == "2":
                # Display the result for 2 seconds
                self.result.set("2")
                self.master.after(2000, self.clear_result)
            else:
                try:
                    # Evaluate the expression and display the result for 3 seconds
                    result = eval(self.result.get())
                    self.result.set(str(result))
                    if self.result.get() == "3":
                        # Generate random numbers for 2 seconds and transform into 10
                        self.master.after(2000, self.transform_result)
                        self.generate_numbers()
                    else:
                        # Display the result for 3 seconds
                        self.master.after(3000, self.clear_result)
                except:
                    # Display an error message if the expression cannot be evaluated
                    self.result.set("Error")
        else:
            # Append the clicked button to the calculator display
            self.result.set(self.result.get() + key)
            
    def clear_result(self):
        """
        Clears the calculator display.
        """
        if self.result.get() == "2":
            # Clear only the result "2" after 2 seconds
            self.result.set("")
        
    def generate_numbers(self):
        """
        Generates random numbers for the calculator display for 2 seconds.
        """
        for i in range(10):
            # Generate a random number and pad with leading zeroes
            number = str(random.randint(0, 10)).zfill(1)
            self.result.set(number)
            self.master.update_idletasks()
            self.master.after(200)

    def transform_result(self):
        """
        Transforms the calculator result from "3" to "10".
        """
        self.result.set("10")
        
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
