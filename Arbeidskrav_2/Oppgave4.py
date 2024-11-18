data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

land = input("Skriv inn et land:")


if(land in data):
    print(f"{data[land][0]} er hovedstaden i {land} og det er {data[land][1]} mill. innbyggere i {data[land][0]}.")
else:
    print(f"Fant ikke {land} i databasen.")
    hovedstad = input(f"Skriv inn hovedstaden i {land}:")
    innbyggere = float(input(f"Skriv inn antall innbyggere i {hovedstad} i mill. :"))
    data[land] = [hovedstad, innbyggere]
    print(f"Data for {land} er lagt til i databasen.")
    print(data)
