from sklearn import tree,neighbors,svm,naive_bayes
from sklearn.metrics import accuracy_score

#Training Dataset
#X contains values of heights, weights and shoe sizes
#Y contains their labels
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

#Decision Tree
clf_dtree = tree.DecisionTreeClassifier()
#KNN
clf_knn = neighbors.KNeighborsClassifier()
#Naive-Bayes
clf_nbayes = naive_bayes.GaussianNB()

#Training
clf_dtree = clf_dtree.fit(X,Y)
clf_knn = clf_knn.fit(X,Y)
clf_nbayes = clf_nbayes.fit(X,Y)

#Testing Data
X1 = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40]]
Y1 = ['male','female','female','female','male','male','male','female']

#Prediction of testing data
prediction1 = clf_dtree.predict(X1)
prediction2 = clf_knn.predict(X1)
prediction3 = clf_nbayes.predict(X1)

#Comparing them
acc1 = {'name' : 'KNN', 'accuracy':accuracy_score(Y1,prediction2)}
acc2 = {'name' : 'NaiveBayes', 'accuracy':accuracy_score(Y1,prediction3)}
acc3 = {'name' : 'DTree', 'accuracy':accuracy_score(Y1,prediction1)}

print (acc1['name'], "has accuracy of ", acc1['accuracy'])
print (acc2['name'], "has accuracy of ", acc1['accuracy'])
print (acc3['name'], "has accuracy of ", acc1['accuracy'])