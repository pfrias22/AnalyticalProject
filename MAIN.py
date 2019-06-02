from imports_func import *
import matplotlib.pyplot as plt
import titanicclass

titanic = titanicclass.TitanicClass()
print("Comenzamos limpieza de datos...")
df = titanic.readCsv()
df_charts = df
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
titanic.bar_chart(df_charts, "Pclass")
titanic.bar_chart(df_charts, "Sex")
titanic.bar_chart(df_charts, "Age")
titanic.bar_chart(df_charts, "SibSp")
titanic.bar_chart(df_charts, "Parch")
titanic.bar_chart(df_charts, "Title")
titanic.bar_chart(df_charts, "Embarked")
titanic.selectAttributes(df)
titanic.replaceNulls(df)
titanic.fixoutliers(df)
titanic.exportDataset(df)

print("Comenzamos análisis de datos...")
survived, nosurvived, male, female, child, adult, old = titanic.creationGroups(df)
titanic.normality(df)
titanic.homogeneity(male, female)

print("Aplicamos pruebas estadísticas...")
print(pd.DataFrame(abs(df.corr()['Survived']).sort_values(ascending = False)))

mapping = {'male': 1, 'female': 2}
df = df.replace({'Sex': mapping})  
male = df[df['Sex'] == 1]
female = df[df['Sex'] == 2]
import random
male_sample = random.sample(list(male['Survived']),100)
female_sample = random.sample(list(female['Survived']),100)
pd.DataFrame(abs(df.corr()['Survived']).sort_values(ascending = False))
print (stats.ttest_ind(male_sample, female_sample))
print ("This is the p-value when we break it into standard form: " + format(stats.ttest_ind(male_sample, female_sample).pvalue, '.32f'))
print(scipy.stats.wilcoxon(x=male_sample, y=female_sample, zero_method='wilcox', correction=False))


print("preparamos variables...")
sc = StandardScaler()

df[['Age', 'Fare']] = sc.fit_transform(df[['Age', 'Fare']])

train = pd.get_dummies(df, columns=['Title','Pclass','Embarked','SibSp','Parch','Sex'], drop_first=False)
X = train[train.columns[7:43]]
y = train[train.columns[0]]
X["Age"] = df["Age"]
X["Fare"] = df["Fare"]

X.head()

print("Generamos conjuntos de train y test")
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

logreg = LogisticRegression(solver='liblinear')
logreg.fit(X_train,y_train)
y_pred_train = logreg.predict(X_train)
y_pred_test = logreg.predict(X_test)

print ("accuracy Score for train set is: {}".format(round(accuracy_score(y_pred_train, y_train),4)))
print ("accuracy Score for test set is: {}".format(round(accuracy_score(y_pred_test, y_test),4)))



