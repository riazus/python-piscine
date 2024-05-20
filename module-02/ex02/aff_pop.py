from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def aff_pop():
    try:
        path = "population_total.csv"
        campus = "France"
        vs_campus = "Russia"

        table = load(path)
        if (table is None):
            raise AssertionError("Failed to load data.")

        france_data = table[table['country'] == campus]
        russia_data = table[table['country'] == vs_campus]

        years = france_data.columns[1:]
        population_fr = france_data.values[0][1:]
        population_ru = russia_data.values[0][1:]

        population_fr = [float(value[:-1]) * 1e6 if value.endswith('M') else
                         float(value[:-1]) * 1e3 for value in population_fr]
        population_ru = [float(value[:-1]) * 1e6 if value.endswith('M') else
                         float(value[:-1]) * 1e3 for value in population_ru]

        plt.plot(years, population_fr, label=campus)
        plt.plot(years, population_ru, label=vs_campus)

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.xticks(years[::40], rotation=45)
        plt.ylabel('Population')

        plt.legend()

        def millions_formatter(x, pos):
            return f'{x/1e6:.0f}M'

        plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

        plt.tight_layout()
        plt.show()
    except AssertionError as err:
        print("\033[31m", AssertionError.__name__ + ":", err, "\033[0m")


def main():
    aff_pop()


if __name__ == "__main__":
    main()
