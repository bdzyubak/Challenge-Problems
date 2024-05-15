class TextInput:
    def __init__(self):
        self.value = ""

    def add(self, value):
        self.value += value

    def get_value(self):
        return self.value


class NumericInput:
    def __init__(self):
        self.value = ""

    def add(self, value):
        if value.isnumeric():
            self.value += value

    def get_value(self):
        return self.value


if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())
    assert input.get_value() == "10"
    print('Tests Done.')
