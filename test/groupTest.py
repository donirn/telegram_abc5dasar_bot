import unittest
from model.group import *


class MyTestCase(unittest.TestCase):
    def countMembers_test(self):
        group = Group()
        assert group.countMembers() == len(group.members)
        group.addMember("1")
        group.addMember("2")
        assert group.countMembers() == len(group.members)
        group.removeMember("3")
        assert group.countMembers() == len(group.members)
        group.removeAllMembers()
        assert group.countMembers() == len(group.members)

    def addMember_test(self):
        group = Group()
        group.addMember("1")
        assert len(group.members) == 1

        group.addMember("1")
        assert len(group.members) == 1

        group.addMember("2")
        assert len(group.members) == 2

        for i in range(1000):
            group.addMember(str(i))
        assert len(group.members) == 1000

    def removeMember_test(self):
        group = Group()

        group.removeMember("1")
        assert len(group.members) == 0

        for i in range(1000):
            group.addMember(str(i))
        group.removeMember("3")
        assert len(group.members) == 999

    def removeAllMembers_test(self):
        group = Group()

        for i in range(1000):
            group.addMember(str(i))
        group.removeAllMembers()
        assert len(group.members) == 0

if __name__ == '__main__':
    unittest.main()
