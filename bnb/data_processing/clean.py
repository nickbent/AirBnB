import pandas as pd
import math
from sklearn.preprocessing import MultiLabelBinarizer


def price_format(dtafrm):
    
    '''accepts a dataframe, remove the "$" sign and converts the price value type from string to numeric '''
    
    return(dtafrm['Price'].str.replace('$','').astype(float))




def bathrooms_int(dtafrm):
    
    ''' accepts a dataframe, cleans the "Bathrooms_num" string and converts it to numeric  '''
    
    for j,num_bathrooms in enumerate(dtafrm['Bathrooms_num']):
        if(str(num_bathrooms)=='nan'):
            dtafrm['Bathrooms_num_int'][j]= -1
        elif('Half' in str(num_bathrooms) or 'half' in str(num_bathrooms)):
            dtafrm['Bathrooms_num_int'][j]= 0.5
        else:
            dtafrm['Bathrooms_num_int'][j]= float(num_bathrooms.split(' ')[0])
    return(dtafrm['Bathrooms_num_int'])



def beds_int(dtafrm):
    
    '''accepts a dataframe, cleans the "Beds_no" string and converts it to numeric  ''' 
    
    for j,beds_num in enumerate(dtafrm['Beds_no']):
        if(str(beds_num)=='nan'):
            dtafrm['Beds_int'][j]= -1
        elif('BREAKFAST' in str(beds_num) or 'breakfast' in str(beds_num)):
            dtafrm['Beds_int'][j]= float(1)
        elif(str(beds_num)== 'Obed'):
            dtafrm['Beds_int'][j]= float(0)
        else:
            dtafrm['Beds_int'][j]= float(beds_num.split(' ')[0])
    return(dtafrm['Beds_int']) 


def bedrooms_int(dtafrm):
    
    '''accepts a dataframe, cleans the string of the "Bedrooms_int" value, returns a clean string '''
    
    for j, bedrooms_num in enumerate(dtafrm.Bedrooms_no):
        if(str(bedrooms_num)== 'nan'):
            dtafrm['Bedrooms_int'][j]= -1
        else:
            dtafrm['Bedrooms_int'][j] = bedrooms_num.split('bedroom')[0].split(' ')[-2]
    return(dtafrm['Bedrooms_int'])


def bedrooms_int_final(dtafrm):
    
    ''' accepts a dataframe, converts "Bedrooms_int" to numeric value '''
    
    for n_bedrooms in dtafrm.Bedrooms_int:
        if(str(n_bedrooms) == 'nan'):
            n_bedrooms= 0
        else:
            n_bedrooms=int(n_bedrooms)
    return(dtafrm.Bedrooms_int)
        
    

def shared_bathroom(dtafrm):
    
    ''' accepts a dataframe, returns a new varibale which indicates whether the corresponding Bathroom(s) is shared or not '''
    temp = ['shared' in str(i) for i in dtafrm['Bathrooms_num']]
    return(temp)
 
    
    
    
def super_host(dtafrm):
    
    ''' accepts a dataframe, returns a new varibale which indicates whether the corresponding host is "super host" or not '''
    
    dtafrm['Super_host']=[isinstance(x, str) for x in dtafrm.Super_host]
    return(dtafrm['Super_host'].map({False:0,True:1}))

def reviews_num(dtafrm):
    
    ''' accepts a dataframe, exract the number of strings from the review string, returns a new variable of int datatype'''
    return([-1 if (str(i)=='nan' or i.split(' ')[0]=='No') else int(i.split(' ')[0])  for i in dtafrm['Review']])


def num_of_stars(dtafrm):
    
    ''' accepts a dataframe, loops through a list of reviews varibles, and returns a clean version of the number of stars '''
    
    for catog in ['Accuracy_stars','CheckIn_stars','Cleanliness_stars','Communication_stars','Location_stars','Value_stars']:
        for j,stars_num in enumerate(dtafrm[catog]):
            if(str(stars_num)=='nan'):
                dtafrm[catog][j]= '0'
            else:
                dtafrm[catog][j]= stars_num.split(' ')[1]
            
    return(dtafrm)


def entire_shared_private_room(dtafrm):
    
    """
    
    accepts a dataframe,returns a new varibale which indicates whether the corresponding rent is for "Entire apartment" ,"shared room" or "private room" 
    
    """
    
    for j,room_type in enumerate(dtafrm['EntireHomeVsRoom']):
        if(str(room_type)== 'nan'):
            dtafrm['shared_room'][j]= -1  
        elif(('ENTIRE' in room_type) or ('Entire' in room_type) or ('Tiny house' in room_type) or ('TINY HOUSE' in room_type) or('Earth house' in room_type)):
            dtafrm['shared_room'][j]= 0
        elif(('SHARED' in room_type) or ('Shared' in room_type)):
            dtafrm['shared_room'][j]= 1
        else:
            dtafrm['shared_room'][j] = 2 
    return(dtafrm['shared_room'])



def bed_type(dtafrm):
    
    """
    accepts a dataframe, cleans the "Sleeping_engagment" variable and maps it to
    a new varibale "BedType" which indicates the type of the bed such as single, double, queen, etc 
    
    """
    
    for j, bed in enumerate(dtafrm.Sleeping_engagment):
        if(str(bed)!= 'nan'):
            dtafrm['BedType'][j]= bed.split(' ')[2]
    return(dtafrm['BedType'])

def one_hot_encode_bedtype(dtafrm):
    return(dtafrm.join(pd.get_dummies(dtafrm.BedType)))

        
def amenities_to_vars(dtafrm):
    
    ''' accepts a dataframe, cleans the amenities string for each sample and returns the clean copy of the variable'''
    
    for j, amenity in enumerate(dtafrm.Amenities):
        dtafrm['Amenities_mod'][j]= amenity.replace("[","").replace("'","").replace("]","").split(", ")
    return(dtafrm['Amenities_mod'])
    
    
def encode_amenities(dtafrm):
    
    '''accepts a dataframe, encode the amenities' strings as dummy varibles '''
    
    mlb = MultiLabelBinarizer()
    df = dtafrm.join(pd.DataFrame(mlb.fit_transform(dtafrm.pop('Amenities_mod')),columns= mlb.classes_, index= dtafrm.index))
    return(df)


            
   
     
   
