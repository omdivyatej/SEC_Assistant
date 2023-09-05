import requests
import urllib.parse

class SECSearch:
    def __init__(self, user_agent_email):
        self.headers = {'User-Agent': user_agent_email}
        self.company_tickers = self.load_company_tickers()

    def load_company_tickers(self):
        response = requests.get("https://www.sec.gov/files/company_tickers.json", headers=self.headers)
        return response.json()
    
    def find_company_info(self,ticker):
        companies = self.load_company_tickers()
        for key,value in companies.items():
            if value["ticker"] == ticker:
                return value["title"]
        return None

    def find_cik_for_ticker(self, target_ticker):
        for key, value in self.company_tickers.items():
            if value['ticker'] == target_ticker:
                cik = value['cik_str']
                complete_cik = str(cik).zfill(10)
                return  complete_cik,cik
        return None

    def generate_search_url(self, ticker, date_range, entity_name, forms, start_date, end_date):
        ciks,cik = self.find_cik_for_ticker(ticker)
        if not ciks:
            return None

        encoded_entity_name = urllib.parse.quote(entity_name)
        url = f"https://efts.sec.gov/LATEST/search-index?dateRange={date_range}&ciks={ciks}&entityName={encoded_entity_name}%20({ticker})%20(CIK%20{ciks})&startdt={start_date}&enddt={end_date}&filter_forms={forms}"
        return url,cik

    def get_latest_form_url(self, search_url,cik):
        response = requests.get(search_url, headers=self.headers)
        data = response.json()["hits"]["hits"]
        
        for item in data:
            k = item["_id"]
            colon_index = k.find(":")
            output_string = k[:colon_index+1].replace("-", "").replace(":", "/") + k[colon_index+1:]
            return f"https://www.sec.gov/Archives/edgar/data/{cik}/{output_string}"



if __name__ == "__main__":
    user_agent_email = "od302002@address.com"
    TICKER = 'NVDA'
    DATE_RANGE = 'custom'
    ENTITY_NAME = 'NVIDIA Corp'
    FORMS = '10-K'
    START_DATE = '2015-09-01'
    END_DATE = '2023-09-01'

    sec_search = SECSearch(user_agent_email)    
    search_url,cik = sec_search.generate_search_url(TICKER, DATE_RANGE, ENTITY_NAME, FORMS, START_DATE, END_DATE)
    print(search_url,cik)
    if search_url:
        form_url = sec_search.get_latest_form_url(search_url,cik)
        print(form_url)
    else:
        print("CIK not found for the given ticker.")
