""" Write a program that calculates a Christmas budget: -
With Christmas coming up you want to save 25 % of your salary in Sept, Oct, Nov after you've paid rent and utilities.

Assume you get paid 1250 per month, your rent is 650 and utilities are 175.

Print the amount you must save each month to meet this target?
Print the amount you will have in December for Christmas shopping
 """
monthlySaving = (1250 - 650 - 175) * 25 / 100
print("You must save " + str(monthlySaving) + " per month to meet your target")

salary = 1250 * 3
rent = 650 * 3
utilities = 175 * 3

decemberSaving = (salary - rent - utilities) * 25 / 100
print("You will have " + str(decemberSaving) +
      " for Christmas shopping in December")
