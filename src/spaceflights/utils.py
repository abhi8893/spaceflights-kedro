from IPython.display import display as display_nb
import pandas as pd

def show_unique_vals(df):
    '''Show nice formatted unique values in each column'''
    
    uniq_df = (df.apply(lambda col: col.unique())
               .reset_index()
               .rename(columns={'index': 'col', 0:'uniq_vals'})
              )
        
    uniq_df['num_uniq'] = uniq_df['uniq_vals'].apply(len)
    
    with pd.option_context('display.max_colwidth', None):
        display_nb(uniq_df)