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
    d = [i.strip().title() for i in sys.argv[1].split(',')]
    for i in d:
        if not i:
            continue
        # print(i)
        a = capital_cities.get(states.get(i))
        if a is not None:
            # print(a)
            print(i,' is the capital of ',a)
            continue
        a = get_key_by_value(i, capital_cities); # O(n)
        b = get_key_by_value(a, states); # O(n)
        if b is not None:
            print(i,' is the capital of ',b)
            continue
        print(i, ' is neither a capital city nor a state')

if __name__ == '__main__':
    main()