#!/usr/bin/env python3
import sys
# Initalise all variables 
M_curr=None
N_curr=None
X_curr=None
currenti=None
currentj=None
current_val = 0


for line in sys.stdin:
   
    i,k,j,Matrix,val = line.strip().split('\t')

    try:
        Matrix=int(Matrix)
        i=int(i)
        k=int(k)
        j=int(j)
        val=int(val)
    except:
        # int was not a number, so silently
        # ignore/discard this line
       break

    # As hadoop sorts mapper outputs by key values , each M value for position (i,k) should be followed
    # by its corresponding N value 

    # ONLY STORES THE 1 MAPPER OUTPUT FOR EACH MATRIX --> NO 2D arrays as that would be to computationaly intensive 
    if Matrix == 1:
        M_curr = [i,k,j,val]
    if Matrix == 2:
        N_curr = [i,k,j,val]
    if Matrix == 3:
        X_curr = [i,k,j,val]

    
    if M_curr:
        if N_curr: 


            if X_curr: 
                if X_curr[0] ==  currenti and X_curr[1] == currentj: #if X val (i,k) corresponds to the previous M vals then it can be subtracted from the current value
                
                    current_val =X_curr[3]-current_val
                    print("{0}\t{1}\t{2}".format(X_curr[0], X_curr[1],current_val))
                    # As X_val should be sorted after all required N and M values for position (i,k)
                    # all variables can be reset for the next i,k position
                    current_val = 0
                    currenti=None
                    currentj=None
                    M_curr=[0,0,0,0]
                   
            
            # Once M val and N val is defined , checks to see if i,k and j value are the same 
            if M_curr[0:3]==N_curr[0:3]:
                current_val += M_curr[3]*N_curr[3] # computes product of mij * njk and adds to current_val
                currenti=M_curr[0]
                currentj=M_curr[1]
       
        
            


    


 