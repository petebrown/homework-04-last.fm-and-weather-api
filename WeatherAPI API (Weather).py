#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[ ]:


import requests


# In[ ]:


api_key = '0d3e848d3d2648e4949185759221306'


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[ ]:


location = 'Norwich'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

r = requests.get(url)
data = r.json()


# In[ ]:


latitude = data['location']['lat']
longitude = data['location']['lon']

print(f'The latitude/longitude returned by the Weather API for {location} is {latitude}/{longitude}')


# In[ ]:


timezone = data['location']['tz_id']

print(f'The timezone returned by the Weather API for {location} is {timezone}')


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[ ]:


windspeed_mph = data['current']['wind_mph']

print(f'The current wind speed in {location} is {windspeed_mph} mph.')


# In[ ]:


current_temp_c = data['current']['temp_c']
feels_like_temp_c = data['current']['feelslike_c']
temp_difference = feels_like_temp_c - current_temp_c


# In[ ]:


if temp_difference > 0:
    print(f"In {location} it currently feels {temp_difference} C warmer than the actual temperature of {current_temp_c} C.")
elif temp_difference < 0:
    print(f"In {location} it currently feels {-temp_difference} C colder than the actual temperature of {current_temp_c} C.")
else:
    print(f"The current temperature in {location} feels the same as the actual temperature, which is {current_temp_c} C.")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[ ]:


astronomy_endpoint = 'http://api.weatherapi.com/v1/astronomy.json'


# In[ ]:


url = f'http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={location}&dt=2022-06-17'

r = requests.get(url)
data = r.json()


# In[ ]:


moon_illumination = data['astronomy']['astro']['moon_illumination']

print(f'Tomorrow {moon_illumination}% of the moon will be visible in {location}.')


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[ ]:


url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=1'

r = requests.get(url)
data = r.json()


# In[ ]:


max_temp = data['forecast']['forecastday'][0]['day']['maxtemp_c']
min_temp = data['forecast']['forecastday'][0]['day']['mintemp_c']
temp_diff = max_temp - min_temp

print(f'The difference between the maximum temperature ({max_temp} C) and the minimum temperature ({min_temp} C) is {temp_diff:.1f} C.')


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# The variables I would rename are:
# ```
# url
# r
# data
# ```
# 
# I would rename them in a way that was relevant to the task they were performing, e.g. for question 1 I might use:
# 
# ```
# current_weather_url
# current_weather_response
# current_weather_data
# ```
# For question 3, I might use:
# ```
# astronomy_url
# astronomy_response
# astronomy_data
# ```

# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[ ]:


n_days = 3
url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={n_days}'
r = requests.get(url)
data = r.json()


# In[ ]:


forecast_days = data['forecast']['forecastday']


# In[ ]:


for day in forecast_days:
    date = day['date']
    max_temp_c = day['day']['maxtemp_c']

    if max_temp_c >= 25:
        temp_ranking = 'hot'
    elif max_temp_c >= 18:
        temp_ranking = 'warm'
    else:
        temp_ranking = 'cold'

    print(f'On {date} the maximum temperature will {max_temp_c}, which is {temp_ranking}')


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[ ]:


n_days = 7
location = 'Norwich'
url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={n_days}&aqi=no'
r = requests.get(url)
data = r.json()

forecast_days = data['forecast']['forecastday']

for day in forecast_days:
    date = day['date']
    max_temp_c = day['day']['maxtemp_c']

    if max_temp_c >= 25:
        temp_ranking = 'hot'
    elif max_temp_c >= 18:
        temp_ranking = 'warm'
    else:
        temp_ranking = 'cold'

    print(f'On {date} the maximum temperature will {max_temp_c}, which is {temp_ranking}')


# The above code only returns forecasts for three days rather than seven due to a limitation of the free subscription plan: "Depending upon your subscription plan we provide current and 3 day air quality data for the given location in json and xml."

# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[ ]:


warmest_temp = -100

for day in forecast_days:
    date = day['date']
    max_temp_c = day['day']['maxtemp_c']

    if max_temp_c > warmest_temp:
        warmest_temp = max_temp_c
        warmest_day = date

print(f'The warmest day will be {warmest_day} when it will be {warmest_temp}.')


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[ ]:


location = 'Miami, FL'
url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}'
r = requests.get(url)
data = r.json()

hourly_forecasts = data['forecast']['forecastday'][0]['hour']

for hour in hourly_forecasts:
    time = hour['time']
    temp_c = hour['temp_c']
    cloud_cover = hour['cloud']

    if cloud_cover > 50:
        cloud_desc = 'cloudy'
    else:
        cloud_desc = 'clear'

    print(f'{time}: Temperature forecast is {temp_c} C and {cloud_desc} ({cloud_cover}% cloud cover).')


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[ ]:


hour_count = 0
over_85_count = 0

for hour in hourly_forecasts:
    hour_count += 1

    temp_f = hour['temp_f']

    if temp_f > 85:
        over_85_count += 1

prop_time_over_85 = (over_85_count / hour_count) * 100
print(f'The temperate will be over 85 degrees (F) {prop_time_over_85:.1f}% of the time in the next 24 hours.')


# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# Answer: Per the Weather API [pricing](https://www.weatherapi.com/pricing.aspx) page, a developer account costs $4/month and permits 2,000,000 calls per month.

# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# Answer: To avoid paying, you could open additional free accounts and use multiple API keys.
