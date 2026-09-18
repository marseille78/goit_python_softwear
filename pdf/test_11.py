from datetime import datetime

datetime_string = '1970:01:01 January Jan 02 02 00'

print(datetime.strptime(datetime_string, "%Y:%m:%d %B %b %H %I %M"))