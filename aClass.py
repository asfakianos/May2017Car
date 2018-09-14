# asdfClass.py
# Written by Alexander Sfakianos and Kyle Chu
# May 2017
# Simple class to get around encapsulation within our threads.


class Asdf():

    def __init__(self):
        """Creates 'storage' list that keeps track of other lists that
        don't require a necc. order."""
        self.list = []

    def addMe(self, add):
        """Adds an item to the list."""
        self.list.append(add)
        return self.list

    def getID(self, pick):
        """Gets the ID of the list. Generally to be used when storing lists
        within the storage list – this can be used to find what the list
        you are accessing holds. e.g. [[SensName, <dist>], Sens2, <dist2>]]
        to get sensNames"""
        return self.list[pick][0]

    def getValue(self, pick):
        """Gets the secondary item of the list within storage list"""
        return self.list[pick][1]

    def length(self):
        """Gets the length of the storage list."""
        return len(self.list)

    def getAll(self):
        """Returns the entire storage list."""
        return self.list

    def reset(self):
        """Resets the list entirely."""
        self.list = []
