#Part II

import datetime
class Player:
    def __init__(self,firstname,lastname,team):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team

    def add_score(self,score):
        n_score=self.scores.append(score)
        return n_score

    def total_score(self):
        t_score=sum(self.scores)
        return t_score

    def average_score(self):
        average=self.total_score()/float(len(self.scores))
        return average

torres=Player('Fernando','Torres','spain')
torres_scores=[0,0,1,0,1]
i=0
for i in torres_scores:
    torres.add_score(i)
    i+=1

print torres.average_score()


        
#Part III
class Team:
    def __init__(self,name,league,manager_name,points):
        self.name=name
        self.league=league
        self.manager_name=manager_name
        self.points=points
        self.players=[]

    def add_player(self,player):
        self.players.append(player)

    def __str__(self):
        return '''Team:%s\nLeague:%s\nManager:%s\nPoints:%d'''\
        %(self.name,self.league,self.manager_name,self.points)

Portugal=Team('Portugal','Euro2012','...',10)
Spain=Team('Spain','Euro2012','...',12)

print Spain.__str__()
print



Torres = Player('Fernando','Torres',Spain)
Ronaldo = Player('Cristiano','Ronaldo',Portugal)

print

#print Torres.team

Spain.add_player(Torres)
Portugal.add_player(Ronaldo)

class Match:
    def __init__(self,home_team,away_team,date):
        self.home_team=home_team
        self.away_team=away_team
        self.date=date
        self.home_scores={}
        self.away_scores={}

    def home_score(self):
        for value in self.home_scores:
            self.home_scores[value] = [sum(self.home_scores[value])]
        if self.home_scores[value]>0:
            return self.home_scores[value]
        elif self.home_scores[value]==0:
            return 0

    def away_score(self):
        for value in self.away_scores:
            self.away_scores[value] = [sum(self.away_scores[value])]
        if self.away_scores[value]>0:
            return self.away_scores[value]
        elif self.away_scores[value]==0:
            return 0

    def winner(self):
        home=self.home_scores[value]
        away=self.away_scores[value]
        if home>away:
            return 'The winner is'+" "+'%s' %(self.home_team)
        elif away>home:
            return 'The winner is'+" "+'%s' %(self.away_team)
        elif away==home:
            return 'DRAW'

    def add_score(self,Player,score):
        team= Player.team.name
        if team==self.home_team:
            self.home_scores[Player]=[score]
            return self.home_score()
        elif team==self.away_team:
            self.away_scores[Player]=[score]
            return self.away_score()
            

euro_semi_final=Match('Spain','Portugal',datetime.date(2012,06,27))
euro_semi_final.add_score(Torres,1)
euro_semi_final.add_score(Ronaldo,1)
euro_semi_final.add_score(Torres,1)
print euro_semi_final.winner()
  


