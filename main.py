students = []
Id = []
marks = []
record = [Id,students,marks]
def add_student():
    student = {
        'id': input('Enter Id: '),
        'name': input('Enter your name: '),
        'marks': {
            'maths': int(input('Enter Maths marks: ')),
            'science': int(input('Enter Science marks: ')),
            'english': int(input('Enter English marks: '))
        }
    }
    students.append(student)
    Id.append(student['id'])
    marks.append(student['marks'])
def display():
    print('\n\t=== Student Data ===')
    for i in range(len(Id)):
        search_id = input('Enter ID to search: ')
        if search_id == Id[i]:     
            print(f"\nStudent ID: {Id[i]}")
            print(f"Name: {students[i]}")
            print("Marks:")
            print(f"\tMaths: {marks[i]['maths']}")
            print(f"\tScience: {marks[i]['science']}")
            print(f"\tEnglish: {marks[i]['english']}")
        else:
            print('Student not found')
def delete_student():
    delete_id = input('Enter ID to delete: ')
    for i in range(len(Id)):
        if Id[i] == delete_id:
            Id.pop(i)
            students.pop(i)
            marks.pop(i)
            print(f"Student with ID {delete_id} has been deleted.")
            return
    print(f"Student with ID {delete_id} not found.")

def update_data():
    update_id = input('Enter ID to update: ')
    for i in range(len(Id)):
        if Id[i] == update_id:
            students[i] = input('Enter new name: ')
            marks[i] = {
                'maths': int(input('Enter Maths marks: ')),
                'science': int(input('Enter Science marks: ')),
                'english': int(input('Enter English marks: '))
            }
            return
    print(f"Student with ID {update_id} not found.")    

while True:
    ques  = int(input('Enter 1 to add student, 2 to display, 3 to delete student, 4 to update data, 5 to exit: '))
    if ques == 1:
        add_student()
    elif ques == 2:
        display()
    elif ques == 3:
        delete_student()
    elif ques == 4  :
        update_data()
    elif ques == 5:
        break       
    else:
        print('Invalid input')
