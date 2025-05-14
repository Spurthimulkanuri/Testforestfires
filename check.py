import pickle

model = pickle.load(open('models/ridge.pkl', 'rb'))
print(type(model))

