import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
df.head()

# Add 'overweight' column
df['overweight'] = (df['weight']/((df['height']/100)**2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x>1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x>1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = "variable",hue="value", data=df_cat, kind="count",col="cardio").fig
    fig.axes[0].set_ylabel("total")
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    
    # Clean the data
    mask_p = (df['ap_lo'] <= df['ap_hi'])
    mask_h = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    mask_w = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    mask_cumulative = mask_p&mask_h&mask_w
    df_heat = df[mask_cumulative]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    # fig = plt.figure(figsize=((len(corr.columns)+2)/1.5,len(corr.index)/1.5))

    # Draw the heatmap with 'sns.heatmap()'
    fig, ax1 = plt.subplots(figsize=(12,12))
    sns.heatmap(corr, annot=True, mask=mask,square=True, fmt='.1f', linewidths=1,ax=ax1 )

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
