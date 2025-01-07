import tkinter as tk
from tkinter import messagebox

class IPhoneSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("iPhone Simulator")
        self.geometry("300x600")
        self.configure(bg="black")

        self.create_widgets()

    def create_widgets(self):
        self.screen = tk.Frame(self, bg="white", width=280, height=500)
        self.screen.pack(pady=20)

        self.home_button = tk.Button(self, text="Home", command=self.home_button_pressed)
        self.home_button.pack(side=tk.BOTTOM, pady=10)

        self.app_buttons = []
        app_names = ["YouTube", "Facebook", "Discord", "WhatsApp", "App 5", "App 6"]
        for i in range(6):
            button = tk.Button(self.screen, text=app_names[i], command=lambda i=i: self.open_app(i+1))
            button.grid(row=i//3, column=i%3, padx=10, pady=10)
            self.app_buttons.append(button)

    def home_button_pressed(self):
        for button in self.app_buttons:
            button.config(state=tk.NORMAL)
        self.screen.config(bg="white")
        self.app_buttons[0].config(text="YouTube")
        self.app_buttons[1].config(text="Facebook")
        self.app_buttons[2].config(text="Discord")
        self.app_buttons[3].config(text="WhatsApp")
        messagebox.showinfo("Home Button", "Home button pressed!")

    def open_app(self, app_number):
        messagebox.showinfo("App Opened", f"App {app_number} opened!")

if __name__ == "__main__":
    app = IPhoneSimulator()
    app.mainloop()