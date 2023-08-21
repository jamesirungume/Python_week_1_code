def highest_value(characterString):
    # This dictionary assigns numeric values to each letter of the alphabet
    alphabetNumbers = {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 0,
                        'f': 6, 'g': 7, 'h': 8, 'i': 0, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 0,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                        'u': 0, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
                        
    # We're setting up two counters to help us track values
    constantValue = 0
    maxConstant = 0

    # Let's go through each letter in the input string
    for character in characterString:
        # If the letter isn't a vowel (a, e, i, o, u)...
        if character not in "aeiou":
            # ...we're adding the assigned value to our counter
            constantValue += alphabetNumbers[character]
        else:
            # If we find a vowel, we'll check if the current value is the highest so far,
            # update it if needed, and then reset the counter for the next round
            maxConstant = max(maxConstant, constantValue)
            constantValue = 0
            
    # Let's show the highest value we found for consonant substrings
    print(f"The highest value of consonant substrings is: {maxConstant}")
    return maxConstant

# Hey there! Could you please provide a lowercase string for us to work with?
input_string = input("Sure thing! Just type in a lowercase string: ")

# Awesome, let's find out the highest value of consonant substrings in that string!
highest_value(input_string)
