from datetime import datetime
import pytz

utc_now = datetime.now(pytz.utc)
print('utc_now: ', utc_now)

kyiv_tz = pytz.timezone('Europe/Kyiv')
print("kyiv_tz: ", kyiv_tz)

london_tz = pytz.timezone('Europe/London')
print("london_tz: ", london_tz)

kyiv_time = utc_now.astimezone(kyiv_tz)
print("kyiv_time: ", kyiv_time)

london_time = utc_now.astimezone(london_tz)
print("london_time: ", london_time)