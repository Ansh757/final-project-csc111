"""
Here are some testing functions which we used below, you can something similar to these.
"""
from main import visualize_graph, load_graph, filtered_graph
from graph_vertex import Graph

# For load_graph
visualize_graph(load_graph("data/small_dataset.csv"))
visualize_graph(load_graph("data/medium_dataset.csv"))

# For Filtered Graph:
visualize_graph(filtered_graph("data/small_dataset.csv", genre=["Crime"]))
visualize_graph(filtered_graph("data/small_dataset.csv", genre=["Drama"]))
visualize_graph(filtered_graph("data/medium_dataset.csv", genre=["Crime", "Romance"]))
visualize_graph(filtered_graph("data/medium_dataset.csv", genre=["Crime", "Romance"],
                               country="UK"))

# For movies recs:
new_graph = load_graph("portions/portion1.csv")
Graph.movie_recs(new_graph, "Men in Black")

new_graph = load_graph("data/large_dataset.csv")
Graph.movie_recs(new_graph, "Captain America: The First Avenger")

new_graph = load_graph("data/small_dataset.csv")
Graph.movie_recs(new_graph, "Cleopatra")
