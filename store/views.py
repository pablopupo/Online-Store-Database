from django.shortcuts import render
from .modules.main import *
from .modules.generateddata import *


def load_data_structures():
    """
    Initialize the BTreeIndex and HashMapIndex with data loaded from a CSV file.

    Returns:
    - b_tree_index: B-tree index loaded with data.
    - hash_map_index: Hash map index loaded with data.
    """
    data = load_data_from_csv()
    if data is not None:
        b_tree_index = BTreeIndex()
        hash_map_index = HashMapIndex()
        for _, row in data.iterrows():
            product_id = row['ProductID']
            price = row['Price']
            b_tree_index.insert(product_id, price)
            hash_map_index.insert(product_id, price)

        return b_tree_index, hash_map_index
    return None, None


def generate_random_data():
    """
    Generates a DataFrame with random ProductIDs and Prices.
    """
    product_ids = random.sample(range(1000000, 2000000), 120000)
    prices = np.random.randint(10, 1000, size=120000)
    itemdata = pd.DataFrame({'ProductID': product_ids, 'Price': prices})
    return itemdata


def manage_data(request):
    productdata = load_data_from_csv()
    if productdata is not None:
        if not productdata.empty:
            context = {"message": f"Data already Generated."}
            return render(request, 'managedata.html', context)
    productdata = generate_random_data()
    save_data_to_csv(productdata)
    context = {"message": f"Data Generated."}
    return render(request, 'managedata.html', context)


def menu(request):
    return render(request, 'menu.html')


def search(request):
    b_tree_index, hash_map_index = load_data_structures()
    if b_tree_index is None or hash_map_index is None:
        return render(request, 'nodata.html')
    if request.method == "POST":
        product_id = int(request.POST.get("product_id"))

        start_time = time.time()
        b_price = b_tree_index.search(product_id)
        end_time = time.time()
        b_time = end_time - start_time

        start_time = time.time()
        h_price = hash_map_index.search(product_id)
        end_time = time.time()
        h_time = end_time - start_time

        context = {
            "product_id": product_id,
            "b_price": b_price,
            "h_price": h_price,
            "b_time": b_time,
            "h_time": h_time,
        }

        return render(request, "search.html", context)
    return render(request, "search.html")


def insert(request):
    b_tree_index, hash_map_index = load_data_structures()
    if b_tree_index is None or hash_map_index is None:
        return render(request, 'nodata.html')
    if request.method == "POST":
        product_id = int(request.POST.get("product_id"))
        price = int(request.POST.get("price"))

        start_time = time.time()
        b_tree_index.insert(product_id, price)
        end_time = time.time()
        b_time = end_time - start_time

        start_time = time.time()
        hash_map_index.insert(product_id, price)
        end_time = time.time()
        h_time = end_time - start_time

        data = load_data_from_csv()
        data.loc[len(data)] = [product_id, price]
        save_data_to_csv(data)

        context = {
            "product_id": product_id,
            "price": price,
            "b_time": b_time,
            "h_time": h_time,
        }

        return render(request, "insert.html", context)
    return render(request, "insert.html")


def delete(request):
    b_tree_index, hash_map_index = load_data_structures()
    if b_tree_index is None or hash_map_index is None:
        return render(request, 'nodata.html')
    if request.method == "POST":
        product_id = int(request.POST.get("product_id"))

        start_time = time.time()
        b_tree_index.delete(product_id)
        end_time = time.time()
        b_time = end_time - start_time

        start_time = time.time()
        hash_map_index.delete(product_id)
        end_time = time.time()
        h_time = end_time - start_time

        data = load_data_from_csv()
        updatedata = data[data['ProductID'] != product_id]
        save_data_to_csv(updatedata)

        context = {
            "product_id": product_id,
            "b_time": b_time,
            "h_time": h_time,
        }

        return render(request, "delete.html", context)
    return render(request, "delete.html")


def sort(request):
    b_tree_index, hash_map_index = load_data_structures()
    if b_tree_index is None or hash_map_index is None:
        return render(request, 'nodata.html')

    b_time, b_sorted = test_sort(b_tree_index)
    h_time, h_sorted = test_sort(hash_map_index)

    context = {
        "b_sorted": b_sorted[:100],
        "h_sorted": h_sorted,
        "b_time": b_time,
        "h_time": h_time,
    }

    return render(request, "sort.html", context)


def performance(request):
    b_tree_index, hash_map_index = load_data_structures()
    if b_tree_index is None or hash_map_index is None:
        return render(request, 'nodata.html')

    data = load_data_from_csv()
    search_keys = random.sample(data['ProductID'].tolist(), 1000)
    delete_keys = random.sample(data['ProductID'].tolist(), 1000)
    new_product_ids = random.sample(range(1000000, 2000000), 1000)
    new_prices = np.random.randint(10, 1000, size=1000)
    insert_items = list(zip(new_product_ids, new_prices))

    b_search_time = test_search(b_tree_index, search_keys)
    b_insert_time = test_insert(b_tree_index, insert_items)
    b_delete_time = test_delete(b_tree_index, delete_keys)
    b_sort_time, _ = test_sort(b_tree_index)

    h_search_time = test_search(hash_map_index, search_keys)
    h_insert_time = test_insert(hash_map_index, insert_items)
    h_delete_time = test_delete(hash_map_index, delete_keys)
    h_sort_time, _ = test_sort(hash_map_index)

    results = pd.DataFrame({
        'Operation': ['Search', 'Insert', 'Delete', 'Sort'],
        'B-Tree Time (s)': [b_search_time, b_insert_time, b_delete_time, b_sort_time],
        'Hash Map Time (s)': [h_search_time, h_insert_time, h_delete_time, h_sort_time]
    })
    results['Speedup (%)'] = ((results['B-Tree Time (s)'] - results['Hash Map Time (s)']) / results[
        'B-Tree Time (s)']) * 100

    results['Speedup (%)'] = results['Speedup (%)'].round(2)
    barchart = plot_speedup_bar_chart(results)
    groupbarchart = plot_grouped_bar_chart(results)
    linechart = plot_line_chart(results)
    piechart = plot_pie_charts(results)
    context = {
        'barchart': barchart,
        'groupbarchart': groupbarchart,
        'linechart': linechart,
        'piechart': piechart,
    }
    return render(request, 'performance.html', context)
