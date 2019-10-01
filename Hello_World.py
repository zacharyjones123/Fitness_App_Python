import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

server = Oauth2.OAuth2Server('22DFYT', 'd4a39b4a3f5e1c8ab789d4bec17c5d23')
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit('22DFYT', 'd4a39b4a3f5e1c8ab789d4bec17c5d23', oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))

fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')


########################################################################
hearttime_list = []
heartval_list = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    heartval_list.append(i['value'])
    hearttime_list.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate':heartval_list,'Time':hearttime_list})

heartdf.to_csv('heart'+ \
               yesterday+'.csv', \
               columns=['Time','Heart Rate'], header=True, \
               index = False)


#####################################################################
"""Sleep data on the night of ...."""
fit_statsSl = auth2_client.sleep(date='today')
sleeptime_list = []
sleepval_list = []
for i in fit_statsSl['sleep'][0]['minuteData']:
    sleeptime_list.append(i['dateTime'])
    sleepval_list.append(i['value'])
sleepdf = pd.DataFrame({'State':sleepval_list,
                     'Time':sleeptime_list})
for j in fit_statsSl['summary'].keys():
    print(j, " : ", fit_statsSl['summary'][j])
sleepdf['Interpreted'] = sleepdf['State'].map({'2':'Awake','3':'Very Awake','1':'Asleep'})
sleepdf.to_csv('sleep' + \
               today+'.csv', \
               columns = ['Time','State','Interpreted'],header=True,
               index = False)

#####################################################################

"""Body Fat Percentage data"""
fit_statsSl = auth2_client.get_bodyfat(period='1w')
fattime_list = []
fatval_list = []
print(fit_statsSl)
for i in fit_statsSl['fat']:
    fattime_list.append(i['date'])
    fatval_list.append(i['fat'])
fatdf = pd.DataFrame({'Fat':fatval_list,
                     'Time':fattime_list})

fatdf.to_csv('bodyFat' + \
               today+'.csv', \
               columns = ['Time','Fat'],header=True,
               index = False)

#####################################################################

"""Body Fat Percentage data"""
fit_statsSl = auth2_client.get_bodyweight(period='1w')
weighttime_list = []
weightval_list = []
print(fit_statsSl)
for i in fit_statsSl['weight']:
    weighttime_list.append(i['date'])
    weightval_list.append(i['weight'])
weightdf = pd.DataFrame({'Weight':weightval_list,
                     'Time':weighttime_list})

weightdf.to_csv('bodyWeight' + \
               today+'.csv', \
               columns = ['Time','Weight'],header=True,
               index = False)

#####################################################################

"""Make the  complete csv"""
fulldf = pd.DataFrame({'Weight':weightval_list,
                       'Fat':fatval_list,
                       'Time':weighttime_list})

fulldf.to_csv('full' + \
               today+'.csv', \
               columns = ['Time', 'Fat', 'Weight'],header=True,
               index = False)