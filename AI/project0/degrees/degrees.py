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
    source = 'Kevin Bacon'
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

def same_movie(source, target):
   # Source and target starred in the same movie
    for m in people[source]['movies']:
        if m in people[target]['movies']:
            return [(m, source), (m, target)]
    return False

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.

    """
    degrees = []
    actor_movie = set()
    source_matches 
    target_matches
    # Source and target starred in the same movie
    star_power = same_movie(source,target)
    if star_power:
        return star_power

    # 'Tom Hanks' & 'Tom Cruise' approach
    for m in people[source]['movies']:
        for star in movies[m]['stars']:
            star_power = same_movie(target,star)
            if star_power:
                print(f"C is in the same movie as B - {star_power}")
    print()


    #print(movies[m])
    #[row["movie_id"]]["stars"].add(row["person_id"])

    exit()

    # create an actor list to be able to sort and search actors
    actors  = []
    # Store the number of movies count the actors has been in.
    # The higher the number the higher likelihood they have been in the same movie as another actor
    moviez = []
    for key, value in people.items():
        for movie_id in value.get('movies', ''):
            movies.append(movie_id)

        person = {
            "id": key,
            "name": value.get('name', ''),
            "movie_count": len(value.get('movies', '')), # the count of movies
            "movie_ids": moviez
        }
        actors.append(person)
        moviez = []

    sorted_data = sort_by_movie_count(actors)

    # Print each row with index ID
    for i in range(len(sorted_data)):
        if source == sorted_data[i]['id'] or target == sorted_data[i]['id']:
            print(f"Record {i+1}: id - {sorted_data[i]['id']}, Name: {sorted_data[i]['name']}, {sorted_data[i]['movie_count']}, {sorted_data[i]['movie_ids']}")



    exit()
    return [(1, 2), (3, 4)]
    raise NotImplementedError

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
