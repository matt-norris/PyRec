import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# Load movie ratings data into a Pandas DataFrame
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')

# Load movie metadata into a Pandas DataFrame
movies_df = pd.read_csv('ml-latest-small/movies.csv')

# Merge the ratings and movies data on the movieId column
merged_df = pd.merge(ratings_df, movies_df, on='movieId')

# Filter out movies with fewer than 10 ratings
movie_ratings_count = merged_df['movieId'].value_counts()
popular_movies = movie_ratings_count[movie_ratings_count >= 10].index
merged_df = merged_df[merged_df['movieId'].isin(popular_movies)]

# Filter out users with fewer than 10 ratings
user_ratings_count = merged_df['userId'].value_counts()
active_users = user_ratings_count[user_ratings_count >= 10].index
merged_df = merged_df[merged_df['userId'].isin(active_users)]

# Convert ratings to numerical data type
merged_df['rating'] = pd.to_numeric(merged_df['rating'])

# Pivot the merged DataFrame into a movie-user rating matrix
movie_user_matrix = merged_df.pivot(index='movieId', columns='userId', values='rating')

# Fill NaN values with 0
movie_user_matrix.fillna(0, inplace=True)

# Calculate item-item similarity using cosine similarity
item_similarity = cosine_similarity(movie_user_matrix.T)

# Convert the similarity matrix into a DataFrame
item_similarity_df = pd.DataFrame(item_similarity, index=movie_user_matrix.columns, columns=movie_user_matrix.columns)

# Define a function to make movie recommendations for a given user
def get_movie_recommendations(user_id, n=10):
    # Get the user's rated movies
    user_rated_movies = ratings_df[ratings_df['userId'] == user_id]['movieId'].values

    # Filter out movieIds not present in item_similarity_df
    user_rated_movies = list(filter(lambda x: x in item_similarity_df.index, user_rated_movies))

    # Calculate item similarity
    similar_items = item_similarity_df.loc[user_rated_movies].sum().sort_values(ascending=False)

    # Filter out movies that the user has already rated
    similar_items = similar_items[~similar_items.index.isin(user_rated_movies)]

    # Get the top n recommended movies
    recommended_movies = similar_items.head(n)

    # Get the movie titles corresponding to the movieIds
    recommended_movie_titles = movies_df[movies_df['movieId'].isin(recommended_movies.index)]['title']

    # Print the list of recommended movie titles
    print("Recommended Movies:")
    for title in recommended_movie_titles:
        print("- " + title)
    return recommended_movie_titles.tolist()

if __name__ == '__main__':
    get_movie_recommendations(1, 10)
