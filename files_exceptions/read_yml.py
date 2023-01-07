# imports
import yaml

try:
# variables:
    filepath1 = '../data/credentials.yml'


    # functions/steps:
    with open(filepath1, "r") as stream:
        credentials = yaml.safe_load(stream)


    print(credentials)
    qa_uname = credentials['qa']['username']
    qa_password = credentials['qa']['password']

    uat_uname = credentials['uat']['username']
    uat_password = credentials['uat']['password']
    print(qa_uname)
    print(qa_password)
    print(uat_uname)
    print(uat_password)

    login_page.enter_username(qa_uname)
    login_page.enter_password(qa_password)

    #data for Negative login tests:
    qa_uname1 = credentials['negative']['case1']['username']
    qa_password1 = credentials['negative']['case1']['password']
    qa_uname2 = credentials['negative']['case2']['username']
    qa_password2 = credentials['negative']['case2']['password']
    qa_uname3 = credentials['negative']['case3']['username']
    qa_password3 = credentials['negative']['case3']['password']

except Exception as err:
    print(err)

print('Game Over!')