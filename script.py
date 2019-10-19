import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import argparse

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
    filename = name + ".jpg"
    plt.savefig(filename)
    os.replace(os.path.join('.', filename), os.path.join(path, filename))

#Parser for script    
parser = argparse.ArgumentParser(description="Script for CPUWallTime Graphs")
parser.add_argument("--csv_file", dest="csv_file", type=str, help="name of the csv_file")
parser.add_argument("--root_dir", dest="root_dir", type=str, help="path to the root diretory")
parser.add_argument("--w_l", dest="w_l", type=int, help="walltime low")
parser.add_argument("--w_h",dest="w_h", type=int, help="walltime high")
parser.add_argument("--num_cpu_l", dest="num_cpu_l", type=int, help="lowest number of used cpus")
parser.add_argument("--num_cpu_h", dest="num_cpu_h", type=int, help="highest number of used cpus")
parser.add_argument("--num_nodes_l", dest="num_nodes_l", type=int, help="lowest number of used nodes")
parser.add_argument("--num_nodes_h", dest="num_nodes_h", type=int, help="highest number of used nodes")
parser.add_argument("--queue_name", dest="queue_name", nargs="+", help="queue type")
parser.add_argument("--dest_path", dest="dest_path", type=str, help="destination path for graphs")


args = parser.parse_args()

data = read_csv(args.root_dir, args.csv_file)
data = filter_data(data, {"WallDurationSeconds": [args.w_l, args.w_h], "NumberCPU":[args.num_cpu_l, args.num_cpu_h], 
                                                           "Nodes":[args.num_nodes_l, args.num_nodes_h], "QueueName": args.queue_name})
save_plot(get_value_by_key(data, "WallDurationSeconds"), "./graph", "wall_duration_plot", "WallDurationSeconds", 1/60)
save_plot(get_value_by_key(data, "NumberCPU"), "./graph", "cpu_plot", "NumberCPU")
save_plot(get_value_by_key(data, "Nodes"), "./graph", "nodes_plot", "Nodes")

