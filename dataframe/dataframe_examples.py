# %%

import pandas as pd
# %%

'''

Creating a dataframe from two lists

'''

products_list = ['book', 'notebook']

products_prices = [40, 20]

products_information = [{'product': item1, 'price': item2} for item1, item2 in zip(products_list, products_prices)]

df = pd.DataFrame(products_information)

df.head()

# %%
