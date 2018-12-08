# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def read_csv(name_of_file, separator):
    return np.asmatrix(pd.read_csv(name_of_file, sep=separator, header=None, skiprows=1))

def read_csv_first_line (name_of_file):
    file_csv = open (name_of_file)
    title = file_csv.readline().replace('#', ' ').replace('\n','')
    file_csv.close()
    return title

if (len(sys.argv) < 10): #there are no guarantee the algorithm will work if the parameters were not correctly setted.
    print("Usage: name_output x_subtitle y_subtitle log_scale lim_x lim_y path_output amount_col list_of_cols list_of_csv_paths. Read more infos below:")
    print("Set local_label as 'upper right' 'upper left' 'lower right' 'lower left' 'best'")
    print("Set log_scale as 'xy' 'x' 'y' 'none' to inform the desired axes in log scale")
    print ("Set the desired limit to the x axis in lim_x param. For default config, pass -1.")
    print ("Set the desired limit to the y axis in lim_y param. For default config, pass -1.")
    print ("Set amount_col as the amount of desired columns (in each csv) to be plotted.")
    print ("Inform the indexes of the desired columns (a total of amount_col of them) according to the csv inputs.")
    print ("Inform the csv paths.")
    exit()

title_chart = sys.argv[1]

log_type = sys.argv[2]

local_label = sys.argv[3]

curr_param = 4
#Limit that can be given to the x axis
#-1 means it is not setted
max_axis_x = float(sys.argv[curr_param])
curr_param += 1

#Limit that can be given to the y axis
#-1 means it is not setted
max_axis_y = float(sys.argv[curr_param])
curr_param += 1

#Path of the outputfile
path_out = sys.argv[curr_param]
curr_param += 1

#Columns which will be considered as y axis from each .csv file
amount_columns = int(sys.argv[curr_param])
curr_param += 1

columns_considered = []
for i in range(curr_param, curr_param + amount_columns): 
    columns_considered.append(int(sys.argv[i]))
curr_param += amount_columns
############# Reading the 1st CSV file  ##############

#it should be given as parameter in case of multiple considered columns 
if amount_columns > 1:
    y_subtitle = sys.argv[curr_param].replace("#", " ")
    curr_param += 1

csv_path = sys.argv[curr_param]
curr_param += 1

data_csv = read_csv(csv_path, ' ')

#Title of the csv is part of the chart labeling
labels = []
labels.append(read_csv_first_line(csv_path))

#x axis from the csv files should be in the 1st column of them
x_values = data_csv[1:,0].astype(int)
x_subtitle = data_csv[0,0].replace("#", " ")

if amount_columns == 1:
    y_subtitle = data_csv[0,columns_considered[0]].replace("#", " ")

columns_label = [] 
for i in range (amount_columns):
    columns_label.append(data_csv[0,columns_considered[i]].replace("#", " "))

#The csv can have multiple columns, but we want the ones in columns_considered array (the labels can be ignored)
data_concatenated = data_csv[:, columns_considered[0]]
for j in range (1, amount_columns):
    data_concatenated = np.concatenate((data_concatenated,
                            data_csv[:,columns_considered[j]]), axis=1)
#######################################################

#Loop to concatenate the considered columns of each .csv file
for i in range(curr_param, len(sys.argv)):
    data_csv = read_csv(sys.argv[i], ' ')
    labels.append(read_csv_first_line(sys.argv[i])) #title of the chart
    for j in range (amount_columns): 
        data_concatenated = np.concatenate((data_concatenated,
                                data_csv[:,columns_considered[j]]), axis=1)
    curr_param += 1
print(data_concatenated)
y_values = data_concatenated[1:,:].astype(float)

#There exists a total of column_amount data from each algorithm
#Note that we need column_amount <= 4, which are all our dashes
dashes = ['-', ':', '-.', '--']
markers = ['o', 's', '^', 'p', 'h'] #in the moment, our algorithm only supports 5 different algorithms (if you need more, please, add more markers)
colors = ['blue', 'red', 'gray', 'green', 'brown']

pgf_with_custom_preamble = {
"font.family": "serif", # use serif/main font for text elements
"text.usetex": True,   # don't setup fonts from rc parameters
"text.latex.preview": True,
"figure.figsize": (10,5),
"pgf.preamble": [
     "\\usepackage{units}",         # load additional packages
     "\\usepackage{metalogo}",
     "\\usepackage{unicode-math}",  # unicode math setup
     r"\setmathfont{xits-math.otf}",
     r"\setmainfont{Arial}", # serif font via preamble
     ]
}
plt.rcParams.update(pgf_with_custom_preamble)

ax = plt.subplot(1, 1, 1)
idx_dm = 0
idx_color = 0
#labels are something like: 'alg1 alg1 alg1 alg2 alg2 alg2 ... algN algN algN'
for i in range(0, len(labels) * amount_columns):
    if i > 0 and i % amount_columns == 0: 
        idx_dm = 0
        idx_color += 1

    _label = labels[idx_color].replace("#"," ") + " (" + columns_label[idx_dm] + ")"
    print (_label)
    ax.plot(x_values, y_values[:,i], dashes[idx_dm], fillstyle='full', color=colors[idx_color], markersize=6, marker=markers[idx_dm], label=_label)
    idx_dm += 1

matplotlib.rcParams.update({'font.size': 12})
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
if (max_axis_x != -1): 
    ax.set_xlim([0,max_axis_x])

if (max_axis_y != -1): 
    ax.set_ylim([0,max_axis_y])

if (log_type == 'x' or log_type == 'xy'):
    ax.set_xscale('log')
if (log_type == 'y' or log_type == 'xy'):
    ax.set_yscale('log')

ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
#ax.set_xlabel(r'$\lambda$')
#ax.set_ylabel(x_subtitle)
ax.legend(loc=local_label, ncol=1)
xticks = [i for i in range(0,105,10)]
plt.xticks(xticks, xticks)
#plt.xlabel(r'$\lambda$', fontsize=18)
print (x_subtitle, y_subtitle)
plt.xlabel(x_subtitle, fontsize=18)
plt.ylabel(y_subtitle, fontsize=18)
# plt.gray()
print (path_out + title_chart)
plt.savefig((path_out + title_chart + '.eps').replace(" ", "-"), bbox_inches='tight', pad_inches = 0)
# plt.show()
