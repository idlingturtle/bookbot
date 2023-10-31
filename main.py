book = "./books/frankenstein.txt"
with open(book) as f:
    contents = f.read()

words = contents.split()
word_count = 0
for word in words:
    word_count += 1

characters = {}
lower_cased = contents.lower()
for alphabet in lower_cased:
    characters[alphabet] = characters.get(alphabet, 0)  + 1

char_list =[]
for key, value in characters.items():
    if key.isalpha() == True:
        temp = [value,key]
        char_list.append(temp)
char_list.sort(reverse=True)

print(f"--- Begin report of {book} ---")
print(f"{word_count} words found in the document")
for char in char_list:
    print(f"the {char[1]} character was found {char[0]} times")
print("--- End report ---")