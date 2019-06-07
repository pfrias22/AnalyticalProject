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
titanic.replaceNullsKNN(df)
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

from sklearn.metrics import confusion_matrix
conf_train = confusion_matrix(y_pred_train, y_train)
conf_test = confusion_matrix(y_pred_test, y_test)
df_cm_train = pd.DataFrame(conf_train, index = [i for i in ["Survived", "Dead"]],
                  columns = [i for i in ["Survived", "Dead"]])

df_cm_test = pd.DataFrame(conf_test, index = [i for i in ["Survived", "Dead"]],
                  columns = [i for i in ["Survived", "Dead"]])
plt.figure(figsize = (10,7))
sn.heatmap(df_cm_train, annot=True)
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.title("Confusion matrix for train data")
plt.show()

plt.figure(figsize = (10,7))
sn.heatmap(df_cm_test, annot=True)
plt.title("Confusion matrix for test data")
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred_test))

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()



