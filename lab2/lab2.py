
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Task 1 
1.1)  Compute the number of wins for all teams in MLB in 2010-2015, display them in a descending sorted order. 
# In[210]:


df_team = pd.read_csv('teams.csv')
years = (df_team['yearID'] >= 2010) & (df_team['yearID'] <= 2015)
df_teams_five_ys = df_team.loc[years]
df_wins = df_teams_five_ys.groupby('teamID', as_index = False)[['teamID','W']].sum()
df_wins.columns = ['Team', 'Number of wins']
df_wins_sort = df_wins.sort_values(by = 'Number of wins', ascending = False)
df_wins_sort


# In[216]:


plt.figure()
df_wins_sort.plot(x = 'Team', y = 'Number of wins', kind = 'bar', figsize = (10, 6))
plt.title("Number of wins for all teams in MLB in 2010-2015")
plt.xlabel("Team")
plt.ylabel("NUmber of wins")
plt.show()

1.2)  Compute the average payroll per year for all teams in 2010-2015, displaying them in a descending sorted order 
# In[217]:


df_player = pd.read_csv('players.csv')
df_player.head(5)
years2 = (df_player['yearID'] >= 2010) & (df_player['yearID'] <= 2015)
df_player_five_ys = df_player.loc[years2]
df_mean_salary = df_player_five_ys.groupby('teamID', as_index = False)[['teamID','salary']].sum()
df_mean_salary['avg_salary'] = df_mean_salary['salary'] / 6
df_mean_salary.columns = ['Team', 'Salary', 'Average payroll per year']
df_salary_sort = df_mean_salary.sort_values(by = 'Average payroll per year', ascending = False)
df_salary_sort


# In[218]:


df_salary_sort.plot(x = 'Team', y = 'Average payroll per year', kind = 'bar', figsize = (10, 6))
plt.title("Average payroll per year for all teams in 2010-2015")
plt.xlabel("Team")
plt.ylabel("Average payroll per year")
plt.show()

1.3)  Create a visualization of your choice which will all allow you to show whether a team’s winning record is related to its payroll. 
# In[219]:


# Merge the the data frame of total wins and the average payroll
df_merge = pd.merge(df_wins, df_mean_salary, on = ['Team'])
plt.figure(figsize = (10, 6))
plt.title("Number of wins VS Average payrolls for all teams from 2010 to 2015")
plt.xlabel("Average payroll per year")
plt.ylabel("Number of wins")
plt.scatter(x = df_merge['Average payroll per year'], y = df_merge['Number of wins'])
plt.show()

Based on this scatter graph, I think that the total wins are not quite related to the average payroll. Some teams with relatively small average payroll (3,000,000 - 5,000,000) also have a high number of wins which is larger than 500. But some teams with this payroll have a smaller number of payrolls (400 - 450). So there is not an abvious relationship between them. However, what is interesting here is that the teams with a very low payroll (2,000,000 is considered a very low payroll among all teams) have a very small number of wins, and the teams with a higher average payroll (a payroll that is larger than 6,000,000 is considered high here) tend to have a higher number of wins (larger than 500). So we can conclude that a team with a relatively higher average payroll usually will not have a very small number of wins, but threre is not a necassary relationship between the average payroll and the number of wins. 2.1)  Compute the Batting Averages  for all the MLB teams in 2010-2015, display them in a descending sorted order. The Batting Average is defined as Hits/At Bats. The average is calculated from all players in each team. 
# In[220]:



def average_batting(x):
    if x['AB'] > 0:
        return (1.0 * x['H']) / (1.0 * x['AB'])
    else:
        return 0

df_player_h_ab = df_player_five_ys.copy()[['yearID', 'teamID', 'H', 'AB']]
df_player_h_ab['Average Batting'] = df_player_h_ab.apply(average_batting, axis = 1)
df_player_h_ab.groupby(['yearID', 'teamID'], as_index = False)[['Average Batting']].mean()
df_player_h_ab.columns = ['yearID', 'Team', 'H', 'AB', 'Average Batting']
df_team_h_ab = df_player_h_ab.groupby('Team', as_index = False).mean()
df_team_h_ab_sort = df_team_h_ab.sort_values(by = 'Average Batting', ascending = False)
df_team_h_ab_sort


# In[221]:


df_team_h_ab_sort.plot(x = 'Team', y = 'Average Batting', kind = 'bar', figsize = (10, 6))
plt.title("Batting Averages  for all the MLB teams in 2010-2015")
plt.xlabel("Team")
plt.ylabel("Batting Averages")
plt.show()

2.2) Create a visualization of your choice which will allow you to decide whether a team’s batting average is related to its win-loss record.
# In[222]:


df_win_loss = df_teams_five_ys.groupby('teamID', as_index = False)[['teamID','W', 'L']].sum()
df_win_loss['Win-loss'] = df_win_loss['W'] - df_win_loss['L']
df_win_loss.columns = [['Team', 'Win', 'Loss', 'Win-loss']]
df_merge2 = pd.merge(df_team_h_ab, df_win_loss, on = 'Team')
plt.figure(figsize = (10, 6))
plt.scatter(x = df_merge2['Win-loss'], y = df_merge2['Average Batting'])
plt.xlabel("Win loss")
plt.ylabel("Average batting")
plt.title("Average batting VS Win loss for all teams from 2010 to 2015")
plt.show()


