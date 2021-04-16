"""
Final Project Title: IMDB Recommendation System

Objective: This file includes the Augmented Graph and Vertex taken from the lectures and assignment.

By: Ansh Malhotra, Armaan Mann, Leya Abubaker

This file is Copyright (c) 2021 Ansh Malhotra, Armaan Mann, Leya Abubaker
"""
from __future__ import annotations
from typing import Any, Union, Optional
import csv
import networkx as nx
import pandas as pd


################################################################################
# _Vertex Class
################################################################################
class _Vertex:
    """A vertex in a movies graph, used to represent a node for the movie.

    List of genres: {'Reality-TV', 'Adventure', 'Drama', 'Biography', 'War', 'Family', 'Music',
    'Crime', 'Film-Noir', 'Romance', 'Musical', 'Comedy', 'Horror', 'News', 'Action', 'Sport',
    'History', 'Western', 'Fantasy', 'Thriller', 'Documentary', 'Animation', 'Adult',
    'Sci-Fi', 'Mystery'}

    Instance Attributes:
        - item: The data stored in this vertex, representing the title of a movie.
        - genres: The type of this vertex: contains the list of genres.
        - neighbours: The vertices that are adjacent to this vertex.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """
    item: Any
    genres: set[str]
    neighbours: set[_Vertex]

    def __init__(self, item: Any, genres: set[str]) -> None:
        """Initialize a new vertex with the given item and genres.

        This vertex is initialized with no neighbours.
        """
        self.item = item
        self.genres = genres
        self.neighbours = set()

    def degree(self) -> int:
        """Return the degree of this vertex"""
        return len(self.neighbours)

    def calculate_weight(self, other: _Vertex) -> float:
        """Return the weight between the given vertex and other."""
        if self.genres == set():
            return 0.0
        else:
            numerator = self.genres.intersection(other.genres)
            denominator = self.genres.union(other.genres)
            result = len(numerator) / len(denominator)
            return result

    def similarity_score(self, other: _Vertex) -> float:
        """Return the weighted similarity score between this vertex and other.
        """
        if self.degree() == 0 or other.degree() == 0:
            return 0.0
        elif self.calculate_weight(other) == 0:
            return 0.0
        else:
            v1_adjacent = self.neighbours
            v2_adjacent = other.neighbours
            numerator = v1_adjacent.intersection(v2_adjacent)
            denominator = v1_adjacent.union(v2_adjacent)
            result = len(numerator) / len(denominator)
            return result * self.calculate_weight(other)


################################################################################
# Graph Class
################################################################################
class Graph:
    """A graph used to represent a movie network.
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _Vertex object.
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def get_all_vertices(self) -> set:
        """Return a set of all vertex items in this graph.
        """
        return {v.item for v in self._vertices.values()}

    def add_vertex(self, item: Any, genres: set[str]) -> None:
        """Add a vertex with the given item and set of genres to this graph.

        The new vertex is not adjacent to any other vertices.

        Preconditions:
            - self not in self._vertices
        """
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item, genres)

    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Add the new edge
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            return any(v2.item == item2 for v2 in v1.neighbours)
        else:
            return False

    def get_neighbours(self, item: Any) -> set:
        """Return a set of the neighbours of the given item.

        Note that the *items* are returned, not the _Vertex objects themselves.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return {neighbour.item for neighbour in v.neighbours}
        else:
            raise ValueError

    def get_similarity_score(self, item1: Any, item2: Any) -> float:
        """Return the similarity score between the two given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]
            return v1.similarity_score(v2)
        else:
            raise ValueError

    def get_weight(self, item1: Any, item2: Any) -> Union[int, float]:
        """Return the weight of the edge between the given items.

        Preconditions:
            - item1 and item2 are vertices in this graph
        """
        v1 = self._vertices[item1]
        v2 = self._vertices[item2]
        weight = v1.calculate_weight(v2)
        return weight

    def movie_recs(self, movie: str, threshold: Optional[float] = 0.0,
                   n: Optional[int] = 3) -> list[str]:
        """Return a list of up to <n> recommended movies based on similarity to the given book,
        with the given threshold and the movie name.

        Optional arguments:
        - threshold: represents the smallest possible similarity scores where all similarity score
        have to be greater than the threshold.
        - n: the number of recommended movies that the function should display.

        Preconditions:
            - self in self._vertices
            - any(movie == title.item for title in self._vertices)
            - n >= 1
            - 0.0 <= threshold < 1.0
        """
        movies_so_far = []
        name_and_score = {}
        v1 = self._vertices.get(movie).item

        lst_books = sorted(self.get_all_vertices(), reverse=True)

        for v2 in lst_books:
            name_and_score[v2] = self.get_similarity_score(v1, v2)

        while len(movies_so_far) < n and name_and_score != {}:
            max_book_score = max(name_and_score, key=name_and_score.get)
            score_of_book = name_and_score.pop(max_book_score)
            if (max_book_score != movie) and (score_of_book > threshold) and (
                    max_book_score not in movies_so_far):
                movies_so_far.append(max_book_score)

        return movies_so_far

    def movie_info(self, imdb_file: str, items: list[str]) -> dict[Any]:
        """Return a dictionary for the corresponding elements in the list of items.

        The dictionary, 'd' is in the form of: [director, language, country, actor,
                                                genres, year, description]
        """
        d = {}

        with open(imdb_file) as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:

                for num in range(len(items)):
                    v = self._vertices[items[num]]

                    if row[2] == v.item:
                        d[row[2]] = [v.genres, row[9], row[8], row[7], row[3],
                                     row[13], str(row[12])]
                    if len(d) == 3:
                        break
        return d

    def to_networkx(self, max_vertices: int = 5000) -> nx.Graph:
        """Convert this graph into a networkx Graph.

        max_vertices specifies the maximum number of vertices that can appear in the graph.
        (This is necessary to limit the visualization output for large graphs.)
        """
        graph_nx = nx.Graph()
        for v in self._vertices.values():
            graph_nx.add_node(v.item, kind=v.genres)

            for u in v.neighbours:
                if graph_nx.number_of_nodes() < max_vertices:
                    graph_nx.add_node(u.item, kind=u.genres)

                if u.item in graph_nx.nodes:
                    graph_nx.add_edge(v.item, u.item)

            if graph_nx.number_of_nodes() >= max_vertices:
                break

        return graph_nx


####################################################################################################
# This function was used for chunking purposes
# DON'T RUN THIS FUNCTION
####################################################################################################
def chunking(file_name: str) -> None:
    """Mutates the current directory csv file into chunks of 1200 rows.

    Note: We already did this and created a portion folder!
    """
    size_per_file = 12000
    file_number = 1

    for size in pd.read_csv(file_name, chunksize=size_per_file):
        size.to_csv("portion" + str(file_number) + '.csv', index=False)
        file_number += 1


# if __name__ == '__main__':
#     import python_ta.contracts
#     python_ta.contracts.check_all_contracts()
#     import python_ta
#     python_ta.check_all(config={
#         'max-line-length': 1000,
#         'disable': ['E1136', 'R0914'],
#         'extra-imports': ['csv', 'networkx', 'pandas'],
#         'allowed-io': ['movie_info'],
#         'max-nested-blocks': 4
#     })
