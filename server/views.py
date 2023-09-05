from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from .util.sec_form_url.sec_form_url import *
from .stock_info.handle_stock_search import *
from .stock_info.download_files import *

@csrf_exempt
def home(request):
    if request.method == 'POST':
        stock_search = request.POST.get("stock-search")
        form_name = request.POST.get("form-name")

        print("Received search query:", stock_search,form_name)
        form_url = handle_stock_search(stock_search,form_name)
        print("Form url:" , form_url)
        file_download = download_and_save_file(url=form_url,stock_ticker=stock_search,form_name=form_name)
        print("File donwload" , file_download)
        # Process the search query here and prepare the response data
        result = {"response": f"Form Url: {file_download}"}
        return JsonResponse(result)
    else:
        # Handle other HTTP methods or render a template
        return JsonResponse({"error": "This view only accepts POST requests for searching."})
    


    

