from kedro.pipeline import Pipeline, node
from .nodes import CompanyPreprocessor, ShuttlesPreprocessor, create_master_table


def create_pipeline(**kwargs):
    preprocess_companies = CompanyPreprocessor()
    preprocess_shuttles = ShuttlesPreprocessor()

    return Pipeline(
        [
            node(
                func=preprocess_companies,
                inputs='companies',
                outputs='preprocessed_companies',
                name='preprocess_companies_node',
            ),
            node(
                func=preprocess_shuttles,
                inputs='shuttles',
                outputs='preprocessed_shuttles',
                name='preprocess_shuttles_node'
            ),
            node(
                func=create_master_table,
                inputs=['preprocessed_shuttles', 'preprocessed_companies', 'reviews'],
                outputs='master_table',
                name='create_master_table_node'
            )
        ]
    )
