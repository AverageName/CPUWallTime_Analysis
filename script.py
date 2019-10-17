import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import argparse

def read_preprocess_csv(root_dir, csv_file, walltime_low, walltime_high):
    data = pd.read_csv(os.path.join(root_dir, csv_file), delimiter=';')
    data = data.loc[(data['WallDurationSeconds'] > walltime_low) & (data['WallDurationSeconds'] < walltime_high)]
    data = data['WallDurationSeconds'].tolist()
    return data

def save_plot(data, path, name):
    ax = sns.distplot(data, hist=False, kde=True)
    filename = name + ".jpg"
    plt.savefig(filename)
    os.replace(os.path.join('.', filename), os.path.join(path, filename))
    
parser = argparse.ArgumentParser(description="Script for CPUWallTime Graphs")
parser.add_argument("--csv_file", dest="csv_file", type=str, help="name of the csv_file")
parser.add_argument("--root_dir", dest="root_dir", type=str, help="path to the root diretory")
parser.add_argument("--w_l", dest="w_l", type=int, help="walltime low")
parser.add_argument("--w_h",dest="w_h", type=int, help="walltime high")
parser.add_argument("--dest_path", dest="dest_path", type=str, help="destination path for graphs")

args = parser.parse_args()

data = read_preprocess_csv(args.root_dir, args.csv_file, args.w_l, args.w_h)
print(data)
save_plot(data, args.dest_path, "plot")

