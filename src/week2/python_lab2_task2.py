numbers = [3, 8, -2, 7, 0, -5, 10]

squares = [n**2 for n in numbers]
positives = [n for n in numbers if n > 0]
even_squares = {n**2 for n in numbers if n % 2 == 0}
cubes = {n: n**3 for n in numbers}

print("Numbers:", numbers)
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
