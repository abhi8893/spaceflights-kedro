import pandas as pd

class CompanyPreprocessor:
    
    def __init__(self, copy=True):
        self.copy = copy
    
    @staticmethod
    def _parse_percentage(x: pd.Series)-> pd.Series:
        return x.str.replace('%', '').astype(float)/100
    
    @staticmethod
    def _is_true(x: pd.Series)-> pd.Series:
        return pd.Series(x.map({'t': True, 'f': False}), dtype='boolean')
    
    @staticmethod
    def _deduplicate(df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates().reset_index(drop=True)
    
    def __call__(self, companies: pd.DataFrame)-> pd.DataFrame:
        if self.copy:
            companies = companies.copy()
            
        companies = self._deduplicate(companies)
        companies['company_rating'] = self._parse_percentage(companies['company_rating'])
        companies['iata_approved'] = self._is_true(companies['iata_approved'])
        
        return companies
        

class ShuttlesPreprocessor:
    
    def __init__(self, copy=True):
        self.copy = copy
    
    @staticmethod
    def _is_true(x: pd.Series)-> pd.Series:
        return pd.Series(x.map({'t': True, 'f': False}), dtype='boolean')
    
    @staticmethod
    def _parse_money(x: pd.Series)-> pd.Series:
        return x.str.replace(r'[^0-9]', '', regex=True)
    
    @staticmethod
    def _deduplicate(df: pd.DataFrame)-> pd.DataFrame:
        return df.drop_duplicates().reset_index(drop=True)
        
    
    def __call__(self, shuttles: pd.DataFrame)-> pd.DataFrame:
        if self.copy:
            shuttles = shuttles.copy()
        
        shuttles = self._deduplicate(shuttles)
        shuttles['price'] = self._parse_money(shuttles['price'])
        shuttles['d_check_complete'] = self._is_true(shuttles['d_check_complete'])
        shuttles['moon_clearance_complete'] = self._is_true(shuttles['moon_clearance_complete'])
        
        return shuttles

def create_master_table(
    shuttles: pd.DataFrame,
    companies: pd.DataFrame,
    reviews: pd.DataFrame)-> pd.DataFrame:
    '''Combines all data to create a master table'''
    
    rated_shuttles = shuttles.merge(reviews, left_on='id', right_on='shuttle_id')
    master_table = rated_shuttles.merge(companies, left_on='company_id', right_on='id').dropna()

    return master_table