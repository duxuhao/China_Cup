import pandas as pd
import numpy as np

def filter_customer(n, df, prefix, filename):
    a = open(prefix + '_record.txt','a')
    a.write(filename)
    a.write(':\n')
    a.write('original shape: ')
    a.write(str(df.shape))
    a.write('\n')
    if prefix == '_train':
        df = df[df.user_id < (n+1)]
    else:
        df = df[df.user_id < (n+1 + 55596)]
    a.write('transform shape: ')
    a.write(str(df.shape))
    a.write('\nunique user number: ')
    a.write(str(len(np.unique(df.user_id))))
    a.write('\n')
    a.write(str(100 - 100 * np.round(len(np.unique(df.user_id))/float(n), 4)))
    a.write(' % users are missing')
    a.write('\n--------------------------------\n')
    a.close()
    return df

def read(fileprename, columnname, datatype, user_number):
    df = pd.read_csv(fileprename +datatype+ '.txt', header = None)
    df.columns = columnname
    df = filter_customer(user_number, df, datatype, fileprename)
    return df

def read_all_cc(datatype):
    overdue = pd.read_csv('usersID' +datatype+ '.txt', header = None)
    user_number = overdue.shape[0]
    
    if datatype == '_train':
        overduecolumns = ['user_id','label']
    else:
        overduecolumns = ['user_id']
    overdue = read('usersID', overduecolumns, datatype, user_number)
    
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

if __name__ == "__main__":
    read_all_cc('_test')