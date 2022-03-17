import seaborn as sns
import matplotlib.pyplot as plt

# Correlation between X and y
def corrs_graph(df_in):
    corr_matrix = df_in.corr()
    fig, ax = plt.subplots(figsize=(16,12))
    ax = sns.heatmap(corr_matrix, annot=True, linewidths=0.5, fmt=".2f", cmap="Blues")
    plt.show()
    
    
def corrs_X_y(df_in, y):    
    # Find correlations with the Target and sort
    correlations = df_in.corr()[y].sort_values()

    # Display correlations with Target
    print('Most Positive Correlations with Target:')
    print(correlations.dropna().tail(10))

    print()

    print('Most Negative Correlations with Target:') 
    print(correlations.dropna().head(10))


def plot_two_series(series_1, series_2, x_label, y_label, legend, title):
    """
    Plot two series in one plot
    """
    plt.plot(series_1,'-o')
    plt.plot(series_2,'-o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(legend)
    plt.title(title)
    plt.show()