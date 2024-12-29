from employee_manager import EmployeeManager

def main():
    while True:
        manager = EmployeeManager()

        print("\nWelcome to Employee Tracking System")
        print("1. Add Employee")
        print("2. View all Employees")
        print("3. Update existing Employee info")
        print("4. Delete Employee")
        print("5. Search Employee name or designation")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_employees()
        elif choice == "3":
            manager.update_employee()
        elif choice == "4":
            manager.delete_employee()
        elif choice == "5":
            manager.search_employee()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()










# while True:
#     print("Welcome to Track Employee Information!!!")
#     print("1. Add new employee")
#     print("2. Update employee information")
#     print("3. Update employee information")
#     print("4. Delete employee record")
#     print("5. View all employees")
#     print("6. View all employees")
#     print("7. Search employee using name or designation")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         name = input("Enter your name: ")
#         age = input("Enter your age: ")
#         designation = input("Enter your designation: ")

#         print(name,age,designation)

#     else:
#         print("Thanks")
#         break

