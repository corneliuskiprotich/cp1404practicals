text = input("Enter a string: ")

word_count = {}
words = text.split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Find the length of the longest word for formatting
max_length = max(len(word) for word in word_count)

print("Word counts:")
for word, count in sorted(word_count.items()):
    print(f"{word:>{max_length}} : {count}")
