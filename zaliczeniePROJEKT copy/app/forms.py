from django import forms
from django import forms
VEHICLE_CHOICES = [
    ('', 'Wybierz rodzaj pojazdu'),  # Opcja braku wyboru
    ('TIR', 'TIR'),
    ('Samochod dostawczy', 'Samochod dostawczy'),]

class FuelCalculationForm(forms.Form):
    vehicle_type = forms.ChoiceField(choices=[('TIR', 'TIR'), ('Samochod dostawczy', 'Samochod dostawczy')])
    route_choice = forms.ChoiceField(choices=[('1', 'Wroclaw'), ('2', 'Krakow'), ('3', 'Gdansk')])
    vehicle_type = forms.ChoiceField(choices=VEHICLE_CHOICES, required=False)
    def set_stops_choices(self):
        route_choice = self.cleaned_data['route_choice']
        additional_stops = []

        if route_choice == '1':
            additional_stops = [('lodz', 'Łódź'), ('kalisz', 'Kalisz')]
        elif route_choice == '2':
            additional_stops = [('radom', 'Radom'), ('kielce', 'Kielce')]
        elif route_choice == '3':
            additional_stops = [('lodz', 'Łódź'), ('torun', 'Toruń')]

        return additional_stops
