from django.shortcuts import render
import pandas as pd
import numpy as np
import os
import pickle

regmodel = None
def loadpickle():
    return pickle.load(open(r'C:\Users\shant\PycharmProjects\carprice\index\models\regression_model.pkl','rb'))
regmodel = loadpickle()

# Create your views here.
def index(request):
    return render(request,'index/index.html')



def predict(request):
    if request.method == 'POST':
        temp = {}
        Year = int(request.POST.get('Year'))
        temp['Present_Price'] = float(request.POST.get('Showroom Price'))
        temp['Kms_Driven'] = int(request.POST.get('Kilometers Driven'))
        temp['Owner'] = int(request.POST.get('Owned'))
        temp['Year'] = 2020 - Year
        fuel_type = request.POST.get('fuel type')
        if fuel_type == 'Petrol':
            temp['Fuel_type_diesel'] = 0
            temp['Fuel_type_petrol'] = 1
        elif fuel_type == 'Diesel':
            temp['Fuel_type_diesel'] = 1
            temp['Fuel_type_petrol'] = 0
        else:
            temp['Fuel_type_diesel'] = 0
            temp['Fuel_type_petrol'] = 0

        dealer_or_individual = request.POST.get('dealer or individual')
        if (dealer_or_individual == 'Individual'):
            temp['Seller_Type_Individual'] = 1
        else:
            temp['Seller_Type_Individual'] = 0

        transmission_type = request.POST.get('transmission')
        if (transmission_type == 'Manual'):
            temp['Transmission_Manual'] = 1
        else:
            temp['Transmission_Manual'] = 0
    testdata = list(temp.values())
    prediction = regmodel.predict([testdata])[0]
    scoreval = round(prediction,2)
    if scoreval < 0:
        scoreval = 'Sorry the car value has depricated to the lowest and cannot be sold.'
    else:
        scoreval = str(scoreval) + " Lakhs."
    context = {'scoreval':scoreval}
    return render(request,'index/index.html', context)