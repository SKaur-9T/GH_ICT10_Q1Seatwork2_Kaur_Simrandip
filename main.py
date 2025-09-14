# data types in Python
from pyscript import display

restaurant_name = 'Pretzel Bites' # string
business_hours = '7:00 AM - 9:00 PM'# string
year_established = 2025 # integer
owner_fname = 'Simrandip'# string
owner_lname = 'Kaur'# string
tax_rate = 0.15 # floating-point
has_delivery = True # boolean

product_names = [ 'Super Pretzel','Pretzel Bum','Coffee','Pretzel Crisps','Cheese Dip','Mini Pretzel Box','Stuffed Pretzel','Pretzel Sandwich']  # list

menu_prices = (90.0, 60.0, 100.0, 160.0, 30.0, 120.0, 180.0, 200.0) # tuple
common_allergens = 'Milk, Wheat, Eggs' # string



# info shop
display(f'Welcome To {restaurant_name}!!', target='shoptitle')    # string
display(f'Owner : {owner_fname} {owner_lname}', target='ownersname')  # string
display(f'Since {year_established}', target='yearestablished') # integer
display(f'Tax rate : {tax_rate} ₱', target='taxrate')  # float

# Product names and prices
display(f'{product_names[0]}', target='Super_Pretzel_product') # string + list
display(f'{menu_prices[0]} ₱', target='Super_Pretzel_price')# tuple

display(f'{product_names[1]}', target='Pretzel_Bum_product') # string + list
display(f'{menu_prices[1]} ₱', target='Pretzel_Bum_price')# tuple

display(f'{product_names[2]}', target='Coffee_product') # string + list
display(f'{menu_prices[2]} ₱', target='Coffee_price')# tuple

display(f'{product_names[3]}', target='Pretzel_Crisps_product') # string + list
display(f'{menu_prices[3]} ₱', target='Pretzel_Crisps_price')# tuple

display(f'{product_names[4]}', target='Cheese_Dip_product') # string + list
display(f'{menu_prices[4]} ₱', target='Cheese_Dip_price')# tuple

display(f'{product_names[5]}', target='Mini_Pretzel_Box_product') # string + list
display(f'{menu_prices[5]} ₱', target='Mini_Pretzel_Box_price')# tuple

display(f'{product_names[6]}', target='Stuffed_Pretzel_product') # string + list
display(f'{menu_prices[6]} ₱', target='Stuffed_Pretzel_price')# tuple

display(f'{product_names[7]}', target='Pretzel_Sandwich_product') # string + list
display(f'{menu_prices[7]} ₱', target='Pretzel_Sandwich_price')# tuple

# Delivery
if has_delivery:
    display("Delivery available!", target="deliverystatus")   # boolean
else:
    display("Sorry, delivery unavailable!", target="deliverystatus")

# Allergens
display(f'⚠ Be careful, our products contain: {common_allergens}.', target='commonallergens')

# Business hours
display(f'Business Hours: {business_hours}', target='businesshours')

