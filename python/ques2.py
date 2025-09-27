# A travel agency wants to calculate trip costs. Write functions for:
# - Calculating flight cost (based on distance)
# - Calculating hotel cost (based on days of stay)
# - A main function that combines both to show the final cost.

def calculate_flight_cost(distance):
    return distance * 0.1  # Assuming $0.10 per unit distance

def calculate_hotel_cost(days):
    return days * 50  # Assuming $50 per day

def calculate_total_cost(distance, days):
    flight_cost = calculate_flight_cost(distance)
    hotel_cost = calculate_hotel_cost(days)
    return flight_cost + hotel_cost

# Example usage
distance = 500
days = 3
total = calculate_total_cost(distance, days)
print("Flight cost:", calculate_flight_cost(distance))
print("Hotel cost:", calculate_hotel_cost(days))
print("Total trip cost:", total)