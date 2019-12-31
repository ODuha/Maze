# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

taille = 5

labyrinthe= [
    [1,1,0,0,1],
    [0,1,0,0,1],
    [1,1,0,1,0],
    [1,0,1,1,0],
    [1,1,1,1,1]
]

solution = [[0]*taille for _ in range(taille)]
def resoudrelab(x, y):
    if (x==taille-1) and (y==taille-1):
        solution[x][y] = 1;
        return True;
    if x>=0 and y>=0 and x<taille and y<taille and solution[x][y] == 0 and labyrinthe[x][y] == 1:
        solution[x][y] = 1
        if resoudrelab(x+1, y):
            print("B")
            return True
        if resoudrelab(x, y+1):
            print("D")
            return True
        if resoudrelab(x-1, y):
            print("H")
            return True
        if resoudrelab(x, y-1):
            print("G")
            return True
        solution[x][y] = 0;
        return False;
    return 0;

if(resoudrelab(0,0)):
    
    for i in solution:
        print (i)
    
                    
else:
    print ("ce labyrinthe n'a pas de solution")

