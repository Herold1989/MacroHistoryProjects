
# Some basic functions used for the MacroHistory Data Analysis.
# Function code has been written by Dominik R. Wehr.
# For any questions refer to: dominikr.wehr(at)gmail.com

def windsorize(data,col_name,lb=1,ub=99):
    df_out = data[col_name].copy()
    bounds = [np.percentile(df_out.dropna(),i) for i in [lb,ub]]
    df_out[(df_out < bounds[0]) | (df_out > bounds[1])] = np.nan
    return df_out
