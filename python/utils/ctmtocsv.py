import os
from pathlib import Path
import pandas as pd
import numpy as np

def add_dict_value(dic, filename, word):
	if dic.get(filename, None) is not None:
		dic[filename] = dic[filename] +" "+ word
	else:
		dic[filename] = word
	return dic

def label_dict(path):
	file = open(path, 'r')
	label_dic = {}
	for line in file:
		label_dic[line[:22]] = line.split("_")[4][:-2]
	return label_dic

def data_dict(path):
	file = open(data_path, 'r', encoding='latin1')

	dev_dir = "../../release1/trans-manu/dev/"
	train_dir = "../../release1/trans-manu/train/"

	dic_dev = {}
	dic_train = {}
	dic_test = {}

	for line in file:
		tokens = line.split()
		dev_file_path = Path(dev_dir+tokens[0]+".trs")
		train_file_path = Path(train_dir+tokens[0]+".trs")
		if dev_file_path.exists():
			dic_dev = add_dict_value(dic_dev,tokens[0],tokens[4])
		elif train_file_path.exists():
			dic_train = add_dict_value(dic_train,tokens[0],tokens[4])
		else:
			dic_test = add_dict_value(dic_test,tokens[0],tokens[4])

	return dic_dev, dic_train, dic_test

def dict_to_list(dic_data, dic_label =None):
	tab = []
	for k in dic_data:
		row = []
		row.append(k)
		row.append(dic_data[k])
		if dic_label is not None:
			row.append(dic_label[k])
		tab.append(row)
	return np.array(tab)


data_path = "../../release2/trans-auto/trans-asr-decoda.ctm"

if Path(data_path).exists():
	label_dev = label_dict("../../release1/labels/dev.2015.lst")
	label_train = label_dict("../../release1/labels/train.2015.lst")
	label_test = label_dict("../../release1/labels/test.2015.lst")
	
	dic_dev, dic_train, dic_test = data_dict(data_path)

	dev = pd.DataFrame(data=dict_to_list(dic_dev, label_dev))
	train = pd.DataFrame(data=dict_to_list(dic_train, label_train))
	test = pd.DataFrame(data=dict_to_list(dic_test, label_test))

	dev.to_csv("../../release2/dev.csv", sep="\t",header=False, index=False)
	train.to_csv("../../release2/train.csv", sep="\t",header=False, index=False)
	test.to_csv("../../release2/test.csv", sep="\t",header=False, index=False)