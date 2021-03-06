"""
Final Project Title: Top3

Objective: The main file which the TA will be running. The purpose of this file
is to run the functions for the visualizations to view the graphs.

By: Ansh Malhotra, Armaan Mann, Leya Abubaker

This file is Copyright (c) 2021 Ansh Malhotra, Armaan Mann, Leya Abubaker
"""
from __future__ import annotations
import csv
from typing import List, Optional
import networkx as nx
from plotly.graph_objs import Scatter, Figure, Layout
from graph_vertex import Graph

####################################################################################################
# Global Variables for Colours
####################################################################################################
LINE_COLOUR = '#DAA520'
VERTEX_BORDER_COLOUR = '#8B0000'
MOVIE_COLOR = '#FF0000'
BACKGROUND = 'rgb(0,0,0)'


####################################################################################################
# Visualization for the Graphs
####################################################################################################
def visualize_graph(graph: Graph,
                    layout: str = 'spring_layout',
                    max_vertices: int = 5000,
                    output_file: str = '') -> None:
    """Use plotly and networkx to visualize the given graph.

    Taken from the Assignment3 to visualize the graph:
    https://www.teach.cs.toronto.edu/~csc111h/winter/assignments/a3/handout/

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
                                 color=MOVIE_COLOR,
                                 line=dict(color=VERTEX_BORDER_COLOUR, width=0.4)
                                 ),
                     text=labels,
                     hovertemplate='%{text}',
                     hoverlabel={'namelength': 0}
                     )
    layout = Layout(
        plot_bgcolor='rgb(0,0,0)'
    )

    data1 = [trace3, trace4]
    fig = Figure(data=data1, layout=layout)
    fig.update_layout({'showlegend': False})
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False)

    if output_file == '':
        fig.show()
    else:
        fig.write_image(output_file)


def filtered_graph(imdb_file: str, genre: Optional[list[str]] = None,
                   director: Optional[str] = None,
                   country: Optional[str] = None) -> Graph:
    """Return a movies review graph corresponding to the filtered IMDB dataset.

    If a filter is not chosen the key-value pair will have a None type..

    The data set must be chosen from either the data folder or the portion folders. Although,
    we recommend to use the small, or medium or large files, so you dont' have to wait long.

    Refer to the dataset for countries and directors available corresponding
    to that csv file.

    Optional arguments:
        - genres: the list of genre(s).
        - director: the director of a movie title
        - country: the country in which the movie is made.

    As an Example of the parameter should look like:
    filtered_graph(imdb_file='portions/portion1.csv', genre=['Animation', 'Comedy', 'Fantasy']
                    ,country='Canada', director=None)

    Preconditions:
        - imdb_file is the path to a CSV file corresponding to the chunks of the IMDB dataset
        given as "portions/portion1.csv" or within the data folder as "data/small_dataset.csv".
        - The given filter should be in the form of country="USA" or genres=["Crime"]
        - 1990 <= year <= 2020.
    """
    new_graph = Graph()
    new_dict = {}

    with open(imdb_file, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:

            check1 = True if country is None or row[7].casefold() == country.casefold() else False
            check2 = True if director is None or row[9].casefold() in director.casefold() else False

            check = [check1, check2]

            genres = [g.strip() for g in row[5].split(",")]

            if genres is None:
                check.append(True)
            else:
                for x in genres:
                    if x in genre:
                        check.append(True)

            if all(check):
                new_dict[row[2]] = set(genres)
                new_graph.add_vertex(row[2], set(genres))

        for title1 in new_dict:
            for title2 in new_dict:
                if title1 != title2:
                    if new_dict[title1].intersection(new_dict[title2]) != set():
                        new_graph.add_edge(title1, title2)

    return new_graph


def load_graph(imdb_file: str) -> Graph:
    """Return a movies review graph corresponding to the given IMBD dataset.

    The data set must be chosen from the portion folder, you may choose any of the portion csv files
    to visualize the graph.

    Preconditions:
        - imdb_file is the path to a CSV file corresponding to the chunks of the IMDB dataset
        given as "portions/portion1.csv" or within the data folder as "data/small_dataset.csv".
    """
    new_graph = Graph()
    new_dict = {}

    with open(imdb_file, encoding="utf8") as f1:
        reader1 = csv.reader(f1)
        next(reader1)

        for row in reader1:
            split_ = row[5].strip()
            genres = [genre.strip() for genre in split_.split(",")]
            new_dict[row[2]] = set(genres)

            new_graph.add_vertex(row[2], set(genres))

        for title1 in new_dict:
            for title2 in new_dict:
                if title1 != title2:
                    if new_dict[title1].intersection(new_dict[title2]) != set():
                        new_graph.add_edge(title1, title2)

    return new_graph


###################################################################################################
# For the Helpers GUI
####################################################################################################
def loading_graph(portion_file: str) -> Graph:
    """Returns a loaded graph

    Preconditions:
        - imdb_file is the path to a CSV file corresponding to the chunks of the IMDB dataset
        given as "portions/portion1.csv" or within the data folder as "data/small_dataset.csv".
    """
    return load_graph(portion_file)


def user_prompts(portion_file: str) -> Optional[str]:
    """Creates a prompt for the user to pick a preferred movie based on filtered information

    Precondition:
        - imdb_file is the path to a CSV file corresponding to the chunks of the IMDB dataset
        given as "portions/portion1.csv" or within the data folder as "data/small_dataset.csv".
        - Note: When inputting the IO in the console, make sure that the movie_title with no strings
         (Be watchful for the cases as well) is within the corresponding file
         as the parameter for imdb_file.
    """
    g = loading_graph(portion_file)

    for _ in range(len(g.get_all_vertices())):
        movie_title = input("What is a movie you like?")
        if movie_title in g.get_all_vertices():
            return movie_title
        print("Invalid selection. Please choose another movie")
    # We must not reach here due to the precondition.
    return None


def get_recs(file: str) -> List[str]:
    """Returns the list of recommended movies depending on parameter, n within the function in
    Graph.movie_recs()

    Preconditions:
        - imdb_file is the path to a CSV file corresponding to the chunks of the IMDB dataset
        given as "portions/portion1.csv" or within the data folder as "data/small_dataset.csv".
    """
    new_graph = loading_graph(file)
    get_movies = new_graph.movie_recs(user_prompts(file))
    return get_movies


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 1000,
    #     'disable': ['E1136', 'R0914', 'W0612', 'E9998', 'R1710'],
    #     'extra-imports': ['csv', 'networkx', 'pandas', 'plotly.graph_objs', 'graph_vertex'],
    #     'allowed-io': ['load_graph', 'filtered_graph'],
    #     'max-nested-blocks': 4
    # })
