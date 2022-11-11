import pyperclip

s = pyperclip.paste()

s = s.split('\t')
string = ''

string += 'Internal Number: ' + s[0] + '\r\n'
string += 'Name: ' + s[2] + '\r\n'
string += 'Address Line 1: ' + s[3] + '\r\n'
string += 'Address Line 2: ' + s[4] + '\r\n'
string += 'City: ' + s[5] + '\t\t' + 'Postal/Zip Code: ' + s[7] + '\r\n'
string += 'Country: USA \t\t' + 'Province/State: ' + s[6] + '\r\n'
string += 'Phone number: ' + '\t\t' + 'Billing Type: Direct Bill' + '\r\n'
string += 'Fax Number: ' + '\t\t' + 'Allow Supplier in Entry: Yes' + '\r\n'
string += 'Credit Treshold: ' + '\r\n'
string += 'Mode: Test' + '\r\n'
string += 'Status: Acknowledged' + '\r\n'
string += 'Description: ' + '\r\n'
string += 'GST/VAT Number: ' + '\r\n'
string += 'Next Invoice Number: ' + '\t\t' +  'Publish to Group Centre: No' + '\r\n'
string += 'Category: ' + '\r\n'
string += 'Head Office: yes' + '\r\n'
string += '\r\n' + '\r\n'
string += 'Contact Name: ' + s[9] + '\r\n'
string += 'Contact Email: ' + s[11] + '\r\n'

string += '\r\n' + '\r\n'
string += '\r\n' + '\r\n'

string += s[0] + '\r\n'
string += s[2] + '\r\n'
string += s[3] + '\r\n'
string += s[4] + '\r\n'
string += s[5] + '\r\n'
string += 'USA' + '\r\n'
string += 'Phone number: ' + '\r\n'
string += 'Fax Number: ' + '\r\n'
string += 'Credit Treshold: ' + '\r\n'
string += 'Mode: Test' + '\r\n'
string += 'Status: Acknowledged' + '\r\n'
string += 'Description: ' + '\r\n'
string += 'GST/VAT Number: ' + '\r\n'
string += 'Next Invoice Number: ' + '\r\n'
string += 'Category: ' + '\r\n'
string += 'Head Office: yes' + '\r\n'

string += '\r\n' + '\r\n'

string += 'Postal/Zip Code: ' + s[7] + '\r\n'
string += 'Province/State: ' + s[6] + '\r\n'
string += 'Billing Type: Direct Bill or central pay' + '\r\n'
string += 'Allow Supplier in Entry: Yes' + '\r\n'


string += '\r\n' + '\r\n'
string += '\r\n' + '\r\n'
string += 'Affiliated Distributors PHCP (965974)' + '\r\n'
string += s[0][0:5]

print(string)
pyperclip.copy(string)