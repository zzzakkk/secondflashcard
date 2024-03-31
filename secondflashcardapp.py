import tkinter as tk

class FlashcardsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcards App")

        self.words = {
            "Python": "A high-level programming language known for its simplicity and readability.",
            "Algorithm": "A step-by-step procedure or formula for solving a problem.",
            "Database": "A structured set of data stored electronically.",
            # Add more words and definitions as needed
        }

        self.current_word = None
        self.word_label = tk.Label(root, font=('Arial', 24, 'bold'), text="")
        self.word_label.pack(pady=20)

        self.show_next_word()

        self.show_definition_button = tk.Button(root, text="Show Definition", command=self.show_definition)
        self.show_definition_button.pack(pady=10)

    def show_next_word(self):
        self.current_word = next(iter(self.words.keys()))
        self.word_label.config(text=self.current_word)

    def show_definition(self):
        if self.current_word:
            definition = self.words.get(self.current_word, "Definition not found")
            self.word_label.config(text=definition)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()