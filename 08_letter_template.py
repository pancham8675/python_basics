
letter= '''Dear <|NAME|>
Greetings from Eliptus Coding House. We are happy to inform you about your selection.
You are selected!
Have a great day ahead!

Regards
Bill

Date: <|DATE|>
'''
name=input("Enter name: ")
date=input("Enter date: ")

letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

print(letter)


