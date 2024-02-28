# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

# def solution(word):
#     word = word.lower()
# #check original word against the reversed string
#     if word == word[::-1]:
#         return True # Return true if the same
#     else:
#         return False #return false if not
    

def solution(word):
    return word.lower() == word.lower()[::-1]