# Based on this graph, I think there is not a relationship between the average batting and the win loss. We notice that for a certain value of win-loss, the average batting can be either low or high. 
3.1) Display the average ERA (Earned Run Average) per pitcher for all the MLB teams in 2010-2015, in a descending sorted order. A lower ERA indicates a better pitching performance. 
# In[223]:


df_team_era = df_teams_five_ys.groupby('teamID', as_index = False)[['ERA']].sum()
df_team_era['Average ERA'] = df_team_era['ERA'] / 6
df_team_era.columns = ['Team', 'ERA', 'Average ERA']
df_team_era_sort = df_team_era.sort_values(by = 'Average ERA', ascending = False)
df_team_era.columns = ['Team', 'ERA', 'Average ERA']
df_team_era_sort


# In[224]:


df_team_era_sort.plot(x = 'Team', y = 'Average ERA', kind = 'bar', figsize = (10, 6))
plt.title("Average ERA (Earned Run Average) per pitcher for all the MLB teams in 2010-2015")
plt.xlabel("Team")
plt.ylabel("Batting Averages")
plt.show()

3.2) Create a visualization of your choice which will allow you to decide if a team’s win-loss record is related to its pitching performance.
# In[225]:


df_merge3 = pd.merge(df_team_era, df_win_loss, on = 'Team')
plt.figure(figsize = (10, 6))
plt.scatter(x = df_merge3['Average ERA'], y = df_merge3['Win-loss'])
plt.title("Wins-loss record VS pitching performance for all teams from 2010 to 2015")
plt.xlabel("Average ERA")
plt.ylabel("Win loss")
plt.show()

I don't think there is an abvious relationship between the average ERA and the number of wins. We can notice that the teams with similar average ERA (when ERA is in the range of 3.5 to 4) have different number of win-loss. But what is interesting is that when the ERA is greater than 4.3, the win-loss are all very poor. Using visualization to show the following trend: For the top 5 teams that have the most total wins between 2010 and 2015: 4.1) How are their Batting Averages changed from 2010-2015
# In[226]:


top_five_teams = list(df_wins.nlargest(5, 'Number of wins').Team)
print "Top five teams based on total wins: ", top_five_teams


# In[227]:


df_top_five_h_ab = df_player_five_ys[df_player_five_ys['teamID'].isin(top_five_teams)].groupby(['yearID', 'teamID'], as_index = False)[['teamID','H', 'AB']].sum()
df_top_five_h_ab['average_batting'] = df_top_five_h_ab.apply(average_batting, axis = 1)
df_top_five_h_ab

fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(6)

plt.title("Changes of batting avaerage of the top 5 teams (based on the total wins) from 2010 to 2015")
for key, row in df_top_five_h_ab.groupby('teamID'):
    ax = row.plot(ax = ax, kind = 'line', x = 'yearID', y = 'average_batting', label = key)
ax.set_xlabel("Year")
ax.set_ylabel("Batting average")
plt.legend()
plt.show()

4.2) How are their Wins/Losses changed from 2010-2015
# In[228]:


df_top_five_wins = df_teams_five_ys[df_teams_five_ys['teamID'].isin(top_five_teams)].groupby(['yearID', 'teamID'], as_index = False)[['teamID', 'W', 'L']].sum()
df_top_five_wins
fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(6)

plt.title("Changes of wins of the top 5 teams (based on the total wins) from 2010 to 2015")
for key, row in df_top_five_wins.groupby('teamID'):
    ax = row.plot(ax = ax, kind = 'line', x = 'yearID', y = 'W', label = key)
ax.set_xlabel("Year")
ax.set_ylabel("Total wins")
plt.legend()
plt.show()


# In[229]:


fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(6)

plt.title("Changes of loss of the top 5 teams (based on the total wins) from 2010 to 2015")
for key, row in df_top_five_wins.groupby('teamID'):
    ax = row.plot(ax = ax, kind = 'line', x = 'yearID', y = 'L', label = key)
ax.set_xlabel("Year")
ax.set_ylabel("Total loss")
plt.legend()
plt.show()

4.3) How are their average ERAs changed from 2010-2015 
# In[230]:


df_top_five_era = df_teams_five_ys[df_teams_five_ys['teamID'].isin(top_five_teams)].groupby(['yearID', 'teamID'], as_index = False)[['ERA']].mean()
df_top_five_era.columns = ['yearID', 'teamID', 'Average ERA']
fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(6)

plt.title("Changes of average ERA of the top 5 teams (based on the total wins) from 2010 to 2015")
for key, row in df_top_five_era.groupby('teamID'):
    ax = row.plot(ax = ax, kind = 'line', x = 'yearID', y = 'Average ERA', label = key)
ax.set_xlabel("Year")
ax.set_ylabel("Average ERA")
plt.legend()
plt.show()

4.4) How are their annual payrolls changed from 2010-2015
# In[231]:


df_top_five_salary = df_player_five_ys[df_player_five_ys['teamID'].isin(top_five_teams)].groupby(['yearID', 'teamID'], as_index = False)[['teamID', 'salary']].mean()
df_top_five_salary.columns = ['yearID', 'teamID', 'Average annual payroll']
fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(6)

plt.title("Changes of average annual payroll of the top 5 teams (based on the total wins) from 2010 to 2015")
for key, row in df_top_five_salary.groupby('teamID'):
    ax = row.plot(ax = ax, kind = 'line', x = 'yearID', y = 'Average annual payroll', label = key)
ax.set_xlabel("Year")
ax.set_ylabel("Annual payroll")
plt.legend()
plt.show()

