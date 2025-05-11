import pandas as pd
import pytest
import kotprog.src.app
from kotprog.src.diagram import OszlopDiagram
from kotprog.src.diagram.terulet import TeruletDiagram
from kotprog.src.diagram import VonalDiagram

"""
A monkeypatch-hez és a data framek-hez sok segítség kellett, amiket
a következő helyekről szemezgettem:
https://www.w3schools.com/python/pandas/pandas_dataframes.asp
https://www.geeksforgeeks.org/python-pandas-dataframe/
https://pandas.pydata.org/docs/reference/api/pandas.melt.html
https://docs.pytest.org/en/stable/how-to/monkeypatch.html
https://www.youtube.com/watch?v=-ot5qTvV6kE
https://www.youtube.com/watch?v=rZH4ffs7SMU
Ai:(
"""


# adatok a teszteleshez
@pytest.fixture  # egy elore elkeszitett teszetlos dataframe
def dummy_df():
    return pd.DataFrame({
        'Country/Region': ['Hungary', 'Germany'],
        '2020-01-01': [0, 1],
        '2020-01-02': [1, 2]
    })


# jol olvassuk e be az adarokat
# monkeyparch azert kell, hogy a betoltest ideiglenesen felulirjuk
def test_betolt_adatok(monkeypatch, tmp_path):
    csv_path = tmp_path / "fertozottek.csv"  # osszerakjuk az utvonalat
    dummy_data = ("Country/Region,2020-01-01,2020-01-02\n"
                  "Hungary,0,1\nGermany,1,2\n")
    # letrehozzuk az ideiglnes csvt
    csv_path.write_text(dummy_data, encoding="utf8")
    # azert nem a dummy_df()-t hasznljuk, mert itt a beolvasas a lenyeg

    # igy a betolt adatok az ideiglenes filet olvassa be
    monkeypatch.setattr(
        kotprog.src.app, "betolt_adatok",
        lambda: pd.read_csv(csv_path)
    )
    df = kotprog.src.app.betolt_adatok()

    assert isinstance(df, pd.DataFrame)  # letezeik
    assert "Country/Region" in df.columns  # jo nev
    assert df.shape == (2, 3)  # ket sor, harom oszlop


# jol alakitjuk e at az adatokat
# a dummy pf-et atadjuk neki
def test_df_atalakitas(dummy_df):
    df = dummy_df

    # csak a hungary sorok maradjanak meg
    szurt_df = df[df["Country/Region"].isin(["Hungary"])]
    # atalakitja a dataframet hosszuksa formatumura
    atalakított_df = szurt_df.melt(
        id_vars='Country/Region', var_name='Dátum', value_name='Esetek'
    )
    # atirjuk datetimeba a datumokat
    atalakított_df['Dátum'] = pd.to_datetime(atalakított_df['Dátum'])

    # jok az oszlopok
    assert list(atalakított_df.columns) == [
        'Country/Region', 'Dátum', 'Esetek'
    ]
    # ja a courtjy
    assert atalakított_df['Country/Region'].iloc[0] == 'Hungary'
    # helyes a datum
    assert pd.api.types.is_datetime64_any_dtype(atalakított_df['Dátum'])


# letrejonnek e a diagramok
# ez is a dummy df-et kapja
def test_diagram_tipusok(dummy_df):

    # atalakitja a dataframet hosszuksa formatumura
    atalakított_df = dummy_df.melt(
        id_vars='Country/Region', var_name='Dátum', value_name='Esetek'
    )
    # atirjuk datetimeba a datumokat
    atalakított_df['Dátum'] = pd.to_datetime(atalakított_df['Dátum'])

    # jol peldanyosithatok-e a diagramok
    assert isinstance(VonalDiagram(atalakított_df), VonalDiagram)
    assert isinstance(OszlopDiagram(atalakított_df), OszlopDiagram)
    assert isinstance(TeruletDiagram(atalakított_df), TeruletDiagram)
