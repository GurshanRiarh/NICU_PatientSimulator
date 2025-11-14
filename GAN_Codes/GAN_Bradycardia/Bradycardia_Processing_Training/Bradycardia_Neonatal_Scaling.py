import pandas as pd
import numpy as np

bpm_file = "/home/Gurshan.R/Documents/GitHub/SYSC4907_Capstone/GAN_Bradycardia/CSV_DATA/BPM_8hr_5min.csv"
df = pd.read_csv(bpm_file, header=None)

adult_normal_range = (60, 100)
adult_brady_range = (df.min().min(), 60)
neonatal_normal_range = (100, 160)
neonatal_brady_range = (60, 90)

def rescale_bpm(data, old_min, old_max, new_min, new_max):
    return ((data - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min

df_neonatal = df.copy()
df_neonatal[df >= 60] = rescale_bpm(df[df >= 60], *adult_normal_range, *neonatal_normal_range)

df_neonatal[df < 60] = rescale_bpm(df[df < 60], *adult_brady_range, *neonatal_brady_range)

brady_mask = df_neonatal < 85
df_neonatal[brady_mask] += np.random.uniform(-5, 5, size=df_neonatal[brady_mask].shape)

neonatal_bpm_file = "/home/Gurshan.R/Documents/GitHub/SYSC4907_Capstone/GAN_Bradycardia/Scaled_CSV_DATA/BPM_8hr_5min_Neonatal.csv"
df_neonatal.to_csv(neonatal_bpm_file, index=False)

print(f"Neonatal BPM data saved: {neonatal_bpm_file}")


import pandas as pd

neonatal_bpm_file = "/home/Gurshan.R/Documents/GitHub/SYSC4907_Capstone/GAN_Bradycardia/Scaled_CSV_DATA/BPM_8hr_5min_Neonatal.csv"
df_neonatal = pd.read_csv(neonatal_bpm_file, header=None)

if (df_neonatal.iloc[0] == range(96)).all():
    df_neonatal = df_neonatal.iloc[1:].reset_index(drop=True)

df_neonatal = df_neonatal.apply(pd.to_numeric, errors="coerce")

brady_threshold = 100
severe_brady_threshold = 80

bradycardia_instances = df_neonatal[df_neonatal < brady_threshold].stack().reset_index()
bradycardia_instances.columns = ["Row", "Column", "BPM"]

severe_brady_instances = bradycardia_instances[bradycardia_instances["BPM"] < severe_brady_threshold]

print("\nBradycardia Instances (BPM < 100):")
print(bradycardia_instances)

print("\nSevere Bradycardia Instances (BPM < 80):")
print(severe_brady_instances)
