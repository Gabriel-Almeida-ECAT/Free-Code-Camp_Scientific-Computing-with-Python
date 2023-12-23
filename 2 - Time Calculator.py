# https://replit.com/@GabrielAlmeid57/boilerplate-time-calculator#time_calculator.py

def add_time(start, duration, day_week = False):
  days_week = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
  new_time = ""

  str_sup1 = start.split(" ")
  period_day = str_sup1[1]
  #["00:00", "AM"]

  st_time = str_sup1[0].split(":")
  ad_time = duration.split(":")
  #["00", "00"]
  
  st_hour = int(st_time[0])
  if(period_day == "PM" and st_hour != 12):
    st_hour += 12
  if(period_day == "AM" and st_hour == 12):
    st_hour -= 12
  st_min = int(st_time[1])

  ad_hour = int(ad_time[0])
  ad_min = int(ad_time[1])

  ed_min = st_min + ad_min
  ed_hour = st_hour + ad_hour

  if(ed_min >= 60):
    ed_hour += 1
    ed_min = ed_min - 60

  days_added = 0
  if(ed_hour >= 24):
    days_added = int(ed_hour/24)
    ed_hour = ed_hour % 24

  if(day_week):
    if(day_week.upper() not in days_week):
        return "Error: day of the week non existent."
    int_day_week = days_week.index(day_week.upper())

    in_ed_day_week = int_day_week + days_added
    if(in_ed_day_week > 6):
      in_ed_day_week = in_ed_day_week % 7

  if(ed_min < 10):
    str_min = "0" + str(ed_min)
  else:
    str_min = str(ed_min)

  if(ed_hour == 0): 
    new_time += "12"
    new_time += ":"
    new_time += str_min
    new_time += " AM"
  elif(ed_hour > 0 and ed_hour < 12):
    new_time += str(ed_hour)
    new_time += ":"
    new_time += str_min
    new_time += " AM"
  elif(ed_hour == 12):
    new_time += "12"
    new_time += ":"
    new_time += str_min
    new_time += " PM"
  else:
    if(ed_hour > 12 and ed_hour < 24):
      new_time += str(ed_hour-12)
      new_time += ":"
      new_time += str_min
      new_time += " PM"

  if(day_week):
    new_time += ", " + days_week[in_ed_day_week].capitalize()
  
  if(days_added == 1):
    new_time += " (next day)"
  
  if(days_added > 1):
    new_time += " (%d days later)"%(days_added)

  return new_time



if __name__ == '__main__':
  print(add_time("11:06 PM", "2:02"))