# Write a Python program to convert seconds to day, hour, minutes and seconds.
s = float(input("Please enter a given amount of seconds: "))

# days =  s /86400
# hours = s / 3600
# minutes = s / 60
#
# print("{} seconds, equates to\n{} days\n{} hours\n{} minutes".format(s, days, hours, minutes))

days = s // 86400
time = s % 86400
hours = time // 3600
time2 = s % 3600
minutes = time2 // 60
seconds = s % 60
print("{} seconds, equates to {} days, {} hours, {} minutes and {} seconds".format(s, days, hours, minutes, seconds))
