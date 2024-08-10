import tkinter as tk
from tkinter import messagebox, simpledialog

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")
        self.root.geometry("400x300")

        # Listbox to display notes
        self.notes_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=10)
        self.notes_listbox.pack(pady=10)

        # Entry for new note
        self.new_note_entry = tk.Entry(self.root, width=40)
        self.new_note_entry.pack()

        # Buttons
        add_button = tk.Button(self.root, text="Add Note", command=self.add_note)
        add_button.pack()

        edit_button = tk.Button(self.root, text="Edit Note", command=self.edit_note)
        edit_button.pack()

        delete_button = tk.Button(self.root, text="Delete Note", command=self.delete_note)
        delete_button.pack()

        # Load existing notes
        self.load_notes()

    def load_notes(self):
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                for note in notes:
                    self.notes_listbox.insert(tk.END, note.strip())
        except FileNotFoundError:
            # Handle the case when the file doesn't exist yet
            pass

    def save_notes(self):
        with open("notes.txt", "w") as file:
            for index in range(self.notes_listbox.size()):
                file.write(self.notes_listbox.get(index) + "\n")

    def add_note(self):
        new_note = self.new_note_entry.get()
        if new_note:
            self.notes_listbox.insert(tk.END, new_note)
            self.save_notes()
            self.new_note_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a note.")

    def edit_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            current_note = self.notes_listbox.get(selected_index)
            edited_note = simpledialog.askstring("Edit Note", "Edit the note:", initialvalue=current_note)
            if edited_note is not None:
                self.notes_listbox.delete(selected_index)
                self.notes_listbox.insert(selected_index, edited_note)
                self.save_notes()
        else:
            messagebox.showwarning("Warning", "Please select a note to edit.")

    def delete_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            self.notes_listbox.delete(selected_index)
            self.save_notes()
        else:
            messagebox.showwarning("Warning", "Please select a note to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
