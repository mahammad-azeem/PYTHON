def greet(first_name, last_name):
    return f"Hi {first_name} {last_name}"
    

print(greet("Mahammad", "Azeem"))


def increment(num, by):
    return num + by


result = increment(3, 4)

print(result)


def increment_by(num, by=2):
    return num + by

result = increment_by(8)
print(result)


def multiple(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

result = multiple(3, 10, 100, 120)
print(result)


def keyword_args(**user):
    return user["name"]

result = keyword_args(id=2, name="Azeem", city="Bangalore")
print(result)