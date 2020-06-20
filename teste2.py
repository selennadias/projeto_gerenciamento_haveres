
result = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
for i in result:
    #print(i)
    if type (i) == list:
       for j in i:
          print(j)  
          