from function import *

df = pd.read_csv('basic_info.csv')
model_example = model(df)
model_example.k_fold_cv(15)
model_example.show_ks()
