import pandas as pd 
from datetime import datetime, timedelta

# Dropdown options function
def drop_options(df_):
        return [{'label': i, 'value': i} for i in df_]

df = pd.read_csv('./database/data/gauges/Master_Gauge_List.csv')



#############################################################################################################################
######################## Filters 

plants = pd.read_csv('./database/data/plants.csv', index_col=False)
plant_names = plants['Plant Name']

gauge_types = df['Type'].dropna().unique()

gauge_manufacturer = df['Manufacturer'].dropna().unique()

# To be added
# gauge_rr
##########################################################################################################################
# Function to filter gauges by upcoming due date
# Returns list of due gauges for the table
# Returns gauge due by Manufacturer for a chart
# Returns gauges due by type for a chart 



def due_date_next(df=df, days=30):
    
     due_date = datetime.today() + timedelta(days=30)
    
     next_due_list = df.loc[df['Next Due Date'] < due_date].sort_values(by='Next Due Date')

     # Number of gauges due by manufacturer
     #due_manufacturers = next_due_list.Manufacturer.value_counts().reset_index().rename(columns={'index': 'Type', 'Type': 'No. Gauges'})

     # Number of gauges due by type
     #due_types = next_due_list.Type.value_counts().reset_index().rename(columns={'index': 'Type', 'Type': 'No. Gauges'})

     return next_due_list #, due_manufacturers, due_types



# Not sure I need all these columns, most of them are empty
drop = ['Service Date','Status','Calib Freq', 'Calibration_Frequency_UOM', 'Calibrator'
        , 'Storage Location'
        ,'Cost', 'User Defined', 'Owner', 'Notes', 'Average Cycles/Usage Per Day', 'Gage Frequency Adjusting Interval', 'AdjPlanCode']

df.drop(drop, axis=1, inplace=True)

# Converting dates to datetime objects
dates = [#'Service Date'
        'Last Cal Date'
        ,'Next Due Date']
df['Due Soon'] = 'No'
due_date = datetime.today() + timedelta(days=30)

for date in dates:
    df[date] = pd.to_datetime(df[date])
    if date=='Next Due Date':
        df.loc[df['Next Due Date'] < due_date, 'Due Soon'] = 'Yes'
    
    df[date] = df[date].dt.strftime('%Y-%m-%d')



gauge_by_mfg = df.Manufacturer.value_counts().reset_index()
gauge_by_mfg = gauge_by_mfg.rename(columns={'index':'Manufacturer', 
                        'Manufacturer': 'No. Gauge Due'}).sort_values(by='No. Gauge Due')

# gauge_by_type = df.Type.value_counts().reset_index()
# gauge_by_type = gauge_by_type.rename(columns={'index':'Type', 
#                         'Type': 'No. Gauge Due'}).sort_values(by='No. Gauge Due')

