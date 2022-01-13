import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

# Clean data
mask_l = (df['value'] >= df['value'].quantile(0.025))
mask_u = (df['value'] <= df['value'].quantile(0.975))
df = df[mask_l & mask_u]

def draw_line_plot():
    # Draw line plot
    fig,axs = plt.subplots(figsize=(20,8),)
    axs.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axs.set_ylabel('Page Views')
    axs.set_xlabel('Date')
    plt.plot(df['date'], df['value'], 'r')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar['date'].apply(lambda x:x.year)
    df_bar['Month'] = df_bar['date'].apply(lambda x:x.month_name())
    df_bar['Month_ID'] = df_bar['date'].apply(lambda x:x.month)
    df_bar = df_bar.groupby(['Year','Month'], as_index=False).mean()
    df_bar.rename({'value':"Average Page Views"}, inplace=True, axis=1)
    df_bar.sort_values(['Month_ID'], inplace=True)
    # Draw bar plot
    pallete = sns.color_palette("Paired")
    fig = sns.catplot(data=df_bar, x='Year' , y="Average Page Views" ,hue='Month' , kind='bar', palette=pallete).fig
    plt.legend()
    fig.axes[0].set_xlabel('Years')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Year'] = df_box['date'].apply(lambda x:x.year)
    df_box['Month'] = df_box['date'].apply(lambda x:x.month_name())
    df_box['Month_ID'] = df_box['date'].apply(lambda x:x.month)
    df_box['Month'] = (df_box['Month'].str.slice(stop=3))
    df_box.sort_values(['Month_ID'], inplace=True)
    df_box.rename({'value':'Page Views'}, inplace=True, axis=1)
    # Draw box plots (using Seaborn)
    fig,[ax1,ax2] = plt.subplots(1,2, figsize=(20,5),)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(data=df_box, x='Year', y='Page Views', ax=ax1 ,)
    sns.boxplot(data=df_box, x='Month', y='Page Views', ax=ax2 ,)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
