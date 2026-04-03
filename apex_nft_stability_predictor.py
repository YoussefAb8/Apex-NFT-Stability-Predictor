import numpy as np
from sklearn.ensemble import RandomForestClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# بيانات تدريب بسيطة: [Listings, Vol_Change, Avg_Price, Holders, Bids]
X = np.array([[100, 10, 1.5, 500, 20], [500, -20, 0.5, 400, 5]], dtype=np.float32)
y = [0, 1]

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

# تعريف المدخلات (مهم جداً لظهور الـ Input لاحقاً)
initial_type = [('float_input', FloatTensorType([None, 5]))]
onx = convert_sklearn(model, initial_types=initial_type)

with open("nft_guard.onnx", "wb") as f:
    f.write(onx.SerializeToString())
print("✅ Created nft_guard.onnx")
