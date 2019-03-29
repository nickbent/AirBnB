import pandas as pd
import numpy as np

def group_by_date(dtafrm):
    
    '''accepts a dataframe, groups data by check_in date and returns the average price for each group '''
    
    return(pd.Series(data= dtafrm.groupby('CheckIn')['Price'].mean()))