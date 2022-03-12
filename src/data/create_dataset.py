
import numpy as np
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

array_beer_style_names = np.load('../data/processed/beer_style_names.npy', allow_pickle=True)
array_brewery_names = np.load('../data/processed/brewery_names.npy', allow_pickle=True)

def normalize_features(df):
    num_cols = ['review_aroma', 'review_appearance', 'review_palate', 'review_taste', 'beer_abv']
    cat_cols = ['brewery_name']

    sc = StandardScaler()
    X_features = df.copy()
    X_features[num_cols] = sc.fit_transform(X_features[num_cols])

    col_encoder = OrdinalEncoder(categories=[array_brewery_names])
    X_features[cat_cols] = col_encoder.fit_transform(X_features[cat_cols])
    
    return X_features


def target_number_to_string(target_num):
    return array_brewery_names[target_num]