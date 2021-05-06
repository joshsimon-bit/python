title = "US Chairforce"
#STOP = 10
counter = 0

while counter < len(title):
    print("the counter value is:" + str(counter))
    if (counter % 2) == 0:
        print(title[counter])
    counter = counter + 1