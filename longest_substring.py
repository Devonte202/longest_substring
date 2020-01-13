"""
Problem: Given a string find the length of the longest substring with no repeating characters
input: string
output: number(integers)

Examples: 
maxSubStr('abcabcbb') == 3
maxSubStr('bbbbb') == 1
maxSubStr('pwwkew') == 3
maxSubStr('kuvsuu') == 4

Data Structure: Dictionary 
Algorithm: 
0: Create an empty dictionaries
1: Create wordCount variable initialized with 0
2: Loop through string
    I: Check to see if each character is in char dictionary & Increment wordCount value while
    II: If character already lives on dictionary, increment property value
    III: 
3: Return the wordCount variable
"""

def maxSubStr(word):
    letterCount = {}
    wordCount = 0
    wordCountTwo = 0
    for char in word:
        if char in letterCount:
            letterCount.clear()
            letterCount[char] = 1
            print(wordCount)
            print(wordCountTwo)
            if wordCount > wordCountTwo:
                wordCountTwo = 0
            else: 
                wordCount = wordCountTwo
                wordCountTwo = 0
            
        else: 
            letterCount[char] = 1
            wordCount += 1
    return wordCount

print(maxSubStr('abcabcbb') == 3)
print(maxSubStr('bbbbb') == 1)
print(maxSubStr('kuvsuu') == 4)
print(maxSubStr('pwwkew') == 3)

