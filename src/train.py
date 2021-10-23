import mlflow
from sklearn import linear_model

from src import data, modelling


def train():
    """Retrieve the data and train the model"""
    df = data.penguins()
    X, y = data.return_X_y(df)

    model = linear_model.LogisticRegression()
    pipeline = modelling.create_pipeline(model)
    pipeline.fit(X, y)

    mlflow.sklearn.save_model(model, "model")
    return pipeline
