from server.util.sec_form_url.sec_form_url import SECSearch


def handle_stock_search(ticker,form_name):
    user_agent_email = "Bobby Technologies bobbytech@gmail.com"
    TICKER = ticker
    DATE_RANGE = 'custom'
    ENTITY_NAME = ''
    FORMS = form_name
    START_DATE = '2015-09-01'
    END_DATE = '2023-09-01'

    sec_search = SECSearch(user_agent_email)
    ENTITY_NAME = sec_search.find_company_info(TICKER)
    search_url,ciks = sec_search.generate_search_url(TICKER, DATE_RANGE, ENTITY_NAME, FORMS, START_DATE, END_DATE)
    
    if search_url:
        form_url = sec_search.get_latest_form_url(search_url,ciks)
        return form_url
    else:
         return "CIK not found for the given ticker."
    
print(handle_stock_search("NVDA","10-Q"))