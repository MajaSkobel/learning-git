def palindrome(word):
    if not isinstance(word, str):
        return None
    word_letters = [letter for letter in word]
    word_letters_reversed = word_letters[::-1]
    if word_letters == word_letters_reversed:
        return True
    else:
        return False