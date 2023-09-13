def string(s):
    words = s.split() #creating an array of the string but split in to words
    reversed_words = [] 
        for word in words:
            reversed_word = ""
            for char in word:
                reversed_word = char + reversed_word
            reversed_words.append(reversed_word)# reversing each word
    reversed_string = " ".join(reversed_words) # joining reversed words back into a string
    print(reversed_string)

def test_string():
    s = "This is a sample string"
    expected_output = "gnirts a emal si sihT"
    assert string(s) == expected_output

