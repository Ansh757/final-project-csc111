"""
Final Project Title: IMBD Recommendation System

Objective: ...

By: Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais

This file is Copyright (c) 2021 Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais
"""
from __future__ import annotations
import csv
from typing import Any, Union


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
    kind: set[str]
    neighbours: dict[_Vertex, Union[float, int]]

    def __init__(self, item: Any, kind: set[str]) -> None:
        """Initialize a new vertex with the given item and kind.

        This vertex is initialized with no neighbours.

        Preconditions:
            - kind in {...}
        """
        self.item = item
        self.kind = kind
        self.neighbours = {}

    def degree(self) -> int:
        """Return the degree of this vertex"""
        return len(self.neighbours)

    def similarity_score_unweighted(self, other: _Vertex) -> float:
        """Return the ... similarity score between this vertex and other.

        The unweighted similarity score is calculated in the same way as the
        similarity score for _Vertex (from Part 1). That is, just look at edges,
        and ignore the weights.
        """
        if self.degree() == 0 or other.degree() == 0:
            return 0.0
        else:
            ...
            # TODO: Implement the formula to find out the similarity score betweem two vertices


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
        Graph.__init__(self)

    def add_vertex(self, item: Any, kind: set[str]) -> None:
        """Add a vertex with the given item and set of kind to this graph.

        The new vertex is not adjacent to any other vertices.
        Do nothing if the given item is already in this graph.

        Preconditions:
            - kind in {...}
        """
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item, kind)

    def add_edge(self, item1: Any, item2: Any, weight: Union[int, float] = 1) -> None:
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
            v1.neighbours[v2] = weight
            v2.neighbours[v1] = weight
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def get_weight(self, item1: Any, item2: Any) -> Union[int, float]:
        """Return the weight of the edge between the given items.

        Return 0 if item1 and item2 are not adjacent.

        Preconditions:
            - item1 and item2 are vertices in this graph
        """
        # TODO: Calculate the formula for the weight
        v1 = self._vertices[item1]
        v2 = self._vertices[item2]
        return v1.neighbours.get(v2, 0)

    def average_weight(self, item: Any) -> float:
        """Return the average weight of the edges adjacent to the vertex corresponding to item.

        Raise ValueError if item does not corresponding to a vertex in the graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return sum(v.neighbours.values()) / len(v.neighbours)
        else:
            raise ValueError
