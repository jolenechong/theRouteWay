# converting input into right format to test AI

import datetime

# mapping days of week
daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


class DataModel:
    year = 0
    month = 0
    day = 0
    hour = 0
    road = 0
    delay = 0

    def from_row(self, row):
        self.year = row[0]
        self.month = row[1]
        self.day = row[2]
        self.hour = row[3]
        self.road = row[4]
        self.delay = 0 if row.__len__() <= 5 else row[5]
        # out of range error (if row[5] is not "present", just return 0)

    # def to_strdate(model):
    #     isPM = 'PM' if model.hour > 12 else 'AM'
    #     hourString = model.hour - 12 if isPM == 'PM' else model.hour
    #     return "({}) {}/{} {} {}{}: {}m".format(model.road, model.month, model.year, daysOfWeek[model.day - 1], hourString, isPM, model.delay)

    # only accept dates from 2016-2024 cuz it divides very weirdly :") and takes in %d/%m/%Y %H:%M format 
    def from_strdate(self, input):
        date = datetime.datetime.strptime(input, "%d/%m/%Y %H:%M") # change format here if needed!!!
        self.day = date.weekday() + 1
        self.month = date.month
        self.year = date.year
        self.hour = date.hour
        self.row = 0

    def to_row(self):
        return [self.year, self.month, self.day, self.hour, self.road, self.delay]

    # normalising data
    # https://medium.com/coderbyte/how-to-normalize-the-data-in-python-18a1cbc47ec1 --> different formulas & just play around with it
    def to_row_normalized(self):
        row = self.to_row()
        return [(row[0] - 2016) / 8.0, (row[1] - 1) / 11.0, (row[2]-1) / 6.0, row[3] / 23.0, (row[4] - 1) / 31.0, row[5] / 30.0]

    pass