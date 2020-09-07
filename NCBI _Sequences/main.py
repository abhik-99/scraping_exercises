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
cred = credentials.Certificate('config/gcp-access-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()




chrome_options = Options()
chrome_options.add_argument("--headless")

#Reading the list of URLS containing mRNA names.

with open('sample_humanURL.txt', 'r') as f:
    contents = [x.strip('"') for x in f.read().strip().split('\n')][1:]
    print("Num URLS-", len(contents))
    f.close()

# # .options = chrome_options
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options = chrome_options)
for idx, each in enumerate(contents):

    while True:
        driver.get(each)
        time.sleep(10)
        seqs = [ x.text for x in driver.find_elements_by_xpath('//pre')]
        if len(seqs) == 18:
            break
    print('Broken')

    if idx%2 == 0:
        if idx != 0:
            batch.commit()
        batch = db.batch()


    for x in seqs:
        name = x.split('.')[0].strip('>')
        sequence = "".join(x.split('\n')[1:]).strip()
        
        # print("Name", name)
        # print("Seq-", sequence)
        doc_ref = db.collection(u'mRNA').document(name)
        batch.set(doc_ref, {'seq':sequence})

    print("\n",len(seqs),"\n")

    #commit and end if length is odd
    if idx == len(contents)-1:
        print("TRUE!")
        batch.commit()

driver.close()