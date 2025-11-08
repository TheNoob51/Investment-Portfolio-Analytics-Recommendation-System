# train_model.py
from models.data_utils import load_and_prepare
from models.model_utils import train_model

df = load_and_prepare("portfolio_sample_1.csv")
train_model(df)
