#!/usr/bin/env python

import os
import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import levene

class TitanicClass:
    
    def __init__(self):
        self.dataset = "./train.csv"
        self.path_output = "./Output/titanic_clean.csv"
        self.numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        
    def readCsv(self):
        df = pd.read_csv(self.dataset, skipinitialspace=True)
        df.head()
        return df

    def selectAttributes(self, df):
        df.drop('PassengerId', axis=1, inplace=True)

    def replaceNulls(self, df): 
        df["Age"].fillna(df["Age"].mean(), inplace=True)
        df["Cabin"].fillna(" ", inplace=True)
        df["Embarked"].fillna(" ", inplace=True)

    def fixoutliers(self, x):
        xColumnNames=x.columns
        for j in xColumnNames:
            try:
                xy=x[j]    
                updated=[]
                Q1,Q3=np.percentile(xy,[25,75])
                IQR=Q3-Q1
                minimum=Q1-1.5*IQR
                maximum=Q3+1.5*IQR
                for i in xy:
                    if(i>maximum):
                        i=maximum
                        updated.append(i)
                    elif(i<minimum):
                        i=minimum
                        updated.append(i)
                    else:
                        updated.append(i)
                x[j]=updated
            except:
                continue
        return x
    
    def exportDataset(self, df):
        df.to_csv(self.path_output)

    def creationGroups(self, df):
        # Agrupación por tipo de Survived
        survived = df.loc[df['Survived'] == 1]
        nosurvived = df.loc[df['Survived'] == 0]

        # Agrupación por sexo
        male = df.loc[df['Sex'] == "male"]
        female = df.loc[df['Sex'] == "female"]

        # Agrupación por edad
        child = df.loc[df['Age'] < 18.0]
        adult = df.loc[(df['Age'] >= 18.0) & (df['Age'] <= 65.0)]
        old = df.loc[df['Age'] < 65.0]

        return (survived, nosurvived, male, female, child, adult, old)

    def normality(self, df):        
        newdf = df.select_dtypes(include=self.numerics)
        statistic, pvalue = shapiro(newdf)
        print("Shapiro Statistic " + str(statistic) + " and p-value " + str(pvalue))
        if pvalue > 0.05:
            print("Normal distribution")
            return True
        else:
            print("Not normal distribution")
            return False

    def homogeneity(self, m, f):
        maledf = m.select_dtypes(include=self.numerics)
        femaledf = f.select_dtypes(include=self.numerics)
        statistic, pvalue = levene(maledf["Survived"], femaledf["Survived"])
        print("Levene Statistic " + str(statistic) + " and p-value " + str(pvalue))
        if pvalue > 0.05:
            print("Homogeneidad")
        else:
            print("No homogeneidad")
