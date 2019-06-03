# #!/usr/bin/env python
from imports_func import *
import matplotlib.pyplot as plt

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
        df.drop(['PassengerId', 'Name', 'Cabin'], axis=1, inplace=True)

    def replaceNulls(self, df):
        #df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\\.', expand=False)
        #df["Age"].fillna(df.groupby("Title")["Age"].transform("median"), inplace=True)
        # RELLENAMOS CON CLASE MAYORITARIA
        df["Embarked"].fillna("S", inplace=True)

    def replaceNullsKNN(self, df):
        df_num = df.select_dtypes(include=[np.float])
        #fancy impute removes column names.
        train_cols = list(df_num)
        # Use 5 nearest rows which have a feature to fill in each row's
        # missing features
        df2 = pd.DataFrame(KNN(k=3).fit_transform(df_num))
        df2.columns = train_cols
        df["Age"] = df2["Age"]

    def fixoutliers(self, x):
        xColumnNames=x.columns
        for j in xColumnNames:
            try:
                xy=x[j]    
                updated=[]
                outliers = []
                Q1,Q3=np.percentile(xy,[25,75])
                IQR=Q3-Q1
                minimum=Q1-1.5*IQR
                maximum=Q3+1.5*IQR
                for i in xy:
                    outlier = False
                    if(i>maximum):
                        outlier = True
                        i=maximum
                    elif(i<minimum):
                        outlier = True
                        i=minimum
                    if(outlier):
                        outliers.append(i)
                    updated.append(i)
                x[j]=updated
                print("Outliers de la columna", j, ":", outliers)
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
        for key in newdf.keys():
            statistic, pvalue = shapiro(newdf[key])
            print("Shapiro Statistic for variable  "+ key + ": " + str(statistic) + " and p-value " + str(pvalue))
            if pvalue > 0.05:
                print("Normal distribution")
            else:
                print("Not normal distribution")

    def homogeneity(self, m, f):
        maledf = m.select_dtypes(include=self.numerics)
        femaledf = f.select_dtypes(include=self.numerics)
        statistic, pvalue = levene(maledf["Survived"], femaledf["Survived"])
        print("Levene Statistic " + str(statistic) + " and p-value " + str(pvalue))
        if pvalue > 0.05:
            print("Homogeneidad")
        else:
            print("No homogeneidad")

    def bar_chart(self, df_charts, feature):
        #%matplotlib inline
        bins = pd.IntervalIndex.from_tuples([(0, 5), (5, 15), (15, 30),  (30, 60),(60, 100)])
        df_charts["Age_disc"] = pd.cut(df_charts["Age"],bins)
        survived = df_charts[df_charts["Survived"]==1][feature].value_counts()
        dead = df_charts[df_charts["Survived"]==0][feature].value_counts()
        df_aux = pd.DataFrame([survived, dead])
        df_aux.index = ["Survived", "Dead"]
        df_aux.plot(kind="bar", stacked=True, figsize=(12,6))
        plt.title("supervivencia en función de característica " + feature)
        filename = feature + "_bar_chart.png"
        plt.savefig(filename)
