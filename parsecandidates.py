import xlrd
import json

def parseCandidates():
    workbook = xlrd.open_workbook('CRP_IDs.xls')
    sheet = workbook.sheet_by_index(0)
    num_rows = sheet.nrows
    candidates = {}
    for row in range(1, num_rows):
        CID = sheet.cell_value(row, 1)
        CRPName = sheet.cell_value(row, 2)
        if ',' in CRPName:
            CRPName = CRPName.split(',')
            CRPName = CRPName[1].strip() + ' ' + CRPName[0].strip()
        Party = sheet.cell_value(row, 3)
        DistIDRunFor = sheet.cell_value(row, 4)
        FECCandID = sheet.cell_value(row, 5)
        candidates[CRPName] = [CID, Party, DistIDRunFor, FECCandID]
    return candidates

candidateTotal = parseCandidates()
with open('candidates.json', 'w') as outfile:
    json.dump(candidateTotal, outfile)
