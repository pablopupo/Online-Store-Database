import random
import numpy as np
import pandas as pd
import time
from bintrees import RBTree  # Using RBTree, red-black (self-balancing) tree, as substitute for B-tree (for simplicity).
import matplotlib.pyplot as plt
import seaborn as sns

# Part 1 of Project: Generating Random Data
def generate_random_data(num_products=10000, id_range=(100000, 999999), price_range=(10, 1000)):
    """
    Generates a DataFrame with random ProductIDs and Prices.

    Args:
    - num_products (int): Number of products to generate.
    - id_range (tuple): Range for ProductIDs.
    - price_range (tuple): Range for Prices.

    Returns:
    - pd.DataFrame: DataFrame containing ProductID and Price.
    """
    product_ids = random.sample(range(id_range[0], id_range[1]), num_products)
    prices = np.random.randint(price_range[0], price_range[1], size=num_products)
    data = pd.DataFrame({
        'ProductID': product_ids,
        'Price': prices
    })
    return data

# Part 2: Creating the Data Structures

# B-Tree:
class BTreeIndex:
    def __init__(self):
        self.tree = RBTree()

    def insert(self, key, value):
        self.tree.insert(key, value)

    def delete(self, key):
        try:
            self.tree.remove(key)
        except KeyError:
            print(f"Key {key} not found.")

    def search(self, key):
        try:
            return self.tree[key]
        except KeyError:
            return None

    def sort_items(self):
        return list(self.tree.items())

# HashMap:
class HashMapIndex:
    def __init__(self):
        self.map = {}

    def insert(self, key, value):
        self.map[key] = value

    def delete(self, key):
        if key in self.map:
            del self.map[key]
        else:
            print(f"Key {key} not found.")

    def search(self, key):
        return self.map.get(key, None)

    def sort_items(self):
        return sorted(self.map.items())

# Part 3: Testing and Comparing Efficiency
def test_search(index, keys_to_search):

    def insert(self, key, value):
        self.tree.insert(key, value)

    def delete(self, key):
        try:
            self.tree.remove(key)
        except KeyError:
            print(f"Key {key} not found.")

    def search(self, key):
        try:
            return self.tree[key]
        except KeyError:
            return None

    def sort_items(self):
        return list(self.tree.items())

# HashMap:
class HashMapIndex:
    def __init__(self):
        self.map = {}

    def insert(self, key, value):
        self.map[key] = value

    def delete(self, key):
        if key in self.map:
            del self.map[key]
        else:
            print(f"Key {key} not found.")

    def search(self, key):
        return self.map.get(key, None)

    def sort_items(self):
        return sorted(self.map.items())

# Part 3: Testing and Comparing Efficiency
def test_search(index, keys_to_search):
    start_time = time.time()
    for key in keys_to_search:
        index.search(key)
    end_time = time.time()
    return end_time - start_time

def test_insert(index, items_to_insert):
    start_time = time.time()
    for key, value in items_to_insert:
        index.insert(key, value)
    end_time = time.time()
    return end_time - start_time

def test_delete(index, keys_to_delete):
    start_time = time.time()
    for key in keys_to_delete:
        index.delete(key)
    end_time = time.time()

    start_time = time.time()
    for key in keys_to_search:
        index.search(key)
    end_time = time.time()
    return end_time - start_time

def test_insert(index, items_to_insert):
    start_time = time.time()
    for key, value in items_to_insert:
        index.insert(key, value)
    end_time = time.time()
    return end_time - start_time

def test_delete(index, keys_to_delete):
    start_time = time.time()
    for key in keys_to_delete:
        index.delete(key)
    end_time = time.time()
    return end_time - start_time

def test_sort(index):
    start_time = time.time()
    sorted_items = index.sort_items()
    end_time = time.time()
    return end_time - start_time, sorted_items

# User Interface: Terminal Menu
def display_menu():
    print("\n=== Online Store Database Index System ===")
    print("1. Search Product")
    print("2. Insert Product")
    print("3. Delete Product")
    print("4. Sort Products")
    print("5. Compare Performance")
    print("6. Exit")


def menu(b_tree_index, hash_map_index, results):
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                key = int(input("Enter ProductID to search: "))
                # Search in B-Tree
                b_price = b_tree_index.search(key)
                # Search in Hash Map
                h_price = hash_map_index.search(key)
                print(f"B-Tree: ProductID {key} has Price {b_price}")
                print(f"Hash Map: ProductID {key} has Price {h_price}")
            except ValueError:
                print("Invalid input. Please enter an integer for ProductID.")

        elif choice == '2':
            try:
                key = int(input("Enter new ProductID to insert: "))
                value = int(input("Enter Price: "))
                b_tree_index.insert(key, value)
                hash_map_index.insert(key, value)
                print(f"Inserted ProductID {key} with Price {value} into both indexes.")
            except ValueError:
                print("Invalid input. Please enter integers for ProductID and Price.")

        elif choice == '3':
            try:
                key = int(input("Enter ProductID to delete: "))
                b_tree_index.delete(key)
                hash_map_index.delete(key)
                print(f"Deleted ProductID {key} from both indexes.")
            except ValueError:
                print("Invalid input. Please enter an integer for ProductID.")

        elif choice == '4':
            print("Sorting Products...")
            b_time, b_sorted = test_sort(b_tree_index)
            h_time, h_sorted = test_sort(hash_map_index)
            print(f"B-Tree sorted in {b_time:.6f} seconds.")
            print(f"Hash Map sorted in {h_time:.6f} seconds.")
            # Optionally, display sorted items
            # print("First 5 sorted items (B-Tree):", b_sorted[:5])
            # print("First 5 sorted items (Hash Map):", h_sorted[:5])

        elif choice == '5':
            print("Comparing Performance...")
            print(results)

        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Visualization Functions:

