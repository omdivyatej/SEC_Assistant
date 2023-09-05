from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.document_loaders import BSHTMLLoader, WebBaseLoader
import os

# loader = WebBaseLoader("https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm", header_template={
# 'User-Agent': 'Burari Technologies omdiv@bartech.com',
# })
# data1 = loader.load()

loader = BSHTMLLoader("SEC_Assistant/testing/filing-details.html")
data = loader.load()

print(data[0].page_content)
# Define the file name
file_name = "my_text_file2.txt"

# Open the file in write mode and store the data
with open(file_name, 'w', encoding="utf-8") as file:
    file.write(data[0].page_content)

print(f"Data has been saved to {file_name}")
