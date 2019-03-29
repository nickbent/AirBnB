import pandas as pd
import math
from sklearn.preprocessing import MultiLabelBinarizer


def price_format(dtafrm):
    
    '''accepts a dataframe, remove the "$" sign and converts the price value type from string to numeric '''
    
    return(dtafrm['Price'].str.replace('$','').astype(float))


def bathrooms_int(dtafrm):
    
    ''' accepts a dataframe, cleans the "Bathrooms_num" string and converts it to numeric  '''
    
    for i, j in zip(dtafrm['Bathrooms_num'],range(len(dtafrm))):
        if(str(i)=='nan'):
            dtafrm['Bathrooms_num_int'][j]= None
        elif('Half' in str(i) or 'half' in str(i)):
            dtafrm['Bathrooms_num_int'][j]= 0.5
        else:
            dtafrm['Bathrooms_num_int'][j]= float(i.split(' ')[0])
    return(dtafrm['Bathrooms_num_int'])



def beds_int(dtafrm):
    
    '''accepts a dataframe, cleans the "Beds_no" string and converts it to numeric  ''' 
    
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

def bedrooms_int(dtafrm):
    
    '''accepts a dataframe, cleans the string of the "Bedrooms_int" value, returns a clean string '''
    
    for i,j in zip(dtafrm.Bedrooms_no,range(len(dtafrm))):
        if(str(i)== 'nan'):
            dtafrm['Bedrooms_int'][j]= None
        else:
            dtafrm['Bedrooms_int'][j] = i.split('bedroom')[0].split(' ')[-2]
    return(dtafrm['Bedrooms_int'])


def bedrooms_int_final(dtafrm):
    
    ''' accepts a dataframe, converts "Bedrooms_int" to numeric value '''
    
    for i in range(len(dtafrm)):
        if(dtafrm.Bedrooms_int[i]== None):
            dtafrm.Bedrooms_int[i]= 0
        else:
            dtafrm.Bedrooms_int[i]=int(dtafrm.Bedrooms_int[i])
    return(dtafrm.Bedrooms_int)
        
    

def shared_bathroom(dtafrm):
    
    ''' accepts a dataframe, returns a new varibale which indicates whether the corresponding Bathroom(s) is shared or not '''
    
    temp=[]
    for i in dtafrm['Bathrooms_num']:
        temp.append ('shared' in str(i))
    return(temp)
 
    
    
def super_host(dtafrm):
    
    ''' accepts a dataframe, returns a new varibale which indicates whether the corresponding host is "super host" or not '''
    
    dtafrm['Super_host']=[isinstance(x, str) for x in dtafrm.Super_host]
    return(dtafrm['Super_host'].map({False:0,True:1}))



def num_of_stars(dtafrm):
    
    ''' accepts a dataframe, loops through a list of reviews varibles, and returns a clean version of the number of stars '''
    
    for k in ['Accuracy_stars','CheckIn_stars','Cleanliness_stars','Communication_stars','Location_stars','Value_stars']:
        for i, j in zip(dtafrm[k],range(len(dtafrm))):
            if(str(i)=='nan'):
                dtafrm[k][j]= '0'
            else:
                dtafrm[k][j]= i.split(' ')[1]
            
    return(dtafrm)


def entire_shared_private_room(dtafrm):
    
    """
    
    accepts a dataframe,returns a new varibale which indicates whether the corresponding rent is for "Entire apartment" ,"shared room" or "private room" 
    
    """
    
    for i,j in zip(dtafrm['EntireHomeVsRoom'],range(len(dtafrm))):
        if(str(i)== 'nan'):
            dtafrm['shared_room'][j]= None  
        elif(('ENTIRE' in i) or ('Entire' in i) or ('Tiny house' in i) or ('TINY HOUSE' in i) or('Earth house' in i)):
            dtafrm['shared_room'][j]= 0
        elif(('SHARED' in i) or ('Shared' in i)):
            dtafrm['shared_room'][j]= 1
        else:
            dtafrm['shared_room'][j] = 2 
    return(dtafrm['shared_room'])



def bed_type(dtafrm):
    
    """
    accepts a dataframe, cleans the "Sleeping_engagment" variable and maps it to
    a new varibale "BedType" which indicates the type of the bed such as single, double, queen, etc 
    
    """
    
    for i,j in zip(dtafrm.Sleeping_engagment,range(len(dtafrm))):
        if(str(i)!= 'nan'):
            dtafrm['BedType'][j]=i.split(' ')[2]
    return(dtafrm['BedType'])

        
def amenities_to_vars(dtafrm):
    
    ''' accepts a dataframe, cleans the amenities string for each sample and returns the clean copy of the variable'''
    
    for i,j in zip(dtafrm.Amenities,range(len(dtafrm))):
        dtafrm['Amenities_mod'][j]= i.replace("[","").replace("'","").replace("]","").split(", ")
    return(dtafrm['Amenities_mod'])
    
    
def encode_amenities(dtafrm):
    
    '''accepts a dataframe, encode the amenities' strings as dummy varibles '''
    
    mlb = MultiLabelBinarizer()
    df = dtafrm.join(pd.DataFrame(mlb.fit_transform(dtafrm.pop('Amenities_mod')),columns=mlb.classes_, index= dtafrm.index))
    return(df)


            
   
     
   
