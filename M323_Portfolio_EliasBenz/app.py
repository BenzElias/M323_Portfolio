from flask import Flask, jsonify, render_template, send_from_directory
from functools import reduce

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/grundlagen')
def grundlagen():
    pdf_documents = [
        'Lernnachweis_A1G_EliasBenz.pdf',
        'Lernnachweis_B1G_EliasBenz.pdf',
        'Lernnachweis_B2G_EliasBenz.pdf',
        'Lernnachweis_B3G_EliasBenz.pdf',
        'Lernnachweis_B4G_EliasBenz.pdf',
        'Lernnachweis_C1G_C1F_C1E_EliasBenz.pdf']

    return render_template('grundlagen.html', pdf_documents=pdf_documents)


@app.route('/fortgeschritten')
def fortgeschritten():
    pdf_documents = [
        'Lernnachweis_A1F_EliasBenz.pdf',
        'Lernnachweis_B1F_EliasBenz.pdf',
        'Lernnachweis_B2F_EliasBenz.pdf',
        'Lernnachweis_B3F_EliasBenz.pdf',
        'Lernnachweis_B4F_EliasBenz.pdf',
        'Lernnachweis_C1G_C1F_C1E_EliasBenz.pdf']
    return render_template('fortgeschritten.html', pdf_documents=pdf_documents)


@app.route('/erweitert')
def erweitert():
    pdf_documents = [
        'Lernnachweis_A1E_EliasBenz.pdf',
        'Lernnachweis_B1E_EliasBenz.pdf',
        'Lernnachweis_B2E_EliasBenz.pdf',
        'Lernnachweis_B3E_EliasBenz.pdf',
        'Lernnachweis_B4E_EliasBenz.pdf',
        'Lernnachweis_C1G_C1F_C1E_EliasBenz.pdf']
    return render_template('erweitert.html', pdf_documents=pdf_documents)


@app.route('/open_pdf/<path:pdf_name>')
def open_pdf(pdf_name):
    return send_from_directory('static/pdf', pdf_name)


# Funktion zum Hinzufügen von Zahlen
def add_numbers(a, b):
    return a + b


# Route für die Summe von 3 und 5
@app.route('/addition')
def addition():
    result = add_numbers(3, 5)
    return f'Die Summe ist {result}'


# Route für Koordinaten
@app.route('/coordinates')
def get_coordinates():
    coordinates = (3, 5)
    # Änderung führt zu einem Fehler
    # coordinates[0] = 2
    return jsonify({'coordinates': coordinates})


# Klasse für Formen
class Shape:
    def area(self):
        pass


# Klasse für einen Kreis, erbt von Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Route für die Fläche eines Kreises mit gegebenem Radius
@app.route('/circle_area/<float:radius>')
def get_circle_area(radius):
    circle = Circle(radius)
    return jsonify({'area': circle.area()})


# Beispielgraph für Dijkstra-Algorithmus
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}


# Dijkstra-Algorithmus
def dijkstra(graph, start):
    # Implementierung des Algorithmus
    pass


# Route für Dijkstra-Algorithmus
@app.route('/dijkstra/<start_node>')
def get_shortest_paths(start_node):
    shortest_paths = dijkstra(graph, start_node)
    return jsonify({'shortest_paths': shortest_paths})


# Merge-Sort-Beispiel
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Teilung
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Rekursive Sortierung
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Vereinigung
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Route für Merge-Sort
@app.route('/merge_sort')
def get_sorted_list():
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    return jsonify({'sorted_list': sorted_arr})


# Suche nach Benutzern
def search_users(users, criteria):
    results = []
    for user in users:
        if criteria(user):
            results.append(user)
    return results


# Sortiere Benutzer nach Namen
def sort_users_by_name(users):
    return sorted(users, key=lambda user: user['name'])


# Beispielbenutzer
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]

# Suche nach Benutzern über 25 und sortiere nach Namen
criteria_function = lambda user: user['age'] > 25
searched_users = search_users(users, criteria_function)
sorted_users = sort_users_by_name(searched_users)


# Route für Suche und Sortierung von Benutzern
@app.route('/search_and_sort_users')
def get_search_and_sort_results():
    return jsonify({'search_results': searched_users, 'sorted_results': sorted_users})


# Beispiel für Funktionen als Objekte und Argumente
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def apply_operation(operation, x, y):
    return operation(x, y)


result_addition = apply_operation(add, 5, 3)
result_subtraction = apply_operation(subtract, 10, 4)


# Route für Funktionen als Objekte und Argumente
@app.route('/apply_operations')
def get_operations_results():
    return jsonify({'addition_result': result_addition, 'subtraction_result': result_subtraction})


# Filtern von Zahlen
def filter_numbers(numbers, condition):
    return [num for num in numbers if condition(num)]


