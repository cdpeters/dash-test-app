"""Test figures.py."""

import plotly.graph_objs as go
from dash.dcc import Graph

from src.components.figures import create_graph_component


def test_create_graph_component() -> None:
    """Test graph component is assembled correctly."""
    # Arrange
    def fake_plotting_func(**params):
        """Replicate output of a plotly express plotting function."""
        return go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 5, 6])])

    id = "test-id"
    fig_params = {"x": [1, 2, 3], "y": [4, 5, 6]}
    expected_graph = Graph(id=id, figure=fake_plotting_func(**fig_params))

    # Act
    graph = create_graph_component(fake_plotting_func, id, fig_params)

    # Assert
    assert graph == expected_graph
