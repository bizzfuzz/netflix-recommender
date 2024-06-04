"""
Combined Data Module

Opens and extracts data from combined data files.
Also serializes the files into more lightweight
feather format if not already serialized.
"""
import os
import pandas as pd

#can be tuned from 1-4. with all 4 files having 100M+ records
LAST_FILE = 2

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

def load_feather_file(index):
    """
    load specific feathe file
    """
    return pd.read_feather(get_feather_path(index))

def dataframe_to_feather(df, filename):
    """
    serializes dataframe to feather format
    """
    df.to_feather(filename)

def combined_ratings_path():
    """
    returns path to feather file with dataframe
    of all ratings
    """
    return "feather-data/combined-ratings.feather"

def load_combined_ratings():
    """
    loads serialized combined ratings
    """
    return pd.read_feather(combined_ratings_path())

def ratings_serialized():
    """
    check if combined ratings already serialized
    """
    return os.path.exists(combined_ratings_path())

def feather_convert_all():
    """
    converts all txt files in repo
    """
    index = 1
    while index <= LAST_FILE:
        feather_convert_txt(index)
        index+= 1

def feather_convert_txt(index):
    """
    converts large combined data txt files into
    feather files and stores them in the feather folder
    for faster repeated testing.
    Skips if file already converted.
    """
    feather_path = get_feather_path(index)

    if not os.path.exists(feather_path):
        path = get_path(index)
        data = load_combined_data(path)
        df = pd.DataFrame(data)
        df.to_feather(feather_path)

def initialize_all_data():
    """
    if data not combined and serialize,
    prepares the data for analysis
    """
    if not ratings_serialized():
        feather_convert_all()
        serialize_ratings(load_all_ratings())

def load_all_ratings():
    """
    loads all 4 combined_data files and combines them
    into one dataframe
    """
    df = load_feather_file(1)
    index = 2
    while index <= LAST_FILE:
        df = pd.concat([df, load_feather_file(index)], axis=0)
        index += 1
    return df

def serialize_ratings(df):
    """saves rating dataframe as a feather file"""
    path = combined_ratings_path()
    if not os.path.exists(path):
        dataframe_to_feather(df, path)