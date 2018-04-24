# Import necessary modules 
# This file does all the calculations and analysis
import csv 
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from rename import *  


# Round Function from notes 
import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

# Get Matchday from excel file 
def getMatchday(league, num):
    if league == 'prem':
        path = 'epl17-18.xlsx'
        allMatches = pd.read_excel(path)
        matchday = allMatches.iloc[num*10-10:num*10, lambda df: [4,5]]
    
    elif league == 'liga':
        path = 'laliga17-18.xlsx'
        allMatches = pd.read_excel(path)
        matchday = allMatches.iloc[num*10-10:num*10, lambda df: [4,5]]

    elif league == 'serie A':
        path = 'seriea17-18.xlsx'
        allMatches = pd.read_excel(path)
        matchday = allMatches.iloc[num*10-10:num*10, lambda df: [4,5]]

    elif league == 'bundes':
        path = 'bundesliga17-18.xlsx'
        allMatches = pd.read_excel(path)
        matchday = allMatches.iloc[num*9-9:num*9, lambda df: [4,5]]

    games = []
    for row in matchday.iterrows():
        games.append([row[1][0], row[1][1]])
    return games

# Get data from csv file
def getCsv(path):
    data = pd.read_csv(path)
    data = data[['HomeTeam','AwayTeam','FTHG','FTAG']]
    data = pd.concat([data[['HomeTeam','AwayTeam','FTHG']].assign(home=1).rename(
        columns={'HomeTeam':'team', 'AwayTeam':'opponent','FTHG':'goals'}), 
        data[['AwayTeam','HomeTeam','FTAG']].assign(home=0).rename(
        columns={'AwayTeam':'team', 'HomeTeam':'opponent','FTAG':'goals'})])

    return data 

def averagesHome(league, home):
    home = renameWrapper('players', league, home)

    data = pd.read_csv('CompleteDataset.csv')
    data = data[['Name', 'Age', 'Overall', 'Club','Preferred Positions']]
    
    homePlayers = data.loc[data['Club'] == home]
    homePlayers = homePlayers.reset_index()

    mvp = homePlayers.loc[homePlayers.loc[:, 'Overall'].idxmax(), 'Name']
    meanAge = roundHalfUp(homePlayers['Age'].mean())

    Defense = {'GK', 'CB', 'RCB', 'LCB', 'RB', 'LB', 'RWB', 'LWB'}
    Midfield = {'CDM', 'CM', 'LM', 'RM', 'CAM'}
    Attack = {'LW', 'RW', 'RF', 'LF', 'RS', 'LS', 'ST', 'CF'}

    ddf, mdf, adf = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    for i in range(homePlayers.shape[0]):
        if homePlayers.loc[i,['Preferred Positions']][0].rsplit()[0] in Defense:
            ddf = ddf.append(homePlayers.loc[i])
        elif homePlayers.loc[i,['Preferred Positions']][0].rsplit()[0] in Midfield:
            mdf = mdf.append(homePlayers.loc[i])
        elif homePlayers.loc[i,['Preferred Positions']][0].rsplit()[0] in Attack:
            adf = adf.append(homePlayers.loc[i])

    meanDefense = roundHalfUp(ddf['Overall'].mean())
    meanMidfield = roundHalfUp(mdf['Overall'].mean())
    meanAttack = roundHalfUp(adf['Overall'].mean())

    return meanAttack, meanMidfield, meanDefense, mvp, meanAge  

def averagesAway(league, away):
    away = renameWrapper('players', league, away)

    data = pd.read_csv('CompleteDataset.csv')
    data = data[['Name', 'Age', 'Overall', 'Club','Preferred Positions']]

    awayPlayers = data.loc[data['Club'] == away] 
    awayPlayers = awayPlayers.reset_index() 

    mvp = awayPlayers.loc[awayPlayers.loc[:, 'Overall'].idxmax(), 'Name'] 
    meanAge = roundHalfUp(awayPlayers['Age'].mean())

    Defense = {'GK', 'CB', 'RCB', 'LCB', 'RB', 'LB', 'RWB', 'LWB'}
    Midfield = {'CDM', 'CM', 'LM', 'RM', 'CAM'}
    Attack = {'LW', 'RW', 'RF', 'LF', 'RS', 'LS', 'ST', 'CF'}

    ddf, mdf, adf = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    for i in range(awayPlayers.shape[0]):
        if awayPlayers.loc[i,['Preferred Positions']][0].rsplit()[0] in Defense:
            ddf = ddf.append(awayPlayers.loc[i])
        elif awayPlayers.loc[i,['Preferred Positions']][0].rsplit()[0] in Midfield:
            mdf = mdf.append(awayPlayers.loc[i])
        elif awayPlayers.loc[i,['Preferred Positions']][0].rsplit()[0] in Attack:
            adf = adf.append(awayPlayers.loc[i])

    meanDefense = roundHalfUp(ddf['Overall'].mean())
    meanMidfield = roundHalfUp(mdf['Overall'].mean())
    meanAttack = roundHalfUp(adf['Overall'].mean())

    return meanAttack, meanMidfield, meanDefense, mvp, meanAge  

 # Get head to head from 2008 to 2016