# Beispiel für Verwendung von Funktionen als Argumente
even_numbers = filter_numbers([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
positive_numbers = filter_numbers([-2, -1, 0, 1, 2], lambda x: x > 0)


# Route für Funktionen als Argumente
@app.route('/filter_numbers')
def get_filtered_numbers():
    return jsonify({'even_numbers': even_numbers, 'positive_numbers': positive_numbers})


# Erstellen von Loggern mit Closures
def create_logger(prefix):
    def logger(message):
        print(f'{prefix}: {message}')

    return logger


log_info = create_logger('INFO')
log_error = create_logger('ERROR')

# Beispiel-Logs
log_info('Anwendung gestartet.')
log_error('Fehler bei der Datenbankverbindung.')

# Lambda-Ausdrücke für einfache Operationen
square = lambda x: x ** 2
uppercase = lambda s: s.upper()

# Beispiel für Anwendung von Lambda-Ausdrücken
result_square = square(5)
result_uppercase = uppercase('hello')


# Route für Lambda-Ausdrücke
@app.route('/lambda_expressions')
def get_lambda_results():
    return jsonify({'square_result': result_square, 'uppercase_result': result_uppercase})


# Lambda-Ausdrücke für mehrere Argumente
sort_tuples = lambda tuples, key: sorted(tuples, key=lambda x: x[key])

# Beispiel für Anwendung von Lambda-Ausdrücken
data = [(1, 'apple'), (3, 'orange'), (2, 'banana')]
sorted_data = sort_tuples(data, key=0)


# Route für Lambda-Ausdrücke mit mehreren Argumenten
@app.route('/lambda_expressions_multiple_arguments')
def get_lambda_multiple_arguments_results():
    return jsonify({'sorted_data': sorted_data})


# Lambda-Ausdrücke zur Steuerung des Programmflusses
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Sortieren der Liste basierend auf dem Alter
sorted_by_age = sorted(data, key=lambda x: x['age'])

# Sortieren der Liste basierend auf dem Namen
sorted_by_name = sorted(data, key=lambda x: x['name'])


# Route für Lambda-Ausdrücke zur Steuerung des Programmflusses
@app.route('/lambda_expressions_control_flow')
def get_lambda_control_flow_results():
    return jsonify({'sorted_by_age': sorted_by_age, 'sorted_by_name': sorted_by_name})


# Funktionen Map, Filter, Reduce zur Datenverarbeitung
numbers = [1, 2, 3, 4, 5]

# Map zur Quadrierung
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Filter für gerade Zahlen
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce für die Summe
sum_all_numbers = reduce(lambda x, y: x + y, numbers)


# Route für Map, Filter, Reduce
@app.route('/map_filter_reduce')
def get_map_filter_reduce_results():
    return jsonify(
        {'squared_numbers': squared_numbers, 'even_numbers': even_numbers, 'sum_all_numbers': sum_all_numbers})


# Kombinierte Anwendung von Map, Filter und Reduce auf Personenliste
people = [
    {'name': 'Alice', 'age': 30, 'salary': 50000},
    {'name': 'Bob', 'age': 25, 'salary': 60000},
    {'name': 'Charlie', 'salary': 70000}  # Kein 'age'-Schlüssel hier
]

# Kombinierte Anwendung von Map, Filter und Reduce
processed_data = reduce(
    lambda acc, person: acc + person.get('age', 0) if person.get('age', 0) > 25 else acc,
    filter(
        lambda person: 'age' in person and person['age'] > 25,
        map(
            lambda person: {'name': person['name'], 'salary': person['salary'] * 1.1},
            people
        )
    ),
    0
)


# Route für kombinierte Anwendung von Map, Filter und Reduce auf Personenliste
@app.route('/combined_map_filter_reduce_people')
def get_combined_map_filter_reduce_people_results():
    return jsonify({'processed_data': processed_data})


# Kombinierte Anwendung von Map, Filter und Reduce auf Verkaufsdaten
sales_data = [
    {'product': 'Laptop', 'quantity': 10, 'price': 1200},
    {'product': 'Smartphone', 'quantity': 20, 'price': 800},
    {'product': 'Tablet', 'quantity': 15, 'price': 500}
]

# Verwendung von Map, Filter und Reduce für komplexe Datenverarbeitung
total_revenue = reduce(
    lambda acc, sale: acc + (sale['quantity'] * sale['price']),
    sales_data,
    0
)

average_price = reduce(
    lambda acc, sale: acc + sale['price'],
    sales_data,
    0
) / len(sales_data)


# Route für kombinierte Anwendung von Map, Filter und Reduce auf Verkaufsdaten
@app.route('/combined_map_filter_reduce_sales')
def get_combined_map_filter_reduce_sales_results():
    return jsonify({'total_revenue': total_revenue, 'average_price': average_price})
