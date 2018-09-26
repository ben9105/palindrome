
# get name of player
print("what is your name?")
n = input()

# ask player to input word or phrase
print("Hi %s, please write a word or phrase and I'll see if it's a palindrome" % n)
a = input()

# reverse word and print out palindrome
a = a[::-1]
print("Your word backwards is " + a)

# test word to backwards version to see if they match to determine if palindrome
if a.upper() == a[::-1].upper():
    print("This is a palindrome")
else:
    print("This makes no sense")
