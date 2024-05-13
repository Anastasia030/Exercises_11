class Object:
    """
    The class of the description of the academic discipline
    """
    def __init__(self, name, auditorium, teacher):
        """
        Initializes an Object with name, auditorium, and teacher attributes.

        :param name: str, name of the object
        :param auditorium: str, auditorium where the object takes place
        :param teacher: str, teacher responsible for the object
        """
        self.name = name
        self.auditorium = auditorium
        self.teacher = teacher

    def __str__(self):
        """
        Represents the Object as a formatted string.

        :return: str, formatted string representation of the Object
        """
        return f'{self.name} / {self.auditorium} / {self.teacher}'

    def __repr__(self):
        """
        Represents the Object for debugging purposes.

        :return: str, string representation of the Object
        """
        return self.__str__()


class Day:
    """
    Class of the day of the school week
    """
    name_day = {'MO': 'Monday',
                'TU': 'Tuesday',
                'WE': 'Wednesday',
                'TH': 'Thursday',
                'FR': 'Friday',
                'SA': 'Saturday',
                'SU': 'Sunday'}

    def __init__(self, day):
        """
        Initializes a Day with a given day abbreviation.

        :param day: str, abbreviation of the day
        """
        self.day = day
        self.time = {}

    def add_time(self, start_time, end_time, obj):
        """
        Adds a time slot to the Day schedule.

        :param start_time: str, start time of the slot
        :param end_time: str, end time of the slot
        :param obj: Object, object scheduled for the slot
        """
        couple = start_time[:2] + ':' + start_time[2:] + ' - ' + end_time[:2] + ':' + end_time[2:]
        self.time[couple] = obj

    def __str__(self):
        """
        Represents the Day as a formatted string.

        :return: str, formatted string representation of the Day
        """
        couples = ''
        for key, val in self.time.items():
            couple = str(key) + ': ' + str(val) + '\n'
            couples += couple
        return f'---{Day.name_day[self.day]}---\n{couples}'

    def __repr__(self):
        """
        Represents the Day for debugging purposes.

        :return: str, string representation of the Day
        """
        return f'{Day.name_day[self.day]}'


class Schedule:
    """
    The class that outputs the schedule.
    """
    def __init__(self, group, week):
        """
        Initializes a Schedule for a group with a specified group name and week schedule.

        :param group: str, name of the group
        :param week: list, list of Day objects representing the weekly schedule
        """
        self.group = group
        self.week = week

    def __str__(self):
        """
        Represents the Schedule as a formatted string.

        :return: str, formatted string representation of the Schedule
        """
        days = ''
        for day in self.week:
            days += str(day)
        return f'Schedule for the group: {self.group}\n{days}'


class Group:
    """
    The group class that stores the schedule of all available groups.
    """
    data_groups = []

    def __init__(self, name):
        """
        Initializes a Group with a given name.

        :param name: str, name of the group
        """
        self.name = name
        self.week = []
        self.data_check = {}

    def write(self, file):
        """
        Writes the schedule for the group by parsing the provided file.

        :param file: str, path to the file containing schedule data
        """
        with open(file, 'r', encoding='utf8') as file_data:
            for data in file_data:
                if 'LOCATION:' in data:
                    aud = data.rfind('LOCATION:')
                    auditorium = data[aud + 20:].rstrip()
                if 'DESCRIPTION:' in data:
                    tea = data.rfind('DESCRIPTION:')
                    teacher = data[tea + 27:].rstrip()
                if 'SUMMARY:' in data:
                    nm = data.rfind('SUMMARY:')
                    name = data[nm + 8:].rstrip()
                if 'BYDAY=' in data:
                    d_wk = data.rfind('BYDAY=')
                    day_week = data[d_wk + 6:d_wk + 8]
                if 'DTSTART' in data:
                    st_tm = data.rfind('DTSTART')
                    start_time = data[st_tm + 39:st_tm + 43].rstrip()
                if 'DTEND' in data:
                    en_tm = data.rfind('DTEND')
                    end_time = data[en_tm + 37:en_tm + 41].rstrip()
                if 'END:VEVENT' in data:
                    obj = Object(name, auditorium, teacher)
                    if day_week not in self.data_check:
                        self.data_check[day_week] = Day(day_week)
                    self.data_check[day_week].add_time(start_time, end_time, obj)

        for day in self.data_check.values():
            if day not in self.week:
                self.week.append(day)

        Group.data_groups.append(Schedule(self.name, self.week))
