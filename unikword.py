string = "Find the unique words in the string and unique string"

# Step 1
words_string = string.split(" ")
# Step 2
unique_words = []
# Step 3
for word in words_string:

	if word not in unique_words:

		unique_words.append(word)

print(unique_words)