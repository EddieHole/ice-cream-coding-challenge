# ice-cream-coding-challenge

### Original idea and design.
1. Extracts orders from the orders.csv file

Answer: Use the values.tolist() function to extract the order information.

2. Computes the price for Purchase orders of Ice-cream cones with toppings

Answer: when calculating the order price, there are three elements to pay attention to:
1) The number of ice creams ordered.
2) The number of flavors of the ice cream.
3) The number of toppings on the ice cream.
The calculation formula of get_item_price is (the price corresponding to the number of flavors + the sum of the topping price after calculation) multiplied by the number of ice creams and multiplied by the original discount of 1.0.
