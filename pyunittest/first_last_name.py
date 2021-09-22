class Person_first:

    name = []
    def set_name(self, first_name):
        self.name.append(first_name)
        return len(self.name) - 1

    def get_name(self, last_name):
        if last_name >= len(self.name):
            return 'there is no such user found'
        else:
            return self.name[last_name]


if __name__ == "__main__":
    person = Person_first()
