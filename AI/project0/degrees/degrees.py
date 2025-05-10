import csv
import sys

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
    if source_movie and target_movie:
        matching_movie = source_movie & target_movie
        if matching_movie:
            return True
    else:
        return False

def get_movie_id(movie_neighbors,source, target):
    source_movie = next((movie_id for movie_id, actor_id in movie_neighbors if actor_id == source), None)
    target_movie = next((movie_id for movie_id, actor_id in movie_neighbors if actor_id == target), None)
    if source_movie and target_movie:
        matching_movie = source_movie & target_movie
        if matching_movie:
            return matching_movie
    else:
        None

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.

    """
    degrees = []
    movie_neighbors = neighbors_for_person(source)
    if in_same_movie(movie_neighbors,source, target):
        movie_id = get_movie_id(movie_neighbors,source, target)
        return [(movie_id, target)]

    exit()

    degree = 1
    while True:
        for actors_in_movie in movie_neighbors:
            if source == actors_in_movie[1]:
                continue

            if in_same_movie(movie_neighbors,actors_in_movie[1],target):
                print(f" degree={degree}  {people[actors_in_movie[1]]['name']} {people[target]['name']}")
                break
            movie_neighbors = neighbors_for_person(actors_in_movie[1])
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
