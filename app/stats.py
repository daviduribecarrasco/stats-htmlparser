import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import datetime
import os
from os.path import isfile, join
import csv
import shutil
import sqlite3
import pandas
import pandas as pd

def get_stats():
    
    pl_url = "https://www.premierleague.com/stats/top/players/goals"
    resp = urllib.request.urlopen(pl_url)
    html = resp.read()
    soup = BeautifulSoup(html,"html.parser")
    playerstats= []
    
    for tr in soup.find_all('tr')[1:]:
        ##playerstats = {'player':""}
        player_info = tr.find_all('td')
        """
        playerstats.update ({'rank' : player_info[0].text})
        playerstats.update ({'player' : player_info[1].text.replace("\n","") })
        playerstats.update ({'team' : player_info[2].text.replace("\n","") })
        playerstats.update ({'nationality' : player_info[3].text.replace("\n","") })
        playerstats.update ({'goals scored' : player_info[4].text })
        """
        playerstats.append({"Rank": player_info[0].text,"Player":player_info[1].text.replace("\n",""),"Team":player_info[2].text.replace("\n",""),"Nationality":player_info[3].text.replace("\n",""),"Goals":player_info[4].text.replace("\n","")})
        
        
        csv_file = "soccerdata.csv"
        csv_columns = ['Rank','Player','Team','Nationality','Goals']
        try:
            with open(csv_file,'w') as csv_file:
                writer = csv.DictWriter(csv_file,fieldnames=csv_columns)
                writer.writeheader()
                for player in playerstats:
                    writer.writerow(player)
        except IOError:
            print('')
        
    print(playerstats)

        

    





if __name__ == '__main__':
    get_stats()