from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum, auto
import pandas as pd


class Flavour(Enum):
    VANILLA = auto()
    CHOCOLATE = auto()
    LEMON = auto()
    STRAWBERRY = auto()


class IceCreamCones(int, Enum):
    price: float

    def __new__(cls, value: int, price: float = 0) -> IceCreamCones:
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.price = price
        return obj

    ZERO = (0, 0.0)
    ONE = (1, 1.0)
    TWO = (2, 1.75)
    THREE = (3, 2.15)



class ToppingType(Enum):
    CARAMEL = auto()
    CHOCOLATE = auto()
    CREAM = auto()
    CANDY = auto()
    SPRINKLES = auto()


class PriceableItem(ABC):

    @abstractmethod
    def get_item_price(self) -> float:
        pass


class IceCream(PriceableItem):

    def __init__(self, num) -> None:
        super().__init__()
        self.flavours = []
        self.toppings = []
        self.num = num
        self.discount = 1.0
        if self.num >= 5:
            if self.num < 10:
                self.discount = 0.9
            else:
                self.discount = 0.8


    def add_flavour(self, flavour: Flavour) -> None:
        self.flavours.append(flavour)

    def add_topping(self, topping: ToppingType) -> None:
        self.toppings.append(topping)

    def get_item_price(self) -> float:

        topping_discount = 1.0
        num_of_toppings = len(self.toppings)
        if num_of_toppings > 1:
            topping_discount = 1 - (num_of_toppings - 1) * 0.1

        return (IceCreamCones(len(self.flavours)).price + 0.1 * num_of_toppings * topping_discount) * self.num * self.discount


class PurchaseOrder(PriceableItem):

    def __init__(self):
        self.ice_cream = None

    def add(self, item: PriceableItem):
        self.ice_cream = item

    def get_item_price(self) -> float:
        return self.ice_cream.get_item_price()

    class Parser:

        @staticmethod
        def parse(order_str: [str]) -> PurchaseOrder:
            num_of_ice_cream = int(order_str[:1])
            p_order = order_str.split("with")
            purchase = PurchaseOrder()
            ice_cream = IceCream(num_of_ice_cream)
            flavour_l = [x.strip(",") for x in p_order[0].split()]

            for i in range(1, len(flavour_l) - 1):

                f = flavour_l[i].upper()

                if f in Flavour.__members__:
                    ice_cream.add_flavour(f)

            if len(p_order) > 1:
                topping_l = [x.strip(",") for x in p_order[1].split()]

                for i in range(0, len(topping_l)):

                    t = topping_l[i].upper()

                    if t in ToppingType.__members__:
                        ice_cream.add_topping(t)

            purchase.add(ice_cream)
            return purchase

order = pd.read_csv('orders.csv')
pd.set_option('display.max_columns', None)
ordercopy = order.copy(())
print(ordercopy)
# extrace orders informations
order_list = ordercopy.values.tolist()
order_id = ordercopy['ID'].values.tolist()
order_orders = ordercopy['Order'].values.tolist()


df= []
df = pd.DataFrame(data= df,columns= ['ID','Price'])
df1 = []
df2 = []
for o in order_list:
    # order_id
    p_order_id = o[0]
    df1.append(p_order_id)
    print(p_order_id)

    # price
    p = PurchaseOrder.Parser.parse(o[1])
    df2.append(p.get_item_price())
    print(p.get_item_price())

df['ID']= df1
df['Price'] = df2

# function 7
# Store the purchase order ID and the computed price in a table in a database

import sqlite3
con = sqlite3.connect(':memory:')
cur = con.cursor()
# Create table
def create_Orders_table():
    cur.execute('''CREATE TABLE ORDERS (                                       
      ID VARCHAR(255),                                                         
      Price NUMERIC                                                            
    )''')
# Insert a row of data
def insert_data():
    cur.executemany("INSERT INTO ORDERS VALUES(?,?)", df.values.tolist())
    con.commit()
def check_data():
    for row in cur.execute('SELECT * FROM ORDERS ORDER BY ID'):
        print(row)
def show_table():
    cur.execute("PRAGMA table_info(ORDERS)")
    print(cur.fetchall())

create_Orders_table()
insert_data()
check_data()