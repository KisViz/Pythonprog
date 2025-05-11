import pytest
from unittest.mock import patch, Mock
import pandas as pd
from datetime import datetime
from kotprog.src.diagram import OszlopDiagram
from kotprog.src.diagram.terulet import TeruletDiagram
from kotprog.src.diagram import VonalDiagram

"""
Itt a legnagyobb gondot a Mock jelentette, amit a gyakorlat anyagából
és a következő helyekről szemezgettem össze:
https://docs.python.org/3/library/unittest.mock.html
https://www.toptal.com/python/an-introduction-to-mocking-in-python
https://www.youtube.com/watch?v=-F6wVOlsEAM
https://www.youtube.com/watch?v=dw2eNCzwBkk
Ai:((
"""


# adatok a teszteleshez
@pytest.fixture
def sample_data():  # egy elore elkeszitett teszetlos dataframe
    return pd.DataFrame({
        'Country/Region': ['Hungary', 'Hungary', 'Germany', 'Germany'],
        'Dátum': [
            datetime(2020, 3, 1),
            datetime(2020, 3, 2),
            datetime(2020, 3, 1),
            datetime(2020, 3, 2)
        ],
        'Esetek': [10, 20, 30, 40]
    })


# ellenorzi, hogy valoban a lineplotot hivaj e meg es jol hivja e
def test_vonal_diagram_create_chart(sample_data):
    # lecserekli a lineplotot egy mockra
    with patch('seaborn.lineplot') as mock_lineplot:
        mock_ax = Mock()  # letrehoz egy tengelyt
        diagram = VonalDiagram(sample_data)  # megcsinaljuk a diaramot
        diagram.create_chart(mock_ax)  # es atadjuk a mockolt tejgelyt

        # ellenorzi, hogy egyszer hija e meg a lineplotot a parameterekkel
        mock_lineplot.assert_called_once_with(
            data=sample_data,
            x='Dátum',
            y='Esetek',
            hue='Country/Region',
            ax=mock_ax
        )


# megnezi, hogy jol csoportosit e es jo e a barplot hivasa
def test_oszlop_diagram_create_chart(sample_data):
    with patch('seaborn.barplot') as mock_barplot:
        mock_ax = Mock()  # letrehoz egy tengelyt
        diagram = OszlopDiagram(sample_data)  # megcsinaljuk a diaramot
        diagram.create_chart(mock_ax)  # es atadjuk a mockolt tejgelyt

        # megnez megvam e a datumcsoport
        assert 'Dátum_csoport' in diagram.data.columns
        # megnezi, hogy egyszer van e hiva es hekyesek e
        mock_barplot.assert_called_once()
        args, kwargs = mock_barplot.call_args
        assert kwargs['x'] == 'Dátum_csoport'
        assert kwargs['y'] == 'Esetek'
        assert kwargs['hue'] == 'Country/Region'
        assert kwargs['ax'] == mock_ax


# megnezzuk jo e a hivasa a teruletnek
def test_terulet_diagram_create_chart(sample_data):
    with patch('pandas.DataFrame.pivot') as mock_pivot:
        mock_plot = Mock()
        # dataframet keszit orszagonkenti oszlopokkal
        mock_pivot.return_value.plot = Mock()
        # atadjuk a mockolt plotot
        mock_pivot.return_value.plot.area = mock_plot
        mock_ax = Mock()  # letrehoz egy tengelyt

        diagram = TeruletDiagram(sample_data)  # megcsinaljuk a diaramot
        diagram.create_chart(mock_ax)  # es atadjuk a mockolt tejgelyt

        # elleonorizzuk, hogy jok vannak e beallitva
        mock_pivot.assert_called_once_with(
            index='Dátum',
            columns='Country/Region',
            values='Esetek'
        )
        mock_plot.assert_called_once_with(
            ax=mock_ax,
            alpha=0.7
        )
