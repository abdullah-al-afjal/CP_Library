def sort_words(sentence):
    words = sentence.split()
    words.sort()
    return " ".join(words)


# Example usage:
sentence = "the quick brown fox jumps over the lazy dog"
print(sort_words(sentence))
