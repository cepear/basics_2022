
#While_loop
name = 'john'
#while expression:
#   code to repeatedly execute with each iteration
#   code to repeatedly execute with each iteration
#   code to repeatedly execute with each iteration

# Be cautious of while loop( INFINITE loop, to avoid make sure the condition is changing with each iteration.

def while_loop_increment():
    print("While loop when we are setting upper limit in the condition, we need to increment")
    current_number = 1
    while current_number <= 2:
        print('Current number : ', current_number)
        current_number = current_number + 1


def while_loop_decrement():
    """ Docstring - While loop when we are setting bottom limit in the condition, we need to decrement"""
    print("While loop when we are setting bottom limit in the condition, we need to decrement")
    current_number = 1
    while current_number > - 1:
        print('Current number : ', current_number)
        current_number = current_number - 1


def fuzz_buzz():
    try:
        print('--------------FUZZ-BUZZ with while loop --------------------------')
        answer = ''
        while (answer.lower() != 'n') and (answer.lower() != 'no'): # n == n -> True code will not be executed further; n != -> False code will continue,
                                     # while answer.lower() != 'n': -> True so code will continue to execute.

    #num = 3
            num = int(input("Please enter number : "))
            if num != 0:
                if num % 3 == 0 and num % 5 == 0:
                    print("FUZZ-BUZZ")
                elif num % 3 == 0:
                    print('dividable by 3 "FUZZ"')
                elif num % 5 == 0:
                    print('Dividable by 5 "BUZZ"')
                else:
                    print('Not dividable by 3 or 5')
            else:
                print("Please enter different number then 0")
            answer = input("Do you want to continue? y/n ")
    except (NameError) as err:
        print('error occurred:', err)



#while_loop_increment()

while_loop_decrement()

#fuzz_buzz()
