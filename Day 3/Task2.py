def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def longest_word(sentence):
    words = sentence.split()
    longest_pal = ""

    for word in words:
        if is_palindrome(word) and len(word) > len(longest_pal):
            longest_pal = word
    if longest_pal:
        return longest_pal  
    else:
        return "No palindrome found"

sen = "I saw madam at noon"
print(longest_word(sen))  