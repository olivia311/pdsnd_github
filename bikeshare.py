#Description
#In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.
#You will write code to import the data and answer interesting questions about it by computing descriptive statistics.
# You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics

# These are the links that i used

# python documentation
# https://www.python-course.eu/python3_input.php
# https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.to_datetime.html
# https://www.geeksforgeeks.org/python-pandas-extracting-rows-using-loc/
# https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
# https://www.geeksforgeeks.org/python-pandas-series-dt-hour/
# https://www2.cs.arizona.edu/people/mccann/errors-python#Five
# stackoverflow
# python documentation


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please input city name: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "City is name is invalid! Please input another name: ").lower()

# TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please input month name: ").lower()

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please input day of week: ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # TO DO: display the most common day of week
    print("The most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(
        df['Start Station'].mode().values[0])
    )

      # TO DO: display most commonly used end station
    print("The most common end station is: {}".format(
        df['End Station'].mode().values[0])
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['routes'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # TO DO: display mean travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given fitered data is: " + str(total_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given fitered data is: \n" + str(user_types))

    if city != 'washington':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given fitered data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given fitered data is: {}\n'.format(most_recent_birth))
        print('Most common birth from the given fitered data is: {}\n'.format(most_common_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
