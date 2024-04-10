# Check if a string does NOT contain substring in Python 

string = 'bobbyhadz.com'

substring = 'abc'

if substring not in string:
    # 👇️ this runs
    print('The string does NOT contain the substring')
else:
    print('The string contains the substring')