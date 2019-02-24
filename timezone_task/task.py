from datetime import datetime, timedelta


class Task(object):

    def __init__(self, task_type, user, country, start_time, end_time, *days):
        self.task_type = task_type
        self.user = user
        self.country = country
        self.start_time = start_time
        self.end_time = end_time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        try:
            if not days:
                if self.start_time < self.end_time:
                    if self.start_time <= current_time <= self.end_time:
                        print(True)
                    else:
                        print(self.start_time)
                else:  # crosses midnight
                    if current_time >= self.start_time or current_time <= self.end_time:
                        print(True)
                    else:
                        print(self.start_time)
            else:
                current_day = now.strftime("%A")
                if current_day in days:
                    if self.start_time < self.end_time:
                        if self.start_time <= current_time <= self.end_time:
                            print(True)
                    else:
                        if current_time >= self.start_time or current_time <= self.end_time:
                            print(True)
                else:
                    for i in range(6):
                        now = now + timedelta(days=1)
                        next_day = now.strftime("%A")
                        if next_day in days:
                            print(next_day, " ", self.start_time)
                            break
        except:
            print("An error occurred")






