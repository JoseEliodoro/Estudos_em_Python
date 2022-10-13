unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Forma sem o uso de função
""" 
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print('Printing model: '+ current_design)
    completed_models.append(current_design)

print('\nThe following models have been printed: ')
for completed_model in completed_models:
    print(completed_model)
     
"""
#Forma dividido em funções
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: '+ current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)
        
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Essa forma é prefirivel pois tem uma maior organização no código, o que facilida uma futura implementação