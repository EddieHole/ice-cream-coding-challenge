# ice-cream-coding-challenge

### Original idea and design.
## 1. Extracts orders from the orders.csv file

Answer: Use the values.tolist() function to extract the order information.

## 2. Computes the price for Purchase orders of Ice-cream cones with toppings

Answer: when calculating the order price, there are three elements to pay attention to:
1) The number of ice creams ordered.
2) The number of flavors of the ice cream.
3) The number of toppings on the ice cream.

The calculation formula of get_item_price is (the price corresponding to the number of flavors + the sum of the topping price after calculation) multiplied by the number of ice creams and multiplied by the original discount of 1.0.


1. Calculate the quantity of ice cream and use the first slice in the order information as the output. Here, in order to facilitate subsequent output, an int conversion process is performed.

2. Observe the description of the order.
There is the word 'with' between flavors and toppings, so take 'with' as the boundary to separate flavors and toppings.
Then count the number of times the flavor and topping appear in the order, respectively.


## 3.Store the purchase order ID and the computed price in a table in a database

Answer: Use the SQLite library to create databases and tables.


## Errors found after inspection:

1. The same ID will have different orders. Orders with the same ID should be merged and then calculated.
2. The save format of 'Price' stored in the table should retain two decimal places.
