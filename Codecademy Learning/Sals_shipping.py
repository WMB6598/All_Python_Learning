#script to work out the cheapest way to ship packages

from lib2to3.pgen2 import driver


weight = 41.5

#Groud shipping
if weight <= 2:
    ground_shipping_cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
    ground_shipping_cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
    ground_shipping_cost = weight * 4 + 20
else:
    ground_shipping_cost = weight * 4.75 + 20

#Drone Shipping
if weight <= 2:
    drone_shipping_cost = weight * 4.5
elif weight > 2 and weight <= 6:
    drone_shipping_cost = weight * 9
elif weight > 6 and weight <= 10:
    drone_shipping_cost = weight * 12
else:
    drone_shipping_cost = weight * 14.25


print("Standard ground shipping will cost £" + str(ground_shipping_cost))
print("Premium ground shipping will cost £125")
print("Drone shipping will cost £" + str(drone_shipping_cost))