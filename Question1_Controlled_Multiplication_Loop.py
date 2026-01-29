#Write a python program that multiples consecutive integers starting from 1 until the product first becomes greater than a given threshold value
#assign/store values in the variables:
the_threshold = 100
final_product_of_the_multiplication = 1
the_current_multiplier = 1

#create the loop that does the multiplication:
while final_product_of_the_multiplication <= the_threshold:
    the_current_multiplier += 1
    final_product_of_the_multiplication *= the_current_multiplier

#print the final product as well as the number that exceeds the threshold:
print("The final product is:", final_product_of_the_multiplication)
print("The number that caused the product to exceed the threshold is:", the_current_multiplier)