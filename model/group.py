#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Group model
# Handles the group management

class Group:
    members = []

    def __init__(self):
        self.members = []

    def addMember(self, username):
        if username not in self.members:
            self.members.append(username)
        else:
            # TODO raise custom exception for adding existing member
            pass

    def removeMember(self, username):
        if username in self.members:
            self.members.remove(username)
        else:
            # TODO raise custom exception for removing non-existing member
            pass

    def removeAllMembers(self):
        self.members = []

    def countMembers(self):
        return len(self.members)