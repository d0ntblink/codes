def addition(input_1 , input_2) : #function calculating the summation of two numbers
    sum = input_1 + input_2
    return sum

user_input_1 = float(input('Please enter a float #\n'))#first user input
user_input_2 = float(input('Please enter a second float #\n'))#second user input
print('%s in addition to %s is %0.4f' %  (str(user_input_1) , str(user_input_2) , addition(user_input_1 , user_input_2))) #function call with two user inputs
