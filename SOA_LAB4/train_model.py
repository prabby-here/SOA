import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import mlflow
import mlflow.sklearn

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save locally
joblib.dump(model, "iris_model.pkl")

# MLflow tracking
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("accuracy", model.score(X_test, y_test))
