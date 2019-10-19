#print(chr(124))
#Ханов Дмитрий Сергеевич ИВТ 1 подгруппа 2
#Лабораторная работа 2
#Занятие: 12.09.2018

print("_"*13)
print(chr(124) + "  A  " + chr(124) + " !A  " + chr(124))
print("-"*13)

A = True;
B = True;

print(chr(124) + "  "+ 
str(int(A)) + "  "+ 
chr(124) + "  "+ str(int(not A)) + 
"  " + chr(124))
print("-"*13)

print(chr(124) + "  "+ 
str(int(not A)) + "  " + 
chr(124) + "  "+ str(int(A)) + 
"  " + chr(124))
print("-"*13)
#-----------------------------------------------

print("_"*19)

print(chr(124) + "  A  " + chr(124) + "  B  " + chr(124) 
+ "A V B" + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(not A)) + "  " + chr(124) + 
"  "+ str(int( not B)) + "  " + chr(124) 
+ "  " + str(int(not A or not B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(not A)) + "  " + chr(124) + 
"  "+ str(int(B)) + "  " + chr(124) 
+ "  " + str(int(not A or B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(A)) + "  " + chr(124) + 
"  "+ str(int(not B)) + "  " + chr(124) 
+ "  " + str(int(A or not B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(A)) + "  " + chr(124) + 
"  "+ str(int(B)) + "  " + chr(124) 
+ "  " + str(int(A or B)) + "  " + chr(124))
print("-"*18)

#-----------------------------------------------------------

print("_"*19)

print(chr(124) + "  A  " + chr(124) + "  B  " + chr(124) 
+ "A /\ B" + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(not A)) + "  " + chr(124) + 
"  "+ str(int( not B)) + "  " + chr(124) 
+ "  " + str(int(not A and not B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(not A)) + "  " + chr(124) + 
"  "+ str(int(B)) + "  " + chr(124) 
+ "  " + str(int(not A and B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(A)) + "  " + chr(124) + 
"  "+ str(int(not B)) + "  " + chr(124) 
+ "  " + str(int(A and not B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(A)) + "  " + chr(124) + 
"  "+ str(int(B)) + "  " + chr(124) 
+ "  " + str(int(A and B)) + "  " + chr(124))
print("-"*18)

#-----------------------------------------------------------
print("_"*19)

print(chr(124) + "  A  " + chr(124) + "  B  " + chr(124) 
+ "A -> B" + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(not A)) + "  " + chr(124) + 
"  "+ str(int( not B)) + "  " + chr(124) 
+ "  " + str(int(A or not B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(not A)) + "  " + chr(124) + 
"  "+ str(int(B)) + "  " + chr(124) 
+ "  " + str(int(A or B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(A)) + "  " + chr(124) + 
"  "+ str(int(not B)) + "  " + chr(124) 
+ "  " + str(int(not A or not B)) + "  " + chr(124))
print("-"*18)

print(chr(124) + "  " + str(int(A)) + "  " + chr(124) + 
"  "+ str(int(B)) + "  " + chr(124) 
+ "  " + str(int(not A or B)) + "  " + chr(124))
print("-"*18)

#-------------------------------------------------------
val = 3
res = (val**2)-1%10
print(res)


[repl](https://repl.it/@DmitriiKhanov/MedicalPinkAdministration)
