user_name = input("Greetings, what is your name? ")
print("Hello " + user_name + "!")

user_answer = input(user_name + " Which day are you requesting off? ")
print("OK " + user_name + " let's see what our schedule can allow for " + user_answer + "!")

user_answer2 = input(user_name + ", how many days have you worked prior to " + user_answer + "?")

days = 4
if days >= 5:
    message = "Please contact your supervisor for futher assistance."
else:
    message = "Your time off request has been approved, Enjoy!"
print(message)







