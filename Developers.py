import pandas as pd
import json
from pprint import pprint

filepath = 'C:\\Users\\Administrator\\Downloads\\Devellopers Skillset.xlsx'
file = pd.ExcelFile(filepath)

Skillsets= pd.read_excel(file,'Skillsets Matrix')
Business= pd.read_excel(file,'Business Area Matrix')
Experience= pd.read_excel(file,'Experience')
Expertise= pd.read_excel(file,'Expertise Matrix')



generalSkillsets = list(Skillsets)
businessAreas = list(Business)
devLevel = list(Experience)
expertiseLevel = list(Expertise)
experienceLevel = list(Experience)

devExperienceDict = {"Trainee": 1,
                     "Novice": 2,
                     "Junior": 3,
                     "Intermediate": 4,
                     "Senior": 5}    
entries = []


id = 1

for index in range((len(Skillsets.index))):
    developer = {}
    name = ""
    devSkillset = []
    devBusinessArea = []
    devExpertise = []
    devDaysOff = []
    

    for i in generalSkillsets :    
        if(i=='Dev'):
            name = Skillsets[i][index]    
        if (Skillsets[i][index] == 'x'):
            devSkillset.append(i)

    for i in businessAreas :
        if(Business[i][index] == 'x'):
            devBusinessArea.append(i)

    for i in expertiseLevel :
        if(Expertise[i][index] == 'x'):
            devExpertise.append(i)

    for i in experienceLevel:
        if(Experience[i][index] == 'x'):
            devExperience = str(devExperienceDict[i])
    developer['Id'] = id
    developer['Name'] =  name
    developer['General Skillset'] = devSkillset
    developer['Business Areas'] = devBusinessArea
    developer['Types of Expertise'] = devExpertise
    developer['Experience'] = devExperience
    developer['Country'] = "Greece"
    developer['Rate'] = 10
    developer['Slack ID'] = "000000"
    developer['DaysOff'] = devDaysOff
    developer['Role'] = "Technical"
    entries.append(developer)
    id += 1




result = {"Developers": [{"Developer" : entry} for entry in entries],
    "Experience Levels": [
        {
            "ID": "1",
            "Value": "Trainee"
        },
        {
            "ID": "2",
            "Value": "Novice"
        },
        {
            "ID": "3",
            "Value": "Junior"
        },
        {
            "ID": "4",
            "Value": "Intermediate"
        },
        {
            "ID": "5",
            "Value": "Senior"
        }
    ]}


