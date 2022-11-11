import pyperclip

spam = pyperclip.paste()

addStr = ' '

spam = spam.split('\n')
for i in spam:
    si = i.split('/')
    si = si[0] + '\t' + si[2]
    print(si)
    addStr += str(si) + '\n'



print(addStr)

pyperclip.copy(addStr)