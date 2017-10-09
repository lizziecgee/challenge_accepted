# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Challenge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    @property
    def winner(self):
        sessions = self.sessions.all()
        return sessions.last()

    @property
    def losers(self):
        losers = []
        sessions = self.sessions.all()
        for session in sessions:
            bouts = session.bouts.all()
            for bout in bouts:
                losers.append(bout.loser)
        return losers   

    @property
    def participants(self):
        results = []
        sessions = self.sessions.all()
        for session in sessions:
            bouts = session.bouts.all()
            for bout in bouts:
                participants = bout.participants.all()
                for participant in participants:
                    results.append(participant)
        return results  
    
