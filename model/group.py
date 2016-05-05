#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Group model
# Handles the group management

class Group:
    members = []

    def addMember(self, username):
        self.members.append(username)

    def removeMember(self, username):
        self.members.remove(username)

    def removeAllMembers(self):
        self.members = []

    def countMembers(self):
        return self.members.count()
