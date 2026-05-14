import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("netflix_titles.csv")

# -----------------------------
# BASIC EDA
# -----------------------------

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# -----------------------------
# DATA CLEANING
# -----------------------------

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = df['date_added'].fillna("Not Available")
df['rating'] = df['rating'].fillna("Unknown")
df['duration'] = df['duration'].fillna("Unknown")

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# -----------------------------
# MOVIES VS TV SHOWS
# -----------------------------

print("\nMOVIES VS TV SHOWS")
print(df['type'].value_counts())

# -----------------------------
# TOP 10 COUNTRIES
# -----------------------------

print("\nTOP 10 COUNTRIES")

top_countries = df['country'].value_counts().head(10)

print(top_countries)

# -----------------------------
# TOP 10 RATINGS
# -----------------------------

print("\nTOP RATINGS")

print(df['rating'].value_counts().head(10))

# -----------------------------
# RELEASE YEAR ANALYSIS
# -----------------------------

print("\nLATEST RELEASE YEARS")

print(df['release_year'].value_counts().head(10))

# -----------------------------
# DATA VISUALIZATION
# -----------------------------

sns.set_style("whitegrid")

# -----------------------------
# GRAPH 1 - Movies vs TV Shows
# -----------------------------

plt.figure(figsize=(6,5))

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows on Netflix")

plt.xlabel("Type")

plt.ylabel("Count")
plt.savefig("movies_vs_tvshows.png")
plt.show()

# -----------------------------
# GRAPH 2 - Top 10 Countries
# -----------------------------

plt.figure(figsize=(12,6))

top_countries.plot(kind='bar')

plt.title("Top 10 Countries with Most Netflix Content")

plt.xlabel("Country")

plt.ylabel("Number of Shows")

plt.xticks(rotation=45)
plt.savefig("top_10_countries.png")
plt.show()

# -----------------------------
# GRAPH 3 - Content Released Per Year
# -----------------------------

plt.figure(figsize=(12,6))

df['release_year'].value_counts().head(15).plot(kind='bar')

plt.title("Top Release Years")

plt.xlabel("Year")

plt.ylabel("Number of Releases")
plt.savefig("content_released_per_year.png")
plt.show()

# -----------------------------
# GRAPH 4 - Ratings Distribution
# -----------------------------

plt.figure(figsize=(12,6))

df['rating'].value_counts().head(10).plot(kind='bar')

plt.title("Ratings Distribution")

plt.xlabel("Rating")

plt.ylabel("Count")

plt.xticks(rotation=45)
plt.savefig("ratings_distribution.png")
plt.show()

# -----------------------------
# FINAL INSIGHTS
# -----------------------------

print("\nFINAL INSIGHTS")

print("1. Netflix has more Movies than TV Shows.")

print("2. United States has the highest amount of content.")

print("3. TV-MA is the most common rating.")

print("4. Content increased rapidly after 2015.")

print("5. Missing values were cleaned successfully.")