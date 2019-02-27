from v3client.api.event_api import EventApi
from v3client.api.team_api import TeamApi

class Team(object):
    def __init__(self, number, stats):
        self.event_key = '2019week0'
        self.number = number
        self.team_key = 'frc' + str(self.number)
        self.async_ = False
        self.stats = stats
        try:
            stats['rank'] = EventApi().get_team_event_status(self.team_key, self.event_key).qual.ranking.rank
        except AttributeError:
            stats['rank'] = 0
        stats['avgScore'], stats['avgClimb'], stats['avgFouls'], stats['avgAuto'] = self.calcScoreStats()


    def getStat(self, stat):
        return self.stats[stat]


    def calcScoreStats(self):
        count = 0
        avgScore = 0
        climbScore = 0
        fouls = 0
        auto = 0
        matches = TeamApi().get_team_event_matches(self.team_key, self.event_key)

        for match in matches:
            try:
                if self.team_key in match.alliances.blue.team_keys:
                    avgScore += match.score_breakdown['blue']['totalPoints']
                    climbScore += match.score_breakdown['blue']['habClimbPoints']
                    #fouls: opposite alliance because we want the foul points caused by blue alliance.
                    fouls += match.score_breakdown['red']['foulPoints']
                    auto += match.score_breakdown['blue']['autoPoints']
                else:
                    avgScore += match.score_breakdown['red']['totalPoints']
                    climbScore += match.score_breakdown['red']['habClimbPoints']
                    #fouls: opposite alliance because we want the foul points caused by red alliance.
                    fouls += match.score_breakdown['blue']['foulPoints']
                    auto += match.score_breakdown['red']['autoPoints']

                count += 1

            except:
                pass

        return round(avgScore / count, 2), round(climbScore / count, 2), round(fouls / count, 2), round(auto / count, 2)
