def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

w = input("Enter a word: ")
print(f"The number of vowels is: {count_vowels(w)}")