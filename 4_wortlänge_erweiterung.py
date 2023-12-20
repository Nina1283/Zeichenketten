def calculate_len(word):
    result = len(word)
    return result

write_a_word = input("Write a word(at least 6 letters): ")

if len(write_a_word) < 6:
    print("The entry was not valid.")

else:
    print(f"The len of the word is: {calculate_len(write_a_word)}")