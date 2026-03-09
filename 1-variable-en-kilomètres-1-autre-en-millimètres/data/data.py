import numpy as np
import pandas as pd

np.random.seed(42)
n = 1200

revenu = np.random.normal(4000000, 1500000, n)
credit = np.random.normal(2000000, 800000, n)
age = np.random.randint(18, 65, n)

# variable informative mais petite échelle
score = np.random.randint(1, 6, n)

# la cible dépend surtout du score
default = (score > 3).astype(int)

df = pd.DataFrame({
    "revenu_fcfa": revenu,
    "credit_fcfa": credit,
    "age": age,
    "score": score,
    "default": default
})

df.head()

df.to_csv("synthetic_credit_data.csv", index=False)