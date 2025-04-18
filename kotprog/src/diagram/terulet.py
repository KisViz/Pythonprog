from .alap import Diagram


class TeruletDiagram(Diagram):
    """Területdiagram"""

    def create_chart(self, tengely):
        self.data.pivot(
            index='Dátum',
            columns='Country/Region',
            values='Esetek'
        ).plot.area(ax=tengely, alpha=0.7)
