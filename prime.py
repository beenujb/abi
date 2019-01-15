number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print( "no")
            break
    else:
        print(number, "yes")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print("no")
