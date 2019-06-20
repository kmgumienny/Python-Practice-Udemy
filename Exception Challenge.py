import sys


def test():
    def factorial(n):
        # n! can also be defined as n * (n-1)!
        if n < 1:
            return 1
        else:
            print(n/0)
            return n * factorial(n-1)

    try:
        print(factorial(100))
    except (RecursionError, OverflowError):
        print("This program cannot calculate factorials that large")
    except ZeroDivisionError:
        print("What are you doing dividing by 0?")

    print("Program terminating")


def get_number(val_string):
    while True:
        try:
            user_input = int(input("Please enter the {} number: ".format(val_string)))
            if user_input == 0 and val_string == "second":
                print("The denominator cannot be 0.")
            else:
                return user_input
        except ValueError:
            print("That is not an integer, try again!")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause ALWAYS executes")


if __name__ == '__main__':

    num_one = get_number("first")
    num_two = get_number("second")

    try:
        print("{} divided by {} is {}".format(num_one, num_two, num_one/num_two))
    except ZeroDivisionError:
        print("You can't divide by zero")
    finally:
        print("Division performed successfully")

