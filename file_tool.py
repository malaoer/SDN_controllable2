# -*- coding:utf-8 -*-
import json
import csv

def read_network_conf():
    with open(".//configuration//network_conf.json","r") as f:
        file_dict = json.load(f)
        print(file_dict)
        Con_IP = file_dict['Con_IP']
        Con_port = file_dict['Con_port']
        return Con_IP,Con_port

def read_policy_file():
    with open(".//data//policy.csv","r") as f:
        lines = csv.reader(f)
        for line in lines:
            print(line)

