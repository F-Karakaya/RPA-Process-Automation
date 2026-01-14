import spacy
import re
import json
import logging
import datetime

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EntityExtractor:
    """
    Extracts structured entities (Invoice Number, Date, Amount, Vendor) 
    using NLP (SpaCy) and Regex patterns.
    """
    
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            logger.warning("Spacy model not found. Downloading...")
            from spacy.cli import download
            download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")
            
    def extract_entities(self, text):
        """
        Extract key business entities from text.
        """
        doc = self.nlp(text)
        entities = {
            "invoice_number": None,
            "date": None,
            "amount": None,
            "vendor": None
        }
        
        # 1. Vendor Extraction (ORG entities from Spacy)
        for ent in doc.ents:
            if ent.label_ == "ORG" and not entities["vendor"]:
                entities["vendor"] = ent.text
                
        # 2. Date Extraction (DATE entities)
        for ent in doc.ents:
            if ent.label_ == "DATE" and not entities["date"]:
                entities["date"] = ent.text
                
        # 3. Invoice Number (Regex)
        # Looks for patterns like INV-1234, Invoice #5555
        inv_match = re.search(r'(INV-\d+|Invoice\s*#?\s*\d+)', text, re.IGNORECASE)
        if inv_match:
            entities["invoice_number"] = inv_match.group(0)
            
        # 4. Amount (Money or Regex)
        # Looks for currency symbols
        amt_match = re.search(r'[\$£€]\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)
        if amt_match:
            entities["amount"] = amt_match.group(0)
            
        return entities

def run_extraction_demo():
    extractor = EntityExtractor()
    
    sample_text = """
    INVOICE
    Invoice Number: INV-2024-001
    Date: March 15, 2024
    
    To: Global Tech Solutions
    From: Acme Corp Services
    
    Description:
    Consulting Services - 40 Hours
    
    Total Amount: $5,000.00
    """
    
    logger.info("Extracting entities from sample invoice...")
    result = extractor.extract_entities(sample_text)
    
    output = {
        "raw_text": sample_text.strip(),
        "extracted_data": result,
        "processing_time": str(datetime.datetime.now())
    }
    
    print(json.dumps(output, indent=4))
    
    with open('ai_integration/entity_results.json', 'w') as f:
        json.dump(output, f, indent=4)

if __name__ == "__main__":
    run_extraction_demo()
