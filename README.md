Amazon 2.0: Database Index System
Project Overview
Amazon 2.0 is a database indexing system designed to explore the performance differences between B-Trees (implemented as Red-Black Trees using bintrees) and Hash Maps. This project aims to determine the most efficient data structure for storing and managing product data in an online store setting, focusing on search, insert, delete, and sort operations.

The findings of this project provide valuable insights into the strengths and trade-offs of these two popular data structures for large-scale data indexing.

Features

Data Generation:
Randomly generate product data (ProductID and Price) using Python libraries.
Data Structures:
Implemented Red-Black Tree (as a substitute for B-Tree) and Hash Map for data storage and operations.
CRUD Operations:
Efficiently search, insert, delete, and sort data.
Performance Testing:
Measure and compare operation times for both data structures.
Visualization:
Use matplotlib and seaborn for detailed performance plots.
Web Interface:
A Django-powered web interface to display performance visualizations.
Visualization:
Use matplotlib and seaborn to generate plots for performance analysis.

Visualizations

Speedup Bar Chart: Highlights the performance advantage of Hash Maps over B-Trees for each operation.
Operation Times Comparison Chart: Compares operation times between the two data structures.
Time Distribution Pie Charts: Breaks down operation times for B-Trees and Hash Maps.
Line Chart: Shows trends in operation performance for both data structures.

Tools and Libraries

Programming Language: Python
Libraries Used:
bintrees - For Red-Black Tree implementation.
pandas - For data generation and manipulation.
numpy - For efficient numerical operations.
matplotlib and seaborn - For visualizing performance results.
random - For generating random product IDs and prices.
Django - For hosting performance visualizations.

Contributors

Pablo Pupo
Myiah Stubbs

References

Pandas Library. (n.d.). pandas. Retrieved from https://pandas.pydata.org/
bintrees Library. (n.d.). bintrees. Retrieved from https://pypi.org/project/bintrees/
Django Documentation. (n.d.). Django. Retrieved from https://www.djangoproject.com/
Matplotlib Documentation. (n.d.). matplotlib. Retrieved from https://matplotlib.org/
Seaborn Documentation. (n.d.). seaborn. Retrieved from https://seaborn.pydata.org/
NumPy Documentation. (n.d.). NumPy. Retrieved from https://numpy.org/
Python Software Foundation. (n.d.). Python Documentation. Retrieved from https://docs.python.org/3/
