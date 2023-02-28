tuple = (1, 3, 5, 9, 8, -1, -2, -3, -4, -5)
newtup1 = ()
newtup2 = ()
for i in tuple:
    if i > 0:
       newtup1 += (i,)
    elif i<0:
      newtup2 += (i,)

print(newtup1)
print(newtup2)
