'''
@ASSESSME.USERID: ab1538
@ASSESSME.AUTHOR: Andrej Biljaka
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''


def add_char(c1,c2):
    char1 = ord(c1)
    char2 = ord(c2)
    sum = char1 + char2
    print("Sum of a and b: ",str(sum), "\nCharacter: ",chr(sum), "\n")


def subtract_char(c3,c4):
    char3 = ord(c3)
    char4 = ord(c4)
    sub = char3 - char4
    print("Subtraction of ", c3," and ",c4," = ",str(sub),"\nCharacter: ", chr(sub), "\n")



def main():
    inp_1 = input("Enter the first character: ")
    inp_2 = input("Enter second character: ")
    """
    When i run the command in terminal it asks for an input and after i enter the input it shows the sum and difference 
    After i saw that it doesnt show the characters for difference
    i googled it and it showed that when the difference is negative it crashes 
    Moreover the numebrs has to be between 33 and 127 in order to ascii table to be able to output visible output
    in other cases are the commands which can not be visible
    """

    add_char(inp_1,inp_2)
    subtract_char(inp_1,inp_2)


"""
When 2 or more characters are entered code crashesh because there are only 2 parametrs which can be used in the funciton
Yes i understand the way it works because i see the output and uderstand the error 


"""


if __name__ == "__main__":
    main()

