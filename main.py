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


