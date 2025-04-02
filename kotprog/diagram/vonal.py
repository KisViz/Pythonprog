import seaborn as sns

from diagram.alap import Diagram


class VonalDiagram(Diagram):
    """vonaldiagram"""

    def create_chart(self, tengely):
        sns.lineplot(
            data=self.data,
            x='Dátum',
            y='Esetek',
            hue='Country/Region',
            ax=tengely
        )
