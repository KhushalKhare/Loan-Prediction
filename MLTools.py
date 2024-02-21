def outliers(df):
    df= standardize(df)
    outliers=[]
    cat,con = catconsep(df)
    for i in con:
        outliers.extend(list(df[df[i]>3].index))
        outliers.extend(list(df[df[i]<-3].index))
    from numpy import unique
    Q= list(unique(outliers))
    return Q
    

def catconsep(df):
    cat= []
    con= []
    for i in df.columns:
        if(df[i].dtypes == "object"):
            cat.append(i)
        else:
            con.append(i)
    return cat,con


def standardize(df):
    import pandas as pd
    cat,con= catconsep(df)
    from sklearn.preprocessing import StandardScaler
    ss= StandardScaler()
    X1= pd.DataFrame(ss.fit_transform(df[con]),columns=con)
    return X1
    
    
    
def replacer(df):
    cat,con = catconsep(df)
    for i in con:
        x = df[i].mean()
        df[i]=df[i].fillna(x)
        
    for i in cat:
        x = df[i].mode()[0]
        df[i]=df[i].fillna(x)
        
        
def preprocessing(df):
    cat,con= catconsep(df)
    from sklearn.preprocessing import StandardScaler
    ss= StandardScaler()
    import pandas as pd
    X1= pd.DataFrame(ss.fit_transform(df[con]),columns=con)
    X2= pd.get_dummies(df[cat])
    Xnew= X1.join(X2)
    return Xnew
    
    
def ANNOVA(df,cat,con):
    from statsmodels.formula.api import ols
    eqn = str(con) + " ~ " + str(cat)
    model = ols(eqn,df).fit()
    from statsmodels.stats.annova import annova_lm
    Q = annova_lm(model)
    return round(Q.iloc[0:1,4:5].values[0][0],5)
    
    
def chisq(df,cat1,cat2):
    import pandas as pd
    from scipy.stats import chi2_contingency
    ct= pd.crosstab(df[cat1],df[cat2])
    a,b,c,d = chi2_contingency(ct)
    return round(b,5)