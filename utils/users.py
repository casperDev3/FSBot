import json

def edit_employee_field(employee_id, filed, value):
    with open("data/employee.json", "r") as file:
        employees = json.load(file)

    print(employees)
    for employee  in employees:
        if employee["id"] == employee_id:
            employee[filed] = value
            break

    with open("data/employee.json", "w") as f:
        json.dump(employees, f, indent=4)

    return True

