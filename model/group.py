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

    def getAllMembersNotInTheList(self, members_list):
        not_in_the_list_members = []
        for member in self.members:
            if member not in members_list:
                not_in_the_list_members.append(member)
        return not_in_the_list_members

    def setMembers(self, members_list):
        self.members = members_list