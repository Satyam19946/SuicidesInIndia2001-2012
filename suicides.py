import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir("C:/users/satyam/desktop/programs/datasets/suicides")
#Reading File
suicides = pd.read_csv("suicides.csv")

#Make the graphs fullscreen before saving
def Fullscreen():
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())

"""
#creating a separate file for each state
#run only one time
for i in suicides.State.unique():
	newdb = suicides.loc[suicides.State == i]
	name_of_file = i + ".csv"
	newdb.to_csv(name_of_file)
"""

#Name of States, Number of States, Counts of Suicides in each State
name_of_states = list(suicides.State.unique())
number_of_states = len(suicides.State.unique())
counts = [0] * len(suicides.State.unique())
for i,j in zip(suicides.State.unique(),range(number_of_states)):
	counts[j] = suicides.Count.loc[suicides.State == i].agg([sum])

#Converting Counts from a dataframe to a list.
counts = np.array(counts)
counts_as_list = [0]* number_of_states
for i in range(len(counts)):
	counts_as_list[i] = counts[i][0]
	

#Plotting StatesvsTotalSuicides.
ax = plt.subplot()
plt.bar(range(len(counts_as_list)), counts_as_list)
ax.set_xticks(range(len(name_of_states)))
ax.set_xticklabels(name_of_states,rotation =90)
plt.subplots_adjust(bottom = 0.3)
plt.ylabel("Number of Suicides")
plt.title("Suicides in India")
Fullscreen()
#plt.savefig("suicides_numberofsuicidesvsstates.png")
#plt.show()

#No. of Suicides of each state for each age group. For ex. A & N Islands 0-14 x_suicides.
age_groups = list(suicides.Age.unique())
suicides_by_age = [0] * len(age_groups)
for i,j in zip(age_groups,range(len(age_groups))):
	suicides_by_age[j] = suicides.groupby('State').apply(lambda g: g.loc[g.Age == i]).groupby('State').Count.sum()

#Making Acronyms for states to fit the graph
states_names_acronyms = [''] * len(name_of_states)
for i,j in zip(name_of_states,range(len(name_of_states))):
	states_names_acronyms[j] = i[0:8]


#Plotting for age groups vs States
plt.close('all')
for i in range(len(suicides_by_age)-2):
	ax = plt.subplot(2,2,i+1)
	plt.bar(range(len(suicides_by_age[i])) , suicides_by_age[i])
	plt.title("Suicides in the age group " + age_groups[i])
	ax.set_xticks(range(len(states_names_acronyms)))
	ax.set_xticklabels(states_names_acronyms,rotation =90)
	ax.set_ylim(0,210000)

Fullscreen()
plt.subplots_adjust(left = 0.07,bottom = 0.11 , right = 0.96 , top = 0.96, wspace = 0.14 , hspace = 0.37)	
#plt.savefig("suicides_agegroupsvsstates.png")
plt.show()


Causes = suicides.groupby('Gender').apply(lambda d: d.loc[d.means == 'Causes']).reasons.unique()
Means = suicides.groupby('Gender').apply(lambda d: d.loc[d.means == 'Means_adopted']).reasons.unique()
Education_Status = suicides.groupby('Gender').apply(lambda d: d.loc[d.means == 'Education_Status']).reasons.unique()
Professional_Status = suicides.groupby('Gender').apply(lambda d: d.loc[d.means == 'Professional_Profile']).reasons.unique()
Social_Status = suicides.groupby('Gender').apply(lambda d: d.loc[d.means == 'Social_Status']).reasons.unique()

#Causes of Female Suicides and Male Suicides
counts_of_causes = [0] * len(Causes)
for i,j in zip(Causes,range(len(Causes))):
	counts_of_causes[j] = (suicides.groupby('Gender').apply(lambda d: d.loc[d.reasons == i]).Count.sum())

#Why Do People Die. Bar Graph of Number of Suicides vs Cause of death
ax = plt.subplot()
plt.bar(range(len(counts_of_causes)),counts_of_causes)
ax.set_xticks(range(len(Causes)))
plt.subplots_adjust(left = 0.05,bottom = 0.49,right = 0.96, top = 0.95 ,wspace = 0.2,hspace = 0.2)
ax.set_xticklabels(Causes,rotation = 90)
plt.title("Why Do People Commit Suicide")
Fullscreen()
#plt.savefig("Countsofcausesvscauses")
#plt.show()