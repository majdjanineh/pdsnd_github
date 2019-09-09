import time #This module provides various time-related functions.
import pandas as pd #Open source library for data structures and data analysis tools
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
    while True: #Loop until getting correct city name
        try:
            city=str(input('Please choose one of these cities (chicago, new york city, washington): ')).lower()
            if city not in ['chicago', 'new york city', 'washington']:
                raise
            break
        except:
            print('Wrong city name was entered, please write one of these city names:\nchicago, new york city, washington')




    # TO DO: get user input for month (all, january, february, ... , june)
    while True: #Loop until getting correct month name
        try:
            month=str(input('Want to choose all months or specific month: ')).lower()
            if month not in ['all', 'january', 'february', 'march', 'april','may','june']:
               raise
            break
        except:
            print('Wrong month was entered, please write one of the following answers:\nall, january, february, march, april, may, june')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: #Loop until getting correct day value
        try:
            day=str(input('Want to choose all days of weeks or a specific day of week: ')).lower()
            if day not in ['all','monday','tuesday','wedensday','thursday','friday','sunday']:
               raise
            break
        except:
            print('Wrong month was entered, please write one of the following answers:\nall, january, february, march, april, may, june')

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

    df=pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

   # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Frequent Month: {}'.format(common_month))
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day: {}'.format(common_day))
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Frequent Hour: {}'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_StartStation = df['Start Station'].mode()[0]
    print('Most commonly used Start Station: {}.'.format(common_StartStation))

    # TO DO: display most commonly used end station
    common_EndStation = df['End Station'].mode()[0]
    print('Most commonly used End Station: {}.'.format(common_EndStation))

    # TO DO: display most frequent combination of start station and end station trip
    common_StartEndStation=(df['Start Station']+' to '+df['End Station']).mode()[0]
    print('Most commonly used Start and End Station Combination: {}.'.format(common_StartEndStation))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['diff_hours'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    df['diff_hours']=df['diff_hours']/np.timedelta64(1,'h')
    print('Total Travel Time: {} Hours'.format(df['diff_hours'].sum(axis=0)))
    # TO DO: display mean travel time
    print('The average travel time is: {} Hours'.format(df['diff_hours'].mean(axis=0)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n{}'.format(user_types))

    # TO DO: Display counts of gender
    try:
        Gender = df['Gender'].value_counts()
        print('\nGender Distribution:\n{}\n'.format(Gender))
    except:
        print('\nGender Distribution:\nNo Gender Data Found')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth is:\n{}'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth is:\n{}'.format(int(df['Birth Year'].max())))
        print('The most common year of birth is:\n{}'.format(int(df['Birth Year'].mode()[0])))
        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print('\nNo year of birth data found!')
    print('-'*40)

def  display_data(df):
    rowcount=5
    while True:
        try:
            if rowcount==5:
                rowdata=str(input('Would you like to see 5 lines of raw data? answer Yes or No\n')).lower()
            else:
                rowdata=str(input('Do you want to see more 5 lines of raw data?')).lower()
            if rowdata=='yes':
                print(df.iloc[:rowcount])
                rowcount+=5
            elif rowdata=='no':
                break
            elif rowdata!=['yes','no']:
                raise
        except:
            print('Please choose yes or no')





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
