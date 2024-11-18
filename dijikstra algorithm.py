import heapq
def get_distance_matrix():
    locations = ['Bus Depot', 'Home A', 'Home B', 'Home C', 'School']
    distances = {loc: {} for loc in locations}
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            while True:
                try:
                    distance = float(input(f"Enter the distance between {locations[i]} and {locations[j]} in km: "))
                    if distance >= 0:
                        distances[locations[i]][locations[j]] = distances[locations[j]][locations[i]] = distance
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
    return distances
def get_speed():
    while True:
        try:
            speed = float(input("Enter the average speed of the bus in km/h: "))
            if speed > 0:
                return speed
        except ValueError:
            print("Invalid input. Please enter a valid speed.")

def dijkstra(graph, start):
    queue, distances, previous_nodes = [(0, start)], {node: float('inf') for node in graph}, {node: None for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    return distances, previous_nodes
def find_shortest_route():
    distances, speed = get_distance_matrix(), get_speed()
    locations, total_distance, total_time = ['Bus Depot', 'Home A', 'Home B', 'Home C', 'School'], 0, 0
    route, visited, current_location = ['Bus Depot'], set(['Bus Depot']), 'Bus Depot'

    while len(visited) < len(locations) - 1:
        shortest_distances, _ = dijkstra(distances, current_location)
        next_location = min((loc for loc in locations if loc != 'School' and loc not in visited),
                            key=lambda loc: shortest_distances[loc])
        min_distance = shortest_distances[next_location]
        time_taken = (min_distance / speed) * 60
        total_time += time_taken
        print(f"From {current_location} to {next_location}: {min_distance} km, Estimated Time: {time_taken:.2f} minutes")
        
        route.append(next_location)
        total_distance += min_distance
        visited.add(next_location)
        current_location = next_location
    
    final_distance = distances[current_location]['School']
    total_time += (final_distance / speed) * 60
    route.append('School')
    total_distance += final_distance
    
    print(f"\nTotal Distance: {total_distance} km")
    print(f"Total Time: {total_time:.2f} minutes")
    print("\nComplete Route:")
    print(" → ".join(route))

if __name__ == "__main__":
    find_shortest_route()
