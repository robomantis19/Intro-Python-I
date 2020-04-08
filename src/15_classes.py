# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon: 
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon): 
    def method(self, name):
        super().method(lat, lon)
        self.name = name

# YOUR CODE HERE
class Family: 
    def __init__(self, greeting, present):
        self.greeting = greeting 
        self.present = present

        def printline(): 
            print(self.greeting, " here's your ", self.present)
        
values = Family('hello there', 'birthday cake')
print(values.greeting, values.present)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(LatLon): 
    def method2(self, difficulty, size):
        super().method2(name, lat, lon)
        self.difficulty = difficulty
        self.size = size


# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
value = Waypoint("Catacombs", 41.7050, -121.51521)

print(value)
# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)
