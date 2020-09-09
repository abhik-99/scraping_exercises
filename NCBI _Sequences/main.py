#first execute - 
# sudo apt-get install chromium-chromedriver
# pip install --upgrade firebase-admin
# pip install selenium

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('config/credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

chrome_options = Options()
chrome_options.add_argument("--headless")

# .options = chrome_options
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options = chrome_options)
# 'dogURL.txt', 'mouseURL.txt', 'ratURL.txt'

for filename in ['chickURL.txt', ]:
    
#Reading the list of URLS containing mRNA names.

    with open(filename, 'r') as f:
        contents = [x.strip('"') for x in f.read().strip().split('\n')][1:]
        print(filename, "Num URLS-", len(contents))
        contents = contents[870:]
        f.close()

    # print(contents)

    for idx, each in enumerate(contents):
        
        mrna_names = each.strip('"https://www.ncbi.nlm.nih.gov/nuccore/')
        mrna_names = mrna_names.strip('?report=fasta&log$=seqview&format=text"').split(',')
        
        # print(mrna_names)
        # print(len(mrna_names))
        # print(filename[:-4])
        print(each)
        while True:
            driver.get(each)
            time.sleep(10)
            seqs = [ x.text for x in driver.find_elements_by_xpath('//pre')]
            if len(seqs) == len(mrna_names):
                break
        
        
        if idx%50 == 0:
            if idx != 0:
                batch.commit()
                print("\nSequences Uploaded!\n")
            batch = db.batch()


        for x in seqs:
            name = x.split('.')[0].strip('>')
            sequence = "".join(x.split('\n')[1:]).strip()
            
            # print("Name", name)
            # print("Seq-", sequence)
            doc_ref = db.collection(filename[:-4]).document(name)
            batch.set(doc_ref, {'seq':sequence})

        print(filename,"Iterating-",idx+871,"Sequences Uploaded-",len(seqs),"\n")

        #commit and end if length is odd
        if idx == len(contents)-1:
            batch.commit()
            print("\nSequences Uploaded!\n")

driver.close()