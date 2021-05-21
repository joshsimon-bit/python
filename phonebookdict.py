user_input = input("Hello, I am the classroom phonebook. Let's get started by asking your name? ")
print(" Thanks " + user_input + " would you like to add your name into our log? ")

Y = True

user_answer = input("Please enter Y for Yes or N for No. ")


if user_answer == True:
    print("Great! ")
    user_number = input("What is your cell phone number? ")
    print("OK " + user_input + "your cell phone number has been saved into our log as " + user_number + "! ")
else:
    print("Ok, who are you looking to contact? ")


def small_number(list):
    min_number = list[0]
    for number in list:
        if number < min_number:
            min_number = number
    return min_number
print(small_number([3, 2, 1, -1, 5, 10]))