def describe_person(name,age):
    if age=="":
        return name,30,"лет"
    return name,age,"лет"

name= input()
age = input()
print(*describe_person(name,age))