def headToHead(matches, hometeam, awayteam):

    #Matches where first team is at home 
    home = matches[(matches['home_team_api_id'] == hometeam) &
                   (matches['away_team_api_id'] == awayteam)]
    #Matches where the second team is at home 
    away = matches[(matches['home_team_api_id'] == awayteam) & 
                   (matches['away_team_api_id'] == hometeam)]
    #Merge these two 
    total = pd.concat([home, away])
    return total 

 # Get goalscoring rate for away and home teams 
def getRates(data, home, away):
    totalHomeGoals = data.mean()[0]
    totalAwayGoals = data.mean()[1]
    homeTeamGoals = data[(data['HomeTeam'] == home)].mean()[0]
    awayTeamGoals = data[(data['AwayTeam'] == away)].mean()[1]
    totalHomeConceds = totalAwayGoals
    totalAwayConceds = totalHomeGoals 
    homeTeamConceds = awayTeamGoals
    awayTeamConceds = homeTeamGoals
    homeRate = (totalHomeGoals*(homeTeamGoals/totalHomeGoals)*
                 (homeTeamConceds/totalHomeConceds))
    awayRate = (totalAwayGoals * (awayTeamGoals/totalAwayGoals) * 
                (awayTeamConceds/totalAwayConceds))
    return homeRate, awayRate

def predict(league, matchday):
    games = getMatchday(league, matchday)

    gamesWithScore = [] 
    
    for i in range(len(games)): 

        home = renameWrapper('goals', league, games[i][0])
        away = renameWrapper('goals', league, games[i][1])
        
        home2 = renameWrapper('players', league, home)
        away2 = renameWrapper('players', league, away)

        gamesWithScore.append({'Away': away,'Home': home,  
        'Home Goals': predictGame(league, home, away)[0], 
        'Away Goals': predictGame(league, home, away)[1],
        'Home Attack Rating': averagesHome(league, home2)[0], 
        'Away Attack Rating': averagesAway(league, away2)[0],
        'Home Midfield Rating': averagesHome(league, home2)[1],
        'Away Midfield Rating': averagesAway(league, away2)[1],
        'Home Defense Rating': averagesHome(league, home2)[2],
        'Away Defense Rating': averagesAway(league, away2)[2],
        'Home Best Player': averagesHome(league, home2)[3], 
        'Away Best Player': averagesAway(league, away2)[3],  
        'Home Player Age': averagesHome(league, home2)[4],
        'Away Player Age': averagesAway(league, away2)[4]}) 

    df = pd.DataFrame(gamesWithScore, 
            columns=['Home', 'Home Goals', 'Away', 'Away Goals',
                'Home Attack Rating', 'Away Attack Rating', 'Home Midfield Rating', 
                'Away Midfield Rating', 'Home Defense Rating', 'Away Defense Rating', 
                'Home Best Player', 'Away Best Player', 'Home Player Age', 
                'Away Player Age'])
    return df  

