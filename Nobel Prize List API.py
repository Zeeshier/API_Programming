import requests
import matplotlib.pyplot as plt
from collections import defaultdict

def fetch_nobel_data():
    url = "http://api.nobelprize.org/v1/prize.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

def process_nobel_data(data):
    prizes_per_category = defaultdict(lambda: defaultdict(int))

    for prize in data['prizes']:
        year = int(prize['year']) 
        category = prize['category']
        prizes_per_category[category][year] += 1
    
    return prizes_per_category

def plot_nobel_data(prizes_per_category, separate_plots=True):
    """
    Plots the Nobel prize data.
    
    Args:
        prizes_per_category (dict): Dictionary of prizes per category per year.
        separate_plots (bool): If True, create separate plots for each category.
                               If False, plot all categories in the same figure.
    """
    if separate_plots:
        for category, year_data in prizes_per_category.items():
            plt.figure(figsize=(8, 5))
            sorted_years = sorted(year_data.items())
            years, counts = zip(*sorted_years)
            plt.plot(years, counts, marker='o', label=category)
            plt.title(f'Trend of Nobel Prizes in {category.capitalize()} over the Years')
            plt.xlabel('Year')
            plt.ylabel('Number of Prizes')
            plt.legend(title='Category')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
    else:
        plt.figure(figsize=(10, 6))
        for category, year_data in prizes_per_category.items():
            sorted_years = sorted(year_data.items())
            years, counts = zip(*sorted_years)
            plt.plot(years, counts, marker='o', label=category)
        plt.title('Trends of Nobel Prizes Awarded per Category over the Years')
        plt.xlabel('Year')
        plt.ylabel('Number of Prizes')
        plt.legend(title='Category')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def main():
    data = fetch_nobel_data()
    if data:
        prizes_per_category = process_nobel_data(data)
        plot_nobel_data(prizes_per_category, separate_plots=True)

if __name__ == '__main__':
    main()
