# %%

PRODUCTS_LIST = ['book', 'notebook', 'bottle', 'headphone']

# %%
'''

 Accessing each item from a list: list[item]
 
 We use range(0, len(list)) when we need to return
 each item position.
 
'''

# print product position
for item in range(0, len(PRODUCTS_LIST)):
    print(item)

# print product
for item in PRODUCTS_LIST:
    print(item)
    
# %%

'''

Accessing list itens and positions using list comprehension

'''

# print product position
list_comp1 = [print(f'{item}\n') for item in range(0, len(PRODUCTS_LIST))]

# print product
list_comp2 = [print(f'{item}\n') for item in PRODUCTS_LIST]

# %%

'''

Creating a new list that modifies products_list

'''

new_list = []

for item in PRODUCTS_LIST:
  new_list.append('product = ' + item)


new_list_comp = ['product = ' + item for item in PRODUCTS_LIST]

# %%

'''

Using conditions in list comprehension

'''

new_list_filtered = [print(f'{item}\n') for item in PRODUCTS_LIST if item != 'book']

# %%

'''

Using ','.join(list) method 

We use this method in order to access each item, for example,
from a list and transform it in a string

'''

str_list = ','.join(PRODUCTS_LIST)
print(str_list)

# %%

'''

.upper() and .lower() methods

'''

list_upper = [print(f'Upper Items: {item.upper()}\n') for item in PRODUCTS_LIST]

list_lower = [print(f'Lower Items: {item.lower()}\n') for item in PRODUCTS_LIST]

# %%

'''

string.split(',') method 

We use this method in order to access each item
from a string and transform it in a list

'''

products_string = 'book notebook bottle headphone'

new_list = products_string.split(' ')

print(new_list)



