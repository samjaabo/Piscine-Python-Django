def parse_file_to_dict(filename: str) -> dict:
    elements = {}
    with open(filename, 'r') as file:
        for line in file:
            element, properties = line.strip().split(' = ')
            properties_dict = {}
            for prop in properties.split(', '):
                key, value = prop.split(':')
                properties_dict[key] = value
            elements[element] = properties_dict
    return elements

def has_position(row: dict, position: int):
    for element, properties in row.items():
        if properties['position'] == str(position):
            return (element, properties)
    return ()
          
def generate_html_periodic_table(periodic_table: dict) -> None:
    table = '<!DOCTYPE html>\n<html>\n<head>\n<title>Periodic Table</title>\n</head>\n<body>\n'
    table += '<table>\n'
    # print(periodic_table)
    rows = []
    row = {}
    for element, properties in periodic_table.items():
        row[element] = properties
        if (properties['position'] == '17'):
            rows.append(row)
            row = {}
    for r in rows:
        # row = r.items()
        # print(r)
        # return 
        table += '<tr>\n'
        for c in range(18):
            e = has_position(r, c)
            if e:
                element, properties = e
                number = properties.get('number')
                small = properties.get('small')
                molar = properties.get('molar')
                electron = properties.get('electron')
                
                # print(element, type(properties))
                table += '<td style="border: 2px solid black; padding: 5px">\n'
                table += f'<h4>{element}</h4>\n'
                table += '<ul>\n'
                table += f'<li>No {number}</li>\n'
                table += f'<li>{small}</li>\n'
                table += f'<li>{molar}</li>\n'
                table += f'<li>{electron} electron</li>\n'
                table += '</ul>\n'
                table += '</td>\n'
            else:
                table += '<td style="border: 2px solid black; padding: 5px"></td>\n'
        table += '</tr>\n'
    table += '</table>\n</body>\n</html>'
    file = open('periodic_table.html', 'w')
    file.write(table)
    file.close()
    

def main():
    a = parse_file_to_dict('periodic_table.txt')
    generate_html_periodic_table(a)

if __name__ == '__main__':
    main()