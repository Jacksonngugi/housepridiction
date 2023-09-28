from django.shortcuts import render,redirect
from django.contrib import messages
import pandas as pd
from classifier import labels
import numpy as np
import joblib


# Create your views here.

def index(request):

    if request.method == 'POST':
        landarea = request.POST['landarea']
        bedroom = request.POST['Bedroom']
        bathroom =request.POST['Bathroom']
        parking = request.POST['Parking']
        furnish = request.POST['furnish']
        mainroad = request.POST['mainroad']
        guest = request.POST['Guestroom']
        basement = request.POST['Basement']
        hotwater = request.POST['Hotwaterheating']
        aircondition = request.POST['Airconditioning']
        prefarea = request.POST['Prefarae']

        if ((bedroom == '') or (bedroom == '') or (parking == '') or (bathroom == '')):
            messages.info(request,'Fill all the fields first!!!')

            return redirect('index')
        else:
            df = pd.DataFrame({
    'mainroad':[mainroad],
    'guestroom':[guest],
    'basement':[basement],
    'hotwaterheating':[hotwater],
    'airconditioning':[aircondition],
    'prefarea':[prefarea],
    'furnishingstatus':[furnish],
    'area':[landarea],
    'bedrooms':[bedroom],
    'bathrooms':[bathroom],
    'parking':[parking]

})
        pred = labels(df)
        loaded_model = joblib.load('models.sav')

        price = np.around(loaded_model.predict(pred))

        return render (request,'index.html',{'price':price})

    else:
       return render(request,'index.html')
    
    
    return render(request,'index.html')
