import random
import math
import csv
import numpy as np

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

class Vehicle:
    Type = ["Motor", "GranMax"]
    Cooler = [0, 1]
    MaxWeight = [10, 100]
    Dimension = [Vector3(10, 10, 10), Vector3(20, 20, 20)]
    PricePerDistance = [50, 200]


    def __init__(self, num):
        self.Type = Vehicle.Type[num]
        self.Cooler = Vehicle.Cooler[num]
        self.MaxWeight = Vehicle.MaxWeight[num]
        self.Dimension = Vehicle.Dimension[num]
        self.PricePerDistance = Vehicle.PricePerDistance[num]

    def generate_vehicles(number_of_vehicles):
        vehicles = []

        for i in range(number_of_vehicles):
            vehicles.append(Vehicle(random.randint(0, len(Vehicle.Type) - 1)))

        return vehicles
    
    def __str__(self):
        return "{ Type : " + str(self.Type) + ", Cooler : " + str(self.Cooler) + ", MaxWeight : " + str(self.MaxWeight) + ", Dimension : " + str(self.Dimension) + ", PricePerDistance : " + str(self.PricePerDistance) + " }"
    
    def __repr__(self):
        return self.__str__()


class Medicine:
    Type = ["Paracetamol", "Bodrex"]
    Temperature = [0, 1]
    Weight = [1, 2]
    Dimension = [Vector3(1, 1, 1), Vector3(2, 2, 2)]
    Fragility = [2, 1]

    def __init__(self, num):
        self.Type = Medicine.Type[num]
        self.Temperature = Medicine.Temperature[num]
        self.Weight = Medicine.Weight[num]
        self.Dimension = Medicine.Dimension[num]
        self.Fragility = Medicine.Fragility[num]

    def generate_medicine():
        return Medicine(random.randint(0, len(Medicine.Type) - 1))
    
    def __str__(self):
        return "{ Type : " + str(self.Type) + ", Temperature : " + str(self.Temperature) + ", Weight : " + str(self.Weight) + ", Dimension : " + str(self.Dimension) + ", Fragility : " + str(self.Fragility) + " }"
    
    def __repr__(self):
        return self.__str__()
    

class Graph:
    Vertices = []
    DistanceMatrix = []

    Sources = []
    Destinations = []

    def load_csv():
        with open('Order large.csv', newline='') as f:
            reader = csv.reader(f)
            your_list = np.array(list(reader))
        return your_list[:, 3:].astype(np.float64)
        


    def input_vertices(number_of_sources):
        Graph.Vertices = Graph.load_csv()
        if len(Graph.Vertices) <= number_of_sources:
            print("too many sources")

        while len(Graph.Sources) < number_of_sources:
            randomIndex = random.randint(0, len(Graph.Vertices) - 1)
            if randomIndex not in Graph.Sources:
                Graph.Sources.append(randomIndex)

        for i in range(len(Graph.Vertices)):
            if i not in Graph.Sources:
                Graph.Destinations.append(i)

    def generate_edges():
        Graph.DistanceMatrix = []
        for i in range(len(Graph.Vertices)):
            Graph.DistanceMatrix.append([])
            for j in range(len(Graph.Vertices)):
                xDist = Graph.Vertices[i][0] - Graph.Vertices[j][0]
                yDist = Graph.Vertices[i][1] - Graph.Vertices[j][1]
                Graph.DistanceMatrix[-1].append(math.sqrt(xDist * xDist + yDist * yDist))

    def get_random_source():
        return random.choice(Graph.Sources)
    
    def get_random_destination():
        return random.choice(Graph.Destinations)


class Transaction:
    def __init__(self, source, destination, medicine):
        self.Source = source
        self.Destination = destination
        self.Medicine = medicine

    def generate_transactions(number_of_transactions):
        transactions = []

        for i in range(number_of_transactions):
            transactions.append(Transaction(Graph.get_random_source(), Graph.get_random_destination(), Medicine.generate_medicine()))

        return transactions

    def __str__(self):
        return "{ Source : " + str(self.Source) + ", Destination : " + str(self.Destination) + ", Medicine : " + str(self.Medicine) + " }"
    
    def __repr__(self):
        return self.__str__()



def generate_problem(number_of_sources, number_of_transactions, number_of_vehicles):
    Graph.input_vertices(number_of_sources)
    Graph.generate_edges()

    return Graph.Sources, Graph.DistanceMatrix, Transaction.generate_transactions(number_of_transactions), Vehicle.generate_vehicles(number_of_vehicles)


source_indices, distance_matrix, transactions, vehicles = generate_problem(3, 10, 20)

#print(source_indices)
#print(distance_matrix)
print(transactions)
#print(vehicles)