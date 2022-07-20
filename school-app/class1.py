#!/usr/bin/env python3

class Class:
    def __init__(self,classId,lessonId,teacherId):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.classId = classId
        self.lessonId = lessonId
        self.teacherId = teacherId

    @staticmethod
    def createClass(obj):
        list = []

        for i in obj:
            list.append(Class(i[0],i[1],i[2]))
