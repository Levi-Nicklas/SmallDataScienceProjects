#Calculate all the idempotents in Z_12

#counts
sol_count=0
bad_count=0


#check values function
def checker(i,j,k,q):
    if ((i==(i**2+j*k)%12) and
        (j==(i*j+j*q)%12) and
        (k==(k*i+q*k)%12) and
        (q==(j*k+q**2)%12)):
        print( "("+str(i)+", "+
               str(j)+", "+
               str(k)+", "+
               str(q)+") "+" satisfies the condition e=e^2.")
        global sol_count
        sol_count+=1
    else:
        global bad_count
        bad_count+=1
                 

elements=list(range(0,12))
elements2=list(range(0,12))
elements3=list(range(0,12))
elements4=list(range(0,12))

for i in elements:
    for j in elements2:
        for k in elements3:
            for q in elements4:
                 checker(i,j,k,q)

print("Solutions: "+str(sol_count))
print("# of incorrects: "+str(bad_count))
   

