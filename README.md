# book-recommendation-system_flask
Book Recommendation System

Description:
A Book Recommendation System which recommends the users a selection of books based on their interests.

Data used for this project was taken from given data set.

1. Data Cleaning and Pre-Processing
The dataset consists of two tables; books.csv and books_new.csv. Data from all two tables are cleaned and preprocessed separately as defined below briefly:

Title:

Check for the number of null values in each column. There comes 0 null values in the table.
Check for the unique Title. all are unique no duplicates.

Author:

Check for the number of null values in each column. There comes 24 null values in the table.then we deal with this null values.
Check for the unique Author. all are unique no duplicates.

Genre:

Check for the number of null values in each column. There comes 0 null values in the table.
check between genre names "-" or " " space not available.

Publisher:

Check for the number of null values in each column. There comes 96 null values in the table.then we deal with this null values.

Algorithms Implemented:
Content Based Recommendation System
we use Count Vecterizer and Cosine Similarity.
This system recommends books by calculating similarities in Book Titles. For this, Count vectors were created for unigrams and bigrams of Book-Titles; only those books' data has been considered according to Genres.

3. Libraries Used:
ipython-notebook - Python Text Editor
sklearn - Machine learning library
seaborn, matplotlib - Visualization libraries
numpy, scipy- number python library
pandas - data handling library
