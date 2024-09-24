import string


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


# Example usage:
text = "Hello, world! How's it going?"
print(remove_punctuation(text))
