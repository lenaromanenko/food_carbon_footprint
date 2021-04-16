from flask import Flask, render_template, make_response, jsonify, request
from recommender import get_recommendation, products_df_parser
import pandas as pd
import numpy as np
import random
import os

app = Flask(__name__)

@app.route('/product') # decorator
def recommend():
    user_input = dict(request.args) # this is the data that was assembled by the form
    user_input
    p1 = user_input['product1']
    products = products_df_parser()
    try:
        e1 = products.loc[p1, 'Total_emissions'].round(1)
        u1 = products.loc[p1, 'picture_file_name']
        u1 = 'https://foodb.ca/system/foods/pictures/'+ u1[:-4] +'/full/' + u1[:-4] + '.png'
        km1 = e1/0.1281 # The average carbon emissions of cars manufactured by German OEMs rose slightly by 0.7 per cent compared to 2016 and reached 128.1 g CO2 per km.
        km1 = km1.round(1)
        plane1 =(e1 / 90 * 60).round(1)  # 90kg CO2 = 60 min of flight #plane
        d1 = products.loc[p1, 'description'] # description
        w1 = products.loc[p1, 'Freshwater_withdrawals_l_per_kg']  # water 
        l1 = products.loc[p1, 'Land_use_m2_per_kg'] # land usage
        cat1 = products['food_subgroup'][p1] # category of the selected product
        cat1 = cat1.lower()

        if float(e1) <= 3.5:
            c1 = '🟢'
        if 3.5 < float(e1) <= 7:
            c1 = '🟡'
        if float(e1) > 7:
            c1 = '🔴'

        predicted_food = get_recommendation(user_input)[0]       
        return render_template('product.html', predicted_food = predicted_food, p1 = p1, e1 = e1, c1 =  c1, u1 = u1, km1 = km1, cat1 = cat1, d1=d1, w1=w1, l1=l1, plane1=plane1) 
    except KeyError: 
        return render_template("main_page.html")  

# 3rd page
@app.route('/recommender')
def new_recommend():
    user_input = dict(request.args) 
    user_input
    p1 = user_input['product2']
    products = products_df_parser()
    e1 = products.loc[p1, 'Total_emissions'].round(1)
    u1 = products.loc[p1, 'picture_file_name']
    u1 = 'https://foodb.ca/system/foods/pictures/'+ u1[:-4] +'/full/' + u1[:-4] + '.png'
    km1 = e1/0.1281 
    km1 = km1.round(1)
    plane1 =(e1 / 90 * 60).round(1) 
    d1 = products.loc[p1, 'description'] 
    w1 = products.loc[p1, 'Freshwater_withdrawals_l_per_kg'] 
    l1 = products.loc[p1, 'Land_use_m2_per_kg']
    cat1 = products['food_subgroup'][p1] 
    cat1 = cat1.lower()

    if float(e1) <= 3.5:
        c1 = '🟢'
    if 3.5 < float(e1) <= 7:
        c1 = '🟡'
    if float(e1) > 7:
        c1 = '🔴'    

    return render_template('recommender.html', p1 = p1, e1 = e1, c1 = c1, u1 = u1, km1 = km1, cat1 = cat1, d1=d1, w1=w1, l1=l1, plane1=plane1) 

@app.route('/')
def main_page():
    return render_template('main_page.html')

if __name__ == "__main__": 
    app.run()