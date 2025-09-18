'''
@ASSESSME.USERID: ab1538
@ASSESSME.AUTHOR: Andrej Biljaka
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = "Hello Everyone!"
INT_GLOBAL = 55
FLOAT_GLOBAL = 6.90


def print_param(param):
    print("print_param:", param)


def print_local():
    local_var = "I am a local variable"
    print("print_local:", local_var)


def print_which():
    STRING_GLOBAL = 999
    print("print_which:", STRING_GLOBAL)


def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)

    local_var = "I am another local variable"
    print("main local_var:",local_var)

    print_local()

    print_which()
    print("Global STRING_GLOBAL:", STRING_GLOBAL)


if __name__ == "__main__":
    main()
