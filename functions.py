import requests,json


class GoogleSearchApi():
    # def __init__(self,search_term):
    #     self.search_term=search_term

    def search(search_term):
        googlecustomsearch='https://www.googleapis.com/customsearch/v1?'
        googleaccesskey='AIzaSyAkFYTMOVmvPniL4Y9dL5RDQehQ7BJ6gCQ'
        cx='014930882088392870627:heixbbhopvu'
        search_term=googlecustomsearch+'key='+googleaccesskey+'&cx='+cx+'&q='+search_term
        search_data=requests.get(search_term,timeout=10)
        search_data = search_data.json()
        return search_data
