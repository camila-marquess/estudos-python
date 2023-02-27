# %%

CAT_DICT = {
  "color": "black",
  "age": 2
}

# %%

'''

Accessing dict keys with dict.keys()

'''

CAT_DICT.keys()

# %%

'''

Accessing dict values with dict.values()

'''

CAT_DICT.values()

# %%

'''

Accessing a specific key from a dict

'''

print(CAT_DICT['color'])

print(CAT_DICT.get('color'))
# %%

'''

Accessing keys and values with dict.items() method

'''

CAT_DICT.items()

# %%

'''

Updating a key using dict.update() method

'''

CAT_DICT.update({"color":"gray"})

CAT_DICT.items()

# %%

'''

Updating a dict value

'''
  
for key, value in CAT_DICT.items():
  if key == 'color':
    CAT_DICT[key] = 'gray' 
  
CAT_DICT.items()
# %%

'''

List comprehension in dicts

'''

new_dict = {k: v for k, v in CAT_DICT.items() if k == 'age'}

print(new_dict)

# %%

'''

Using functions in dicts

'''

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

def total_value(current_price):
  return (current_price[0], current_price[1] * 10)

final_value = dict(map(total_value, prices.items()))

print(final_value)

# %%

'''

Using toolz library

'''

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

import toolz 

def total_value(current_price):
  return (current_price * 10)

final_value = toolz.valmap(total_value, prices)

print(final_value)

# %%
