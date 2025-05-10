import csv
import sys
import sqlite3

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    '''
    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")
    path = shortest_path(source, target)
    '''
    #source = 'Kevin Bacon'
    source = 'Tom Hanks'
    source = person_id_for_name(source)

    target = 'Tom Cruise'
    #target = 'Kevin Bacon'
    target = person_id_for_name(target)


    path = shortest_path(source, target)
    #exit()

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

def in_same_movie(movie_neighbors,source, target):
    source_movie = next((movie_id for movie_id, actor_id in movie_neighbors if actor_id == source), None)
    target_movie = next((movie_id for movie_id, actor_id in movie_neighbors if actor_id == target), None)
    if source_movie and source_movie:
        if isinstance(source_movie, set) and isinstance(source_movie, set):
            matching_movie = source_movie.intersection(target_movie)
            if matching_movie:
                return True
            return False
    else:
        return False

def get_movie_id(movie_neighbors,source, target):
    source_movie = next((movie_id for movie_id, actor_id in movie_neighbors if actor_id == source), None)
    target_movie = next((movie_id for movie_id, actor_id in movie_neighbors if actor_id == target), None)
    if source_movie and target_movie:
        if isinstance(source_movie, set) and isinstance(source_movie, set):
            matching_movie = source_movie.intersection(target_movie)
            if matching_movie:
                return matching_movie
            else:
                None
    else:
        None

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.

    """
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("actors_movies.db")

    # Create a cursor object
    cursor = conn.cursor()

    # Create table (if it doesn't exist)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS actor_movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        degree INTEGER,
        actor_id TEXT,
        movie_id TEXT
    )
    """)
    conn.commit()

    degrees = []
    movie_neighbors = neighbors_for_person(source)
    if in_same_movie(movie_neighbors,source, target):
        movie_id = get_movie_id(movie_neighbors,source, target)
        return [(movie_id, target)]

    #with open(f"{directory}/people.csv", encoding="utf-8") as f:

    actor_data = []

    for actor_id in people:
        for movie_id in people[actor_id]['movies']:
            if source == actor_id:
                actor_data.append({"degree": 1, "actor_id": actor_id, "movie_id": movie_id})
            elif target == actor_id:
                actor_data.append({"degree": -1, "actor_id": actor_id, "movie_id": movie_id})
            else:
                actor_data.append({"degree": 0, "actor_id": actor_id, "movie_id": movie_id})

    sorted_actor_data = sorted(actor_data, key=lambda x: x['degree'], reverse=True)

    source_movie = []
    count = sum(1 for row in sorted_actor_data if row['degree'] == 1)

 


    exit()
    # Sample dictionary

    actor_datq = {"actor_id": "James", "movie_id": 30},


    # Define CSV file path
    file_path = "data.csv"

    # Write to CSV file
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())  # Use keys as column headers
        writer.writeheader()  # Write headers
        writer.writerows(data)  # Write row data


    degree = 1
    while True:
        for actors_in_movie in movie_neighbors:
            if source == actors_in_movie[1]:
                continue
            this_actors_movie_neighbors = neighbors_for_person(actors_in_movie[1])
            for for_this_actor in this_actors_movie_neighbors:
                if in_same_movie(this_actors_movie_neighbors,for_this_actor[1],target):
                    print(f" degree={degree}  {people[for_this_actor[1]]['name']} {people[target]['name']}")
                    break

            movie_neighbors = neighbors_for_person(for_this_actor[1])
            degree += 1
        break

def sort_by_movie_count(data):
    # Sort the data by movie_count in descending order
    return sorted(data, key=lambda x: int(x['movie_count']), reverse=True)



def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
