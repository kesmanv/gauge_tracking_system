import dash_table
import pandas as pd
from database import transforms as tf

cols = ['Gage ID', 'Description', 'Gage S/N', 'Asset No', 'Current Location', 'Manufacturer'
        ,'Last Calibrated By', 'Last Cal Date', 'Next Due Date']


# Table records
# gauge_table = dash_table.DataTable(
                                            
#                                 id='gauge-table' 
#                                 ,data = tf.df.to_dict('rows')
#                                 ,columns=[
#                                         {'name':'Plant'
#                                         ,'id':'Plant'}
#                                         ,{'name': 'Gauge ID'
#                                         ,'id': 'Gage ID'
#                                         }, {
#                                                 'name':'Description'
#                                                 ,'id': 'Description'
#                                         }, {
#                                                 'name':'Gauge S/N'
#                                                 ,'id': 'Gage S/N'
#                                         }, {
#                                                 'name':'Asset No'
#                                                 ,'id': 'Asset No'
#                                         }, {
#                                                 'name':'Model No.'
#                                                 ,'id': 'Model No.'
#                                         },{
#                                                 'name':'Current Location'
#                                                 ,'id': 'Current Location'
#                                         }, {
#                                                 'name':'Manufacturer'
#                                                 ,'id': 'Manufacturer'
#                                         }, {
#                                                 'name':'Last Calibration By'
#                                                 ,'id': 'Last Calibrated By'
#                                         } , {
#                                                 'name':'Last Calibration Date'
#                                                 ,'id': 'Last Cal Date'
#                                         }, {
#                                                 'name':'Next Due Date'
#                                                 ,'id': 'Next Due Date'
#                                                 ,'type': 'datetime'
#                                         }
#                                         ]
#                                         ,page_size=20
#                                         ,style_cell_conditional=[
#                                                                 {'if': {'column_id':'Plant'}, 'width':'60px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Gage ID'}, 'width':'100px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Description'}, 'width':'280px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Gage S/N'}, 'width':'120px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Asset No'}, 'width':'80px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Model No.'}, 'width':'80px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Current Location'}, 'width':'140px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Manufacturer'}, 'width':'100px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Last Calibrated By'}, 'width':'180px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Last Cal Date'}, 'width':'170px', 'textAlign':'center'}
#                                                                 ,{'if': {'column_id':'Next Due Date'}, 'width':'130px', 'textAlign':'center'}
#                                         ]
#                                         ,style_header={'fontWeight':'bold'}
#                                         ,sort_action='native' 
#                                         #,editable=True
#                                         #,filter_action='native'
#                                         # ,style_data_conditional=[{
#                                         #         'if':{
#                                         #                 'filter_query':'{Due Soon} contains "Yes"'
#                                         #         }, 'column_id':'Plant', 'backgroundColor':'#ffeeb2'
#                                         # }]

                                                
                                         
# )

# gauge_table_updated = dash_table.DataTable(
#         id = 'gauge-table-updated'
# )

