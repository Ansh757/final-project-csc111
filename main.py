"""
Final Project Title: IMBD Recommendation System

Objective: ...

By: Ansh Malhotra, Armaan Mann, Leya Abubaker

This file is Copyright (c) 2021 Ansh Malhotra, Armaan Mann, Leya Abubaker
"""
from __future__ import annotations
import csv
from typing import Optional
import networkx as nx
from plotly.graph_objs import Scatter, Figure
from Graph_Vertex import Graph

LINE_COLOUR = 'rgb(210,210,210)'
VERTEX_BORDER_COLOUR = 'rgb(50, 50, 50)'
BOOK_COLOUR = 'rgb(89, 205, 105)'
USER_COLOUR = 'rgb(105, 89, 205)'


def filtered_graph(imdb_file: str, genre: list[str], year: tuple[int, int],
                   director: Optional[str] = None, language: Optional[str] = None,
                   country: Optional[str] = None) -> Graph:
    """ Return a movies review graph corresponding to the filtered IMDB dataset.

    If a filter is not chosen the key-value pair will have a None type.
    """
    new_graph = Graph()
    new_dict = {}

    with open(imdb_file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:

            check1 = True if int(row[3]) in range(year[0], year[1] + 1) else False
            check2 = True if country is None or row[7].casefold() == country.casefold() else False
            check3 = True if language is None or row[8].casefold() == language.casefold() else False
            check4 = True if director is None or row[9].casefold() == director.casefold() else False

            check = [check1, check2, check3, check4]

            genres = [g.strip() for g in row[5].split(",")]
            for x in genres:
                if x in genre:
                    check.append(True)

            if all(check):
                new_dict[row[1]] = set(genres)
                new_graph.add_vertex(row[1], set(genres))

        for title1 in new_dict:
            for title2 in new_dict:
                if title1 != title2:
                    if new_dict[title1].intersection(new_dict[title2]) != set():
                        new_graph.add_edge(title1, title2)

    return new_graph


def load_graph(imbd_file: str) -> Graph:
    """Return a movies review graph corresponding to the given IMBD dataset."""
    new_graph = Graph()
    new_dict = {}

    with open(imbd_file) as f1:
        reader1 = csv.reader(f1)
        next(reader1)

        for row in reader1:
            split_ = row[5].strip()
            genres = [genre.strip() for genre in split_.split(",")]
            new_dict[row[1]] = set(genres)

            new_graph.add_vertex(row[1], set(genres))

        for title1 in new_dict:
            for title2 in new_dict:
                if title1 != title2:
                    if new_dict[title1].intersection(new_dict[title2]) != set():
                        new_graph.add_edge(title1, title2)

    return new_graph


def visualize_graph(graph: Graph,
                    layout: str = 'spring_layout',
                    max_vertices: int = 5000,
                    output_file: str = '') -> None:
    """Use plotly and networkx to visualize the given graph.

    Optional arguments:
        - layout: which graph layout algorithm to use
        - max_vertices: the maximum number of vertices that can appear in the graph
        - output_file: a filename to save the plotly image to (rather than displaying
            in your web browser)
    """
    graph_nx = graph.to_networkx(max_vertices)

    pos = getattr(nx, layout)(graph_nx)

    x_values = [pos[k][0] for k in graph_nx.nodes]
    y_values = [pos[k][1] for k in graph_nx.nodes]
    labels = list(graph_nx.nodes)

    x_edges = []
    y_edges = []
    for edge in graph_nx.edges:
        x_edges += [pos[edge[0]][0], pos[edge[1]][0], None]
        y_edges += [pos[edge[0]][1], pos[edge[1]][1], None]

    trace3 = Scatter(x=x_edges,
                     y=y_edges,
                     mode='lines',
                     name='edges',
                     line=dict(color=LINE_COLOUR, width=1),
                     hoverinfo='none',
                     )
    trace4 = Scatter(x=x_values,
                     y=y_values,
                     mode='markers',
                     name='nodes',
                     marker=dict(symbol='circle-dot',
                                 size=5,
                                 color=BOOK_COLOUR,
                                 line=dict(color=VERTEX_BORDER_COLOUR, width=0.5)
                                 ),
                     text=labels,
                     hovertemplate='%{text}',
                     hoverlabel={'namelength': 0}
                     )

    data1 = [trace3, trace4]
    fig = Figure(data=data1)
    fig.update_layout({'showlegend': False})
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False)

    if output_file == '':
        fig.show()
    else:
        fig.write_image(output_file)
