high_income = False
good_credit = True
student = False

output = "Eligible" if (high_income or good_credit) and not student else f"Not Eligible. because its a student"
print(output)