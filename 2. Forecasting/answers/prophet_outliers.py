outliers = (forecast
            .set_index(schiphol.index)
            .assign(y_real=schiphol_train['y'],
                    outlier = lambda df: np.where(df['y_real'].between(df['yhat_lower'],df['yhat_upper']),
                                                 np.nan, #if condition above is met
                                                 df['y_real']) #otherwise
                   )
        )
display(outliers[['ds', 'y_real', 'yhat_lower', 'yhat_upper', 'outlier']].head())

fig, ax = plt.subplots(figsize=(18,8))
model.plot(forecast, ax=ax);
outliers['outlier'].plot(ax=ax, c='red')
plt.xlim(pd.Timestamp('1999-01-01'), pd.Timestamp('2017-01-01'));
