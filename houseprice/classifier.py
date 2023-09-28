import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV,train_test_split
from  sklearn.ensemble import RandomForestRegressor
import joblib


df = pd.read_csv("Housing.csv")

df['mainroadT'] = df['mainroad'].str.split(',')

categorical_features = ['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']

# craete a dict containing labelencoders for all the columns that contains values that need to be encoded
encoders = dict()
for cat in categorical_features:
    encoders[cat] = LabelEncoder()
    df[f'{cat}_n'] = encoders[cat].fit_transform(df[cat])

def labels(d):
    MR = encoders['mainroad']
    GR = encoders['guestroom']
    BS = encoders['basement']
    HW = encoders['hotwaterheating']
    AC = encoders['airconditioning']
    PRE = encoders['prefarea']
    FUR =encoders['furnishingstatus']

    d['mainroad_n']=MR.transform(d['mainroad'])
    d['guestroom_n']=GR.transform(d['guestroom'])
    d['basement_n']=BS.transform(d['basement'])
    d['hotwaterheating_n']=HW.transform(d['hotwaterheating'])
    d['airconditioning_n']=AC.transform(d['airconditioning'])
    d['prefarea_n']=PRE.transform(d['prefarea'])
    d['furnishingstatus_n']=FUR.transform(d['furnishingstatus'])

    
    Df = d[['mainroad_n','guestroom_n','basement_n','hotwaterheating_n','airconditioning_n','prefarea_n','furnishingstatus_n','area','bedrooms','bathrooms','parking']]

    return Df


x = df[['mainroad_n','guestroom_n','basement_n','hotwaterheating_n','airconditioning_n','prefarea_n','furnishingstatus_n','area','bedrooms','bathrooms','parking']]
y = df['price']

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2,shuffle=True)

clf = RandomForestRegressor(n_estimators=250,max_depth=6,max_leaf_nodes=9,max_features='log2')

clf.fit(x_train,y_train)

joblib.dump(clf, 'models.sav')


#param_grid = {
    #'n_estimators': [150,200,250],
    #'max_features': ['sqrt', 'log2', None],
    #'max_depth': [3, 6, 9],
    #'max_leaf_nodes': [3, 6, 9],
#}

#print('Starting gridsearch')
#grid_search = GridSearchCV(RandomForestRegressor(),
                           #param_grid=param_grid)
#grid_search.fit(x_train, y_train)

#print(grid_search.best_estimator_)
