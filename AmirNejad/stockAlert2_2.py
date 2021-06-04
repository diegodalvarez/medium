def alertFinder(data):

    data['MA100']: data['Close'].rolling(window=100).mean()
    data['Alert'] = np.nan

    Index = data[data.Close<data.MA100].index 
    data.loc[Index, 'Alert']  = 1
    
    return data

    

