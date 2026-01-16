import pandas as pd

def check_labels(df, gold_df):
    """
    Compare annotator CSV with gold standard.
    Returns accuracy %, mistakes dataframe.
    """
    correct = (df['label'] == gold_df['label']).sum()
    total = len(gold_df)
    accuracy = correct / total * 100
    mistakes = df[df['label'] != gold_df['label']]
    return accuracy, mistakes

