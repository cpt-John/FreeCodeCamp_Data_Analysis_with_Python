import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots()

    # Create scatter plot
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, * \
        _ = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    years = list(range(df['Year'][0], 2051))
    r_x = pd.Series(years)
    r_y = slope*r_x + intercept
    ax.plot(r_x, r_y, 'r')

    # Create second line of best fit
    sub_years_df = df[df['Year'] >= 2000]
    slope, intercept, * \
        _ = linregress(x=sub_years_df['Year'],
                       y=sub_years_df['CSIRO Adjusted Sea Level'])
    years = list(range(sub_years_df['Year'].iloc[0], 2051))
    r_x = pd.Series(years)
    r_y = slope*r_x + intercept
    ax.plot(r_x, r_y, 'g')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
