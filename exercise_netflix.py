import pandas as pd

# Load the Netflix dataset
netflix_path = '/Users/lorenzoferrantin/Python-Data-Science-Session6/netflix_titles.csv'
netflix_df = pd.read_csv(netflix_path)

# 1. Check for missing ratings
missing_ratings_count = netflix_df['rating'].isna().sum()
print(f"Missing ratings: {missing_ratings_count}")

# 2. Count the number of films from 2021 corresponding to Italy
country = "Italy" 
films_2021 = netflix_df[(netflix_df['release_year'] == 2021) & 
                        (netflix_df['country'] == country) & 
                        (netflix_df['type'] == "Movie")]
print(f"Number of films from 2021 in {country}: {len(films_2021)}")

# 3. Determine the number of movies in 2020 with complete information
movies_2020 = netflix_df[
    (netflix_df['release_year'] == 2020) & 
    (netflix_df['type'] == "Movie") &
    netflix_df.notna().all(axis=1)
]
print(f"Number of movies in 2020 with complete information: {len(movies_2020)}")

# 4. Identify the year with the most titles released
titles_per_year = netflix_df['release_year'].value_counts()
year_most_titles = titles_per_year.idxmax()
print(f"Year with the most titles: {year_most_titles} ({titles_per_year.max()} titles)")

# 5. Calculate the average number of releases per year since 2010
releases_since_2010 = netflix_df[netflix_df['release_year'] >= 2010]
average_releases = releases_since_2010['release_year'].value_counts().mean()
print(f"Average number of releases per year since 2010: {average_releases:.2f}")