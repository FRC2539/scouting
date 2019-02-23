import csv
import v3client
from team import Team
from v3client.api.event_api import EventApi
from v3client.api.match_api import MatchApi

with open('csvfile.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')

    event_key = '2019week0'

    eventApi = EventApi()
    matchApi = MatchApi()
    oprResponse = eventApi.get_event_op_rs(event_key)
    matchResponse = matchApi.get_event_matches(event_key)

    avgScore = 0
    avgWin = 0
    avgLoss = 0
    count = 0

    for match in matchResponse:
        print('Match: ' + str(match.match_number))

        try:
            blue = match.score_breakdown['blue']['totalPoints']
            red = match.score_breakdown['red']['totalPoints']

            print('     Blue: ' + str(blue))
            print('     Red:  ' + str(red))

            avgScore = avgScore + blue + red

            if blue >= red:
                avgWin = avgWin + blue
                avgLoss = avgLoss + red
            else:
                avgWin = avgWin + red
                avgLoss = avgLoss + blue

            count += 2

        except TypeError:
            print('     No score data')

    avgScore = avgScore / count
    avgWin = avgWin / (count / 2)
    avgLoss = avgLoss / (count / 2)

    print('Average:      ' + str(avgScore))
    print('Average Win:  ' + str(avgWin))
    print('Average Loss: ' + str(avgLoss))

    teamRow, ccwmRow, dprRow, oprRow = [], [], [], []

    for team, ccwm in oprResponse.ccwms.items():
        ccwmRow.append(round(ccwm, 2))
        teamRow.append(int(team[3:len(team)]))

    for team, dpr in oprResponse.dprs.items():
        dprRow.append(round(dpr, 2))

    for team, opr in oprResponse.oprs.items():
        oprRow.append(round(opr, 2))


    teamNums, ccwms, dprs, oprs = [], [], [], []


    count = len(teamRow) - 1
    while count >= 0:
        smallest = count

        array2 = teamRow
        count2 = count
        while count2 >= 0:
            if array2[count2] <= array2[smallest]:
                smallest = count2

            count2 -= 1

        teamNums.append(teamRow.pop(smallest))
        ccwms.append(ccwmRow.pop(smallest))
        dprs.append(dprRow.pop(smallest))
        oprs.append(oprRow.pop(smallest))

        count -= 1

    count = 0
    teams = []
    teamKey = ''
    for team in teamNums:
        print(team)
        teamKey = 'frc' + str(team)

        teams.append(Team(team, {'ccwm' : ccwms[count], 'dpr' : dprs[count], 'opr' : oprs[count]}))

        count += 1

    ranks = []
    avgs = []

    for team in teams:
        ranks.append(team.getStat('rank'))
        avgs.append(team.getStat('avgScore'))


    writer.writerow(['Team:    '] + teamNums)
    writer.writerow(['Rank:    '] + ranks)
    writer.writerow(['OPR:     '] + oprs)
    writer.writerow(['DPR:     '] + dprs)
    writer.writerow(['CCWM:    '] + ccwms)
    writer.writerow(['AVG:     '] + avgs)
    writer.writerow([])
    writer.writerow(['Avg:     ', round(avgScore, 2)])
    writer.writerow(['AvgWin:  ', round(avgWin, 2)])
    writer.writerow(['AvgLoss: ', round(avgLoss, 2)])