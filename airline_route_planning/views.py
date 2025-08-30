from django.shortcuts import render, redirect, get_object_or_404
from .models import Airport, Route
from .forms import AirportForm, RouteForm
from .services import RoutePlanner


def index(request):
    airports = Airport.objects.all()
    path = []
    if request.method == 'POST' and 'from' in request.POST:
        from_code = request.POST['from']
        to_code = request.POST['to']
        planner = RoutePlanner()
        path = planner.get_path(from_code, to_code)
    return render(request, 'index.html', {'airports': airports, 'path': path})


def manage_airports(request):
    airports = Airport.objects.all()
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('manage_airports')
    return render(request, 'manage_airports.html', {'form': form, 'airports': airports})

def delete_airport(request, code):
    airport = get_object_or_404(Airport, code=code)
    airport.delete()
    return redirect('manage_airports')


def manage_routes(request):
    form = RouteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('manage_routes')

    routes = Route.objects.all()
    return render(request, 'manage_routes.html', {
        'form': form,
        'routes': routes
    })


def delete_route(request, id):
    route = get_object_or_404(Route, id=id)
    route.delete()
    return redirect('manage_routes')

def home(request):
    airports = Airport.objects.all()
    path = None

    if request.method == "POST":
        from_code = request.POST.get("from")
        to_code = request.POST.get("to")

        planner = RoutePlanner()
        route_codes = planner.get_path(from_code, to_code)

        # Convert each code to its airport name (uppercase)
        path = [
            Airport.objects.get(code=code).name.upper()
            for code in route_codes
        ]

    return render(request, "home.html", {
        "airports": airports,
        "path": path
    })
