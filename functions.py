import math as m
def gen_lags(df, var_name, n_lag):
    # returns a copy of the original df with the additional column
    df_out = df.copy(deep = True)
    newvar_name = var_name + "_" + str(n_lag)
    n_obs = len(df_out)
    newvar_values = list(df_out[var_name][:(n_obs-n_lag)])
    for p in range(n_lag):
        newvar_values.insert(0, m.nan)
    df_out[newvar_name] = newvar_values
    return df_out 