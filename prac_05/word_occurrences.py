"""
Word Occurrences
Estimate: 30min
Actual: 45min
"""


def count_words():

    text = input("Text: ")

    # Split the string into words
    words = text.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the dictionary by key word
    sorted_word_counts = dict(sorted(word_counts.items()))

    # Find the longest word for formatting
    max_length = max(len(word) for word in sorted_word_counts)

    # Print the word counts aligned in a neat column
    for word, count in sorted_word_counts.items():
        print(f"{word:{max_length}} : {count}")

count_words()