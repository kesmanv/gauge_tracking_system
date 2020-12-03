import dash_table
import pandas as pd
from database import transforms as tf

cols = ['Gage ID', 'Description', 'Gage S/N', 'Asset No', 'Current Location', 'Manufacturer'
        ,'Last Calibrated By', 'Last Cal Date', 'Next Due Date']


# Table records
gauge_table = dash_table.DataTable(
                                            #,
                                            id='gauge-table' 
                                            ,columns=[{'name': i, 'id': i} for i in tf.df.columns]
                                            ,data = tf.df.to_dict('rows')
                                            # ,columns=[
                                            #             {'name':'Plant'
                                            #             ,'id':'Plant'}
                                            #             ,{'name': 'Gauge ID'
                                            #             ,'id': 'Gage ID'
                                            #             }, {
                                            #                 'name':'Description'
                                            #                 ,'id': 'Description'
                                            #             }, {
                                            #                 'name':'Gauge S/N'
                                            #                 ,'id': 'Gage S/N'
                                            #             }, {
                                            #                 'name':'Asset No'
                                            #                 ,'id': 'Asset No'
                                            #             }, {
                                            #                 'name':'Model No.'
                                            #                 ,'id': 'Model No.'
                                            #             },{
                                            #                 'name':'Current Location'
                                            #                 ,'id': 'Current Location'
                                            #             }, {
                                            #                 'name':'Manufacturer'
                                            #                 ,'id': 'Manufacturer'
                                            #             }, {
                                            #                 'name':'Last Calib By'
                                            #                 ,'id': 'Last Calibrated By'
                                            #             } , {
                                            #                 'name':'Last Calib Date'
                                            #                 ,'id': 'Last Cal Date'
                                            #             }, {
                                            #                 'name':'Next Due Date'
                                            #                 ,'id': 'Next Due Date'
                                            #                 ,'type': 'datetime'
                                            #             }
                                            #         ]
                                            # ,style_cell_conditional=[
                                            #     {'if': {'column_id':'Plant'}, 'width':'80%'}
                                            #     ,{'if': {'column_id':'Gauge ID'}, 'width':'210%'}
                                            #     ,{'if': {'column_id':'Description'}, 'width':'10%'}
                                            #     ,{'if': {'column_id':'Gage S/N'}, 'width':'2%'}
                                            #     ,{'if': {'column_id':'Asset No'}, 'width':'2%'}
                                            #     ,{'if': {'column_id':'Current Location'}, 'width':'2%'}
                                            #     ,{'if': {'column_id':'Manufacturer'}, 'width':'2%'}
                                            #     ,{'if': {'column_id':'Last Calibrated By'}, 'width':'10%'}
                                            #     ,{'if': {'column_id':'Last Cal Date'}, 'width':'2%'}
                                            #     ,{'if': {'column_id':'Next Due Date'}, 'width':'2%'}
                                            # ]
                                            )