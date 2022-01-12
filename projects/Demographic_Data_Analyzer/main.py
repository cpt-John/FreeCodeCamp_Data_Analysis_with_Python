import numpy as np
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask_m = (df['sex']=='Male')
    average_age_men = round(df[mask_m]['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education']=='Bachelors'])/len(df) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask_h = (df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')
    mask_l = ~mask_h
    higher_education = len(df[mask_h])
    lower_education = len(df[mask_l])

    # percentage with salary >50K
    mask_h = mask_h & (df['salary']=='>50K')
    mask_l = mask_l & (df['salary']=='>50K')
    higher_education_rich = round(len(df[mask_h])/higher_education * 100, 1)
    lower_education_rich = round(len(df[mask_l])/lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask_m_h = (df['hours-per-week']==df['hours-per-week'].min())
    mask_h_s = (df['salary']=='>50K')
    num_min_workers = mask_m_h.sum()

    rich_percentage = round((mask_h_s & mask_m_h).sum()/num_min_workers *100, 1)

    # What country has the highest percentage of people that earn >50K?
    percentages = (df[df['salary']=='>50K'].groupby(['native-country'])['salary'].count()\
                    /df.groupby(['native-country'])['salary'].count() * 100)
    item = percentages[percentages == percentages.max()]
    highest_earning_country = item.index[0]
    highest_earning_country_percentage = round(item.values[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask_in = (df['native-country']=='India')
    mask_h_s = (df['salary']=='>50K')
    in_h_s_df = df[mask_in & mask_h_s]
    in_h_s_sr = in_h_s_df.groupby(['occupation'])['occupation'].count()
    item = in_h_s_sr[in_h_s_sr == in_h_s_sr.max()]
    top_IN_occupation = item.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
