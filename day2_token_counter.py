# 1. The raw string
text = "AI is great and AI is the future"

# 2. Split into list
word_list = text.split()

# 3. The empty dictionary
word_counts = {}

# 4. The loop and conditional logic design
for word in word_list:
    if word in word_counts:
        # If the word is already a key, increase its value by 1
        word_counts[word] += 1
    else:
        # If it's a new word, add it as a key and set its value to 1
        word_counts[word] = 1


print(word_counts)
