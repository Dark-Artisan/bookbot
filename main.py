#print("hello world")
def count_words(string):
    """Count the number of words in a string"""
    words = string.split()
    word_count = len(words)
    return word_count

def count_characters(string):
    """ Convert any character to lowercase, creates a dictionary used to count the number of characters and spaces from a string."""
    # example -- {'p': 6121, 'r': 20818, 'o': 25225, ...
    char_counter_dict = {}
    lowered_string = string.lower()
    for char in lowered_string:
        #print(char)
        if char in char_counter_dict:
            char_counter_dict[char] += 1
        else:
            char_counter_dict[char] = 1
            #print(char_counter_dict)
    return char_counter_dict

def create_report(word_count, char_count, file_name):
    """Create a report of the findings from word_count and count_characters functions, includes only characters from the alphabet"""
    # Example output:
    #--- Begin report of books/frankenstein.txt ---
    #77986 words found in the document
    #The 'e' character was found 46043 times
    #--- End report ---
    char_dict = {}
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    #print(char_count)
    for key, value in char_count.items():
        if key.isalpha():
            char_dict[key] = value
    # sort the dictionary by keys
    sorted_by_keys = dict(sorted(char_dict.items()))
    #print(char_dict)
    #print(sorted_by_keys)
    # print the key/value pairs
    for key, value in sorted_by_keys.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

    

def main():
    """Main function"""
    path_to_file = "books/frankenstein.txt"
    #path_to_file = "test_file.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    #print(count_words(file_contents))
    #count_characters("Hello World")
    #print(count_characters(file_contents))
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    create_report(word_count, char_count, path_to_file)

main()

