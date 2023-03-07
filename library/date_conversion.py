from datetime import datetime

class FormateDate():
    def __init__(self):
        pass

    def seconds(self, time:str):
        clock = datetime.utcnow()
        time = time.replace('T', ' ')[0:19]
        timeResult = datetime.strptime(f'{time}', '%Y-%m-%d %H:%M:%S')
        timeDifference = (clock - timeResult).seconds
        return timeDifference

    def minutes(self, time:str):
        clock = datetime.utcnow()
        time = time.replace('T', ' ')[0:19]
        timeResult = datetime.strptime(f'{time}', '%Y-%m-%d %H:%M:%S')
        timeDifference = (clock - timeResult).seconds / 60
        return timeDifference
    
    def hours(self, time:str):
        clock = datetime.utcnow()
        time = time.replace('T', ' ')[0:19]
        timeResult = datetime.strptime(f'{time}', '%Y-%m-%d %H:%M:%S')
        timeDifference = ((clock - timeResult).seconds / 60) / 60
        return timeDifference
    
    def days(self, time:str):
        clock = datetime.utcnow()
        time = time.replace('T', ' ')[0:19]
        timeResult = datetime.strptime(f'{time}', '%Y-%m-%d %H:%M:%S')
        timeDifference = (clock - timeResult).days
        return timeDifference 
    
    def formateDate(self, time:str):
        time = time.replace('T', ' ')[0:19]
        return time

    


