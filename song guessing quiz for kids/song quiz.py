import random
import string
import sys


file1='artists.txt'
file2='songs.txt'


#User authentication
print("     **IT'S A MUSIC QUIZ GAME** \n")
gaming_id = 'sam'
gaming_pw = '123'
id_1= input("Enter Gaming ID: ")

if id_1 == gaming_id:
    id_2 = input("Enter Gaming Password: ")
    if id_2 == gaming_pw:
        print("\n      **WELCOME TO THE GAME**")
        name=input("\nEnter your name: ")
    else:
        print("Incorrect password !!," "\nStart again... ")
        sys.exit()
else:
    print("Incorrect Gaming id !!", "\nStart again... ")
    sys.exit()


#Generate random artist names from artist's text file
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
artist=random_line(file1)
print("\nYour Artist name is", artist,"!!\n")


#Generate random 1st letter for songs in song's text file
song_letter = random.choice(string.ascii_lowercase[0:2])
print("Now, you have to guess a song of", artist ,"which starts from ==>", song_letter, "\n")


#Hint to avoid errors
print("HINT:\n" , "1.Don't use capital letters\n" , "2.Use hyphen instead of spaces", "\n")


#Guessing Conditions
g = (input("Guess song name: "))
with open(file2) as f:
    content = f.readlines()
content = [x.strip() for x in content]
if g in content:
    print("yes you have got correct ans")
    scores = 3
else:
        print("\n", "INCORRECT !! \n" "Now you have got a 2nd chance so TRY AGAIN ..\n")
        g = (input("Again, Guess song name "))
        with open(file2) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        if g in content:
            print("you are right now")
            scores = 1
        else:
            print("no more chances,Don't lose hope \nTRY NEXT TIME...!!")
            scores = 0


#Display scores at the end of the game
print('your score', scores)


#Store name of player and scores in external file (need to be done)


#Display name of player and scores of top 5 winnings




