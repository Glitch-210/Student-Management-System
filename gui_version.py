import tkinter as tk
from tkinter import ttk, messagebox

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")

        # Data storage
        self.students = []
        self.Id = []
        self.marks = []

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create notebook for different operations
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Add Student Tab
        self.add_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.add_frame, text="Add Student")
        self.setup_add_student_frame()

        # Display Tab
        self.display_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.display_frame, text="Display Student")
        self.setup_display_frame()

        # Update Tab
        self.update_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.update_frame, text="Update Student")
        self.setup_update_frame()

        # Delete Tab
        self.delete_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.delete_frame, text="Delete Student")
        self.setup_delete_frame()

    def setup_add_student_frame(self):
        # Add Student Form
        ttk.Label(self.add_frame, text="Student ID:").grid(row=0, column=0, pady=5)
        self.student_id = ttk.Entry(self.add_frame)
        self.student_id.grid(row=0, column=1, pady=5)

        ttk.Label(self.add_frame, text="Name:").grid(row=1, column=0, pady=5)
        self.student_name = ttk.Entry(self.add_frame)
        self.student_name.grid(row=1, column=1, pady=5)

        ttk.Label(self.add_frame, text="Maths Marks:").grid(row=2, column=0, pady=5)
        self.maths_marks = ttk.Entry(self.add_frame)
        self.maths_marks.grid(row=2, column=1, pady=5)

        ttk.Label(self.add_frame, text="Science Marks:").grid(row=3, column=0, pady=5)
        self.science_marks = ttk.Entry(self.add_frame)
        self.science_marks.grid(row=3, column=1, pady=5)

        ttk.Label(self.add_frame, text="English Marks:").grid(row=4, column=0, pady=5)
        self.english_marks = ttk.Entry(self.add_frame)
        self.english_marks.grid(row=4, column=1, pady=5)

        ttk.Button(self.add_frame, text="Add Student", command=self.add_student).grid(row=5, column=0, columnspan=2, pady=20)

    def setup_display_frame(self):
        ttk.Label(self.display_frame, text="Enter Student ID:").grid(row=0, column=0, pady=5)
        self.search_id = ttk.Entry(self.display_frame)
        self.search_id.grid(row=0, column=1, pady=5)
        ttk.Button(self.display_frame, text="Search", command=self.display_student).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Result display area
        self.result_text = tk.Text(self.display_frame, height=10, width=40)
        self.result_text.grid(row=2, column=0, columnspan=2, pady=10)

    def setup_update_frame(self):
        ttk.Label(self.update_frame, text="Enter Student ID:").grid(row=0, column=0, pady=5)
        self.update_id = ttk.Entry(self.update_frame)
        self.update_id.grid(row=0, column=1, pady=5)
        
        ttk.Label(self.update_frame, text="New Name:").grid(row=1, column=0, pady=5)
        self.update_name = ttk.Entry(self.update_frame)
        self.update_name.grid(row=1, column=1, pady=5)

        ttk.Label(self.update_frame, text="New Maths Marks:").grid(row=2, column=0, pady=5)
        self.update_maths = ttk.Entry(self.update_frame)
        self.update_maths.grid(row=2, column=1, pady=5)

        ttk.Label(self.update_frame, text="New Science Marks:").grid(row=3, column=0, pady=5)
        self.update_science = ttk.Entry(self.update_frame)
        self.update_science.grid(row=3, column=1, pady=5)

        ttk.Label(self.update_frame, text="New English Marks:").grid(row=4, column=0, pady=5)
        self.update_english = ttk.Entry(self.update_frame)
        self.update_english.grid(row=4, column=1, pady=5)

        ttk.Button(self.update_frame, text="Update", command=self.update_student).grid(row=5, column=0, columnspan=2, pady=20)

    def setup_delete_frame(self):
        ttk.Label(self.delete_frame, text="Enter Student ID:").grid(row=0, column=0, pady=5)
        self.delete_id = ttk.Entry(self.delete_frame)
        self.delete_id.grid(row=0, column=1, pady=5)
        ttk.Button(self.delete_frame, text="Delete", command=self.delete_student).grid(row=1, column=0, columnspan=2, pady=20)

    def add_student(self):
        try:
            student = {
                'id': self.student_id.get(),
                'name': self.student_name.get(),
                'marks': {
                    'maths': int(self.maths_marks.get()),
                    'science': int(self.science_marks.get()),
                    'english': int(self.english_marks.get())
                }
            }
            self.students.append(student)
            self.Id.append(student['id'])
            self.marks.append(student['marks'])
            messagebox.showinfo("Success", "Student added successfully!")
            
            # Clear the entries
            self.student_id.delete(0, tk.END)
            self.student_name.delete(0, tk.END)
            self.maths_marks.delete(0, tk.END)
            self.science_marks.delete(0, tk.END)
            self.english_marks.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid marks (numbers only)")

    def display_student(self):
        search_id = self.search_id.get()
        found = False
        self.result_text.delete(1.0, tk.END)
        
        for i in range(len(self.Id)):
            if search_id == self.Id[i]:
                found = True
                display_text = f"""
Student Data
------------
Student ID: {self.Id[i]}
Name: {self.students[i]['name']}
Marks:
    Maths: {self.marks[i]['maths']}
    Science: {self.marks[i]['science']}
    English: {self.marks[i]['english']}
"""
                self.result_text.insert(tk.END, display_text)
                break
        
        if not found:
            messagebox.showinfo("Not Found", "Student not found")

    def delete_student(self):
        delete_id = self.delete_id.get()
        for i in range(len(self.Id)):
            if self.Id[i] == delete_id:
                self.Id.pop(i)
                self.students.pop(i)
                self.marks.pop(i)
                messagebox.showinfo("Success", f"Student with ID {delete_id} has been deleted.")
                self.delete_id.delete(0, tk.END)
                return
        messagebox.showinfo("Not Found", f"Student with ID {delete_id} not found.")

    def update_student(self):
        update_id = self.update_id.get()
        for i in range(len(self.Id)):
            if self.Id[i] == update_id:
                try:
                    self.students[i]['name'] = self.update_name.get()
                    self.marks[i] = {
                        'maths': int(self.update_maths.get()),
                        'science': int(self.update_science.get()),
                        'english': int(self.update_english.get())
                    }
                    messagebox.showinfo("Success", "Student data updated successfully!")
                    
                    # Clear the entries
                    self.update_id.delete(0, tk.END)
                    self.update_name.delete(0, tk.END)
                    self.update_maths.delete(0, tk.END)
                    self.update_science.delete(0, tk.END)
                    self.update_english.delete(0, tk.END)
                    return
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid marks (numbers only)")
                    return
        messagebox.showinfo("Not Found", f"Student with ID {update_id} not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()