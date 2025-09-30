# Function to calculate flight cost
def calculate_flight_cost(distance):
    return distance * 0.1  # Assuming $0.10 per unit distance

# Function to calculate hotel cost
def calculate_hotel_cost(days):
    return days * 50  # Assuming $50 per day

# Function to calculate total trip cost
def calculate_total_cost(distance, days):
    flight_cost = calculate_flight_cost(distance)
    hotel_cost = calculate_hotel_cost(days)
    total_cost = flight_cost + hotel_cost
    return total_cost, flight_cost, hotel_cost

# Main program
print("✈️ Welcome to the Travel Cost Calculator 🏖️")

    # Taking input from user
distance = float(input("Enter travel distance (in km or miles): "))
days = int(input("Enter number of days to stay: "))

    # Calculating total cost
total, flight_cost, hotel_cost = calculate_total_cost(distance, days)

    # Display results
print("\n--- Trip Cost Summary ---")
print(f"Flight cost: ${flight_cost:.2f}")
print(f"Hotel cost: ${hotel_cost:.2f}")
print(f"Total trip cost: ${total:.2f}")