def predictGame(league, team1, team2):
    import rpy2.robjects as robjects
    from rpy2.robjects.packages import importr
    from rpy2.robjects import pandas2ri, Formula

    pandas2ri.activate()

    countr = importr('Countr')
    base = importr('base')
    lmtest = importr('lmtest')
    stats = importr('stats')
    

    if league == 'prem':
        data_ = getCsv('EPL17-18.csv')
    
    elif league == 'liga':
        data_ = getCsv('Liga17-18.csv')

    elif league == 'serie A':
        data_ = getCsv('SerieA17-18.csv')

    elif league == 'bundes':
        data_ = getCsv('Bundes17-18.csv')

    robjects.globalenv['rdata'] = data_

    # R code came from this guy: 
    # https://github.com/dashee87/blogScripts/blob/master/R/2017-05-30-predicting-football-results-with-statistical-modelling.R
    a = robjects.r(''' glm(goals ~ home + team + opponent, family=poisson(link=log),data=rdata)
        ''')

    robjects.r('''
        library(Countr)
        simulate_match_home <- function(foot_model, homeTeam, awayTeam){
          home_goals_avg <- predict(foot_model, data.frame(home=1, team=homeTeam,
                                      opponent=awayTeam), type="response")
          away_goals_avg <- predict(foot_model, data.frame(home=0, team=awayTeam,
                                      opponent=homeTeam), type="response")
          return(round(home_goals_avg, 0))
        }
        ''')

    robjects.r('''
        library(Countr)
        simulate_match_away <- function(foot_model, homeTeam, awayTeam){
          home_goals_avg <- predict(foot_model, data.frame(home=1, team=homeTeam,
                                      opponent=awayTeam), type="response")
          away_goals_avg <- predict(foot_model, data.frame(home=0, team=awayTeam,
                                      opponent=homeTeam), type="response")
          return(round(away_goals_avg, 0))
        }
        ''')

    r_f = robjects.globalenv['simulate_match_home']
    r_f1 = robjects.globalenv['simulate_match_away']
    
    HomeGoals = int(r_f(a, team1, team2)[0])
    AwayGoals = int(r_f1(a, team1, team2)[0])

    return HomeGoals, AwayGoals 


def predictGameProb(league, team1, team2): 
    import rpy2.robjects as robjects
    from rpy2.robjects.packages import importr
    from rpy2.robjects import pandas2ri, Formula

    pandas2ri.activate()

    countr = importr('Countr')
    base = importr('base')
    lmtest = importr('lmtest')
    stats = importr('stats')
    

    if league == 'prem':
        data_ = getCsv('EPL17-18.csv')
    
    elif league == 'liga':
        data_ = getCsv('Liga17-18.csv')

    elif league == 'serie A':
        data_ = getCsv('SerieA17-18.csv')

    elif league == 'bundes':
        data_ = getCsv('Bundes17-18.csv')

    robjects.globalenv['rdata'] = data_
    fmla = Formula("goals ~ 1")
    env = fmla.environment

    homeWei = countr.renewalCount(formula = fmla, data = data_,
    dist = "weibull", weiMethod = "conv_dePril", computeHessian = False,
    control = countr.renewal_control(trace = 0, method = "nlminb"))

    plistHome = []
    for i in range(6):
        plistHome.append(countr.predict_renewal(homeWei, 
    pd.DataFrame(data={'team': team1, 'opponent': team2,'home':1, 'goals':i},
                                                       index=[1]), 'prob'))

    return plistHome



def getTeams(league):
    if league == 'prem': 
        a = getCsv('EPL17-18.csv').head(10).loc[0:9,'team']
        b = getCsv('EPL17-18.csv').head(10).loc[0:9,'opponent']
        teams = pd.concat([a,b]) 
        teams = teams.reset_index()
        del teams['index']
        teams.columns = ['Teams']
        return teams

    elif league == 'serie A':
        a = getCsv('SerieA17-18.csv').head(10).loc[0:9,'team']
        b = getCsv('SerieA17-18.csv').head(10).loc[0:9,'opponent']
        teams = pd.concat([a,b])
        teams = teams.reset_index()
        del teams['index']
        teams.columns = ['Teams']
        return teams

    elif league == 'liga':
        a = getCsv('Liga17-18.csv').head(10).loc[0:9,'team']
        b = getCsv('Liga17-18.csv').head(10).loc[0:9,'opponent']
        teams = pd.concat([a,b])
        teams = teams.reset_index()
        del teams['index']
        teams.columns = ['Teams']
        return teams

    elif league == 'bundes':
        a = getCsv('Bundes17-18.csv').head(9).loc[0:9,'team']
        b = getCsv('Bundes17-18.csv').head(9).loc[0:9,'opponent']
        teams = pd.concat([a,b]).reset_index()
        del teams['index']
        teams.columns = ['Teams']
        return teams
