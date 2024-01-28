import math

def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Test the function
kilometers = 10
miles = km_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles.")