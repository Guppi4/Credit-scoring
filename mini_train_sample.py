import pandas as pd

# Read the original train file
train = pd.read_csv('shift_ml_2025_train.csv')

# Take only the first 300 rows
mini_train = train.head(300)

# Save to a new file
mini_train.to_csv('mini_train_sample.csv', index=False)

# Print shape for confirmation
print('mini_train_sample.csv created with shape:', mini_train.shape)