def plot_grouped_bar_chart(results):
    df_melted = results.melt(id_vars="Operation", value_vars=["B-Tree Time (s)", "Hash Map Time (s)"],
                             var_name="Data Structure", value_name="Time (s)")

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Operation', y='Time (s)', hue='Data Structure', data=df_melted, palette='muted')

    plt.title('Operation Times: B-Tree vs Hash Map')
    plt.xlabel('Operation')
    plt.ylabel('Time (seconds)')
    plt.legend(title='Data Structure')
    plt.tight_layout()
    plt.show()


def plot_speedup_bar_chart(results):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Operation', y='Speedup (%)', data=results, palette='pastel')

    plt.title('Speedup of Hash Map over B-Tree per Operation')
    plt.xlabel('Operation')
    plt.ylabel('Speedup (%)')
    plt.ylim(0, results['Speedup (%)'].max() + 10)  # Adding space for labels
    plt.tight_layout()

    for index, row in results.iterrows():
        plt.text(index, row['Speedup (%)'] + 1, f"{row['Speedup (%)']}%", ha='center')

    plt.show()


def plot_pie_charts(results):
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.pie(results['B-Tree Time (s)'], labels=results['Operation'], autopct='%1.1f%%', startangle=140,
            colors=sns.color_palette("Blues"))
    plt.title('B-Tree: Time Distribution per Operation')

    plt.subplot(1, 2, 2)
    plt.pie(results['Hash Map Time (s)'], labels=results['Operation'], autopct='%1.1f%%', startangle=140,
            colors=sns.color_palette("Greens"))
    plt.title('Hash Map: Time Distribution per Operation')

    plt.tight_layout()
    plt.show()


def plot_line_chart(results):
    plt.figure(figsize=(10, 6))

    sns.lineplot(x='Operation', y='B-Tree Time (s)', marker='o', label='B-Tree', data=results, color='blue')
    sns.lineplot(x='Operation', y='Hash Map Time (s)', marker='o', label='Hash Map', data=results, color='green')

    plt.title('Operation Times Comparison: B-Tree vs Hash Map')
    plt.xlabel('Operation')
    plt.ylabel('Time (seconds)')
    plt.legend(title='Data Structure')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Generate data
    print("Generating random data...")
    data = generate_random_data(num_products=100000)

    # Initialize indexes
    print("Initializing data structures...")
    b_tree_index = BTreeIndex()
    hash_map_index = HashMapIndex()

    # Populate indexes
    print("Populating indexes...")
    for _, row in data.iterrows():
        product_id = row['ProductID']
        price = row['Price']
        b_tree_index.insert(product_id, price)
        hash_map_index.insert(product_id, price)
    print("Indexes populated.")

    # Prepare test data
    print("Preparing test data for performance evaluation...")
    search_keys = random.sample(data['ProductID'].tolist(), 1000)
    delete_keys = random.sample(data['ProductID'].tolist(), 1000)
    new_product_ids = random.sample(range(1000000, 2000000), 1000)
    new_prices = np.random.randint(10, 1000, size=1000)
    insert_items = list(zip(new_product_ids, new_prices))
    print("Test data prepared.")

    # Perform tests
    print("Running performance tests...")
    b_search_time = test_search(b_tree_index, search_keys)
    b_insert_time = test_insert(b_tree_index, insert_items)
    b_delete_time = test_delete(b_tree_index, delete_keys)
    b_sort_time, _ = test_sort(b_tree_index)

    h_search_time = test_search(hash_map_index, search_keys)
    h_insert_time = test_insert(hash_map_index, insert_items)
    h_delete_time = test_delete(hash_map_index, delete_keys)
    h_sort_time, _ = test_sort(hash_map_index)

    # Create results DataFrame
    results = pd.DataFrame({
        'Operation': ['Search', 'Insert', 'Delete', 'Sort'],
        'B-Tree Time (s)': [b_search_time, b_insert_time, b_delete_time, b_sort_time],
        'Hash Map Time (s)': [h_search_time, h_insert_time, h_delete_time, h_sort_time]
    })
    results['Speedup (%)'] = ((results['B-Tree Time (s)'] - results['Hash Map Time (s)']) / results[
        'B-Tree Time (s)']) * 100

    # Round the percentage for better readability
    results['Speedup (%)'] = results['Speedup (%)'].round(2)

    print("Performance tests completed.")

    # Start the menu
    menu(b_tree_index, hash_map_index, results)