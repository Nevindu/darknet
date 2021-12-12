import pandas as pd
import numpy as np

df = pd.read_csv('test_data_detection_stats.csv')
mtrx = df.to_numpy()

orig_detections = mtrx[:,0]
thresh_vals = np.arange(0.2,1,0.05)
rmse_vals = []
col_names = []
N = mtrx.shape[0]
for i in range(1, mtrx.shape[1]):
  thresh = np.around(thresh_vals[i-1], 2)
  error = (orig_detections - mtrx[:,i]) ** 2
  error = error.sum(axis=0)
  rmse = error/N
  rmse = np.sqrt(rmse)
  rmse_vals.append(rmse)
  col_names.append(f"RMSE @{thresh}")
rmse_df = pd.DataFrame(data = [rmse_vals], columns=col_names)
rmse_df.to_csv('RMSE_Values.csv', index=False)

print(rmse_df)