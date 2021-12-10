import pandas as pd
df = pd.read_csv(r'C:\Users\hp\PycharmProjects\criket_match project\match.csv')
df['start_date']=pd.to_datetime(df['start_date'])
df['year_of_match']=df['start_date'].dt.year
df['month_of_match'] = df['start_date'].dt.month

def countsmatch(df, name):
    if name == 'Overall':
        tm = df
    if name != 'Overall':
        tm = df[(df['name'] == name)]

    x = tm['name'].value_counts().reset_index()
    x.columns = ['match of country', 'count of match']
    return x

def yearlycountmatch(df):
    yearofmatch = df.groupby(['year_of_match'])['name'].count().reset_index()
    yearofmatch.columns = ['year', 'counts of match']
    return yearofmatch

def participate_all_match_each_country(df):
    c = df['name'].str.split('v', expand=True)
    c.columns = ['country1', 'country2', 'f']
    c.drop('f', axis=1, inplace=True)

    df = df.join(c)


    country1 = df['country1'].value_counts().reset_index()
    country1.columns = ['country1', 'particepate match']
    match1 = country1.drop('country1', axis=1)

    country2 = df['country2'].value_counts().reset_index()
    country2.columns = ['country2', 'particepate match']
    match2 = country2.drop('country2', axis=1)

    total_match = match1 + match2

    total_match['particepate match'] = total_match['particepate match'].fillna(0)
    total_match['particepate match'] = total_match['particepate match'].astype(int)
    countrys = country1.drop('particepate match', axis=1)
    participate_all_match_each_country = countrys.join(total_match)
    participate_all_match_each_country.columns = ['countrys', 'particepate match']
    participate_all_match_each_country['countrys'] = participate_all_match_each_country['countrys'].astype(str)

    return participate_all_match_each_country

def t20(df):
    c = df['name'].str.split('v', expand=True)
    c.columns = ['country1', 'country2', 'f']
    c.drop('f', axis=1, inplace=True)
    df = df.join(c)

    t20 = df[(df['matchtype'] == 't20')]
    c1 = t20['country1'].value_counts().reset_index()
    c1.columns = ['country', 't20match']
    c2 = t20['country2'].value_counts().reset_index()
    c2.columns = ['country', 't20match']

    m = c1.drop('country', axis=1)
    n = c1.drop('t20match', axis=1)
    m1 = c2.drop('country', axis=1)
    n1 = c1.drop('t20match', axis=1)

    totalt20 = m + m1
    totalt20.fillna(0, inplace=True)
    totalt20['t20match'] = totalt20.astype(int)
    totalcountry = n.merge(n1)
    totalt20matchscountrys = totalcountry.join(totalt20)
    return totalt20matchscountrys
def odi(df):
    c = df['name'].str.split('v', expand=True)
    c.columns = ['country1', 'country2', 'f']
    c.drop('f', axis=1, inplace=True)
    df = df.join(c)

    odi = df[(df['matchtype'] == 'odi')]
    c11 = odi['country1'].value_counts().reset_index()
    c11.columns = ['country', 'odimatch']
    c22 = odi['country2'].value_counts().reset_index()
    c22.columns = ['country', 'odimatch']

    v = c11.drop('country', axis=1)
    n11 = c11.drop('odimatch', axis=1)
    k = c22.drop('country', axis=1)
    n22 = c22.drop('odimatch', axis=1)

    todi = v + k
    todi.fillna(0, inplace=True)
    todi['odimatch'] = todi.astype(int)
    totalodimatchscountrys = n11.join(todi)

    return totalodimatchscountrys
def test(df):
    c = df['name'].str.split('v', expand=True)
    c.columns = ['country1', 'country2', 'f']
    c.drop('f', axis=1, inplace=True)
    df = df.join(c)

    test = df[(df['matchtype'] == 'test')]
    c111 = test['country1'].value_counts().reset_index()
    c111.columns = ['country', 'testmatch']
    c222 = test['country2'].value_counts().reset_index()
    c222.columns = ['country', 'testmatch']

    p = c111.drop('country', axis=1)
    n111 = c111.drop('testmatch', axis=1)
    w = c222.drop('country', axis=1)
    n222 = c222.drop('testmatch', axis=1)

    test = p + w
    test.fillna(0, inplace=True)
    test['testmatch'] = test.astype(int)
    totalcountry = n111.merge(n222)
    totaltestmatchscountrys = n111.join(test)

    return totaltestmatchscountrys

