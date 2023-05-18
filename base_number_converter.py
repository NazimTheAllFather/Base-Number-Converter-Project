import math
import random

#A function to convert the parameter input_string into its valid integer representation and return it
def to_valid_int(input_string):
    integer_part = 0
    int_string_length = len(input_string)
    
    #Using a for loop to access every element in input_string, convert it into a valid numeric value and add it to the integer part
    for i in range(int_string_length):  
        integer_part += (ord(input_string[i]) - ASCII_ZERO) *  (BASE_10 ** (int_string_length -1)) 
        int_string_length -= 1

    return integer_part
#A function that converts parameter int_as_string within base of "base_value" to a decimal representation of that number 
def convert_to_base_10 (int_as_string, base_value):
    number_part = 0
    length = len(int_as_string)

    #Using a for loop to access every character in int_as_String
    for i in int_as_string:
        #obtaining the integer value of i (by subtracting it from the ordinal value of ASCII character '0' as base)
        current_character =  ord(i) - ASCII_ZERO 

        #if current_character's value is greater than 9 or less than 36 (representing characters '10-36') 
        # then current_character is changed
        if current_character > 9 and current_character <= 36:
            current_character = (ord(i) - ASCII_A ) + 10    

        #converting every character to base 10 and adding it a returnable integer
        number_part += current_character * (base_value ** (length - 1))      
        length -= 1
    
    #returning the obtained integer
    return number_part
#A function that generates a random number within base of base_value
def gen_random_base_num (base_value):
    #it is assumed that base_value will be between 2-36
    valid_numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    log_of_2Billion = math.floor(math.log10(2 * (BASE_10 ** 9)))
    range_of_loop = int(random.random() * log_of_2Billion) 
    random_string = ''

    #if statement to ensure the randomly generated number for range_of_loop is never 0
    if range_of_loop == 0:
        range_of_loop = 1
    

    #A for loop that obtains random numbers from valid_numbers (by indexing it) and adds the result into a returnable string
    for i in range(range_of_loop):
            index = int((random.random() * base_value))
            random_string += valid_numbers[index]
            
                
    #returning a valid random number in base as a string
    return random_string   
#A function that converts the decimal base_10_number to new_base and returns the results
def convert_to_new_base(base_10_Number,  new_base):
    #It is assumed that the arguments will always be valid
    valid_numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return_val_in_rev = ''
    return_val = ''
    remainder = -1

    #using a while loop to convert base 10 number to pBase (by utilizing the modular opreator and integer divison)
    while base_10_Number > 0:
        remainder = base_10_Number % new_base
        return_val += valid_numbers[int(remainder)] 
        base_10_Number = base_10_Number // new_base

    #reversing the characters
    return_val = return_val[::-1]
   
    return return_val
# A function that prompts the user for input and ensures that the resturned function is within the base of "base_value"
def get_num_from_user (base_value):
    #Declaring variables
    valid_numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_valid_numbers = ''
    is_valid_match = True
    
    # creating a new string of valid_numbers that only holds characters up til base_value
    new_valid_numbers = valid_numbers[:base_value]

    #creating a do-while loop to ensure that valid numbers within the base can be returned
    while True:
        print(f'Your numeric digit choices for your number are {new_valid_numbers}')
        user_test_value = input('Please enter a number within that base: ')
        
        #an if-else that calls on the is_correct_num_as char to see if any invalid characters are entered 
        if (is_correct_num_as_char(user_test_value)):
            #a nested for-loop that checks if the user's input is present in the new_valid_numbers string
            for i in user_test_value:
                is_valid_match = False
                for j in new_valid_numbers:
                    if i == j:
                        is_valid_match = True
                        break
                if is_valid_match == False:
                    break
            if is_valid_match == False:
                continue
            else:
                break
        #if user's input was invalid it simply continues
        else:
            continue
    
    return user_test_value
#A function that takes in user_input and makes sure that it is a valid character (0-9 and A-Z)
def is_correct_num_as_char (user_input):
        is_valid = True
        character = user_input[0]
        length = len(user_input) 
        current_character = 0

        #Detecting leading positve or negative signs
        if (character == '+' or character == '-') and length > 1:
            user_input = user_input[1:]
            #adusting the string length variable
            length = len(user_input) 

        #a for loop that checks to see if user's input contains any invalid characters
        for i in user_input:
            #obtaining the integer value of the character (by subtracting the ordinal value of ASCII '0' from it)
            current_character =  ord(i) - ASCII_ZERO 

            #an if statement that validates ascii characters 0 - 36 (by ignoring anything whoses ordinal value is less than 0
            #or between 10 and 16 (which are ascii characters ;, :, <, =, >, ?, @) and beyond 36 which is beyond the ascii
            # character Z
            if current_character < 0 or (current_character > 10 and current_character <= 16) or current_character > 36:
                    is_valid = False

        return is_valid
