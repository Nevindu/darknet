import os
import pandas as pd
test_images = []
test_label_paths = []
num_cranberries = []
with open('data/test.txt') as f:
  lines = f.readlines()
  for jpg in lines:
    label_file = jpg.strip()[0: len(jpg) - 4] + "txt"
    test_images.append(os.path.basename(jpg).strip())
    test_label_paths.append(label_file)

for label in test_label_paths:
  with open(label) as lb:
    annotations = lb.readlines()
    num_cranberries.append(len(annotations))
df = pd.DataFrame(list(zip(test_images, num_cranberries)), columns = ["Test Image", "Num. Cranberries"])
df.to_csv("test_data_stats.csv", index=False)