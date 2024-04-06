import sys

def print_capital_city():
    if len(sys.argv) != 2:
        sys.exit(0)
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    print(capital_cities.get(states.get(sys.argv[1]), 'Unknown state'))

if __name__ == '__main__':
    print_capital_city()