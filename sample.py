import pandas as pd

order = pd.read_csv('orders.csv')
pd.set_option('display.max_columns', None)
ordercopy = order.copy(())
print(ordercopy)

order_list = ordercopy.values.tolist()
order_id = ordercopy['ID'].values.tolist()
order_orders = ordercopy['Order'].values.tolist()

order_NumberCones = order_list.copy()
print('*-----------------------11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
# function 1
def Number_Cones():  
    n = len(order_orders)
    for i in range(n):
        order_NumberCones[i].append(int(order_NumberCones[i][1][:1]))
        i += 1

Number_Cones()
print(order_NumberCones)

print('*-----------------------2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')


order_SplitFlavourTopping = order_NumberCones.copy()
print('*-----------------------333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333')


# function 2
def Split_Flavor_Topping(): 
    n = len(order_SplitFlavourTopping)
    for i in range(0, n):
        # split flavour and topping with 'with'
        order_SplitFlavourTopping[i][1] = order_SplitFlavourTopping[i][1].split("with")
    return order_SplitFlavourTopping


Split_Flavor_Topping()
print(order_SplitFlavourTopping)


# function 3
def Count_Flavor():  
    n = len(order_SplitFlavourTopping)
    for x in range(n):
        a = order_SplitFlavourTopping[x][1][0]
        VanillaCount = a.count('vanilla')
        ChocoCount = a.count('chocolate')
        LemonCount = a.count('lemon')
        StrCount = a.count('strawberry')
        countTotal = VanillaCount + ChocoCount + LemonCount + StrCount
        order_SplitFlavourTopping[x].append(countTotal)
        if order_SplitFlavourTopping[x][3] == 1:
            order_SplitFlavourTopping[x][3] = 1
        elif order_SplitFlavourTopping[x][3] == 2:
            order_SplitFlavourTopping[x][3] = 1.75
        elif order_SplitFlavourTopping[x][3] == 3:
            order_SplitFlavourTopping[x][3] = 2.15
        x += 1


Count_Flavor()
print(order_SplitFlavourTopping)
print('*-----------------------4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444')


# function 4
def Count_Topping():  
    n = len(order_SplitFlavourTopping)
    for x in range(n):
        order_SplitFlavourTopping[x][1].insert(1, '0')
        a = order_SplitFlavourTopping[x][1][-1]
        CaramelCount = a.count('caramel')
        CreamCount = a.count('cream')
        CandyCount = a.count('candy')
        SprCount = a.count('sprinkles')
        countTotal2 = CaramelCount + CreamCount + CandyCount + SprCount
        order_SplitFlavourTopping[x].append(countTotal2)
        if order_SplitFlavourTopping[x][4] == 1:
            order_SplitFlavourTopping[x][4] = 0.1
        elif order_SplitFlavourTopping[x][4] == 2:
            order_SplitFlavourTopping[x][4] = 0.18
        elif order_SplitFlavourTopping[x][4] == 3:
            order_SplitFlavourTopping[x][4] = 0.24
        elif order_SplitFlavourTopping[x][4] == 4:
            order_SplitFlavourTopping[x][4] = 0.28
        x += 1


Count_Topping()
print(order_SplitFlavourTopping)


# function 5


def PriceOrder(): 
    n = len(order_SplitFlavourTopping)
    for i in range(n):
        df = pd.DataFrame()
        discountNumber = order_SplitFlavourTopping[i][2]
        if discountNumber <10 and discountNumber >=5:
            rate = 0.9
        elif discountNumber >10:
            rate = 0.8
        else:
            rate = 1
        ConesNumber=[]
        FlavorPrice=[]
        ToppingPrice =[]
        ConesNumber =order_SplitFlavourTopping[i][2]
        FlavorPrice =order_SplitFlavourTopping[i][3]
        ToppingPrice= order_SplitFlavourTopping[i][4]
        OrderPrice = ConesNumber*(FlavorPrice+ToppingPrice)*rate
        OrderPrice =  '%.2f' % OrderPrice # output the prices using the format of Code_requirements
        order_SplitFlavourTopping[i].append(OrderPrice)
        #print(order_SplitFlavourTopping[i])
        del order_SplitFlavourTopping[i][1:5]
    return order_SplitFlavourTopping

PriceOrder()

print(order_SplitFlavourTopping)
print(order_SplitFlavourTopping[0])

# function 6

df = pd.DataFrame(data=order_SplitFlavourTopping,columns=['ID','Price'])
print(df)

print('*-----------------------666666666666666666666666666666666666666664   6666666666666666666666666666666666666666666666')
# function 7


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
    cur.executemany("INSERT INTO ORDERS VALUES(?,?)",order_SplitFlavourTopping)
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
