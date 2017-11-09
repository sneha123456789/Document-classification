
# coding: utf-8

# In[1]:

get_ipython().magic('pylab inline')


# In[4]:

import pandas


# In[5]:

import seaborn


# # Load CSV file into memory 

# In[6]:

get_ipython().set_next_input('data = pandas.read_csv');get_ipython().magic('pinfo pandas.read_csv')


# In[11]:

data


# In[12]:

dt = '4/1/2014 0:11:00'


# In[17]:

dt.split(' ')


# In[20]:

d, t =dt.split(' ')
print(d)
print(t)


# In[22]:

data['Date/Time']


# In[23]:

data.tail()


# In[24]:

data.head()


# # Convert datetime and add some useful columns

# In[132]:

m,d,y = d.split('/')


# In[ ]:

int(d)


# In[27]:

dt = pandas.to_datetime(dt)


# In[28]:

dt


# In[29]:

dt.month


# In[32]:

dt.day


# In[33]:

data['Date/Time']= data['Date/Time'].map(pandas.to_datetime)


# In[41]:

def get_dom(dt):
    return dt.day
data['dom'] = data['Date/Time'].map(get_dom)


# In[45]:

dt = data['Date/Time'][500000]dt


# In[36]:

def get_weekday(dt):
    return dt.weekday

data['weekday'] = data['Date/Time'].map(get_weekday)
data.tail()


# In[44]:

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)
data.tail()


# # Analyzing the dom

# In[49]:

hist(data.dom)


# In[51]:

hist(data.dom, bins=20, rwidth=.9)


# In[55]:

hist(data.dom, bins=30, rwidth=.9, range=(0.5, 30.5))
xlabel('Date of the month')
ylabel('Frequency')
title('Frequency by Dom - Uber - Apr 2014')


# In[58]:

for k, rows in data.groupby('dom'):
    print((k, len(rows)))


# In[59]:

for k, rows in data.groupby('dom'):
    print((k, rows))
    break


# In[60]:

def count_rows(rows):
    return len(rows)
by_date = data.groupby('dom').apply(count_rows)
by_date


# In[61]:

plot(by_date)


# In[62]:

bar(range(1,31),by_date)


# In[63]:

by_date_sorted = by_date.sort_values()
by_date_sorted


# In[64]:

bar(range(1,31), by_date_sorted)


# In[65]:

bar(range(1,31),by_date_sorted)
xticks(range(1,31), by_date_sorted.index)


# # Analyze the hour

# In[66]:

hist(data.hour)


# In[67]:

hist(data.hour, bins=24, range=(0.5,24))


# # Analyze the weekday

# In[95]:

hist(data.weekday)


# In[91]:

hist(data.weekday, bins=7, range =(-.5,7), rwidth=.8, color='green')


# In[ ]:




# In[72]:

hist(data.weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='green')
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())


# # Cross Analysis (hour, dow)

# In[80]:

count_rows(data)


# In[ ]:

data.groupby('hour weekday'.split()).apply(count_rows).unstack()


# In[85]:

by_h_d = data.groupby('hour weekday'.split()).apply(count_rows)


# In[87]:

by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[ ]:

seaborn.heatmap(by_cross)


# # By lat and lon

# In[99]:

hist(data['Lat'])


# In[98]:

hist(data['Lat'], bins=100)


# In[100]:

hist(data['Lat'], bins=100, range = [40.5,41])


# In[101]:

hist(data['Lon'], bins=100);


# In[102]:

hist(data['Lon'], bins=100, range = (-74.5, -73.5));


# In[104]:

hist(data['Lon'], bins=100, range = (-74.5, -73.5))
twiny()
hist(data['Lat'], bins=100, range = (40.5,41))
("")


# In[106]:

hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='g', alpha=.5)
twiny()
hist(data['Lat'], bins=100, range = (40.5,41), color='r', alpha=.5)
("")


# In[110]:

hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='g', alpha=.5, label = 'longitude')
grid()
legend(loc='upper left')
twiny()
hist(data['Lat'], bins=100, range = (40.5,41), color='r', alpha=.5, label = 'latitude')
grid()
legend(loc='best')
("")


# In[111]:

plot(data['Lat'])


# In[112]:

plot(data['Lat'])
xlim(0,100)


# In[117]:

plot(data['Lat'], '.', ms=100, color= 'green')
xlim(0,100)


# In[119]:

plot(data['Lat'], '^', ms=20, color='green', label='lat')
plot(data['Lon'], '^', ms=20, color='green', label='lon')
xlim(0,100)


# In[120]:

plot(data['Lon'], data['Lat'])


# In[121]:

plot(data['Lon'], data['Lat'], '.')


# In[124]:

figure(figsize=(20,20))
plot(data['Lon'], data['Lat'], '.', ms=1,alpha=.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[ ]:



