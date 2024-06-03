"""
Combined Data Module

Opens and extracts data from combined data files.
Also serializes the files into more lightweight
feather format if not already serialized.
"""
import os
import pandas as pd

LAST_FILE = 4

def get_path(number):
    """
    creates path to the relevant combined
    data file
    """
    return f"netflix-data/combined_data_{number}.txt"

def get_feather_path(number):
    """
    creates path to the relevant feather
    data file
    """
    return f"feather-data/combined_data_{number}.feather"

def load_combined_data(path):
    """
    function that opens
    combined_data_{number}.txt files
    and extracts the data
    """
    movies, users, ratings = [],[],[]

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.endswith(":"):#lines with movie id's end in ":", rest are structured like a csv
                movie = line.rstrip(":")
            elif line:# is not empty
                user, rating, _ = line.split(",")
                movies.append(int(movie))
                users.append(int(user))
                ratings.append(int(rating))
    return {
        "movie":movies,
        "user":users,
        "rating":ratings
    }

def feather_conversion():
    """
    converts large combined data files into
    feather files and stores them in the feather folder
    for faster repeated testing
    """
    index = 1
    while index <= LAST_FILE:
        feather_path = get_feather_path(index)

        if not os.path.exists(feather_path):
            path = get_path(index)
            data = load_combined_data(path)
            df = pd.DataFrame(data)
            df.to_feather(feather_path)
