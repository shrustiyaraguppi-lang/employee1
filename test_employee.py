from employee import employee_details
def test_employee_details():
    result = employee_details("Shrusti", 101, "IT", 25000)
    expected = (
        "Employee Name: Shrusti\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 25000"
    )

