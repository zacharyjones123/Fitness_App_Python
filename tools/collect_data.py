import fitbit
from tools import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

server = Oauth2.OAuth2Server('22DFYT', 'd4a39b4a3f5e1c8ab789d4bec17c5d23')
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit('22DFYT', 'd4a39b4a3f5e1c8ab789d4bec17c5d23', oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y-%m-%d"))

fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')


########################################################################
def heartCollection():
    hearttime_list = []
    heartval_list = []
    for i in fit_statsHR['activities-heart-intraday']['dataset']:
        heartval_list.append(i['value'])
        hearttime_list.append(i['time'])
    heartdf = pd.DataFrame({'Heart Rate':heartval_list,'Time':hearttime_list})

    heartdf.to_csv('../data/heart/heart'+ \
                yesterday+'.csv', \
                columns=['Time','Heart Rate'], header=True, \
                index = False)


#####################################################################
def sleepCollection():
    """Sleep data on the night of ...."""
    fit_statsSl = auth2_client.sleep(date='today')
    sleeptime_list = []
    sleepval_list = []
    for i in fit_statsSl['sleep'][0]['minuteData']:
        sleeptime_list.append(i['dateTime'])
        sleepval_list.append(i['value'])
    sleepdf = pd.DataFrame({'State':sleepval_list,
                        'Time':sleeptime_list})
    #for j in fit_statsSl['summary'].keys():
        #print(j, " : ", fit_statsSl['summary'][j])
    sleepdf['Interpreted'] = sleepdf['State'].map({'2':'Awake','3':'Very Awake','1':'Asleep'})
    sleepdf.to_csv('../data/sleep/sleep' + \
                today+'.csv', \
                columns = ['Time','State','Interpreted'],header=True,
                index = False)


#####################################################################
# Put everything together



"""Body Fat Percentage data"""
fit_statsBf = auth2_client.get_bodyfat(base_date=today, period='1m')
fattime_list = []
fatval_list = []
#print(fit_statsSl)
for i in fit_statsBf['fat']:
    fattime_list.append(i['date'])
    fatval_list.append(i['fat'])
fatdf = pd.DataFrame({'Fat':fatval_list,
                     'Time':fattime_list})

fatdf.to_csv('../data/bodyFat/bodyFat' + \
               today+'.csv', \
               columns = ['Time','Fat'],header=True,
               index = False)

#####################################################################

"""Body Fat Percentage data"""
fit_statsBw = auth2_client.get_bodyweight(base_date=today, period='1m')
weighttime_list = []
weightval_list = []
#print(fit_statsSl)
for i in fit_statsBw['weight']:
    weighttime_list.append(i['date'])
    weightval_list.append(i['weight'])
weightdf = pd.DataFrame({'Weight':weightval_list,
                     'Time':weighttime_list})

weightdf.to_csv('../data/bodyWeight/bodyWeight' + \
               today+'.csv', \
               columns = ['Time','Weight'],header=True,
               index = False)

#####################################################################

"""Food Logs data"""
foodtime_list = []
food_calories_list = []
food_carbs_list = []
food_fat_list = []
food_fiber_list = []
food_protein_list = []
food_sodium_list = []

for i in range(31, 0, -1):
    the_day = str((datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d"))
    fit_statsSl = auth2_client.foods_log(date=the_day)
    foodtime_list.append(fit_statsSl['foods'][0]['logDate'])
    food_calories_list.append(fit_statsSl['summary']['calories'])
    food_carbs_list.append(fit_statsSl['summary']['carbs'])
    food_fat_list.append(fit_statsSl['summary']['fat'])
    food_fiber_list.append(fit_statsSl['summary']['fiber'])
    food_protein_list.append(fit_statsSl['summary']['protein'])
    food_sodium_list.append(fit_statsSl['summary']['sodium'])

print(weighttime_list)
print(fattime_list)
print(foodtime_list)
print('--------------------------------------------')

for i in range(40):
    temp_day = str((datetime.date(year=2019, month=9, day=9) + datetime.timedelta(days=i)).strftime("%Y-%m-%d"))
    # Now need to check the date
    # Weight
    if temp_day != weighttime_list[i]:
        weighttime_list.insert(i, temp_day)
        weightval_list.insert(i, weightval_list[i-1])

    # Body Fat
    if temp_day != fattime_list[i]:
        fattime_list.insert(i, temp_day)
        fatval_list.insert(i, fatval_list[i-1])


    # Food
    if temp_day != foodtime_list[i]:
        foodtime_list.insert(i, temp_day)
        food_calories_list.insert(i, food_calories_list[i-1])
        food_carbs_list.insert(i, food_carbs_list[i-1])
        food_fat_list.insert(i, food_fat_list[i-1])
        food_fiber_list.insert(i, food_fiber_list[i-1])
        food_protein_list.insert(i, food_protein_list[i-1])
        food_sodium_list.insert(i, food_sodium_list[i-1])



#Need to go through and check the arrays

print(weighttime_list[0], ' and end with ', weighttime_list[-1])
print(fattime_list[0], ' and end with ', fattime_list[-1])
print(foodtime_list[0], ' and end with ', foodtime_list[-1])
print(weighttime_list)
print(fattime_list)
print(foodtime_list)
print(len(weighttime_list))
print(len(fattime_list))
print(len(foodtime_list))


#print(weighttime_list)
#print(fatval_list)
"""Make the  complete csv"""
fulldf = pd.DataFrame({'Sodium': food_sodium_list,
                       'Protein': food_protein_list,
                       'Fiber': food_fiber_list,
                       'Fat':food_fat_list,
                       'Carbs': food_carbs_list,
                       'Calories':food_calories_list,
                       'Weight':weightval_list,
                       'Fat':fatval_list,
                       'Time':foodtime_list})

fulldf.to_csv('../data/full/full' + \
               today+'.csv', \
               columns = ['Time', 'Fat', 'Weight', 'Calories', 'Carbs', 'Fat', 'Fiber', 'Protein', 'Sodium'],header=True,
               index = False)

print("Data Collection complete!")