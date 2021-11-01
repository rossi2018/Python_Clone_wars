# // is called floor division. A floor division devides a number abd takes the interger parts of the number ignoring the decimal numbers

def conver_seconds(seconds):
    hours=seconds // 3600
    minutes=(seconds - hours * 3600) // 60
    remaining_seconds= seconds -hours * 3600 - minutes * 60
    return hours, minutes,remaining_seconds

hours, minutes, seconds=conver_seconds(5000)
print(hours,minutes, seconds)