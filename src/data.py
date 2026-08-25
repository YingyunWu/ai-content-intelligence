import pandas as pd


def create_article_dataset():
    return pd.DataFrame(
        columns=[
            "source",
            "date",
            "article"
        ]
    )