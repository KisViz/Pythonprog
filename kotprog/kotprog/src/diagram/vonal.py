import seaborn as sns

from .alap import Diagram


class VonalDiagram(Diagram):
    """Vonaldiagram"""

    def create_chart(self, tengely):
        sns.lineplot(
            data=self.data,
            x='Dátum',
            y='Esetek',
            hue='Country/Region',
            ax=tengely
        )
