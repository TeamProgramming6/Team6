import sys


# Function to initialize contact book
def initiate_contactbook():
    rows, cols = int(input("Enter the number of contacts you would like to add: ")), 5

    contact_book = []
    print(contact_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order:" % (i + 1))
        print("NOTE: * indicates mandatory fields")
        temp = []
        for j in range(cols):

            # Using a temp variable to assign the details to the contact
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit(
                        "No name was entered. Shutting down...")

            if j == 1:
                temp.append(int(input("Enter number*: ")))
                # Contact book will automatically shut down if no number is entered.

            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                # "None" will take the place of the rest of the fields if they are left blank
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth (MM/DD/YYYY): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(
                    str(input("Enter Student ID: ")))
                # Student ID is being entered as a string since using int would make the contact book shut down
                if temp[j] == "" or temp[j] == ' ':
                    temp[j] = None

        contact_book.append(temp)
        # Turning the details from temps into a list for the contact

    print(contact_book)
    return contact_book


def menu():
    # Menu function to tell users what actions they can perform after initialization function
    print("\tChoose one of the following options to perform:\n")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("0. Exit contact book")

    # User inputs their choice
    choice = int(input("Please enter your choice: "))

    return choice


def add_contact(cb):
    # Function to add a contact
    dip = []
    for i in range(len(cb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(
                str(input("Enter Student ID: ")))
    cb.append(dip)
    # And once you modify the list, you return it to the calling function wiz main, here.
    return cb


def remove_existing(cb):
    # Function to remove an existing contact
    query = str(
        input("Please enter the name of the contact you wish to remove: "))

    temp = 0
    # Using a temp variable to check and make sure the contact that is inputted exists.

    for i in range(len(cb)):
        if query == cb[i][0]:
            temp += 1
            # Temp will no longer satisfy the requirements for the if function

            print(cb.pop(i))
            # The tutor said this function removes entry at index i, which will delete the contact

            print("This contact has now been removed")
            # A message that confirms that the contact was successfully removed

            return cb
    if temp == 0:
        # If the temp variable is 0 at this point, it signifies that the name inputted was not found in (cb)
        print("Sorry, the name you entered does not exist.")

        return cb


def delete_all(cb):
    # Function that clears all information that has been inputted into (cb)
    return cb.clear()


def search_existing(cb):
    # Function to allow the user to search for a contact by the contact's details
    choice = int(input("You can search by any of the following criteria:\n\n\
    1. Name\n2. Phone Number\n3. Email Address\n4. Date of Birth\n5. Student ID Number\
    \nEnter your choice: "))

    temp = []
    check = -1

    if choice == 1:
        # Search by name
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        for i in range(len(cb)):
            if query == cb[i][0]:
                check = i
                temp.append(cb[i])

    elif choice == 2:
        # Search by phone number
        query = int(
            input("Please enter the number of the contact you wish to search: "))
        for i in range(len(cb)):
            if query == cb[i][1]:
                check = i
                temp.append(cb[i])

    elif choice == 3:
        # Search by email address
        query = str(input("Please enter the e-mail address of the contact you wish to search: "))
        for i in range(len(cb)):
            if query == cb[i][2]:
                check = i
                temp.append(cb[i])

    elif choice == 4:
        # Search by DOB
        query = str(input("Please enter the DOB (MM/DD/YYYY) of the contact you wish to search: "))
        for i in range(len(cb)):
            if query == cb[i][3]:
                check = i
                temp.append(cb[i])

    elif choice == 5:
        # Search by Student ID
        query = str(
            input("Please enter the student ID of the contact you wish to search: "))
        for i in range(len(cb)):
            if query == cb[i][4]:
                check = i
                temp.append(cb[i])

    else:
        print("Invalid search criteria.")
        return -1
    # Return -1 means the user input was something other than the given options

    # all the searches are stored in temp and all the results will be displayed with

    if check == -1:
        return -1
        # returning -1 indicates that the query did not exist in the directory
    else:
        display_all(temp)
        return check
        # we're just returning a index value wiz not -1 to calling function just to notify
        # that the search worked successfully


# this function displays all content of contact book cb
def display_all(cb):
    if not cb:
        # if display function is called after deleting all contacts then the len will be 0
        # And then without this condition it will throw an error
        print("List is empty: []")
    else:
        for i in range(len(cb)):
            print(cb[i])


def closecontactbook():
    # A simple gesture of courtesy towards the user to enhance user experience
    sys.exit("Goodbye!")


# Code for initializing function
print("Starting up...")
ch = 1
cb = initiate_contactbook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        cb = add_contact(cb)
    elif ch == 2:
        cb = remove_existing(cb)
    elif ch == 3:
        cb = delete_all(cb)
    elif ch == 4:
        d = search_existing(cb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(cb)
    else:
        closecontactbook()