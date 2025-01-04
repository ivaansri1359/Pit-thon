import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.screen = tk.StringVar()
        entry = tk.Entry(self.root, textvar=self.screen, font="lucida 20 bold")
        entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        frame = tk.Frame(self.root)
        frame.pack()

        for i, button in enumerate(buttons):
            btn = tk.Button(frame, text=button, font="lucida 15 bold")
            btn.grid(row=i//4, column=i%4, padx=10, pady=10)
            btn.bind("<Button-1>", self.click)

    def click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            self.calculate()
        elif text == "C":
            self.clear_screen()
        else:
            self.update_screen(text)

    def calculate(self):
        try:
            result = str(eval(self.screen.get()))
            self.screen.set(result)
        except Exception:
            self.screen.set("Error")

    def clear_screen(self):
        self.screen.set("")

    def update_screen(self, text):
        self.screen.set(self.screen.get() + text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()