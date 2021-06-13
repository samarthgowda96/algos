def palindrome(string):
    return string[::] == string[::-1]

string="namasn"
print(palindrome(string))