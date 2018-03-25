import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Task 1 
# 1.1)  Compute the number of wins for all teams in MLB in 2010-2015, display them in a descending sorted order. 

# Get the number of wins for all teams in 2010-2015
df_team = pd.read_csv('teams.csv')
years = (df_team['yearID'] >= 2010) & (df_team['yearID'] <= 2015)
df_teams_five_ys = df_team.loc[years]
df_wins = df_teams_five_ys.groupby('teamID', as_index = False)[['teamID','W']].sum()
df_wins.columns = ['Team', 'Number of wins']

# Sort by descending order
df_wins_sort = df_wins.sort_values(by = 'Number of wins', ascending = False)
df_wins_sort

# Show in the figure
plt.figure()
df_wins_sort.plot(x = 'Team', y = 'Number of wins', kind = 'bar', figsize = (10, 6))
plt.title("Number of wins for all teams in MLB in 2010-2015")
plt.xlabel("Team")
plt.ylabel("NUmber of wins")
plt.show()

# 1.2)  Compute the average payroll per year for all teams in 2010-2015, displaying them in a descending sorted order 

# Get the total payroll for each team in the five years
df_player = pd.read_csv('players.csv')
df_player.head(5)
years2 = (df_player['yearID'] >= 2010) & (df_player['yearID'] <= 2015)
df_player_five_ys = df_player.loc[years2]
df_mean_salary = df_player_five_ys.groupby('teamID', as_index = False)[['teamID','salary']].sum()
# Average payroll per year
df_mean_salary['avg_salary'] = df_mean_salary['salary'] / 6
df_mean_salary.columns = ['Team', 'Salary', 'Average payroll per year']
# Sort by descending order
df_salary_sort = df_mean_salary.sort_values(by = 'Average payroll per year', ascending = False)
df_salary_sort

# Show in a figure
df_salary_sort.plot(x = 'Team', y = 'Average payroll per year', kind = 'bar', figsize = (10, 6))
plt.title("Average payroll per year for all teams in 2010-2015")
plt.xlabel("Team")
plt.ylabel("Average payroll per year")
plt.show()

# 1.3) Create a visualization of your choice which will all allow you to show whether a team’s winning record is related to its payroll.
# Merge the the data frame of total wins and the average payroll
df_merge = pd.merge(df_wins, df_mean_salary, on = ['Team'])
# Plot the number of win and average payrolls in the graph to see if they are related
plt.figure(figsize = (10, 6))
plt.title("Number of wins VS Average payrolls for all teams from 2010 to 2015")
plt.xlabel("Average payroll per year")
plt.ylabel("Number of wins")
plt.scatter(x = df_merge['Average payroll per year'], y = df_merge['Number of wins'])
plt.show()

# 2.1) Compute the Batting Averages for each of the MLB teams over 2010-2015, display them in a descending sorted order. The Batting Average is defined as Hits/At Bats. The average is calculated from all players in each team.
# function for computing average batting
def average_batting(x):
    if x['AB'] > 0:
        return (1.0 * x['H']) / (1.0 * x['AB'])
    else:
        return 0

# Average batting in five years
df_player_h_ab = df_player_five_ys.copy()[['yearID', 'teamID', 'H', 'AB']]
df_player_h_ab['Average Batting'] = df_player_h_ab.apply(average_batting, axis = 1)
df_player_h_ab.groupby(['yearID', 'teamID'], as_index = False)[['Average Batting']].mean()
df_player_h_ab.columns = ['yearID', 'Team', 'H', 'AB', 'Average Batting']
df_team_h_ab = df_player_h_ab.groupby('Team', as_index = False).mean()
df_team_h_ab_sort = df_team_h_ab.sort_values(by = 'Average Batting', ascending = False)
df_team_h_ab_sort


df_team_h_ab_sort.plot(x = 'Team', y = 'Average Batting', kind = 'bar', figsize = (10, 6))
plt.title("Batting Averages  for all the MLB teams in 2010-2015")
plt.xlabel("Team")
plt.ylabel("Batting Averages")
plt.show()

# 2.2) Create a visualization of your choice which will allow you to decide whether a team’s batting average is related to its win-loss record.
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

# # 3.1) Display the average ERA (Earned Run Average) per pitcher for all the MLB teams in 2010-2015, in a descending sorted order. A lower ERA indicates a better pitching performance. 
df_team_era = df_teams_five_ys.groupby('teamID', as_index = False)[['ERA']].sum()
df_team_era['Average ERA'] = df_team_era['ERA'] / 6
df_team_era.columns = ['Team', 'ERA', 'Average ERA']
df_team_era_sort = df_team_era.sort_values(by = 'Average ERA', ascending = False)
df_team_era.columns = ['Team', 'ERA', 'Average ERA']
df_team_era_sort


df_team_era_sort.plot(x = 'Team', y = 'Average ERA', kind = 'bar', figsize = (10, 6))
plt.title("Average ERA (Earned Run Average) per pitcher for all the MLB teams in 2010-2015")
plt.xlabel("Team")
plt.ylabel("Batting Averages")
plt.show()

# 3.2) Create a visualization of your choice which will allow you to decide if a team’s win-loss record is related to its pitching performance.
df_merge3 = pd.merge(df_team_era, df_win_loss, on = 'Team')
plt.figure(figsize = (10, 6))
plt.scatter(x = df_merge3['Average ERA'], y = df_merge3['Win-loss'])
plt.title("Wins-loss record VS pitching performance for all teams from 2010 to 2015")
plt.xlabel("Average ERA")
plt.ylabel("Win loss")
plt.show()

# I don't think there is an abvious relationship between the average ERA and the number of wins. We can notice that the teams with similar average ERA (when ERA is in the range of 3.5 to 4) have different number of win-loss. But what is interesting is that when the ERA is greater than 4.3, the win-loss are all very poor. Using visualization to show the following trend: For the top 5 teams that have the most total wins between 2010 and 2015: 4.1) How are their Batting Averages changed from 2010-2015

# Top 5 teams based on number of wins
top_five_teams = list(df_wins.nlargest(5, 'Number of wins').Team)
print "Top five teams based on total wins: ", top_five_teams

# 4.1) How are their Batting Averages changed from 2010-2015
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

# 4.2) How are their Wins/Losses changed from 2010-2015

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

# 4.3) How are their average ERAs changed from 2010-2015 

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

# 4.4) How are their annual payrolls changed from 2010-2015

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

