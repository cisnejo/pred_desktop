from datetime import datetime

#"2023-03-23 12:37:28"
timestamp = datetime.strptime("2023-03-23 12:30:16", '%Y-%m-%d %H:%M:%S')
epoch_time = int(timestamp.timestamp())

print(epoch_time)