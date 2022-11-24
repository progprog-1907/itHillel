def salary_hours(in_time, out_time, cost_per_hour):
    many_hours_worked = out_time - in_time
    if many_hours_worked < 8:
        return f"Ваша зарплата за день {0} долларов"
    else:
        return f"Ваша зарплата за день " \
               f"{many_hours_worked * cost_per_hour + (many_hours_worked - 8) * 1.5}" \
               f" долларов. Ваш полуторная зарплата составляет " \
               f"{(many_hours_worked - 8) * 1.5} $ долларов"


data = salary_hours(9, 20, 5)
print(data)