import MySQLdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TopMovies():
    """
    Display histograms and scatter plots using data from imdb_data.top_movies
    """
    def __init__(self, con):
        self.con = con

    def plot_histogram(self, col_name):
        # Generate pandas dataframe and prepare x-axis
        sql = 'SELECT {} FROM top_movies'.format(col_name)
        df = pd.read_sql(sql, self.con)
        x_axis = np.array(df[[col_name]])[:,0]

        # Clear plot, add properties, and then show plot
        # plt.clf()
        plt.hist(x_axis)
        plt.xlabel(col_name)
        plt.ylabel('frequency')
        plt.show()

    def plot_scatter(self, first_col, second_col):
        # Generate pandas dataframe and prepare x and y axes
        sql = 'SELECT {}, {} FROM top_movies'.format(first_col, second_col)
        df = pd.read_sql(sql, self.con)
        x_axis = np.array(df[[first_col]])[:,0]
        y_axis = np.array(df[[second_col]])[:,0]

        # Clear plot, add properties, and then show plot
        # plt.clf()
        plt.scatter(x_axis, y_axis)
        plt.xlabel(first_col)
        plt.ylabel(second_col)
        plt.show()

# Create a connection to database imdb_data
con = MySQLdb.connect(host='localhost', port=3306, user='guest', \
                      passwd='password', db='imdb_data')

# Create and display a scatter plot of movie ratings vs their ranks
movies = TopMovies(con)
movies.plot_scatter('rating', 'rank')