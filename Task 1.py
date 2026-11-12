class CountGenerator:
    def __init__(self, max_number):
        self.max_number = max_number

    def __iter__(self):
        current = 1
        while current <= self.max_number:
            yield current
            current += 1

counter_obj = CountGenerator(5)

for elem in counter_obj:
    print(elem)

iterator = iter(counter_obj)
print(iterator)
print(next(iterator))
print(next(iterator))
