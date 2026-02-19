# Write a python program that iterates through integers from 1 to 100. 
# For each multiples of three print "Fizz" instead of the number, 
# For each multiple of five, print "Buzz" 
# For Numbers that are both multiple of three and five print "FizzBuzz"

# items = [ 1, 2 , 3]
# for item in items:
#     print(item)



for number in range (1,101):
    if number % 3 == 0 and number % 5 ==0:
        print ("fizzBuzz")
    if number % 3 == 0:
        print("fizz")
    elif number % 5 ==0:
        print ("buzz")
       
    else:
        print(number)

  



