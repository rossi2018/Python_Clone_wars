class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


def get_event_date(event):
    return event.date


def current_users(eents):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machinees[event.machine] = set()
        if event.type = "login":
            machines[event.machine].add(event.user)
        elif event.type = "logout":
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, user in machines.item():
        if len(users) > 0:
            user_list = " ,".join(users)
            print("{}: {}".format(machine, user_list))


events = []

# This script is work in progress 1
