#!/usr/bin/env python

import titanicclass

titanic = titanicclass.TitanicClass()
print("Comenzamos limpieza de datos...")
df = titanic.readCsv()
titanic.selectAttributes(df)
titanic.replaceNulls(df)
titanic.fixoutliers(df)
titanic.exportDataset(df)

print("Comenzamos análisis de datos...")
survived, nosurvived, male, female, child, adult, old = titanic.creationGroups(df)



