import pandas as pd
import os
import shutil

# Load training labels
df = pd.read_excel("all_three_stations/labels/combined_only_train_labels.xlsx")

# Moisture classification function
def classify_moisture(v):
    if v < 0.23:
        return "dry"
    elif v < 0.33:
        return "normal"
    else:
        return "wet"

df["label"] = df["vwc"].apply(classify_moisture)

image_folder = "all_three_stations/images"
output_folder = "dataset"

count = 0

for index, row in df.iterrows():
    img_name = row["image"]
    label = row["label"]

    src_path = os.path.join(image_folder, img_name)
    dest_path = os.path.join(output_folder, label, img_name)

    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        count += 1

print("Total images copied:", count)
