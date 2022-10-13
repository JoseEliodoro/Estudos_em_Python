#Exercício 8.9
magicians = ['ciro', 'simone', 'soraia', 'bolsonaro', 'lula']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)
        
#show_magicians(magicians)

#Exercício 8.10
""" def make_great(list_magicians):
    n = len(list_magicians)
    while n > 0:
        n -= 1
        list_magicians[n] = 'O(a) grande '+ list_magicians[n]
        

make_great(magicians)
show_magicians(magicians) """



#Exercício 8.11
def make_great(list_magicians):
    n = len(list_magicians)
    while n > 0:
        n -= 1
        list_magicians[n] = 'O(a) grande '+ list_magicians[n]
    return list_magicians

new_list = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_list)