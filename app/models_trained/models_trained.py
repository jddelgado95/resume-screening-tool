import pickle
from sklearn.naive_bayes import MultinomialNB

# Example dummy training
model = MultinomialNB()
X_train = [[1, 0, 0], [0, 1, 1]]
y_train = ["Data Engineer", "Backend Developer"]
model.fit(X_train, y_train)

# Save model
with open("app/models_trained/resume_classifier.pkl", "wb") as f:
    pickle.dump(model, f)