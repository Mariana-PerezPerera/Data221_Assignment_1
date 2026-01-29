#Safe Function Application:
#define a function that computes x^y, then given a list of pairs (x,y):
def computing_powers_to_a_list_of_pairs(x, y):
    return x ** y

#assigning the variable and creating the final empty list (the pairs)
number_pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
final_pairs_of_the_numbers = []

#creating the loop where it skips when y is negative.
for x, y in number_pairs:
    if y >= 0:
        final_pairs_of_the_numbers.append(computing_powers_to_a_list_of_pairs(x, y))

#print out the final list of pairs of numbers:
print(final_pairs_of_the_numbers)