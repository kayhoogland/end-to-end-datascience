from sklearn import pipeline, preprocessing


def create_pipeline(model):
    return pipeline.make_pipeline(preprocessing.StandardScaler(), model)
