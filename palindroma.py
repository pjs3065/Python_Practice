text = input("Enter a string \n")
text.replace(" ","")
reverse = str()

index = len(text)-1

while index >= 0:
    reverse += text[index]
    index -= 1

if text == reverse:
    print('This is a palindrome')
else:
    print('This is not a plindrom')

