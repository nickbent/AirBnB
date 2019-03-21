import pandas as pd

def group_by_date(df):
    return(pd.Series(data= df.groupby('CheckIn')['Price'].mean()))

def price_format(dtafrm):
    return(dtafrm['Price'].str.replace('$','').astype(float))
    
   
