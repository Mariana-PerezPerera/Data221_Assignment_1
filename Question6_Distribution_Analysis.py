#Distribution Analysis:
#define a function that receives a list of numbers and returns a dictionary
#creating the function that is taking a list of numbers and finding the length
def list_of_numbers_to_a_dictionary(list_of_numbers):
    final_dictionary = {}
    length_of_the_list_of_numbers = len(list_of_numbers)

#sorting the list of numbers:
    sorted_list_of_numbers = sorted(set(list_of_numbers))

#for loop to inititate the count and if <= the value it adds:
    for value in sorted_list_of_numbers:
        count = 0
        for num in list_of_numbers:
            if num <= value:
                count +=1

#calculating the percentage and adding it the dictionary:
        percentage_of_the_value_greater_than_or_equal_to_the_other_values = (count / length_of_the_list_of_numbers) * 100
        final_dictionary[value] = percentage_of_the_value_greater_than_or_equal_to_the_other_values

    return final_dictionary

#printing the final dictionary:
list_of_numbers = [3, 1, 2, 3, 4, 2]
print(list_of_numbers_to_a_dictionary(list_of_numbers))