#A simple function that takes in an input from the user and ensures that it is within an acceptable base of 2-36
def get_base_from_user ():
    base_value_as_char = ''
    base_value_as_int = 0
    
    #a while loop that takes in an input and ensures that invalid bases do not get returned
    while True:
        base_value_as_char = input('Please select a base value from 2 to 36: ')
        base_value_as_int = to_valid_int(base_value_as_char)
        if base_value_as_int >= 2 and base_value_as_int <= 36:
            break
        else:
            continue
           
    return base_value_as_int
    

#variable decleration
ASCII_ZERO = 48
ASCII_A = 65
BASE_10 = 10
menu_option = ''
random_num_in_base = ''
valid_base_value = 0
valid_num_from_user = ''
num_in_base10 = 0
new_value_in_base = ''
target_base_of_choice = 0


print('\t\t\t\t-------')
print('\t\t\t\tWelcome!!')
print('\t\t\t\t-------\n')


while True:

    print('\nSelect from one of the following menu options!!\n')
    print('\t1) Generate a random number in a base of your choice')
    print('\t2) Generate a random number in a base of your choice and convert it to another base also of your choice')
    print('\t3) Enter a number in a selected base and convert it to a base of your choice')
    print('\t4) Quit Program')
    
    menu_option = input('\nPlease enter 1, 2, 3, or 4: ')
    
    if menu_option == '1' or menu_option == '2' or menu_option == '3':
        if menu_option == '1':
            #displaying a print statement
            print('What base would you like to use for your new number?')

            #calling on the valid_base_value function to get a valid number from the user
            valid_base_value = get_base_from_user()

            #calling on the get_random_base_num function to get a random number in the base
            random_num_in_base = gen_random_base_num(valid_base_value)

            #calling on the convert_to_base_10 function convert the random number to base 10
            num_in_base10 = convert_to_base_10(random_num_in_base, valid_base_value)

            #Displaying results
            print(f'{random_num_in_base} is a randomly generated number in base {valid_base_value}' 
                  + f' (Equal to {num_in_base10} in base 10)')
            
        elif menu_option == '2':
            #displaying the prompt
            print()
            print('What base would you like to use for your new number?')

            #calling on the get_base_from_user function to recieve a valid base value (2-36)
            valid_base_value = get_base_from_user() 

            #calling on the get_random_base_num function to get a valid random number in the passed base_value arg
            random_num_in_base = gen_random_base_num(valid_base_value)

            #display a prompt to the user indicating that thus far everything is succesful 
            print()
            print(f'The generated number is {random_num_in_base} in base {valid_base_value}!')
            print()
            
            #asking the user what base they would like next
            print('We will convert that number to a new base!')
            print('--What base would you like to use for your new number?--')
            print()

            #reusing the get_base_from_user to generate a target base value
            target_base_of_choice = get_base_from_user()

            #calling on the convert_to_base_10 function to convert user's input to base 10 and storing it in a variable
            num_in_base10 = convert_to_base_10(random_num_in_base, valid_base_value)

            #calling on the convert_to_new_base function to convert from base 10 to the base of choice and storing it in a variable
            new_value_in_base = convert_to_new_base (num_in_base10, target_base_of_choice)

            #Displaying results
            print()
            print(f'{random_num_in_base} in base {valid_base_value} is equal to {new_value_in_base} in base {target_base_of_choice}.')

        elif  menu_option == '3':
            #Displaying print statements
            print()
            print('What base would you like to use for your new number? ')
            print()

            #calling on the get_base_from_user function to get a valid base
            valid_base_value = get_base_from_user()
            print()

            #calling on the get_num_From_user function to get a valid number from the user within the base of the arg
            valid_num_from_user = get_num_from_user (valid_base_value)

            # asking the user what base they would like next
            print()
            print('We will convert that number to a new base!')
            print('What base would you like to use for your new number? ')
            print()

            #calling on the get_base_function to get a valid base from the user
            target_base_of_choice = get_base_from_user()

            #calling on the convert_to_base_10 function to convert user's input to base 10 and storing it in a variable
            num_in_base10 = convert_to_base_10(valid_num_from_user, valid_base_value)

            #calling on the convert_to_new_base function to convert from base 10 to the base of choice and storing it in a variable
            new_value_in_base = convert_to_new_base (num_in_base10, target_base_of_choice)

            #Displaying results
            print()
            print(f'{valid_num_from_user} in base {valid_base_value} is equal to {new_value_in_base} in base {target_base_of_choice}.')
    
    elif menu_option == '4':
        print('\nThank you for using my base conversion program!!')
        break
    else:
        continue 



