import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s')

list_of_files  = [    "src/__init__.py",
                      "src/helper.py",
                      "src/prompt.py",
                      ".env",
                      "requirements.txt",
                      "setup.py",
                      "research/trials.ipynb",
                      "app.py",
                      "static/docs",
                      "static/output"
                  ]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,file_name = os.path.split(filepath)
    

    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory {file_dir} for the files {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath , "w") as f:
            pass 
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{file_name} is already exists")
    