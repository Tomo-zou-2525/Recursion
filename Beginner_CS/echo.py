def echo(val):
    if val % 5 == 0 and val % 3 == 0:
        return print("fizzbuzz")
    elif val % 5 == 0:
        return print("buzz")
    elif val % 3 == 0:
        return print("fizz")
    else:
        print("NOT FOUND!")


echo(3)  # -> fizz
echo(5)  # -> buzz
echo(15)  # -> fizzbuzz
echo(67)  # -> NOT FOUND!
