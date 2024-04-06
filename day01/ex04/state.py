import sys

def get_key_by_value(value, d=dict()):
    for k, v in d.items():
        if v == value:
            return k

def main():
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
    a = get_key_by_value(sys.argv[1], capital_cities); # O(n)
    b = get_key_by_value(a, states); # O(n)
    print(b if b else 'Unknown state')

if __name__ == '__main__':
    main()