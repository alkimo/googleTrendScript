from datetime import datetime
import gspread
import os
import emailData

def generateSimpleCSV(data, generateCsvOf, keyword, path):
    final_word = '+'.join(keyword) 
    title = generateCsvOf + '_' + final_word + '.csv'
    data.to_csv(path + '/' + title)
    updateCsvToSheet(path + '/' + title, title)

def generateComplexCSV(data, generateCsvOf, path):
    if generateCsvOf == 'rt':
        wordType = 'RELATED TOPICS'
    elif generateCsvOf == 'rq':
        wordType = 'RELATED QUERIES'

    for searchWord in data:
        try:
            if data[searchWord]['top'].empty == False:
                title =  'TopSearch-' + wordType + '-' + searchWord.split(" ")[0] + '.csv'
                data[searchWord]['top'].to_csv(path + '/' + title)
                # updateCsvToSheet(path + '/' + title, title)
        except:
            print("Top search of \'" + searchWord + "\' " + wordType + " ended with no results.")
            print("No local CSV or Google Sheet generated.")
            pass

        try:
            if data[searchWord]['rising'].empty == False:
                title = 'RisingSearch -' + wordType + '-' + searchWord.split(" ")[0] + '.csv'
                data[searchWord]['rising'].to_csv(path + '/' + title)
                # updateCsvToSheet(path + '/' + title, title)
        except:
            print("Top search of \'" + searchWord + "\' " + wordType + " ended with no results.")
            print("No local CSV or Google Sheet for it were generated.")
            pass

        
def updateCsvToSheet(path, title):
    address_json = os.getcwd() + '/service_account.json'
    gc = gspread.service_account(filename=address_json)
    sheet = gc.create(title)
    
    content = open(path, 'r').read() 
    
    sheet.share(value=emailData.email, perm_type='user', role='writer')
    gc.import_csv(sheet.id, content)