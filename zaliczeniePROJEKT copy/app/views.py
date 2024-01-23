from django.shortcuts import render
from django.http import HttpResponse
from .forms import FuelCalculationForm

# Funkcja calculate_distance z uwzględnieniem dodatkowych wyborów
def calculate_distance(route_choice, selected_additional_stops):
    distances = {'1': 360, '2': 370, '3': 410}
    additional_distance = len(selected_additional_stops) * 50
    total_distance = distances.get(route_choice, 0) + additional_distance
    return total_distance

# Funkcje do obliczeń
def calculate_fuel_needed(distance, fuel_consumption):
    return (distance / 100) * fuel_consumption

def calculate_refueling_count(fuel_needed, tank_capacity):
    return fuel_needed / tank_capacity + 1

# Funkcja do wyznaczania najoptymalniejszej stacji paliwowej
def find_optimal_station(route_choice, remaining_distance, stations):
    if not remaining_distance:
        return min(stations[route_choice], key=stations[route_choice].get)

    for station in stations[route_choice]:
        if stations[route_choice][station] <= remaining_distance:
            return station

    # Jeśli nie znaleziono odpowiedniej stacji, wybierz najbliższą
    return min(stations[route_choice], key=stations[route_choice].get)


def fuel_calculation(request):
    form = FuelCalculationForm()
    selected_stops = []

    if request.method == 'POST':
        form = FuelCalculationForm(request.POST)

        if form.is_valid():
            vehicle_type = form.cleaned_data['vehicle_type']
            route_choice = form.cleaned_data['route_choice']

            if not vehicle_type:
                return HttpResponse("Proszę wybrać rodzaj pojazdu.")
            fuel_consumption, tank_capacity = 0, 0

            if vehicle_type == 'TIR':
                fuel_consumption, tank_capacity = 30, 600
            elif vehicle_type == 'Samochod dostawczy':
                fuel_consumption, tank_capacity = 15, 50
           

            selected_additional_stops = request.POST.getlist('stop')

            distance = calculate_distance(route_choice, selected_additional_stops)
            fuel_needed = calculate_fuel_needed(distance, fuel_consumption)
            refueling_count = calculate_refueling_count(fuel_needed, tank_capacity)

            remaining_distance = tank_capacity - (distance % tank_capacity)

            stations = {
                '1': {'W1 Orlen': 328, 'W2 Mol': 263, 'W3 Shell': 100},
                '2': {'K1 Mol': 225, 'K2 Shell': 90, 'K3 Mol': 155},
                '3': {'G1 Shell': 359, 'G2 Mol': 295, 'G3 BP': 260},
            }

            optimal_station = find_optimal_station(route_choice, remaining_distance, stations)

            return render(request, 'result.html', {
                'form': form,
                'selected_stops': selected_stops,
                'fuel_needed': fuel_needed,
                'refueling_count': refueling_count,
                'selected_additional_stops': selected_additional_stops,
                'total_distance': distance,
                'optimal_station': optimal_station,
                'route_choice': route_choice,
            })

    return render(request, 'index.html', {'form': form, 'selected_stops': selected_stops})

