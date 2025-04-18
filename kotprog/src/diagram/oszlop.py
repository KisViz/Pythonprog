import seaborn as sns
from matplotlib import pyplot as plt
from .alap import Diagram


class OszlopDiagram(Diagram):
    """Oszlopdiagram"""

    def create_chart(self, tengely):
        # datumok hetenkent, hogy ne legyen egy fkete kocka (ehhez kellett egy kis help:'))
        self.data['Dátum_csoport'] = self.data['Dátum'].dt.to_period('W').dt.to_timestamp()
        grouped_df = self.data.groupby(['Dátum_csoport', 'Country/Region'])['Esetek'].mean().reset_index()

        sns.barplot(
            data=grouped_df,
            x='Dátum_csoport',
            y='Esetek',
            hue='Country/Region',
            ax=tengely
        )

        # ez azert kell, hogy az x tengely normalisan nezzen ki, max 10 cimke lehet
        tengely.xaxis.set_major_locator(plt.MaxNLocator(10))
