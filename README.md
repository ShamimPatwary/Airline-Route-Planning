# Airline Route Planning System ✈️

A Django-based web application that helps plan the shortest route between airports using **Dijkstra's algorithm**.  
The system allows administrators to manage airports and routes dynamically and provides users with an interactive interface to find optimal flight paths.

---

## Features

- **Shortest Path Finder**: Calculates the shortest route between two airports using Dijkstra's algorithm.
- **Airport Management**: Add, view, and delete airports.
- **Route Management**: Add, view, and delete routes between airports.
- **Dynamic Graph Construction**: Automatically builds a weighted graph based on the database.
- **Web Interface**: Simple and user-friendly interface built with Django templates.

---

## Why Dijkstra?

- All routes have **non-negative distances (km)** → Dijkstra is ideal.
- Only **single-source shortest path** is required (one origin to one destination per query).
- **Faster for sparse graphs** (`O((V + E) log V)`) compared to:
  - Bellman–Ford → `O(V * E)` (slower, used for graphs with negative weights).
  - Floyd–Warshall → `O(V³)` (computes all-pairs, unnecessary overhead).

---

## Project Structure
```
airline_route_planning/
│
├── airline_route_planning/ # App configuration files
│ ├── admin.py # Admin panel registration
│ ├── apps.py # App configuration class
│ ├── forms.py # AirportForm & RouteForm
│ ├── models.py # Airport & Route models
│ ├── services.py # RoutePlanner with Dijkstra
│ ├── urls.py # URL routes
│ ├── views.py # View functions
│ ├── templates/ # HTML templates
│ │ ├── index.html
│ │ ├── manage_airports.html
│ │ ├── manage_routes.html
│ │ └── home.html
│
└── manage.py # Django project runner
```
---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/airline-route-planner.git
   cd airline-route-planner
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run migrations:**
    ```bash
    python manage.py migrate

5. **Start the server:**
    ```bash
    python manage.py runserver


## Usage

- Open the web app.

- Add airports with their code, name, latitude, and longitude.

- Add routes between airports with distance (km).

- Select origin and destination airports.

- Click Find Route → Shortest path will be displayed.


## Example

**Airports:**

DAC – Dhaka

CGP – Chittagong

ZYL – Sylhet

**Routes:**

DAC → CGP: 250 km

DAC → ZYL: 230 km

ZYL → CGP: 200 km

Query: Dhaka → Chittagong

Result: Dhaka → Sylhet → Chittagong (430 km)


## Technologies Used

- Python 3.x

- Django

- MySQL

- HTML, CSS (Django templates)

## Future Enhancements

- Visual map-based route planner.

- Flight cost optimization.

- Real-time API integration for airports.

- Multi-stop route planning.
