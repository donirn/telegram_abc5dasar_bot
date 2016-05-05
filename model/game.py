from model.group import Group
from model.question import Question


class Game:
    def __init__(self):
        self.group = Group()
        self.isCreated = False
        self.isStarted = False
        self.question = Question()

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
            self.startQuestion()
            return True
        elif not self.isCreated:
            # TODO handle game not created yet
            pass
        else:
            # TODO handle group members should be more than 1
            pass

    def startQuestion(self):
        self.question = Question()

    def answerQuestion(self, username, answer_text):
        # TODO check if the answer is true given the question
        return True

    def endQuestion(self):
        # TODO check if end game condition is met then end the game
        return True

    def end(self):
        self.isCreated = False
        self.isStarted = False
        self.group.removeAllMembers()
