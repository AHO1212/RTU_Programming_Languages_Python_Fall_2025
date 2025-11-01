import math


def circle_area(radius: float) -> float:
    """Return the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius * radius


if __name__ == "__main__":
    try:
        r = float(input("Enter radius: ").strip())
        print(f"Area: {circle_area(r):.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}")
