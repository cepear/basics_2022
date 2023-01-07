#  Python uses spetial oblects called exceptions to manage errors that arise during execution
import yaml
try:
    #usual code to execute
    print('Executing a code in try/except block')
    #print(5/0)


    filepath1 = '../data/credential.yml'

    # functions/steps:
    with open(filepath1, "r") as stream:
        credentials = yaml.safe_load(stream)
    print('****try/except block execution completed:)****')

except ZeroDivisionError as err:
    # executes only if ZeroDivisionError happens
    print("You cant divide by 0!!!")
    print('Printing the standard error: ', err)
except FileNotFoundError:
    # executes only if FileNotFoundError happens
    print("ops, file not found")
except Exception as err:
    print('Printing the standard error: ', err)
finally:
    #this block will be executed regardless exceptions happens or not
    print('Clean up and close the browser')

# print('Executing a code in try/except block')
# print(5/0)
# print('****try/except block execution completed:)****')
print("Execution completed")