import requests,json

class GoogleSearchApi():
    def search(search_term):
        googlecustomsearch='https://www.googleapis.com/customsearch/v1?'
        googleaccesskey='AIzaSyAkFYTMOVmvPniL4Y9dL5RDQehQ7BJ6gCQ'
        cx='014930882088392870627:heixbbhopvu'
        search_term=googlecustomsearch+'key='+googleaccesskey+'&cx='+cx+'&q='+search_term
        try:
            search_data=requests.get(search_term,timeout=10)
            search_data = search_data.json()
        except Exception:
            return "GSA couldn't connect to the internet\n Please check your internet connection and try again.\n Happy searching!"
        
        return search_data
