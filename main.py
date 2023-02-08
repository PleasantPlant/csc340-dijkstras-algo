from dijsktra import Graph


def run_flight_graph(start, stop):
    name_dict = {
        "YVR": "Vancouver",
        "LAX": "Los Angeles",
        "LAS": "Las Vegas",
        "SLC": "Salt Lake City",
        "FLL": "Fort Lauderdale",
        "BOS": "Boston",
        "NYC": "New York City",
        "CHI": "Chicago",
        "MSP": "Minneapolis",
    }

    edges = [
        ("YVR", "LAS", 327),
        ("YVR", "BOS", 561),
        ("YVR", "NYC", 603),
        ("LAX", "SLC", 222),
        ("LAX", "LAS", 169),
        ("LAX", "FLL", 676),
        ("LAS", "SLC", 69),
        ("LAS", "CHI", 254),
        ("LAS", "NYC", 617),
        ("LAS", "FLL", 99),
        ("FLL", "NYC", 299),
        ("FLL", "BOS", 465),
        ("BOS", "NYC", 133),
        ("NYC", "CHI", 226),
        ("NYC", "MSP", 237),
    ]
    graph = Graph(edges)
    path = graph.dijsktra_shortest_path_airport(start, stop, name_dict)
    pathLen = len(path) - 1
    cost = costCalculate(path, pathLen, edges)
    fixedPath = makeReadable(pathLen, path, name_dict)
    print(f"Your route is: {fixedPath}")
    print(f"The Total Cost is {cost} dollars.")
    match pathLen:
        case _ if pathLen > 2:
            print(f"There are {pathLen-1} layovers on this trip.")
        case 2:
            print("There is 1 layover on this trip.")
        case 1:
            print("There are no layovers on this trip.")
    print("\n")


def makeReadable(pathLen, path, name_dict):
    readablePath = ""
    for i in range(pathLen):
        if i < pathLen - 1:
            readablePath += "".join(name_dict[path[i]])
            readablePath += "".join(" to ")
            readablePath += "".join(name_dict[path[i + 1]])
            readablePath += "".join(", ")
        else:
            readablePath += "".join("and ")
            readablePath += "".join(name_dict[path[i]])
            readablePath += "".join(" to ")
            readablePath += "".join(name_dict[path[i + 1]])
            readablePath += "".join(".")
    return readablePath


def costCalculate(path, pathLen, edges):
    cost = 0
    iterator = 0
    i = 0
    while i < pathLen:
        if (path[i] == edges[iterator][0] and path[i + 1] == edges[iterator][1]) or (
            path[i] == edges[iterator][1] and path[i + 1] == edges[iterator][0]
        ):
            cost += edges[iterator][2]
            i += 1
        iterator += 1
    return cost


def main():
    run_flight_graph("LAX", "CHI")
    run_flight_graph("LAX", "MSP")
    run_flight_graph("SLC", "BOS")


if __name__ == "__main__":
    main()
