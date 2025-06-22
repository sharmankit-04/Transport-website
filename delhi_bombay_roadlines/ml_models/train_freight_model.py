import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load CSV
df = pd.read_csv("freight_data.csv")

X = df[['weight', 'distance', 'vehicle_type']]
y = df['price']

# Preprocessing
preprocessor = ColumnTransformer([
    ('vehicle', OneHotEncoder(), ['vehicle_type'])
], remainder='passthrough')

# Pipeline
model = Pipeline([
    ('preprocessing', preprocessor),
    ('regression', LinearRegression())
])

# Train
model.fit(X, y)

# Save
joblib.dump(model, 'freight_price_model.pkl')
print("Model trained & saved!")
