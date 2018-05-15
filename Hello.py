text = input('Enter a string. \n')

new_text = str()
for word in text:
    if word.islower():
        new_text += word.upper()
    else:
        new_text += word.lower()

print(new_text)




