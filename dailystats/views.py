from urllib import request, response
from django.shortcuts import render
import json, requests, math

from .forms import *

import country_converter as coco
cc = coco.CountryConverter()

datasrc = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.json"
defaultCountry = "United States"


def getHomepage(request):
    response = requests.get(datasrc)

    # countryData = response.json()['USA']

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = countrySelectForm(request.POST)
    else:
        form = countrySelectForm(initial={'max_number': 'USA'})

    # check whether it's valid:
    if form.is_valid():
        countryCode = form.cleaned_data.get('country')
    else:
        countryCode = "USA"
    
    countryName = coco.convert(names=[countryCode], to='name_short')

    error = ""

    response = requests.get(datasrc)
    if response.status_code != 200:
        error = "Data server is being weird."
        return render(request, 'homepage.html', {'error': error, 'form': form})

    dataBack = response.json()
    if countryCode not in dataBack.keys():
        error = f"No data available for {countryName}. Enter another country."
        return render(request, 'homepage.html', {'error': error, 'form': form})


    countryData = dataBack[countryCode]
    dailyCases = countryData['new_cases']
    dailyDeaths = countryData['new_deaths']


    return render(request, 'homepage.html', {'country': countryName, 'dailyCases': int(dailyCases), 'dailyDeaths': int(dailyDeaths), 'form': form})
