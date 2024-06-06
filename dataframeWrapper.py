"""
"""
from pandas import DataFrame


class DataFrameWrapper():
    """
    Class to simplify dataframe operations
    """
    def __init__(self, df:DataFrame):
        self.df = df
    
    def column_search(self, conditions:list):
        """
        searches dataframe column for specific value
        """
        first_condition = conditions[0]
        #print(conditions[0])
        filtered = self.df[self.df[first_condition[0]] == first_condition[1]]
        if len(conditions) > 1:
            index = 0
            for condition in conditions:
                if index == 0:
                    index += 1
                    continue
                column = condition[0]
                search = condition[1]
                filtered = filtered[filtered[column] == search]
        return filtered
    
    def drop_column(self, column:str):
        """"""
        self.df.drop(column, axis=1, inplace=True)
    
    def drop_columns(self, columns:list):
        """"""
        for column in columns:
            self.drop_column(column)
    
    def random_rows(self, number):
        return self.df.sample(n=number)
    
    def head(self, n):
        return self.df.head(n)
    def first_column_value(self, column):
        return self.df[column].head(1).values[0]