import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score as ac


def process(epochs):
    dta = 'D:\local-code\Main.xlsx'
    data = pd.DataFrame(pd.read_excel(dta))
    maping = {'Nandhan' : 1, 'Person1': 0, 'Person_JIN':2}

    data['target'] = data['User'].map(maping)

    X = data.drop(['User', 'target'], axis=1)
    Y = data['target']
    global X_test

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1423)

    global model
    model = LogisticRegression(n_jobs=epochs)

    model.fit(X_train, y_train)

def resultant(intake):
    prdt = model.predict(intake)
    return prdt
    



