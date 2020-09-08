import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv')

    years_predicted = np.arange(1880, 2050)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_predicted2 = np.arange(2000, 2050)
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df[df['Year'] >= 2000]['Year'],
                                                                  df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='b', label='original data')
    plt.plot(years_predicted, intercept + slope * years_predicted, 'r', label='predicted data')
    plt.plot(years_predicted2, intercept2 + slope2 * years_predicted2, 'g', label='predicted data 2')
    plt.legend()
    plt.title("Rise in Sea Level")
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
