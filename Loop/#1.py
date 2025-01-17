for i in range(10):
    hours_worked = int(input(f"Enter hours worked by employee {i + 1}: "))
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * 12
        print(f"Employee {i + 1} earns Rs. {overtime_pay} in overtime pay.")
    else:
        print(f"Employee {i + 1} does not earn any overtime pay.")
