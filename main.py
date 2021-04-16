current_speed =float(input("Enter speed limit in km/h:"))
speed = float(input("Enter speed allowed on the road in km/h"))
points = (current_speed - speed)/5
if speed < current_speed:
    print('OK')
if speed == current_speed:
    print('Ok')
elif points > 12:
    print('Dimerit: ' + str(current_speed))
else:
    print('Time to go to Jail')

