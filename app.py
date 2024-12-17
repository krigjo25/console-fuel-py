#    Fuel Gauge

def main():
    print(convert(input("Type in a fraction :")))


def convert(arg):
    """ Converting the fraction to prosentage """

    x, y = str(arg).split('/')
    x, y = int(x), int(y)

    #   Ensuring the convertion to procetage
    arg = round((x / y) * 100)

    if arg < 101:
        return gauge(arg)


def gauge(arg):

    """  Returns the grade of the percentage """
    if arg > 95:
        return 'F'
    
    elif arg < 2:
        return 'E'
    
    else:
        return f"{arg}%"


if __name__ == "__main__":
    main()
