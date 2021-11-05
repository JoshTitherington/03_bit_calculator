# checks user choice is 'integer' , 'text' or 'image'
def user_choice():

    valid = False
    while not valid:

        response = input("File type (integer / text / image): ").lower()

        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"  

        else: 
            print("Please choose a valid file type!")
            print()

# Main routine goes here
keep_going =""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()

# Checks for valid response and returns text, interger or image

if response in text_ok:
    return "text"

elif response in integer_ok:

elif response in image_ok:
    return "image"

elif response == "i":
    want_interger = input("Press <enter> for an integer or any key for an image")
    if wnat_integer == "":
        return "integer"
    else:
        return "image"

    else:
        print("Please choose a valid file type!")
        print()
