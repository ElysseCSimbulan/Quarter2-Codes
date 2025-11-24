destinations = []

print("Please enter your 5 travel destinations:")

for i in range(5):
    place = input(f"Destination {i+1}: ")
    destinations. append (place)

print("Original Travel Itinerary:")
for i in range(5):
    print(f"{i+1}, {destinations[i]}")

print("Let's update your 2nd and 5th destinations.")

new_second = input( "Enter a new destination for position 2: ")
new_fifth = input("Enter a new destination for position 5: ")

destinations[1] = new_second
destinations [4] = new_fifth

print("\n Updated Travel Itinerary:")
for i in range (5):
    print(f"{i+1}, {destinations[i]}")