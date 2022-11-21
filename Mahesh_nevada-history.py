import pandas as pd
from typing import Any
from numpy import int64
 
#creating class with CovidData name
class CovidData:
       #specifing init and initializing the column names
       def __init__(self,state,death,deathConfirmed,deathIncrease):
              self.state = state
              self.death = death
              self.deathConfirmed = deathConfirmed
              self.deathIncrease = deathIncrease
           
       def __str__(self) -> Any:
              s= "************************************************\n"
              s += "State:\n" +self.state +"\n"
              s += "Death:\n"+self.death
              s += "\n" +"DeathConfirmed:\n" +self.deathConfirmed
              s += "\n" +"DeathIncrease:\n"+self.deathIncrease
              s += "\n************************************************\n"
              return s
           
#defining the datatypes for the columns     
data_type = {'date' :str, 'state':str, 'death':'Int64', 'deathConfirmed':str, 'deathIncrease':'Int64',
       'deathProbable':str, 'hospitalized':str, 'hospitalizedCumulative':str,
       'hospitalizedCurrently':'Int64', 'hospitalizedIncrease':'Int64', 'inIcuCumulative':str,
       'inIcuCurrently':'Int64', 'negative':'Int64', 'negativeIncrease':'Int64',
       'negativeTestsAntibody':'Int64', 'negativeTestsPeopleAntibody':'Int64',
       'negativeTestsViral':'Int64', 'onVentilatorCumulative':'Int64', 'onVentilatorCurrently':'Int64',
       'positive':'Int64', 'positiveCasesViral':'Int64', 'positiveIncrease':'Int64', 'positiveScore':'Int64',
       'positiveTestsAntibody':'Int64', 'positiveTestsAntigen':'Int64',
       'positiveTestsPeopleAntibody':'Int64', 'positiveTestsPeopleAntigen':'Int64',
       'positiveTestsViral':'Int64', 'recovered':'Int64', 'totalTestEncountersViral':'Int64',
       'totalTestEncountersViralIncrease':'Int64', 'totalTestResults':'Int64',
       'totalTestResultsIncrease':'Int64', 'totalTestsAntibody':'Int64', 'totalTestsAntigen':'Int64',
       'totalTestsPeopleAntibody':'Int64', 'totalTestsPeopleAntigen':'Int64',
       'totalTestsPeopleViral':'Int64', 'totalTestsPeopleViralIncrease':'Int64',
       'totalTestsViral':'Int64', 'totalTestsViralIncrease':'Int64'}
#reading the nevada-history.csv and loading into data variable
data = pd.read_csv("nevada-history.csv",dtype=data_type)
#specifing only 4 column names from data variable and calling CovidData class
covid_data = CovidData(data['state'].to_string(),data['death'].to_string(),data['deathConfirmed'].to_string(),data['deathIncrease'].to_string())
print(covid_data)
