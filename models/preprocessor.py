import pandas as pd
def remove_noise_column(dataset: pd.DataFrame, columns_names: list = ['location']) -> pd.DataFrame:
    """
    Remove specified columns from a pandas DataFrame.

    This function drops the columns provided in `columns_names` from the
    given DataFrame and returns the cleaned DataFrame. Useful for 
    removing irrelevant or noisy features from the dataset.

    Args:
        dataset (pd.DataFrame): The input DataFrame.
        columns_names (list, optional): List of column names to remove.
            Defaults to ['location'].

    Returns:
        pd.DataFrame: A DataFrame with the specified columns removed.

    Raises:
        KeyError: If any column in `columns_names` does not exist in `dataset`.
    """
    dataset = dataset.drop(columns=columns_names)
    return dataset

