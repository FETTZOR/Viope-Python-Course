
# In this exercise the aim is to try out different datatypes. Start by defining
# two variables, and assign the first variable the float value 10.6411.
# The second variable gets a string "Stringline!" as a value.


# Convert the first variable to an integer, and multiply the variable with
# the string by 2. After this, finalize the program to print out the results in the following way:

first_variable = 10.6411
second_variable = "Stringline!"

first_variable = int(first_variable)

second_variable = second_variable * 2

print("Integer conversion cannot do roundings: ", first_variable)
print("Multiplying strings also causes trouble: ", second_variable)