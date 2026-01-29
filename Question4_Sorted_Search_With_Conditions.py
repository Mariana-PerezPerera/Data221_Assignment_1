#Sorted search with conditions
#given a list of random values between 0 and 1 and a random value x
from random import random
list_of_random_values = [random() for i in range(20)]
random_number = random()

#sort the list
list_of_random_values.sort()

#finding the indices where the value is >= x
indices_of_the_list_where_the_value_is_greater_than_or_to_x = []
for i in range(len(list_of_random_values)):
    if list_of_random_values[i] >= random_number:
        indices_of_the_list_where_the_value_is_greater_than_or_to_x.append(i)

print("The sorted values:", list_of_random_values)
print("The value of x:", random_number)

if (indices_of_the_list_where_the_value_is_greater_than_or_to_x):
    print("The first matching index:", indices_of_the_list_where_the_value_is_greater_than_or_to_x[0])
else:
    print("There is no value is greater than or equal to x")
