class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=score
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

torres=Player('Fernando','Torres')
torres_scores=[0,0,1,0,1]
i=0
for i in torres_scores:
    torres.add_score(i)
    i+=1

print torres.average_score()


        
    
