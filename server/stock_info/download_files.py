from django.http import JsonResponse
import requests,os

def download_and_save_file(url,stock_ticker,form_name):    
    # Make a request to the URL to fetch the file
    headers =  {'User-Agent': '"Bobby Technologies bobbytech@gmail.com"'}  
    response = requests.get(url, headers=headers)
    #print("Response content ",response.content )    
    if response.status_code == 200:
        try:
            # Specify the base folder for stock files in your Server App directory
            base_folder = os.path.join('server', 'stock_files')
            
            # Create the folder structure if it doesn't exist
            stock_folder = os.path.join(base_folder, stock_ticker)
            form_folder = os.path.join(stock_folder, form_name)

            # Create the folders if they don't exist
            os.makedirs(form_folder, exist_ok=True)

            # Specify the file path
            file_path = os.path.join(form_folder, f'{stock_ticker}_{form_name} filename.htm')       

            # Save the file to the specified path
            with open(file_path, 'wb') as file:
                file.write(response.content)
        
        except Exception as e:
            return e

        return JsonResponse({"success": "File downloaded and saved successfully."})
    else:
        return JsonResponse({"error": "Failed to fetch the file."})
    
#print(download_and_save_file('https://www.sec.gov/Archives/edgar/data/789019/000095017023014423/msft-20230331.htm','MSFT','10-Q'))