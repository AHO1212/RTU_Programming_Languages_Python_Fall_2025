temperatures = [15.5, 17.2, 16.8, 18.0, 19.4, 20.1, 21.3]
city_population = {
    "Riga": 605802,
    "Liepaja": 68745,
    "Ventspils": 34805,
    "Jelgava": 55672,
    "Daugavpils": 80630,
}

average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get)
smallest_city = min(city_population, key=city_population.get)
total_population = sum(city_population.values())

print(f"Average temperature: {average_temperature:.1f}°C")
print(f"Largest city: {largest_city} ({city_population[largest_city]})")
print(f"Smallest city: {smallest_city} ({city_population[smallest_city]})")
print(f"Total population: {total_population}")
