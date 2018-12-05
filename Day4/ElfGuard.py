class ElfGuard:
    id = -1
    time_asleep = 0

    def __init__(self, guard_id):
        self.id = guard_id

    def __str__(self):
        return f'id: {self.id}, sleep time: {self.time_asleep}.'

    def __ref__(self):
        return self.__str__()
