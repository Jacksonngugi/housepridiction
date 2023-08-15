from django.shortcuts import render,redirect
from django.contrib import messages
import pandas as pd
from classifier import labels
import numpy


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
        print(pred)
    else:
       return render(request,'index.html')
    
    
    return render(request,'index.html')
