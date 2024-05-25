from load_csv import load
import matplotlib.pyplot as plt


def projection_life():
    """
    Plots a scatter plot of GDP per capita against
    life expectancy for a specified year.
    """
    try:
        gdp_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        population_path = "life_expectancy_years.csv"

        gdp = load(gdp_path)
        population = load(population_path)

        if (gdp is None or population is None):
            raise AssertionError("Failed to load data.")

        year = "1900"
        gdp_for_year = gdp[year]
        population_for_year = population[year]

        plt.figure(figsize=(10, 6))
        plt.scatter(gdp_for_year, population_for_year)
        plt.title(year)

        plt.xlabel('Gross domestic product')
        plt.ylabel("Life expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])

        plt.tight_layout()
        plt.show()
    except AssertionError as err:
        print("\033[31m", AssertionError.__name__ + ":", err, "\033[0m")


def main():
    """Driver main function"""
    projection_life()


if __name__ == "__main__":
    main()
