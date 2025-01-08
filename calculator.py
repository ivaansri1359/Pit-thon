import math
import tkinter as tk
from tkinter import filedialog, font
import matplotlib.pyplot as plt
import numpy as np

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.create_home_screen()

    def create_home_screen(self):
        self.clear_screen()

        tk.Button(self.root, text="Normal Math", command=self.normal_math).pack(pady=10)
        tk.Button(self.root, text="Scientific Math", command=self.sci_math).pack(pady=10)
        tk.Button(self.root, text="Graph Math", command=self.graph_math).pack(pady=10)
        tk.Button(self.root, text="Math Notes", command=self.math_notes).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def normal_math(self):
        self.clear_screen()
        self.expression = ""
        self.entry = tk.Entry(self.root, width=40, borderwidth=5)
        self.entry.pack(pady=10)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for i, button in enumerate(buttons):
            tk.Button(self.root, text=button, width=10, height=2, command=lambda b=button: self.click(b)).grid(row=i//4+1, column=i%4)
        tk.Button(self.root, text="Clear", width=10, height=2, command=self.clear).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Back", width=10, height=2, command=self.create_home_screen).grid(row=5, column=2, columnspan=2)

    def click(self, button):
        if button == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += button
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

    def sci_math(self):
        self.clear_screen()
        self.expression = ""
        self.entry = tk.Entry(self.root, width=40, borderwidth=5)
        self.entry.pack(pady=10)
        buttons = [
            'sin', 'cos', 'tan', 'log',
            'sqrt', 'pi', 'e', '^',
            '(', ')', 'C', '=',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+'
        ]
        for i, button in enumerate(buttons):
            tk.Button(self.root, text=button, width=10, height=2, command=lambda b=button: self.sci_click(b)).grid(row=i//4+1, column=i%4)
        tk.Button(self.root, text="Back", width=10, height=2, command=self.create_home_screen).grid(row=8, column=0, columnspan=4)

    def sci_click(self, button):
        if button == "=":
            try:
                self.expression = str(eval(self.expression.replace('^', '**').replace('sqrt', 'math.sqrt').replace('log', 'math.log').replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan').replace('pi', 'math.pi').replace('e', 'math.e')))
            except:
                self.expression = "Error"
        elif button == "C":
            self.expression = ""
        else:
            self.expression += button
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def graph_math(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter function of x (e.g., x**2 + 2*x + 1):").pack(pady=10)
        self.function_entry = tk.Entry(self.root, width=40, borderwidth=5)
        self.function_entry.pack(pady=10)
        tk.Button(self.root, text="Plot", command=self.plot_graph).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_home_screen).pack(pady=10)

    def plot_graph(self):
        function = self.function_entry.get()
        x = np.linspace(-10, 10, 400)
        y = eval(function)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of {function}')
        plt.grid(True)
        plt.show()

    def math_notes(self):
        self.clear_screen()
        self.text_area = tk.Text(self.root, wrap='word', font=("Arial", 12))
        self.text_area.pack(expand=1, fill='both')
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Back", command=self.create_home_screen)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()