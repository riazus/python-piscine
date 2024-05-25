from load_csv import load
import matplotlib.pyplot as plt


def aff_life():
    """
    Plots the life expectancy trend over the years for a specified country.
    """
    try:
        path = "life_expectancy_years.csv"
        campus = "France"

        table = load(path)
        if (table is None):
            raise AssertionError("Failed to load data.")

        france_data = table[table['country'] == campus]
        years = france_data.columns[1:]
        life_expectancy = france_data.values[0][1:]

        plt.plot(years, life_expectancy)
        plt.title('Life Expectancy in France Over the Years')
        plt.xlabel('Year')
        plt.xticks(years[::40], rotation=45)
        plt.ylabel('Life Expectancy')
        plt.yticks(range(30, 101, 10))
        plt.tight_layout()
        plt.show()
    except AssertionError as err:
        print("\033[31m", AssertionError.__name__ + ":", err, "\033[0m")


def main():
    """Driver main function"""
    aff_life()


if __name__ == "__main__":
    main()
