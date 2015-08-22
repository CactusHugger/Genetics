import random
password = str("Failed")
counter = 0
while(password == str("Failed")):
    j = random.randrange(1,170000)
    if (j == 100):
        password = str("Pass")
        print(password)
    else:
        counter = counter + 1
        print (str("Attempt number ") + str(counter) + str(" ") + password)

wait = input("Press enter to continue")