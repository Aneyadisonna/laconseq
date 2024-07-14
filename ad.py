# Example in Python
timestamp = 1718582293

# Converting to a human-readable date
from datetime import datetime
date_time = datetime.fromtimestamp(timestamp)
print("The date and time is:", date_time.strftime('%Y-%m-%d %H:%M:%S'))
