import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import argparse
import yaml

def parse_yaml(yaml_path):
    stream = open(yaml_path, "r")
    data = yaml.safe_load(stream)
    return data

def read_csv(root_dir, csv_file):
    data = pd.read_csv(os.path.join(root_dir, csv_file), delimiter=';')
    return data

def filter_data(data, params):
    for key in params.keys():
        if type(params[key][0]) == int:
    	    data = data.loc[(data[key] >= params[key][0]) & (data[key] <= params[key][1])]
        elif type(params[key][0]) == str:
            data = data.loc[(data[key].isin(params[key]))]
            print(data)
    return data

def get_value_by_key(data, key):
    return np.array(data[key].to_list())

def save_plot(data, path, name, label, x_scale=1):
    plt.figure()
    ax = sns.distplot(data * x_scale, hist=False, kde=True, axlabel=label)
    ax.set_yticklabels([])
    filename = name + ".jpg"
    plt.savefig(filename)
    os.replace(os.path.join('.', filename), os.path.join(path, filename))

#  Parser for script.    
parser = argparse.ArgumentParser(description="Script for CPUWallTime Graphs")
parser.add_argument("--yaml_path", dest="yaml_path", type=str, help="path to yaml config file")

args = parser.parse_args()

params = parse_yaml(args.yaml_path)
data = read_csv(params["root_dir"], params["csv_file"])
data = filter_data(data, params["filters"])
save_plot(get_value_by_key(data, "WallDurationSeconds"), params["dest_path"], "wall_duration_plot", "WallDurationSeconds")
save_plot(get_value_by_key(data, "NumberCPU"), params["dest_path"], "cpu_plot", "NumberCPU")
save_plot(get_value_by_key(data, "Nodes"), params["dest_path"], "nodes_plot", "Nodes")

