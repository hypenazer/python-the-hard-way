# Initialize the day's commuter data
cars = 100
space_in_a_car = 4		# making this 4.0 will cause line 13 to output 1 decimal place; all other outputs are unchanged
drivers = 30
passengers = 90

# set count of cars not driven
cars_not_driven = cars - drivers

# set count of cars driven
cars_driven = drivers

# carpool_capacity is total number of seats available including driver seat
carpool_capacity = cars_driven * space_in_a_car

# set the number of passengers needed in each car to accomodate all passengers.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."


#  the error "'car_pool_capacity' is not defined" will be thrown if
#  the variable is defined as 'carpool_capacity' on line 7 but referenced
#  as 'car_pool_capacity' on line 13

# 