import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.sentiment.util import mark_negation
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import os

# Download NLTK resources
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

file_path = "winemag-data-130k-v2.csv"

# Load the dataset
data = pd.read_csv(file_path)
data["description"] = data["description"].str.replace("[^a-zA-Z0-9 ]", " ", regex=True)
data.dropna(subset=["description", "country", "price"], inplace=True)
data.drop_duplicates(subset=["title", "description"], inplace=True)


# Function to extract meaningful keywords from user inputs
def extract_keywords(text):
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    # Filtering for nouns and adjectives
    keywords = [word for word, tag in tagged_tokens if tag in ("NN", "NNS", "JJ")]
    return keywords


# Function to check for negation in the description column
def is_negated(description, taste_keywords):
    tokens = nltk.word_tokenize(description.lower())
    negated_tokens = mark_negation(tokens)
    for keyword in taste_keywords:
        if "not_" + keyword.lower() in negated_tokens:
            return True
    return False


# Function to get recommendations based on country and taste preferences
def get_recommendations(data, country_preference, taste_preference):
    # Normalize country preference
    country_preference = (
        country_preference.upper() if country_preference else country_preference
    )

    # Converting to lower case and extracting keywords
    processed_taste_keywords = extract_keywords(taste_preference.lower())

    # Filter wines based on the users country preference if that is provided
    if country_preference:
        filtered_wines = data[data["country"].str.upper() == country_preference].copy()
    else:
        filtered_wines = data.copy()

    # Removes wines with descriptions that negate the taste preferences ("not sweet")
    filtered_wines = filtered_wines[
        ~filtered_wines["description"].apply(
            lambda x: is_negated(x, processed_taste_keywords)
        )
    ]

    # Apply TF-IDF and cosine similarity to the filtered wines using extracted keywords
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 1))
    tfidf_matrix = vectorizer.fit_transform(filtered_wines["description"])
    preference_vector = vectorizer.transform([" ".join(processed_taste_keywords)])
    similarity_scores = cosine_similarity(tfidf_matrix, preference_vector)
    filtered_wines["similarity_score"] = similarity_scores.flatten()

    # Rank the wines by similarity score,
    # If two wines have the same simliarity score, sort by points in descending order
    ranked_wines = filtered_wines.sort_values(
        by=["similarity_score", "points"], ascending=[False, False]
    )

    # Select the top 9 wines to show on the page
    top_9_wines = ranked_wines.head(9)

    # The columns to be displayed
    columns_to_display = [
        "title",
        "description",
        "points",
        "price",
        "country",
        "province",
        "similarity_score",
    ]

    # Returns the to recommended wines as a list of dictionaries
    return top_9_wines[columns_to_display].to_dict(orient="records")
