import streamlit as st
import pandas as pd
from .diagram import VonalDiagram, OszlopDiagram, TeruletDiagram


"""
A streamlitet hallásból ismertem már, de még nem póbáltam ki ezelőtt.
Utánanézés után azért válaszottam a webes felület megavlósításhoz, mert nem
kellett így külön html-lel, css-sel foglalkoznom, de egy viszonylag igényes,
modern felültet kaptam így is. Emellet az is hasznos vol, hogy jól támogatja
a pandast és ezért jól tudtam használni a feldolgozott adatok egjelenítésére.
https://youtu.be/2siBrMsqF44?si=GJCR6ViMTr1cy-fT
https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/
ez a videó kimondottan hasznos volt a pandasos részhez is:
https://youtu.be/8W8NQFFbDcU?si=6YczQjV_La_hNcDp
"""


# adarokat betoltjuk
def betolt_adatok():
    return pd.read_csv('csv/feldolgozott/fertozottek.csv')
    # dataframebe tolti az adatokat es visszaadja


def main():

    # leerjuk az adatokat
    df = betolt_adatok()

    # orszagok oszlop
    orszagok = df['Country/Region'].unique()

    # beallitgatjuk az oldalt
    st.title('COVID-19 Adatvizualizáció')

    # orszag valaszto
    st.sidebar.header('Beállítások')
    kivalasztott_orszagok = st.sidebar.multiselect(
        'Válassz országokat', orszagok
    )

    # datumook
    datum_oszlopok = [
        oszlop for oszlop in df.columns
        if oszlop != 'Country/Region'
    ]
    min_datum = pd.to_datetime(datum_oszlopok).min()
    max_datum = pd.to_datetime(datum_oszlopok).max()

    st.sidebar.subheader("Dátumkiválasztás")

    kezdo_datum = st.sidebar.date_input(
        'Kezdő dátum',
        value=min_datum,
        min_value=min_datum,
        max_value=max_datum
    )

    vegso_datum = st.sidebar.date_input(
        'Végdátum',
        value=max_datum,
        min_value=pd.to_datetime(kezdo_datum),  # a vege nem lehet hamarabb
        max_value=max_datum
    )

    # diagram tipus valasztas
    st.sidebar.subheader("Diagram típusa")

    diagram_tipus = st.sidebar.selectbox(
        'Diagram',
        ['Vonal', 'Oszlop', 'Terület']
    )

    # adatok kiszedese
    szurt_df = df[df['Country/Region'].isin(kivalasztott_orszagok)]

    # ez a diagrammokhoz kell, mert nem feltetlenul jo nekik sorban
    # az edat a melt pedig beteszi a datumok az esetszam melle oszlopos modon
    atalakított_df = szurt_df.melt(
        id_vars='Country/Region',
        var_name='Dátum',
        value_name='Esetek'
    )
    atalakított_df['Dátum'] = pd.to_datetime(atalakított_df['Dátum'])

    # csak a kivalsztott tartomany szerepeljen a datumok kozott a diagrammokon
    atalakított_df = atalakított_df[
        (atalakított_df['Dátum'] >= pd.to_datetime(kezdo_datum)) &
        (atalakított_df['Dátum'] <= pd.to_datetime(vegso_datum))
    ]

    # diagammok
    chart = None
    if diagram_tipus == 'Vonal':
        chart = VonalDiagram(atalakított_df)
    elif diagram_tipus == 'Oszlop':
        chart = OszlopDiagram(atalakított_df)
    elif diagram_tipus == 'Terület':
        chart = TeruletDiagram(atalakított_df)

    if chart:
        chart.show()

    # siman tablakent megjeleniti az adatot
    if st.checkbox('Mutasd a nyers adatokat'):
        st.subheader('Nyers adatok')
        st.write(szurt_df)


if __name__ == '__main__':
    main()
