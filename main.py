import pandas as pd
import requests
from datetime import date
import time
import random

# PARAMS - set according to preference
CAR_MAKE = 'Honda' # brand
CAR_MODEL = 'Civic' # specific model
ZIP = '10001' # input as string

# FOLLOW README TO GET YOUR OWN AUTHORIZATION TOKEN AND SET TO VARIABLE BELOW
AUTH = 'YOUR AUTH TOKEN HERE'

def request_carfax(zip_code, car_make, car_model):
    scraped_results = []

    pages_headers = {  # initial request to find # pages for current search
      'authority': 'www.carfax.com',
      'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
      'authorization': AUTH,
      'accept': 'application/json',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    }

    pages_url = f"https://www.carfax.com/api/v2/consumers/auth0%7Coasc%7C454836195/findVehicles?tpQualityThreshold=150&tpPositions=1%2C2%2C3&tpValueBadges=GOOD%2CGREAT&zip={zip_code}&radius=50&sort=BEST&dynamicRadius=false&make={car_make}&model={car_model}&certified=false&oneAccountId=auth0%7Coasc%7C454836195"
    response = requests.request("GET", pages_url, headers=pages_headers, data={})
    json_res1 = response.json()
    pages_in_search = json_res1['totalPageCount'] # number of pages in search
    print(f'There are {pages_in_search} pages of search results', f'for {car_make} {car_model} in Area Code: {zip_code}')

    for x in range(pages_in_search):  # scraping each page of search results
        print("Scraping page", x , "...")
        headers = {
            'authority': 'www.carfax.com',
            'method': 'GET',
            'scheme': 'https',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'x-cfx-alternator': 'Qhids3yPOM5IZ7U6FyGoXSBbcI2q+VnCGv+8KEy6twk=',
            'x-cfx-dynamo': '1631218927918',
            'sec-ch-ua-mobile': '?0',
            'authorization': AUTH,
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.carfax.com/',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cookie': 'uuid=2785a5d4-9028-4fc2-b119-4f1a2dc8f20b; abt=eligible; vdp=1; s_fid=4A9CDC63CCF1CF8F-3CEE39DC979DF661; numberOfRecentSearches=3; search_uuid=b061514d-3656-4b36-8132-da1873db78b1; g_state={"i_p":1630433297917,"i_l":2}; id=auth0%7Coasc%7C454836195; name=awsomdude17%40aim.com; api_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EUkNRMEZETnpReVFrVXlNVE01TkVNME5URkNOREU1TWpGQ01EaEVOalZHUWtJNU16Z3pNdyJ9.eyJodHRwczovL2NhcmZheC5jb20vY29uc3VtZXJzIjp7ImVtYWlsIjoiYXdzb21kdWRlMTdAYWltLmNvbSIsInN0YXR1cyI6IkFDVElWRSJ9LCJpc3MiOiJodHRwczovL2F1dGguY2FyZmF4LmNvbS8iLCJzdWIiOiJhdXRoMHxvYXNjfDQ1NDgzNjE5NSIsImF1ZCI6Imh0dHBzOi8vd3d3LmNhcmZheC5jb20vYXBpIiwiaWF0IjoxNjMwMzQ3MDA2LCJleHAiOjE2MzI5MzkwMDYsImF6cCI6ImZSWlhYSjdlWUwzaDk5R2RERmcyU1BUejBRWjR2MVZIIiwiZ3R5IjoicGFzc3dvcmQifQ.S7UXbvh_QaAKMxSbmyENjVoGHuJaR5fw6PAOGRo6H_LyzjXRJB6BZJ5kU4oek1DjW5HBaqeLTDhJNCuI2yEdc9R8wRBPwGN7xvNu_q2YcySlw2VeBM2QOc91azPNDw6ChBD-pZpOWoNL4WAzxXMZg5BUblBW9wSPyXC6Ey9iflCSIj20vXof0oAulcwYnAnTYZ7go4Fl-eNaSMdgBJli26pfnSsR8lWeEStdUJfmF4MEusG7yjf-wH0tM8uo-YNmGQH1k5VLT1DNai9JWDm4WqiCKUxzPTPX_DQnJUyPM1fQKpcfPGKDCMvmoW6ANpoMSVvueKdgaWGW2S-4FgD43w; en=p; carousel_uuid=b8b42d2f-3da5-48a0-b6ef-8a457b9f31e0; cache=MISS; AMCVS_AAC63BC75245B47C0A490D4D%40AdobeOrg=1; s_sess=%20s_cc%3Dtrue%3B; OptanonConsent=isIABGlobal=false&datestamp=Thu+Sep+09+2021+15%3A57%3A29+GMT-0400+(Eastern+Daylight+Time)&version=5.15.0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=&legInt=&AwaitingReconsent=false&geolocation=US%3BMA; OptanonAlertBoxClosed=2021-09-09T19:57:29.123Z; AMCV_AAC63BC75245B47C0A490D4D%40AdobeOrg=1406116232%7CMCIDTS%7C18880%7CMCMID%7C23126708835703172285165607164356578194%7CMCAID%7CNONE%7CMCOPTOUT-1631224649s%7CNONE%7CvVersion%7C2.5.0; crv=2.288.0; d_l_a=%7B%22fname%22%3A%22%22%2C%22lname%22%3A%22%22%2C%22hzip%22%3A%7B%22words%22%3A%5B-2025185127%2C-384937933%2C1643938057%2C1825401765%2C829041662%2C-659239416%2C-595878451%2C1106219770%5D%2C%22sigBytes%22%3A32%7D%2C%22emailHashed256%22%3A%7B%22words%22%3A%5B-865319190%2C1120342809%2C-939676476%2C38293973%2C494886427%2C178949054%2C1602683276%2C-1549884321%5D%2C%22sigBytes%22%3A32%7D%2C%22pno%22%3A%22%22%7D; zip=01545; datadome=SlyD2pIaGE62Rs0znkFWmQt91ZO.c9fs.j0-~l8Z4LxoPLDK9jVQqc_ppQr2CVOZPU8hCAfN6aXOC4hEvmy9tQU085Dh.U8ASK.cMkiVrT; cfx_search_params=%7B%22vin%22%3A%22JF1VA2E63L9803015%22%2C%22params%22%3A%7B%22tpQualityThreshold%22%3A%22150%22%2C%22tpPositions%22%3A%221%2C2%2C3%22%2C%22tpValueBadges%22%3A%22GOOD%2CGREAT%22%2C%22zip%22%3A%2201545%22%2C%22radius%22%3A50%2C%22sort%22%3A%22BEST%22%2C%22make%22%3A%22Subaru%22%2C%22model%22%3A%22WRX%22%2C%22page%22%3A1%2C%22urlInfo%22%3A%22Subaru-WRX_w621%22%7D%2C%22apiUrl%22%3A%22https%3A%2F%2Fwww.carfax.com%2Fapi%2Fv2%2Fconsumers%2Fauth0%257Coasc%257C454836195%2FfindVehicles%3FtpQualityThreshold%3D150%26tpPositions%3D1%252C2%252C3%26tpValueBadges%3DGOOD%252CGREAT%26zip%3D01545%26radius%3D50%26sort%3DBEST%26make%3DSubaru%26model%3DWRX%26certified%3Dfalse%26oneAccountId%3Dauth0%257Coasc%257C454836195%22%2C%22seoUrl%22%3A%22Used-Subaru-WRX_w621%22%2C%22srpTitle%22%3A%22Used%20Subaru%20WRX%20for%20Sale%20in%20Shrewsbury%2C%20MA%20(with%20Photos)%20-%20CARFAX%22%7D; search_uuid=42e36ec1-f1ac-45a2-976c-6a26aa5c03c7; s_pers=%20gpv_p17%3Dno%2520value%7C1631220727861%3B%20gpv_p18%3Dno%2520value%7C1631220727883%3B; s_sq=%5B%5BB%5D%5D'
        }
        url = f"https://www.carfax.com/api/v2/consumers/auth0%7Coasc%7C454836195/findVehicles?tpQualityThreshold=150&tpPositions=1%2C2%2C3&tpValueBadges=GOOD%2CGREAT&zip={zip_code}&radius=50&sort=BEST&dynamicRadius=false&make={car_make}&model={car_model}&certified=false&page={x}&oneAccountId=auth0%7Coasc%7C454836195"
        response = requests.request("GET", url, headers=headers, data={})
        json_res = response.json()
        todays_date = date.today().strftime('%m-%d-%Y') #date for exporting
        for cars in json_res["listings"]:
            year = cars["year"]
            make = cars["make"]
            model = cars["model"]
            car_listing_price = cars["listPrice"]
            car_mileage = cars["mileage"]
            dealer_address = cars["dealer"]["address"]
            dealer_city = cars["dealer"]["city"]
            dealer_state = cars["dealer"]["state"]
            dealer_name = cars["dealer"]["name"]
            car_url = cars["vdpUrl"]



            listing_details = {
                'year': year,
                'make': make,
                'model': model,
                'list_price': car_listing_price,
                'mileage': car_mileage,
                'dealer_address': dealer_address,
                'dealer_city': dealer_city,
                'dealer_state': dealer_state,
                'dealer_name': dealer_name,
                'link': car_url
            }

            scraped_results.append(listing_details)  # add listing details as dict to ongoing list
            time.sleep(random.uniform(0, 0.8))  # adding delay to prevent IP ban -> increase delay for larger scrapes


    scraped_results = pd.DataFrame(scraped_results) # convert list of dicts to dataframe
    scraped_results = scraped_results.drop_duplicates(subset=['link'])  # check & delete duplicates

    print("Successfully scraped", str(len(scraped_results)), car_make, car_model, "listing(s) from Area Code:", zip_code)
    scraped_results.to_excel('scrapes/{}_{}_{}_scrapes_{}.xlsx'.format(car_make, car_model, zip_code, todays_date))

request_carfax(ZIP, CAR_MAKE, CAR_MODEL)


