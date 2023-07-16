import tkinter as tk
import random
import string

class pg(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Password Generator")
        self.geometry("4000x2000")
        self.label = tk.Label(self, text="Random Password Generator", font=("Helvetica", 16))
        self.label.pack(pady=10)
        self.password_label = tk.Label(self, text="Generated Password:")
        self.password_label.pack()
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password_var, state='readonly')
        self.password_entry.pack()
        self.generate_button = tk.Button(self, text="Generate Password", command=self.gp)
        self.generate_button.pack(pady=10)
        self.copy_button = tk.Button(self, text="Copy to Clipboard", command=self.ctc)
        self.copy_button.pack()
    def gp(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
    def ctc(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_var.get())
        self.update()  # required for macOS to work properly
app = pg()
app.mainloop()
