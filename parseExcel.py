#-*- coding:utf-8 -*-

import xlrd
import json

workbook = xlrd.open_workbook('res/riddles.xlsx')

sheet = workbook.sheet_by_index(0)

riddleList = []
for index in range(1, sheet.nrows):
    riddle =  sheet.cell_value(index, 0)
    solution = sheet.cell_value(index, 1)
    if len(riddle) <= 3:
        break
    riddleItem = {}
    riddleItem["riddle"] = riddle.strip()
    riddleItem["solution"] = solution.strip()
    riddleList.append(riddleItem)
print json.dumps(riddleList)