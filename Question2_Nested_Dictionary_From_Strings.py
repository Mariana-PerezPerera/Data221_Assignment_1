#define a function that receives a list of strings and returns a dictionary with the following structure:
#create the function:
def list_of_strings_to_nested_dictionary(list_of_strings):
    nested_dictionary_information = {}

    #create the for loop that looks at the length and decides if the words are even or odd and then creates the dictionary
    for s in list_of_strings:
        length_of_the_strings = len(s)
        parity_of_the_length_of_the_string = "even" if length_of_the_strings % 2 == 0 else "odd"

        nested_dictionary_information[s] = {
            "The length of the string is": length_of_the_strings,

            "The parity of the string is": parity_of_the_length_of_the_string
        }

    return nested_dictionary_information

#print the final dictionary:
print(list_of_strings_to_nested_dictionary(["Data", "Science"]))