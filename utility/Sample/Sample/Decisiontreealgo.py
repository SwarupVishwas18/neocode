# Import the necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from graphviz import Source

# Load the dataset
iris = load_iris()
X = iris.data[:, 2:] # petal length and width
y = iris.target


tree_clf = DecisionTreeClassifier(criterion='entropy',
								max_depth=2)
tree_clf.fit(X, y)

# Plot the decision tree graph
export_graphviz(
	tree_clf,
	out_file="iris_tree.dot",
	feature_names=iris.feature_names[2:],
	class_names=iris.target_names,
	rounded=True,
	filled=True
)

with open("iris_tree.dot") as f:
	dot_graph = f.read()
	
Source(dot_graph)
