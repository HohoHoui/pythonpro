def frequency_analytic(a):
    dic = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0,
            "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, 
            "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, 
            "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, 
            "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" :0,
            "A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0,
            "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, "P" : 0, "Q" : 0, "R" : 0,
            "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0}
    
    #print(a)
    #print(len(a))
    for i in range(len(a)):
    	#print(a[i])
    	if a[i] in dic:
    		dic[a[i]] += 1
    		#print(a , "puls 1")
    
    for j in dic:
    	if dic[j] == 0:
    		continue
    	else: 
    		print(j, dic[j])
    		dic[j] -= 1
#print("first")
frequency_analytic("PangolinPartyPRO");

#print("second")
#frequency_analytic("PangolinPartyPRO");
