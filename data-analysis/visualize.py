import pandas as pd

# Load the data
ratings_df = pd.read_csv("data/Ratings.csv")


books_df = pd.read_csv("data/Books.csv")

user_df = pd.read_csv("data/Users.csv")

ratings_df.set_index('User-ID')
user_df.set_index('User-ID')

merged_df = ratings_df.merge(user_df, on='User-ID' )
print(merged_df)
grouped = ratings_df.groupby('ISBN')['Book-Rating'].agg(['mean', 'count'])

# Rename columns
grouped.columns = ['weight', 'num_people']

# Convert DataFrame group to dictionary
weighted_ratings = grouped.to_dict('index')
top_100_books = grouped.sort_values(by='num_people', ascending=False).head(100)

# From these top 100 books, find the book with the highest weight
best_rated_book = top_100_books.sort_values(by='weight', ascending=False).head(1)


print(books_df[books_df['ISBN']== best_rated_book.index.values[0]])
print(best_rated_book)