from model.group import Group
from model.question import Question


class Game:
    def __init__(self):
        self.group = Group()
        self.isCreated = False
        self.isStarted = False
        self.question = Question()
        self.correct_members = []

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
        self.correct_members = []

    def answerQuestion(self, username, answer_text):
        # TODO flag if answer correctly
        is_correct = self.question.checkAnswer(answer_text)
        if is_correct:
            # TODO prevent user to be added twice in correct_members
            self.correct_members.append(username)
        return is_correct

    def endQuestion(self):
        self.group.setMembers(self.correct_members)
        return self.group.members > 1

    def checkWinner(self):
        if self.group.countMembers() == 1:
            return self.group.members[0]
        else:
            return None

    def end(self):
        self.isCreated = False
        self.isStarted = False
        self.group.removeAllMembers()
