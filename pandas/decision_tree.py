# Download dataset from Kaggle Manually
# https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
# Unpack to: D:\data\pima_indians or change location below

import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics  #Import scikit-learn metrics module for accuracy calculation

# Plotting architecture
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dataset = r"D:\data\pima_indians\diabetes.csv"
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv(dataset)

dict_rename = dict()
for origin, target in zip(pima.columns, ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']):
    dict_rename[origin] = target
pima = pima.rename(columns=dict_rename)
print(pima.head())

features = [col for col in pima.columns if col != 'label']
X = pima[features]
y = pima.label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names=features,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
Image(graph.create_png())

