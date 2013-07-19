# -*- coding: cp1253 -*-
#-------------------------------------------------------------------------------
# Name:         json_parser_singlefile
# Purpose:      parsing data from a json file to a form:
#               author1 mentioned1 "timestamp"\n
#               author1 mentioned2,... "timestamp"\n
#               creating a single file without the text content to render the
#               matlab functions more efficient.
# Author:       konkonst
#
# Created:      31/05/2013
# Copyright:    (c) ITI (CERTH) 2013
# Licence:      <apache licence 2.0>
#-------------------------------------------------------------------------------
import json
import codecs
import os,glob
import wx

# User selects dataset folder
app = wx.PySimpleApp()
datasetPath = 'F:/konkonst/retriever_backup/Journalist jsons'
dialog = wx.DirDialog(None, "Please select your dataset folder:",defaultPath=datasetPath)
if dialog.ShowModal() == wx.ID_OK:
    dataset_path= dialog.GetPath()
dialog.Destroy()
#User selects target folder
targetPath = 'F:/konkonst/retriever_backup/Journalist jsons'
dialog = wx.DirDialog(None, "Please select your target folder:",defaultPath=targetPath)
if dialog.ShowModal() == wx.ID_OK:
    target_path= dialog.GetPath()
dialog.Destroy()
#Parsing commences
my_txt=open(target_path+"/authors_mentions_time.txt","w")
for filename in glob.glob(dataset_path+"/*.json"):
    print(filename)
    my_file=open(filename,"r")
    read_line=my_file.readline()
    while read_line:
        json_line=json.loads(read_line)##,encoding="cp1252")#.decode('utf-8','replace')
        if "delete" in json_line or "scrub_geo" in json_line or "limit" in json_line:
            read_line=my_file.readline()
            continue
        else:     
            if json_line["entities"]["user_mentions"]:
                len_ment=len(json_line["entities"]["user_mentions"])
                for i in range(len_ment):##mentions.append(json_line["entities"]["user_mentions"][i]["screen_name"]) ##my_text=str(json_line["text"].encode('ascii','replace').replace('\n', ''))
                    my_txt.write(json_line["user"]["screen_name"]+"\t" + json_line["entities"]["user_mentions"][i]["screen_name"]+"\t"+"\""+json_line["created_at"]+"\""+"\n")            
        read_line=my_file.readline()
    else:
        my_file.close()
my_txt.close()
