import pandas as pd
import math

def group_by_date(df):
    return(pd.Series(data= df.groupby('CheckIn')['Price'].mean()))

def price_format(dtafrm):
    return(dtafrm['Price'].str.replace('$','').astype(float))

def bathrooms_int(dtafrm):
    for i, j in zip(dtafrm['Bathrooms_num'],range(len(dtafrm))):
        if(str(i)=='nan'):
            dtafrm['Bathrooms_num_int'][j]= None
        elif('Half' in str(i) or 'half' in str(i)):
            dtafrm['Bathrooms_num_int'][j]= 0.5
        else:
            dtafrm['Bathrooms_num_int'][j]= float(i.split(' ')[0])
    return(dtafrm['Bathrooms_num_int'])

def beds_int(dtafrm):
    for i, j in zip(dtafrm['Beds_no'],range(len(dtafrm))):
        if(str(i)=='nan'):
            dtafrm['Beds_int'][j]= None
        elif('BREAKFAST' in str(i) or 'breakfast' in str(i)):
            dtafrm['Beds_int'][j]= float(1)
        elif(str(i)== 'Obed'):
            dtafrm['Beds_int'][j]= float(0)
        else:
            dtafrm['Beds_int'][j]= float(i.split(' ')[0])
    return(dtafrm['Beds_int'])        
    

def shared_bathroom(dtafrm):
    temp=[]
    for i in dtafrm['Bathrooms_num']:
        temp.append ('shared' in str(i))
    return(temp)
    
def super_host(dtafrm):
    dtafrm['Super_host']=[isinstance(x, str) for x in dtafrm.Super_host]
    return(dtafrm['Super_host'].map({False:0,True:1}))

def num_of_stars(Rev):
    for i in range(len(Rev)):
        Rev[i]=float(Rev[i].split(' ')[1])    
    return(Rev)
    
            
   
    
   
