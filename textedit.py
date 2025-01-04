import tkinter as tk
from tkinter import filedialog, font

class TextEdit:
    def __init__(self, root, bold_font, italic_font, underline_font):
        self.root = root
        self.root.title("Text Editor")

        self.text_area = tk.Text(self.root, wrap='word', font=("Arial", 12))
        self.text_area.pack(expand=1, fill='both')

        self.bold_font = bold_font
        self.italic_font = italic_font
        self.underline_font = underline_font

        self.create_menu()

        # Bind Ctrl+B to make_bold
        self.root.bind('<Control-b>', self.make_bold)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        format_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Bold", command=self.make_bold)
        format_menu.add_command(label="Italic", command=self.make_italic)
        format_menu.add_command(label="Underline", command=self.make_underline)

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

    def make_bold(self, event=None):
        try:
            current_tags = self.text_area.tag_names("sel.first")
            if "bold" in current_tags:
                self.text_area.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text_area.tag_add("bold", "sel.first", "sel.last")
                self.text_area.tag_configure("bold", font=self.bold_font)
        except tk.TclError:
            current_index = self.text_area.index(tk.INSERT)
            current_tags = self.text_area.tag_names(current_index)
            if "bold" in current_tags:
                self.text_area.tag_remove("bold", current_index)
            else:
                self.text_area.tag_add("bold", current_index)
                self.text_area.tag_configure("bold", font=self.bold_font)

    def make_italic(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "italic" in current_tags:
            self.text_area.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("italic", "sel.first", "sel.last")
            self.text_area.tag_configure("italic", font=self.italic_font)

    def make_underline(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "underline" in current_tags:
            self.text_area.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("underline", "sel.first", "sel.last")
            self.text_area.tag_configure("underline", font=self.underline_font)

if __name__ == "__main__":
    root = tk.Tk()
    bold_font = font.Font(root, root.option_get("font", "Font"))
    bold_font.configure(weight="bold")
    italic_font = font.Font(root, root.option_get("font", "Font"))
    italic_font.configure(slant="italic")
    underline_font = font.Font(root, root.option_get("font", "Font"))
    underline_font.configure(underline=True)
    app = TextEdit(root, bold_font, italic_font, underline_font)
    root.mainloop()