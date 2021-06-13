def palindrome(string):
    return string[::] == string[::-1]

string="naman"
print(palindrome(string))