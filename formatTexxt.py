import pyperclip

spam = pyperclip.paste()
spam = spam.replace('A.', '\r\nA.')
spam = spam.replace('B.', '\r\nB.')


print(spam)
pyperclip.copy(spam)