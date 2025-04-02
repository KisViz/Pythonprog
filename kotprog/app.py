import streamlit as st
import pandas as pd
from diagram import *


#adarokat betoltjuk
def betolt_adatok():
    return pd.read_csv('csv/feldolgozott/fertozottek.csv')
    #dataframebe tolti az adatokat es visszaadja

def main():

    #leerjuk az adatokat
    df = betolt_adatok()

    #orszagok oszlop
    orszagok = df['Country/Region'].unique()

    #beallitgatjuk az oldalt
    st.title('COVID-19 Adatvizualizáció')

    #orszag valaszto
    st.sidebar.header('Beállítások')
    kivalasztott_orszagok = st.sidebar.multiselect(
        'Válassz országokat', orszagok
    )

    #datumook
    datum_oszlopok = [oszlop for oszlop in df.columns if oszlop != 'Country/Region']
    min_datum = pd.to_datetime(datum_oszlopok).min()
    max_datum = pd.to_datetime(datum_oszlopok).max()
    kezdo_datum, vegso_datum = st.sidebar.date_input(
        'Dátumtartomány',
        value=(min_datum, max_datum),
        min_value=min_datum,
        max_value=max_datum
    )

    #diagram tipus valasztas
    diagram_tipus = st.sidebar.selectbox(
        'Diagram típusa',
        ['Vonal', 'Oszlop', 'Terület']
    )

    #adatok kiszedese
    szurt_df = df[df['Country/Region'].isin(kivalasztott_orszagok)]

    #ez a diagrammokhoz kell, mert nem feltetlenul jo nekik sorban
    #az edat a melt pedig beteszi a datumok az esetszam melle oszlopos modon
    atalakított_df = szurt_df.melt(
        id_vars='Country/Region',
        var_name='Dátum',
        value_name='Esetek'
    )
    atalakított_df['Dátum'] = pd.to_datetime(atalakított_df['Dátum'])

    #csak a kivalsztott tartomany szerepeljen a datumok kozott a diagrammokon
    atalakított_df = atalakított_df[
        (atalakított_df['Dátum'] >= pd.to_datetime(kezdo_datum)) &
        (atalakított_df['Dátum'] <= pd.to_datetime(vegso_datum))
    ]


    st.header('COVID-19 esetszámok összehasonlítása')

    #diagammok
    chart = None
    if diagram_tipus == 'Vonal':
        chart = VonalDiagram(atalakított_df)
    elif diagram_tipus == 'Oszlop':
        chart = OszlopDiagram(atalakított_df)
    elif diagram_tipus == 'Terület':
        chart = TeruletDiagram(atalakított_df)

    if chart:
        chart.show()

    #siman tablakent megjeleniti az adatot
    if st.checkbox('Mutasd a nyers adatokat'):
        st.subheader('Nyers adatok')
        st.write(szurt_df)


if __name__ == '__main__':
    main()