import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt

def filter_customer(n, df, prefix, filename):
    a = open(prefix + '_record.txt','a')
    '''
    a.write(filename)
    a.write(':\n')
    a.write('original shape: ')
    a.write(str(df.shape))
    a.write('\n')
    '''
    df = df[df.user_id < (n+1)]
    '''
    a.write('transform shape: ')
    a.write(str(df.shape))
    a.write('\nunique user number: ')
    a.write(str(len(np.unique(df.user_id))))
    a.write('\n')
    a.write(str(100 - 100 * np.round(len(np.unique(df.user_id))/float(n), 4)))
    a.write(' % users are missing')
    a.write('\n--------------------------------\n')
    a.close()
    '''
    return df

def read(fileprename, columnname, datatype, user_number):
    df = pd.read_csv(fileprename +datatype+ '.txt', header = None)
    df.columns = columnname
    df = filter_customer(user_number, df, datatype, fileprename)
    return df

def read_all_cc(datatype):
    overdue = pd.read_csv('overdue' +datatype+ '.txt', header = None)
    user_number = overdue.shape[0]
    
    if datatype == '_train':
        overduecolumns = ['user_id','label']
    else:
        overduecolumns = ['user_id']
    overdue = read('overdue', overduecolumns, datatype, user_number)
    
    user_infocolumns = ['user_id','gender','occupation','education','marriage','residence']
    user_info = read('user_info', user_infocolumns, datatype, user_number)
    
    loan_timecolumns = ['user_id','loan_time']
    loan_time = read('loan_time', loan_timecolumns, datatype, user_number)
    
    browse_historycolumns = ['user_id','browse_time','activity','activity_label']
    browse_history = read('browse_history', browse_historycolumns, datatype, user_number)
    
    billcolumns = ['user_id','bill_time','bank_id','prior_period_bill_amt','prior_period_repay_amt','credit_lmt_amt','current_bill_bal','current_bill_min_repay_amt','cost_cnt','current_bill_amt','adj_amt','circle_interest','avlb_bal','pre_borrow_cash_amt','repay_stat']
    bill = read('bill_detail', billcolumns, datatype, user_number)
    
    bankcolumns = ['user_id','record_time','trade_type','trade_money','income']
    bank = read('bank_detail', bankcolumns, datatype, user_number)
    return overdue, user_info, loan_time, browse_history, bill, bank

def basic_statis_distribution(df):
    for col in df.columns[2:]:
        g = sns.kdeplot(df.loc[df.label == 0, col], shade=True)
        g = sns.kdeplot(df.loc[df.label == 1, col], shade=True)
        sns.plt.legend(['on time','overdue'])
        sns.plt.show()

def basic_statis_boxplot(df):
    for col in df.columns[2:]:
        g = sns.boxplot(x="label", y=col,  data=df, palette="PRGn")
        sns.plt.show()

def pearsonr_col(df):
    for col in df.columns[2:]:
        print col + ': ',
        print pearsonr(df.label, df[col])

if __name__ == "__main__":
    overdue, user_info, loan_time, browse_history, bill, bank = read_all_cc('_train')
    new = pd.merge(overdue, user_info, on = 'user_id', how = 'left', left_index = None)
    new = pd.merge(new, loan_time, on = 'user_id', how = 'left', left_index = None)
    new.to_csv('basic_info.csv', index = None)
    #basic_statis_boxplot(new)
    billnew = bill.drop_duplicates(subset = 'user_id', keep = 'last')
    test = pd.merge(new, billnew, on = 'user_id', how = 'left')
    test = test[~pd.isnull(test.bill_time)]
    basic_statis_distribution(test)
    basic_statis_boxplot(test)
    billnew = bill.drop_duplicates(subset = 'user_id', keep = 'first')
    test = pd.merge(new, billnew, on = 'user_id', how = 'left')
    test = test[~pd.isnull(test.bill_time)]
    basic_statis_distribution(test)
    print test.describe()
    print browse_history.describe()
    
    ac = browse_history[['activity','activity_label']].drop_duplicates(subset = ['activity','activity_label'])
    print 'activity category {0}'.format(ac.shape[0])
    
    activity_counts_per_times = browse_history.groupby(['user_id','browse_time']).count()
    activity_counts_per_times = activity_counts_per_times.reset_index()
    activity_times = browse_history.drop_duplicates(subset=['user_id','browse_time']).groupby('user_id')['browse_time'].count()
    activity_times=activity_times.reset_index()
    
    ac = browse_history[['activity','activity_label']].groupby('activity_label').count().reset_index().sort('activity')
    print ac
    
    ac = browse_history[['activity','activity_label']].groupby('activity').count().reset_index().sort('activity_label')
    print ac