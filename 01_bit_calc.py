# Functions go here 

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five charecters
    ends = decoration * 5

    # add decoration to start and end of statment
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""
# Main Routine goes here
statement_generator("hello world", "-")