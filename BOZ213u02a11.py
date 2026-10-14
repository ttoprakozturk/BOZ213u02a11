hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_mins = mins + dura
end_hour = (hour + (total_mins // 60)) % 24
end_mins = total_mins % 60

print(f"{end_hour}:{end_mins}")
