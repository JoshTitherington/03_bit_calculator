# Functions go here

# puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    decor = decoration * 5
    print(decor,text,decor)

# displays instruction / information
def instructions():
    
    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). for text, we assume that ascii encoding is being used (8 bits per charecter).")
    print()
    print("Completye as many calculations as necessary, pressing <enter> at the end of each calculation ot any key to quit")
    print()
    return ""

# Checks user choice is 'integer', 'text' or 'image'
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

# checks input is a number more than given value
def num_check(question, low):
    valid = False

    while not valid: 

        error = "Please enter a number more than "
        "(or equal to) {}".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print("An error occured.")
    return ""

# calculates the # of bits for text (# of characters x 8)
def text_bits():
    print()
    # ask user for a string...
    var_text = input("Enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working 
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    #return ""

    #finds # of bits for 24 bit colour


    # get width and height...
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # claculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working
    print()
    print("# of pixels = {} x {} = {}".format(image_height,
                                              image_width, num_pixels))
    print("# bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""

# converts decimal to binary and states how
# many bits are needed to represent the original integer
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_integer)

    # Calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))

    return ""

# Main routine goes here

# Heading
statement_generator ("Bit Calculator for Intergers, Text & Images", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going =="":


    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)
    # For integers, ask for integer
    if data_type =="integer":
        var_integer = num_check("Enter an integer: ", 0)
   
    # for images, ask for width and height
    # (must be an integer more than / equal to 0)
    elif data_type =="image":
        image_width = num_check("Image width? ", 1)
        print()
        image_height = num_check("Image height? ", 1)

    # For text, ask for a string
    else:
        var_text = input("Enter some text:  ")
        
    # For images, ask for width and height