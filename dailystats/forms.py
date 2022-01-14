from django import forms
import country_converter as coco
cc = coco.CountryConverter()
allCountries = cc.get_correspondence_dict('ISO3', 'name_short')
countryChoices = [(short, country[0]) for short, country in allCountries.items()]

class countrySelectForm(forms.Form):
    country = forms.ChoiceField(label='Country', 
    choices=countryChoices,
    required=False,
    )
