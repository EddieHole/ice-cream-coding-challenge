import pandas as pd

order = pd.read_csv('orders.csv')
pd.set_option('display.max_columns', None)
ordercopy = order.copy(())
print(ordercopy)
# 提取订单信息
order_list = ordercopy.values.tolist()
order_id = ordercopy['ID'].values.tolist()
order_orders = ordercopy['Order'].values.tolist()

order_NumberCones = order_list.copy()
print('*-----------------------11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
# function 1
def Number_Cones():  # 计算每个订单有几个冰淇淋，将总数加在data[2]
    n = len(order_orders)
    for i in range(n):
        order_NumberCones[i].append(int(order_NumberCones[i][1][:1]))
        i += 1

Number_Cones()
print(order_NumberCones)

print('*-----------------------2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')

# 如何计算flavor数量
order_SplitFlavourTopping = order_NumberCones.copy()
print('*-----------------------333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333')


# function 2
def Split_Flavor_Topping():  # 把订单信息中的flavor和topping 从 'with'分开
    n = len(order_SplitFlavourTopping)
    for i in range(0, n):
        # split flavour and topping with 'with'
        order_SplitFlavourTopping[i][1] = order_SplitFlavourTopping[i][1].split("with")
    return order_SplitFlavourTopping


Split_Flavor_Topping()
print(order_SplitFlavourTopping)


# function 3
def Count_Flavor():  # 计算每个订单的冰淇淋有几种flavor，计算其对应价格将总数加在data[3]
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
def Count_Topping():  # 计算每个订单的冰淇淋有几种topping，并将其价格加在data[4]
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
# 计算每个订单的价格

def PriceOrder(): # 计算每个订单的价格，将价格放在data[-1]
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
# 提取表格最终格式
df = pd.DataFrame(data=order_SplitFlavourTopping,columns=['ID','Price'])
print(df)

print('*-----------------------666666666666666666666666666666666666666664   6666666666666666666666666666666666666666666666')
# function 7
# 使用python 创建database，创建table

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