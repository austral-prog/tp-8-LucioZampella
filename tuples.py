"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]
print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))


def convert_coordinate(coordinate):
   a, b = coordinate
   return(a, b)
print(convert_coordinate("2A"))


def create_record(azara_record, rui_record):
    combined_record = azara_record + rui_record
    rui_coordinate = rui_record[1][0] + rui_record[1][1]
    azara_coordinate = azara_record[1]
    
    if rui_coordinate == azara_coordinate:
        return combined_record
    else:
        return "not a match"
print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
