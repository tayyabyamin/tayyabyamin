number = input ("what is your favorite number?")
if number.isdigit():
    number = int(number)
    fav_number = number*10
    print (f"your favuorite number is {fav_number}")
else:
    num_len=len(number)
    print (f"length of your string is {num_len}")