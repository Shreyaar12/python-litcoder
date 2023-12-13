def to_goat_latin(sentence):
    """
    Function to convert a sentence to Goat Latin.

    Parameters:
    sentence (str): The input sentence to be converted.

    Returns:
    str: The converted Goat Latin sentence.
    """
    vowels = "aeiouAEIOU"
    words = sentence.split()

    for i, word in enumerate(words):
        if word[0] in vowels:
            words[i] = word + "ma"
        else:
            words[i] = word[1:] + word[0] + "ma"
        words[i] += "a" * (i + 1)

    return ' '.join(words)

# Adding user input handling
if __name__ == "__main__":
    # User inputs the sentence
    sentence_input = input("Enter the sentence: ")

    # Running the function and displaying the result
    goat_latin_sentence = to_goat_latin(sentence_input)
    print("Goat Latin Sentence:", goat_latin_sentence)
