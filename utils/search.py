import json


def search_employee_by_name(query):
    #  open
    with open("data/employee.json", "r") as file:
        employees = json.load(file)

    # search
    result = []
    for employee in employees:
        if query.lower() in employee['full_name'].lower():
            result.append(employee)

    if len(result) == 0:
        return "No employees found"

    message_txt = ""
    for employee in result:
        message_txt += f"{employee['full_name']} - {employee['description']}\n"

    return message_txt
