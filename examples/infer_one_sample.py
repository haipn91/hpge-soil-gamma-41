import numpy as np
import pandas as pd
from pathlib import Path
import joblib

# ---- Paths (chỉnh nếu bạn đặt khác) ----
NPZ_PATH      = Path("data/hpge-soil-gamma-41.npz")
LABELS_PATH   = Path("data/Activity.csv")                # để lấy tên đồng vị (không bắt buộc)
SCALER_PATH   = Path("scaler/input_scaler.sav")          # scaler đã fit ở lúc train
MODEL_PATHS   = [
    Path("models/ridge_multioutput_model.sav"),          
    Path("models/xgboost_multioutput_model.sav"),        
]

# ---- Load data ----
data = np.load(NPZ_PATH)
X_test, y_test = data["x_test"], data["y_test"]

# isotope names (optional, for nicer printing)
try:
    isotope_names = pd.read_csv(LABELS_PATH).columns.tolist()
except Exception:
    isotope_names = [f"Iso_{i:02d}" for i in range(y_test.shape[1])]

# ---- Load scaler ----
if not SCALER_PATH.exists():
    raise FileNotFoundError(f"Scaler not found at {SCALER_PATH}. Re-check your training script/output.")
scaler = joblib.load(SCALER_PATH)

# ---- Load model (try both names) ----
model = None
for p in MODEL_PATHS:
    if p.exists():
        model = joblib.load(p)
        MODEL_USED = p
        break
if model is None:
    raise FileNotFoundError(f"Model not found. Tried: {', '.join(str(p) for p in MODEL_PATHS)}")

# ---- Scale test set with the SAME scaler used in training ----
X_test_scaled = scaler.transform(X_test)

# ---- Pick a random test sample and predict ----
rng = np.random.default_rng(42)
idx = int(rng.integers(0, X_test.shape[0]))
x1 = X_test_scaled[idx:idx+1]
y_true = y_test[idx]

y_pred = model.predict(x1)[0]  # shape: (41,)

# ---- Show top-10 predicted isotopes by activity ----
top_k = 10
order = np.argsort(-y_pred)[:top_k]

print(f"[Model] {MODEL_USED}")
print(f"[Sample index] {idx}")
print("\nTop-10 predicted isotopes:")
for r, j in enumerate(order, 1):
    print(f"{r:2d}. {isotope_names[j]:12s}  pred={y_pred[j]:9.3f}   true={y_true[j]:9.3f}")

# If you need the full 41 predicted activities as a dict:
pred_dict = {isotope_names[j]: float(y_pred[j]) for j in range(len(isotope_names))}
# print(pred_dict)
