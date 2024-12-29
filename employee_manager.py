import os

class EmployeeManager:
    def __init__(self):
        self.employees = {}   # employee er database
        self.file_name = "employee_records.txt"
        self.load_employee_data()


    def load_employee_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                for line in file:
                    employee_id,name,age,department,designation,salary = line.strip().split(",")
                    self.employees[employee_id] ={
                        "name": name,
                        "age": age,
                        "department": department,
                        "designation": designation,
                        "salary": salary,
                    }


    def save_employee_data(self):
        with open(self.file_name, "w") as file:
            for employee_id,details  in self.employees.items():
                line = f"{employee_id},{details["name"]},{details["age"]},{details["department"]},{details["designation"]},{details["salary"]}\n"
                file.write(line)

    def add_employee(self):
        employee_id = input("Enter employee Id: ")
        if employee_id in self.employees:
            print("Employee Id already exists")
            return
        name = input("Enter name: ")
        age = input("Enter age: ")
        department = input("Enter department: ")
        designation = input("Enter designation: ")
        salary = input("Enter salary: ")
        self.employees[employee_id]={
            "name": name,
            "age": age,
            "department": department,
            "designation": designation,
            "salary": salary,
        }
        print("Employee added successfully")
        self.save_employee_data()

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        print("\nEmployee list")
        for emp_id,details in self.employees.items():
            print(f"\nID: {emp_id}")
            for key,value in details.items():
                print(f"{key.capitalize()} : {value}")

    def update_employee(self):
        emp_id = input("Which Employee ID you want to update: ")
        if emp_id not in self.employees:
            print("Employee ID not found")
            return
        print("Enter new details (leave blank to keep current value):")
        
        fields = ["name","age","department","designation","salary"]
        updated_details = {}

        for field in fields:
            current_value = self.employees[emp_id][field]
            new_value = input(f"{field.capitalize()} ({current_value}): ").strip()
            updated_details[field] = new_value if new_value else current_value
       

         # Update the employee record
        self.employees[emp_id] = updated_details
        print(f"Employee Id {emp_id} updated successfully.")
        self.save_employee_data()


    def delete_employee(self):
        emp_id = input("Which Employee ID you want to delete: ")
        if emp_id not in self.employees:
            print("Employee ID not found.")
            return
        del self.employees[emp_id]
        print(f"Employee ID {emp_id} deleted successfully.")
        self.save_employee_data()

    
    def search_employee(self):
        keyword = input("Enter name or designation to search: ").lower()
        found = False
        print("\nSearch Results:")
        for emp_id, details in self.employees.items():
            if keyword in details["name"].lower() or keyword in details["designation"].lower():

                found = True
                print(f"\nID: {emp_id}")
                print(f"Name: {details['name']}")
                print(f"Age: {details['age']}")
                print(f"Department: {details['department']}")
                print(f"Designation: {details['designation']}")
                print(f"Salary: {details['salary']}")

        if not found:
            print("No matching employee found.")


