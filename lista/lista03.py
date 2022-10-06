requested_toppings = []
if requested_toppings: #Verifica se a lista esá vazia
    for requested_topping in requested_toppings:
        print('Adding '+ requested_topping +'.')
        print('\nFinished makeng your pizza!')
else:
    print('Are you sure you want a plain pizza?')  
    
available_toppings = ['mushrooms', 'olives', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding '+ requested_topping +'.')
    else:
        print("Sorry, we don't have "+ requested_topping +".")
print('\nFinished making your pizza!')