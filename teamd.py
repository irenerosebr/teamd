
roomArray = []
for i in range(999):
    roomArray.append(False)

roomArray[102] = "You are standing in the corner of the dark prison cell. \nTo the east is a bed. To the south is a toilet."
roomArray[103] = "You are now infront of your bed. The matress is made out of cardboard, and the pillow is a stuffed aligator. \nTo the west is another part of your cell. To the south is the cell door."
roomArray[202] = "Here is your toilet, or rather your bucket. You have fond memories of using this against the gaurd. \nTo the north is the cell corner. To the east is the cell door."
roomArray[203] = "The cell door is open, so it must be break time. You can continue east down the hallway towards the mess. \nTo the north is your bed, and to the west is the toilet."
roomArray[303] = "You now find yourself in a damp hall with a flickering overhead light.\nHeading east will have you in the mess hall. Going west leads back to the cell."

# mess hall
roomArray[402] = "To the north and west, there are walls. To the east, you see a tall figure lurking in the shadows. To the south, there is a table."
roomArray[403] = "You are in the mess hall. You stand before a table. To the west is the entrance to the hall. There is another table to the east."
roomArray[404] = "There are walls to the south and west. To the north, there is a table. To the east, you see a red light blinking in the darkness."
roomArray[504] = "You are in the mess hall. To the south there is an entrance to the guard's office, and to the east, a wall. A security camera with a blinking red light is nestled in the corner. To the north is a table."
# if (PLAYER HAS ITEM):
    # roomArray[502] = "The guard snores where he stands. South of you is a table. To the north is the exit. To the east is a wall."
# else:
    # roomArray[502] = "You've run into the guard. It's on sight. You're dead."
roomArray[502] = True
roomArray[503] = "You stand before a table. To the south, there is a red, blinking light in the darkness. To the west, there is another table. To the north, there is a tall figure lurking in the shadows. To the east, there is a wall."
# exit
roomArray[501] = "You have made it to the exit. The Eagle has left the nest."

def doesRoomExist(roomNumber):
    try: 
        if roomArray[roomNumber] == False:
            print("You can't go there. You hit a wall, -1 intelligence")
            return False
        else:
            return True
    except:
        print("You can't go there. You hit a wall, -1 intelligence")
        return False

def move(userInput, location):
    userInput = userInput.lower()
    if userInput == "n":
        location = location -1
        if doesRoomExist(location) == True:
            return location
        else:
            return location + 1
    elif userInput == "s":
        location = location + 1
        if doesRoomExist(location) == True:
            return location 
        else:
            return location - 1
    elif userInput == "e":
        location = location + 100
        if doesRoomExist(location) == True:
            return location
        else:
            return location - 100
    elif userInput == "w":
        location = location - 100
        if doesRoomExist(location) == True:
            return location
        else:
            return location + 100

