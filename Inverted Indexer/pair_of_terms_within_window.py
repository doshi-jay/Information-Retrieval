word1 = "earth"
word2 = "orbit"
window = 5

inverted_index = {}


# Decode the delta encoding
def decode(positions):
    for i in range(1, len(positions)):
        positions[i] = positions[i] + positions[i-1]
    return positions

# Open the delta encoded file 
with open('inverted_list_unigram_delta_encoding.txt','r') as f:
    lines = list(f.readlines())
    for line in lines:
        # Split to get key value pairs
        line = line.split(" -> ")
        positions = line[1].strip()
        # Construct string of only numbers and commas
        positions = positions.replace(" ", "").replace("[", "").replace("]", "")
        positions = [int(position) for position in positions.split(",")]
        new_positions = []
        index = 1
        doc_positions = []
        new_position = []
        # Loop through all the positions
        while index < len(positions):
            start = index + 1
            end = start + int(positions[index])
            doc_positions = positions[start: end]
            doc_positions = decode(doc_positions)
            new_position.append(positions[index - 1])
            new_position.append(positions[index])
            new_position.append(doc_positions)
            # Create a list of lists
            new_positions.append(new_position)
            new_position = []
            # Reset index
            index = end + 1
        # Add to the inverted_index 
        inverted_index[line[0].strip()] = new_positions

print len(inverted_index)

inverted_index_word1 = inverted_index[word1]
inverted_index_word2 = inverted_index[word2]

index_en_word1 = len(inverted_index_word1)
index_en_word2 = len(inverted_index_word2)

i = 0
j = 0

docs_window = []

# Check if the 2 words are within the window
def is_within_window(words1, words2):
	for word1 in words1:
		for word2 in words2:
			if abs(word1 - word2) <= window:
				return True
	return False			

print "Checking for windows"

print len(inverted_index_word1)
print len(inverted_index_word2)

# Check all the docs in the inverted_index
while(i < len(inverted_index_word1) and j < len(inverted_index_word2)):
	doc_word_1 = inverted_index_word1[i][0]
	doc_word_2 = inverted_index_word2[j][0]
    # if both belong to the same document
	if doc_word_1 == doc_word_2:
		print "Equal"
		if is_within_window(inverted_index_word1[i][2], inverted_index_word2[j][2]):
			docs_window.append(doc_word_1)
		i += 1
		j += 1
    # If the document id of word2 is more than that of word1
	elif  doc_word_1 < doc_word_2:
		print "Increase i"
		i += 1

    # If the document id of word2 is less than that of word1
	else:
		print "Increase j"
		j += 1

print docs_window

# Writing to the file
f = open(word1 + "_" + word2 + "_window_" + str(window) + ".txt", 'w')
for doc in docs_window:
    f.write("Document ID :" + str(doc) + "\n")
f.close()


