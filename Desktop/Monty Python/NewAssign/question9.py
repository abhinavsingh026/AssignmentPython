from datetime import datetime, timedelta
today = datetime.now()
print("Today's Date & Time is: ",today)
days_add = 10
new_date = today + timedelta(days_add)
print(f"Date after adding {10} days: ",new_date)