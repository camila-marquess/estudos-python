# %%

import pandas as pd
# %%

'''

Creating a dataframe from two lists
The zip() function returns an iterator of tuples based on the iterable objects.

'''

products_list = ['book', 'notebook']

products_prices = [40, 20]

products_information = [{'product': item1, 'price': item2} for item1, item2 in zip(products_list, products_prices)]

df = pd.DataFrame(products_information)

df.head()

# %%

''''

Adding a column by applying a function in other column

'''

def add_shipping(price, shipping_price):
    result = price + shipping_price
    return result 

df['shipping_price'] = add_shipping(df['price'], 10)

df.head()

# %%

'''

Using df.iterrows()

'''

def add_shipping(price, shipping_price):
  for index, row in df.iterrows():
    result = price + shipping_price 
  return result

df['shipping_price'] = add_shipping(df['price'], 10)

df.head()
# %%
