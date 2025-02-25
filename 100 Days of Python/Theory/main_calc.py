# class Calculator:
#     def __init__(self):
#         self.answer = 0

#     def sum(self, n1, n2):
#         self.answer = n1 + n2
#         print(self.answer)
    
#     def substraction(self, n1, n2):
#         self.answer = n1 - n2
    
# new_calculator = Calculator()
# new_calculator.sum(1, 2)

class Task:
    def __init__(self, name, due_date, completion_status):
        self.name = name
        self.due_date = due_date
        self.completion = completion_status

    def mark_completed(self):
        self.completion = "Completed 📝"

    def update_due_date(self, new_due_date):
        self.due_date = new_due_date

    def display_task(self):
        print(self.name)
        print(self.due_date)
        print(self.completion)

new_task = Task("Finish day 17", "24-02-2025", "Pending")
new_task.display_task()

new_task.mark_completed()
new_task.update_due_date("25-02-2025")
new_task.display_task()