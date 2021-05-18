cities = ["adelaide","Alice springs","darwin","Melbourne","Sydney"]
with open("cities.txt",'w') as city_files:
    for city in cities:
        print(city,file=city_files)