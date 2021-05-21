#  Sum the numbers 
#  # Create a list of numbers, print their sum.

list_of_numbers = [1, 2, 3]

#print(sum(list_of_numbers))

total = 0

# version 1
for number in list_of_numbers:
#print("The number is now: " + str(number))
    #total = total + number
    #print("The total is now: "  + str(total))

# version 2
 #print("The number is now: " + str(number))
    #total = total + number
    #print("The total is now: "  + str(total))
    
 # Version 3
 # This prints just the final total
 for number in list_of_numbers:
    total = number + total
    print("The total is now: "  + str(total))