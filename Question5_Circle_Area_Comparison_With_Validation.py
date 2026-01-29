#Circle Area Comparison with validation
#write a function that takes the radii of two circles and performs the following given tasks:
import math

#create the function that will determine the area of the circles and comparing the circles:
def comparison_of_the_area_of_two_circles(radius_of_circle1, radius_of_circle2):
    if not isinstance(radius_of_circle1, int) or not isinstance(radius_of_circle2, int):
        return ("Error: the radii must be integers.")
    if radius_of_circle1 <= 0 or radius_of_circle2 <= 0:
        return ("Error: the radius must be positive.")

    area_of_circle1= math.pi * radius_of_circle1 ** 2
    area_of_circle2= math.pi * radius_of_circle2 ** 2

    smaller_circle = min(area_of_circle1, area_of_circle2)
    larger_circle = max(area_of_circle1, area_of_circle2)

#dividing the smaller circle by the larger circle and finding the percentage that can cover the larger circle:
    percentage_of_the_larger_circe_that_can_be_covered_by_the_smaller_circle = smaller_circle / larger_circle * 100
    return percentage_of_the_larger_circe_that_can_be_covered_by_the_smaller_circle

#pringint/testing two values:
print(comparison_of_the_area_of_two_circles(8, 2))
