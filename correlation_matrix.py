import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Correlation:
    FIGURE_SIZE = (20, 20)

    def __init__(self, df):
        self.df = df
        self.figure_size = self.FIGURE_SIZE

    def create_correlation_matrix(self):
        plt.figure(figsize=self.FIGURE_SIZE)
        corr_mat = self.df.corr(numeric_only=True)
        return sns.heatmap(corr_mat, annot=True)

    def create_correlation_matrix_triangle(self):
        plt.figure(figsize=self.FIGURE_SIZE)
        corr_mat_type_two = self.df.corr()
        mask = np.triu(np.ones_like(corr_mat_type_two, dtype=bool))
        corr_mat =  corr_mat_type_two.mask(mask)
        return sns.heatmap(corr_mat, annot=True)

    def filter_most_correlated_features(self):
        plt.figure(figsize=self.FIGURE_SIZE)
        corr = self.df.corr().abs()
        trimask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(corr, cmap='RdYlGn_r', mask=trimask | (np.abs(corr) <= 0.4), annot=True)

    def show_column_desc_order(self, column_name):
        corr = self.df.corr().abs()
        column_correlation = corr[column_name]
        # last_column = corr.iloc[:, -1]
        return column_correlation.sort_values(ascending=False)