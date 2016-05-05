from model.group import *


class Game:
    def __init__(self):
        self.group = Group()
        self.isCreated = False
        self.isStarted = False

    def create(self):
        if not self.isCreated:
            self.isCreated = True
            self.isStarted = False
            self.group = Group()
            return True
        else:
            # TODO handle game already created
            pass

    def join(self, username):
        if self.isCreated and not self.isStarted:
            self.group.addMember(username)
            return True
        else:
            # TODO handle game not created yet
            pass

    def start(self):
        if self.isCreated and self.group.countMembers() == 1:
            self.isStarted = True
            return True
        elif not self.isCreated:
            # TODO handle game not created yet
            pass
        else:
            # TODO handle group members should be more than 1
            pass

    def answerQuestion(self, username, answerText):
        return True

    def end(self):
        self.isCreated = False
        self.isStarted = False
        self.group.removeAllMembers()
