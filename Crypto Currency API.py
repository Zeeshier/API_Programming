import requests
import csv
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Define the list of cryptocurrencies to fetch
cryptocurrencies = ['bitcoin', 'ethereum', 'dogecoin', 'litecoin', 'ripple']

# URL for the API
url = 'https://api.coingecko.com/api/v3/simple/price'

# Parameters for the API
params = {
    'ids': ','.join(cryptocurrencies),
    'vs_currencies': 'usd'
}

def fetch_crypto_prices():
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror('Error', f'An error occurred: {e}')
        return None

def save_to_csv(data):
    filename = f"cryptocurrency_prices_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        fieldnames = ["Currency", "Price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for currency, price in data.items():
            writer.writerow({'Currency': currency.capitalize(), 'Price': f"${price['usd']:.2f}"})

def update_gui(data):
    for crypto, price in data.items():
        # Format the price to show two decimal places
        formatted_price = f"${price['usd']:.2f}"
        tree.insert('', 'end', values=(crypto.capitalize(), formatted_price))

def refresh_data():
    # Clear the existing data in the treeview
    for row in tree.get_children():
        tree.delete(row)
    
    # Fetch new data
    data = fetch_crypto_prices()
    if data:
        update_gui(data)
        save_to_csv(data)

# Initialize the Tkinter GUI
root = tk.Tk()
root.title('Crypto Currency Prices')

# Create the treeview widget
tree = ttk.Treeview(root, columns=("CryptoCurrency", "Price"), show='headings')
tree.heading('CryptoCurrency', text='Crypto Currency')
tree.heading('Price', text='Price (USD)')
tree.pack(fill=tk.BOTH, expand=True)

# Add a refresh button to the GUI
refresh_button = tk.Button(root, text='Refresh Data', command=refresh_data)
refresh_button.pack(pady=10)

# Fetch initial data when the program starts
initial_data = fetch_crypto_prices()
if initial_data:
    update_gui(initial_data)
    save_to_csv(initial_data)

# Start the Tkinter main loop
root.mainloop()
