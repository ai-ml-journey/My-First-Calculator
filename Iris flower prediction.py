

# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Machine Learning model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("================================")
print("   IRIS FLOWER PREDICTION")
print("================================")

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Take flower measurements from user
print("\nEnter Flower Measurements:")

sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

# Make prediction
sample = [[sepal_length, sepal_width,
           petal_length, petal_width]]

prediction = model.predict(sample)

flower_name = iris.target_names[prediction[0]]

print("\n================================")
print("       PREDICTION RESULT")
print("================================")

print("Predicted Flower:", flower_name)
print("================================")
