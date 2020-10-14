class PascalList:
    """Переопределение номера элемента в списке."""
    def __init__(self, lst):
        self.lst = lst

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __getitem__(self, key):
        return self.lst[key-1]

    def __str__(self):
        return self.lst


l = PascalList(['1', '3', '2'])
print(l[2])
