# HW 8-4, 8-5, 8-7, 8-8, 8-15

def make_shirt(size, message):
    print(f'Your shirt is {size} , and it has "{message}" text')
make_shirt('M', 'Its awesome!')

def make_shirt1(message, size='L'):
    print(f'Your shirt is {size} , and it has "{message}" text')


def make_shirt2(size, message= 'I like dogs!'):
    print(f'Your shirt is {size} , and it has "{message}" text')


def make_shirt3(size, message= 'I like dogs!'):
    print(f'Your shirt is {size} , and it has "{message}" text')


def make_shirt4(size, message):
    if size != 'M' and size != 'L':
        print(f'Your shirt is {size} ,  it can get  "{message}" text')
    else:
        print("You can't get this print with size M or L")





make_shirt1(message='I love Python!')
make_shirt2(size='L')
make_shirt3(size='M')
make_shirt4('S', 'Uzbekistan')
make_shirt4('M', 'Uzbekistan')


print("-------exercise 8.5 ---------------------")
def describe_city1(city, country='Italy'):
    print(f"{city.title()} is located in {country.title()}")


def describe_city2(country, city= 'Rome'):
    print(f"{city.title()} is located in {country.title()}")


describe_city1('palermo')
describe_city2('italy ')
describe_city1('berlin', 'germany')

print("---------exercise 8.7--------------------")
def make_album(artist, title):
    return {'name': artist, 'album title': title}

album1 =  make_album('Adele', 'NY')
print("Executing the function in the print statement :", make_album('Adele', 'NY'))

print('printing album1: ', album1)
print('Second Album: ', make_album('Tupac', 'California'))
print('Third Album: ', make_album('Justin', 'Changes'))

def make_album2(firstname, lastname, title):
    return {'Firstname': firstname,
            'Last Name': lastname,
            'album title': title}

print(make_album2('Justin', 'Beiber', 'Changes'))

make_album2('Justin', 'Beiber', 'Changes')
##print(make_album2['First Name'] + ' ' + make_album2(['Last Name'])

def make_album_tracks(artist, title, tracks = 0):
    album = {'Artist Name': artist, 'album title': title}
    if tracks > 0:
        #add tracks key value pair to dictionary
        album['Num_tracks'] = tracks
    return album

album3 = make_album_tracks('Beyonce', 'Renaissance')
album4 = make_album_tracks('Beyonce', 'Lemonade', 12)

print("album3:", album3)
print("album4:", album4)

print("------------same code with while loop- exer 8.8 ------------")

def make_album_tracks(artist, title, tracks = 0):
    album = {'Artist Name': artist, 'album title': title}
    if tracks > 0:
        #add tracks key value pair to dictionary
        album['Num_tracks'] = tracks
    return album

album3 = make_album_tracks('Beyonce', 'Renaissance')
album4 = make_album_tracks('Beyonce', 'Lemonade', 12)

print("album3:", album3)
print("album4:", album4)


is_next = ''
while is_next != 'n':
    artist = input("Enter artist name: ")
    album = input("Enter album name: ")
    track = input("Enter track number: ")
    track = int(track)
    album3 = make_album_tracks(artist, album, track)

    print("album3: ", album3)
    is_next = input("do you want to continue? y/n")

#album3.setdefault()
#write function that returns letters with counts, how many times each letter is used in the string(one word)
# Sample input and Output: 'hello' -> {'h': 1, 'e': 1, 'l': 2, 'o':1}
#album['letter'] += tracks    #adding value to the previous value of the key in the dictionary
#album['letter'] = album['letter'] + tracks

#def count_letters():







