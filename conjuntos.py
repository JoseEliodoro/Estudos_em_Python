'''
conjunto = {1, 2, 3, 4, 4, 2}
conjunto.add(5) #Add elementos ao conjunto
conjunto.discard(2) #Remove elementos do conjunto
print(conjunto)
'''
'''
conjunto = {1, 2, 3, 4, 5, 6}
conjunto2 = {5, 6, 7, 8, 9, 0}
print(f'A = {conjunto} \nB = {conjunto2}')
#União de dois conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print('A U B =', conjunto_uniao)

#Intesecção de dois conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('A ∩ B =', conjunto_interseccao)

#Diferença entre conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
print('A - B =', conjunto_diferenca)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('B - A =', conjunto_diferenca2)

#Difetença simétrica
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica', conjunto_diff_simetrica)
'''

conjunto_a, conjunto_b = {1, 2, 3}, {1, 2, 3, 4, 5}
print(f'A = {conjunto_a} \nB = {conjunto_b}')
#Subconjunto 
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A ⊆ B :', conjunto_subset)

conjunto_supset = conjunto_b.issuperset(conjunto_a)
print('A ⊆ B :', conjunto_subset)
