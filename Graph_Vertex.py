"""
Final Project Title: ...

Objective: ...

By: Ansh Malhotra, Armaan Mann, Leya Abubaker

This file is Copyright (c) 2021 Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais
"""
from __future__ import annotations
import csv
from typing import Any, Optional, Union
import networkx as nx
from plotly.graph_objs import Scatter, Figure


# TODO LOOK OVER DOCSTRINGS.
class _Vertex:
    """A vertex in a ... graph, used to represent a node for each movie.

    List of genres: [
                    ]

    Instance Attributes:
        - item: The data stored in this vertex, representing the title of a movie.
        - kind: The type of this vertex: contains the list of genres.
        - neighbours: The vertices that are adjacent to this vertex.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
        - self.kind in {...}
    """
    item: Any
    genres: set[str]
    neighbours: set[_Vertex]

    def __init__(self, item: Any, kind: set[str]) -> None:
        """Initialize a new vertex with the given item and kind.

        This vertex is initialized with no neighbours.

        Preconditions:
            - kind in {...}
        """
        self.item = item
        self.genres = kind
        self.neighbours = set()

    def degree(self) -> int:
        """Return the degree of this vertex"""
        return len(self.neighbours)

    def calculate_weight(self, other: _Vertex) -> float:
        """Return the weight between this vertex and other."""
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

        # This call isn't necessary, except to satisfy PythonTA.
        # Graph.__init__(self)

    def get_all_vertices(self) -> set:
        """Return a set of all vertex items in this graph.
        """

        return {v.item for v in self._vertices.values()}

        # return {v.item for v in self._vertices}

    def add_vertex(self, item: Any, kind: set[str]) -> None:
        """Add a vertex with the given item and set of kind to this graph.

        The new vertex is not adjacent to any other vertices.
        Do nothing if the given item is already in this graph.

        Preconditions:
            - kind in {...}
        """
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item, kind)

    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph,
        with the given weight.

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

    def average_weight(self, item: Any) -> float:
        """Return the average weight of the edges adjacent to the vertex corresponding to item.

        Raise ValueError if item does not corresponding to a vertex in the graph.
        """
        # TODO
        if item in self._vertices:
            v = self._vertices[item]
            return sum(v.neighbours.values()) / len(v.neighbours)
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

        Return 0 if item1 and item2 are not adjacent.

        Preconditions:
            - item1 and item2 are vertices in this graph
        """
        v1 = self._vertices[item1]
        v2 = self._vertices[item2]
        weight = v1.calculate_weight(v2)
        return weight

    def to_networkx(self, max_vertices: int = 5000) -> nx.Graph:
        """Convert this graph into a networkx Graph.

        max_vertices specifies the maximum number of vertices that can appear in the graph.
        (This is necessary to limit the visualization output for large graphs.)

        Note that this method is provided for you, and you shouldn't change it.
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

    def movie_recs(self, threshold: float, n: int, movie: str) -> list[str]:
        """
        ...
        """
        movies_so_far = []
        name_and_score = {}
        v1 = self._vertices.get(movie).item

        lst_books = sorted(self.get_all_vertices(), reverse=True)
        for v2 in lst_books:
            # name_and_score[v2] = v1.get_similarity_score(v1, v2)
            name_and_score[v2] = self.get_similarity_score(v1, v2)

        while len(movies_so_far) < n and name_and_score != {}:
            max_book_score = max(name_and_score, key=name_and_score.get)
            score_of_book = name_and_score.pop(max_book_score)
            if (max_book_score != movie) and (score_of_book > threshold) and (
                    max_book_score not in movies_so_far):
                movies_so_far.append(max_book_score)

        return movies_so_far

