"""

Codes by Farhan

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# Reading in data
ds = pd.read_csv("Social_Network_Ads.csv")
X = ds.iloc[:, 2:4].values
y = ds.iloc[:,4].values


# Splitting and scaling
X_train, X_test, y_train, y_test = train_test_split(X,y)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)


# Classifier
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(metric='minkowski', p = 2)

from sklearn.SVM import SVC
clf = SVC(kernel='rbf')

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy')

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators =  10, criterion = 'entropy')

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Plot
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(X_set[:,0].min() - 1, 
                               X_set[:,0].max() + 1, 
                               step = 0.01),
                     np.arange(X_set[:,1].min() - 1, 
                               X_set[:,1].max() + 1, 
                               step = 0.01))
boundary = clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape)
plt.contourf(X1, X2, boundary, alpha = 0.75, 
             cmap = ListedColormap(('#fc7a74', '#6ff785')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), 
                label = j, s = 8)
plt.title('Title')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()