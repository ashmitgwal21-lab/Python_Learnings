word = input("Enter a word: ").lower()

vowel_count = 0
vowel = "aeiou"

for char in word:
    if char in vowel:
        vowel_count += 1

print(f'The word "{word}" has {vowel_count} vowels"')