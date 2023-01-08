from itertools import combinations 
comb = combinations (["musa","software","2010","March","fitness","istanbul","cat"],4)
with open("passw.txt", "w") as f:
    for i in list(comb):
        f.write(str(i))
        f.write("\n")
