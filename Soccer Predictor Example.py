import pandas as pd
import selenium

leagues_short = ['SP1', 'D1', 'E0', 'I1']
dict_historical_data = {}


for league in leagues_short:
    frames = []
    for i in range (15, 21):
        df = pd.read_csv("http://www.football-data.co.uk/mmz4281/"+str(i)+str(i+1)+"/"+league+".csv")
        df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
        df = df.rename(columns= {'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        df = df.assign(Season=i)
        frames.append(df)
    df_historical_data = pd.concat(frames)
    dict_historical_data[league] = df_historical_data