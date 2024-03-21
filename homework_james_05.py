# James Carlson 
# Coding Temple - SE FT-144
# Backend Lesson 4 Assignment: Python Loop Statements



### 1. The Range Riddle ###
print("\n1. The Range Riddle \n")

import random

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods_list = ["Happy", "Sad", "Energetic", "Calm", "Livid", "Existential Dread", "Ennui", "Sleepy", "Meh", "Depressy", "Caffeinated"]

for i in range(len(days_of_the_week)):
    print(f"On {days_of_the_week[i]} I was feeling {random.choice(moods_list)}")



### 2. Double Scoop with Nested Loops ###
print("\n2. Double Scoop with Nested Loops \n")

times_of_day = ["Morning", "Afternoon", "Evening"]
for d in range(len(days_of_the_week)):
    for t in range(len(times_of_day)):
        print(f"On {days_of_the_week[d]} {times_of_day[t]} I was feeling {random.choice(moods_list)}")



### 3. Loop Condition Logic ###
print("\n3. Loop Condition Logic \n")

# Task 1 - infinite loop with break
merciful_release = 0
while True:
    print("Help!! I'm looping forever!")
    merciful_release += 1
    if merciful_release >= 5:
        break

# Task 2 - modify the previous loop to be conditional
merciful_release = 0
while merciful_release < 5:
    print("Oh phew; the loop has been modified!")
    merciful_release += 1



### 4. Python's Random Game Night ###
print("\n4. Python's Random Game Night \n")

# set up items and selected item
items = ["goblet", "dagger", "pendant", "waterskin", "bangle", "smelly boot"]
magic_item = random.choice(items)

# weave a fantastical world and get input from user
print("Your party is approached by an elderly merchant, who says,\n\n\
\"Salutations, traveler! Before you are six items. I have imbued one and only one\n\
with a special incantation invisible to all! Guess which item has been enchanted\n\
and I shall award you a sum of 10 gold pieces!\"\n\n\
He motions to the items set on a table beside him:\n\n\
Goblet - Dagger - Pendant - Waterskin - Bangle - Smelly Boot\n")

user_input = input("Which item will you choose?: ").casefold()
print()

# correct guess
if(user_input == magic_item):
    print("The merchant claps his hands together and lets out a gleeful squeal. \"Yes, that's it! \n\
You've guessed correctly!\"\n\n\
You find yourself 10 gold pieces richer!")

# incorrect guess
elif(user_input in items):
    print(f"The merchant chuckles as he puts his wares away. \"I'm afraid that's not it,\" he says.\n\
\"No, it was the {magic_item}! Perhaps we'll play again another day.\"\n\n\
Better luck next time, adventurer!")

# secret bad ending
elif("attack" in user_input):
    print("The merchant leaps out of the way of your attack with dizzying speed.\n\
Faster than you can react, he hurls an enormous fireball at you and your companions.\n\n\
Your entire party is obliterated!")

# invalid input
else:
    print("The merchant seems baffled by your answer. He shuffles away to find\n\
another contestant for his game.")



### 5. Looping Lists - The Rhythm of Repetition ###
print("\n5. Looping Lists - The Rhythm of Repetition \n")

# Task 1 - for loop that prints each genre with custom message
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_number = 0

for genre in genres:
    track_number += 1
    print(f"Track {track_number} - You're listening to {genre}!")
    if genre == 'Jazz':
        print("Hope this song mellows you out!")
    elif genre == 'Rock':
        print("Don't headbang too hard!")
    elif genre == 'Hip-hop':
        print("Show me your moves!")
    elif genre == 'Classical':
        print("You know, they say you should play this for your plants.")
    print()

# Task 2 - convert for loop to while loop
track_number = 0
while track_number != genres.index('Hip-hop'):
    print(f"Track {track_number + 1} - You're listening to {genres[track_number]}!")
    if genres[track_number] == 'Jazz':
        print("This is getting kind of romantic, huh?")
    elif genres[track_number] == 'Rock':
        print("Get up and dance!")
    elif genres[track_number] == 'Hip-hop':
        print("Okay, I don't want to listen anymore.")
    elif genres[track_number] == 'Classical':
        print("My plant is moving??")
    print()
    track_number += 1

# Task 3 - convert loop to use range() function
for i in range(len(genres)):
    if genres[i] != 'Classical':
        print(f"Track {i + 1} - You're listening to {genres[i]}!\nThe light show is ready!")
        if genres[i] == 'Jazz':
            print("We've got some mellow lighting to match the mood!")
        elif genres[i] == 'Rock':
            print("We turned all the lights to red so you feel like you're in hell!")
        elif genres[i] == 'Hip-hop':
            print("Flashing! Strobing! We've got it all!")
        elif genres[i] == 'Classical':
            print("Uh?! My plant is growing really big and it's moving towards me??")
        print()



### 6. Advanced Looping Techniques ###
print("\n6. Advanced Looping Techniques \n")

# Task 1 - loop through a slice of genres
for genre in genres[1:4]:
    print(genre)
print()

# Task 2 - create new list with list comprehension
genre_music_list = [genre + " Music" for genre in genres]
print(genre_music_list, "\n")

# Task 3 - a loop with range() to DROP THE BEAT
for i in range(10, 0, -1):
    print(i)
print("The beat drops now!")