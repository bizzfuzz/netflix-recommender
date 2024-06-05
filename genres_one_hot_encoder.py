"""

"""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer

# Custom transformer to split genres column and perform one-hot encoding
class GenresOneHotEncoder(BaseEstimator, TransformerMixin):
    """
    
    """
    def __init__(self):
        """"""
        self.mlb = MultiLabelBinarizer()

    def fit(self, X):
        # Split the genres column into a list of categories
        genres = X['genres'].str.split(',')
        # Fit MultiLabelBinarizer
        self.mlb.fit(genres)
        return self

    def transform(self, X):
        # Split the genres column into a list of categories
        genres = X['genres'].str.split(', ')
        # Perform one-hot encoding using MultiLabelBinarizer
        one_hot_encoded = self.mlb.transform(genres)
        # Create a DataFrame with one-hot encoded columns
        one_hot_encoded_df = pd.DataFrame(one_hot_encoded, columns=self.mlb.classes_)
        return one_hot_encoded_df