from abc import ABC, abstractmethod

import streamlit as st
import matplotlib.pyplot as plt

class Diagram(ABC):
    """
    Alap osztaly a diarammokhoz
    wow, lehet ilyet is
    ezt meg nem probaltam
    """

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def create_chart(self, tengely):
        pass

    def show(self):
        """megjelenites"""

        #letrehozzuk az abrat
        abra, tengely = plt.subplots(figsize=(12, 6))
        self.create_chart(tengely)

        #beallitjuk adolgokat
        plt.xticks(rotation=45)
        plt.title('COVID-19 esetszámok időbeli alakulása')
        plt.ylabel('Esetek száma')
        plt.xlabel('Dátum')

        #megjelenitjuk az oldalon
        st.pyplot(abra)