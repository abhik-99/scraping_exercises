# NCBI Nucleotide Sequence Scraper using Selenium

The scraper runs to first read the name of the mRNA or miRNA or any similar genetic material and then scrapes it and stores the FASTA Format in a Google Cloud Firestore database.

## Authors:

**Abhik Banerjee**

## Requirements:
1. Selenium.
2. Chromium Driver.
3. Linux (Originally Made for)
4. GCP account.
5. Service Key for GCP (should be stored in ```config/gcp-access-key.json```)
6. File containing the URLs of NCBI to be scraped (Nucleotide names have to be embedded in the URLS).

The name of the file orginally chosen is ```humanURL.txt``` and is made available with this project.

## How to run?

Assumming that all the requirements are fulfilled and modifications are made, the project can begin scraping by executing

```python main.py```

