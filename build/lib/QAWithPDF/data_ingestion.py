from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data):
    """
    load PDF document from a specified directory.
    
    Parameters:
    -data(str): The path to the directory containing PDF file
    
    Returns:
    - A list of loaded PDF documents. The specific type of document may vary.
    """
    
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("Exception in loading the data...")
        raise customexception(e,sys)