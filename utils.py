import pandas as pd

def load_data():
    titanic = pd.read_csv('data/titanic.csv')
    men = titanic[titanic['Sex'] == 'male']
    return men
