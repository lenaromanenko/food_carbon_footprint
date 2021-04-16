# /usr/bin/env python
import pandas as pd
import numpy as np
import random
import os
from mysql.connector import MySQLConnection
import pymysql
from sqlalchemy import create_engine

def products_df_parser():
    USER = '...'
    HOST = '...' 
    PASSWORD = '...' 
    PORT = '...'
    DB = '...'

    engine = create_engine('mysql+pymysql://'+USER+':'+PASSWORD+'@'+HOST+':'+PORT+'/'+DB)
    products = pd.read_sql_query("SELECT * FROM food_merged", engine)
    products = products.drop(columns=["key"])
    products = products.set_index("name")
    return products

products = products_df_parser()

def get_recommendation(user_input: dict):   
    p1 = user_input['product1']
    chosen_subgroup = products['food_subgroup'][p1]
    pred = products.reset_index().copy()
    pred = pred[['food_subgroup', 'name', 'Total_emissions']].copy()
    pred = pred.groupby(['food_subgroup']).min()
    best_recommendation = pred['name'][chosen_subgroup]
    e2 = products.loc[best_recommendation, 'Total_emissions'].round(1)
    u2 = products.loc[best_recommendation, 'picture_file_name']
    u2 = 'https://foodb.ca/system/foods/pictures/' + u2[:-4] +'/full/' + u2[:-4] + '.png' 
    km2 = e2/0.1281 # The average carbon emissions of cars manufactured by German OEMs rose slightly by 0.7 per cent compared to 2016 and reached 128.1 g CO2 per km.
    km2 = km2.round(2)
    return (best_recommendation, e2, u2, km2)

if __name__ == '__main__':
    """ good place for test code """
    print('⚡️')
    predicted_food = get_recommendation()
    print(best_recommendation)