mapper = {
    'E1':
    'Username is null',
    'E2':
    'Name is null',
    'E3':
    'No work is defined',
}


class DataException(Exception):
    def __init__(self, code):
        super().__init__()
        self.msg = mapper[code]

    def __str__(self):
        return self.msg