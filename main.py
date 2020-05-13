filename = "input.txt"
data = []
afile = ""
keyNumber = []
roomNum = 0
floorNum = 0

def getCommandsFromFileName(filename):
    f = open(filename, "r")
    while(True):
        afile = f.readline().rstrip()
        if (afile != "" and afile != " "):
            data.append(afile)
        else:
            break
    return data

def availableRooms(hotel):
    num = ""
    for i in range(len(hotel)):
        for j in range(len(hotel[i])):
            if (hotel[i][j] == None):
                num = num + str(i + 1) + str(j + 1).zfill(2) + " "
    return num

def checkout(hotel, keycard):
    name = ""
    room = ""
    for i in range(len(hotel)):
        for j in hotel[i]:
            if (j != None and j.split(' ')[1] == keycard):
                name = j.split(' ')[2]
                room = j.split(' ')[0]
    return name, room

def checkKey():
    for i in range(len(keyNumber)):
        if (keyNumber[i] != None):
            return keyNumber[i]

def genKeycard(f, r):
    for i in range(f * r):
        keyNumber.append(i + 1)

def listGuest(hotel):
    sort = {}
    for i in range(len(hotel)):
        for j in hotel[i]:
            if (j != None):
                sort[int(j.split(' ')[1])] = j.split(' ')[2] + " " + j.split(' ')[0] + " " + j.split(' ')[3]    #คีย์การ์ด: ชื่อ เลขห้อง อายุ
    return sort

def checkoutByFloor(hotel, floor, roomNum):
    room = ""
    for i in range(len(hotel)):
        if (i == (int(floor) - 1)):
            for j in hotel[i]:
                if (j != None):
                    room = room + j.split(' ')[0] + " "
                    keyNumber[int(j.split(' ')[1]) - 1] = int(j.split(' ')[1])
            hotel[i] = [None] * int(roomNum)

    return room

def bookByFloor(hotel, floor, name, age, roomNum):
    count = 0
    key = ""
    room = ""
    for i in range(len(hotel)):
        if (i == (int(floor) - 1)):
            for j in hotel[i]:
                if (j == None):
                    count = count + 1
    if (count == int(roomNum)):
        for i in range(len(hotel)):
            if (i == (int(floor) - 1)):
                for j in range(len(hotel[i])):
                    keyNum = checkKey()
                    num = str(i + 1) + str(j + 1).zfill(2)
                    hotel[i][j] = num + " " + str(keyNum) + " " + name + " " + age
                    keyNumber[int(keyNum) - 1] = None
                    key = key + str(keyNum) + " "
                    room = room + num + " "
        return "Room " + room + " are booked with keycard number " + key
    else:
        return "Cannot book floor " + floor + " for " + name + "."

def main():
    getCommand = getCommandsFromFileName(filename)
    for i in range(len(data)):
        command = data[i].split(" ")[0]
        information = data[i].split(' ')
        if (command == "create_hotel"):
            floorNum = information[1]
            roomNum = information[2]
            hotel = [[None] * int(roomNum) for i in range(int(floorNum))]
            genKeycard(int(floorNum), int(roomNum))
            print("Hotel created with " + floorNum + " floor(s), " + roomNum + " room(s) per floor.")
        if (command == "book"):
            bookRoom = information[1]
            name = information[2]
            age = information[3]
            keyNum = checkKey()
            if (hotel[(int(bookRoom[0]) - 1)][(int(bookRoom[1 : 3]) - 1)] == None):
                hotel[(int(bookRoom[0]) - 1)][(int(bookRoom[1 : 3]) - 1)] = bookRoom + " " + str(keyNum) + " " + name + " " + age      #['เลขห้อง คีย์การ์ด ชื่อ อายุ']
                print("Room " + bookRoom + " is booked by " + name + " with keycard number " + str(keyNum) + ".")
                keyNumber[int(keyNum) - 1] = None
            else:
                detail = hotel[(int(bookRoom[0]) - 1)][(int(bookRoom[1 : 3]) - 1)]
                print("Cannot book room " + bookRoom + " for " + name + ", The room is currently booked by " + detail.split(' ')[2] + ".")
        if (command == "book_by_floor"):
            floor = information[1]
            name = information[2]
            age = information[3]
            print(bookByFloor(hotel, floor, name, age, roomNum))
        if (command == "checkout"):
            keycard = information[1]
            name = information[2]
            nameCheck = checkout(hotel, keycard)
            if (name == nameCheck[0]):
                print("Room " + nameCheck[1] + " is checkout.")
                keyNumber[int(keycard) - 1] = int(keycard)
                hotel[(int(nameCheck[1][0]) - 1)][(int(nameCheck[1][1 : 3]) - 1)] = None
            else:
                print("Only " + nameCheck[0] + " can checkout with keycard number " + keycard + ".")
        if (command == "checkout_guest_by_floor"):
            floor = information[1]
            room = checkoutByFloor(hotel, floor, roomNum)
            print("Room " + room.split(' ')[0] + ", " + room.split(' ')[1] + " are checkout.")
        if (command == "list_available_rooms"):
            print(availableRooms(hotel))
        if (command == "list_guest"):
            guest = listGuest(hotel)
            nameGuest = ""
            for i in range(len(keyNumber)):
                if (keyNumber[i] == None):
                    nameGuest = nameGuest + guest[i + 1].split(' ')[0] + " "
            print(nameGuest)
        if (command == "list_guest_by_age"):
            age = information[2]
            operation = information[1]
            guest = listGuest(hotel)
            if (operation == "<"):
                for x in guest:
                    if(int(guest[x].split(' ')[2]) < int(age)):
                        print(guest[x].split(' ')[0])
            elif (operation == ">"):
                for x in guest:
                    if(int(guest[x].split(' ')[2]) > int(age)):
                        print(guest[x].split(' ')[0])
            elif (operation == ">="):
                for x in guest:
                    if(int(guest[x].split(' ')[2]) >= int(age)):
                        print(guest[x].split(' ')[0])
            elif (operation == "<="):
                for x in guest:
                    if(int(guest[x].split(' ')[2]) <= int(age)):
                        print(guest[x].split(' ')[0])
            elif (operation == "=="):
                for x in guest:
                    if(int(guest[x].split(' ')[2]) == int(age)):
                        print(guest[x].split(' ')[0])
            elif (operation == "!="):
                for x in guest:
                    if(int(guest[x].split(' ')[2]) != int(age)):
                        print(guest[x].split(' ')[0])

        if (command == "list_guest_by_floor"):
            floor = information[1]
            guest = listGuest(hotel)
            for x in guest:
                if(guest[x].split(' ')[1][0] == floor):
                    print(guest[x].split(' ')[0])
        if (command == "get_guest_in_room"):
            room = information[1]
            guest = listGuest(hotel)
            for x in guest:
                if(guest[x].split(' ')[1] == room):
                    print(guest[x].split(' ')[0])

    print(hotel)
    print(keyNumber)

main()

