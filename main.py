import requests
import os
import subprocess
from tqdm import tqdm

# URL and headers for the request
url1 = "https://kpapiop.ckjr001.com/api/column?searchName=&page=1&limit=100&fromApp=oa"
headers1 = {
    'Host': 'kpapiop.ckjr001.com',
    'accept': 'application/json, text/plain, */*',
    'x-from': 'oa',
    'authorization': 'Bearer <YOUR_AUTHORIZATION_TOKEN>',
    'x-dmp': 'u=lknr8x8&c=qggaa&url=%2FhomePage%2Fcolumn%2FcolumnList&chl=gxh',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wx393fa15d9a499597.wx.ckjr001.com/',
    'Cookie': 'HWWAFSESID=<YOUR_SESSION_ID>; HWWAFSESTIME=<YOUR_SESSION_TIME>'
}

url2_1 = "https://kpapiop.ckjr001.com/api/column/getCourses/"
url2_2 = "?page=1&limit=100&sort=asc&name=&isCoursePage=0&columnPermission=0&fromApp=oa"
headers2 = {
    'Host': 'kpapiop.ckjr001.com',
    'accept': 'application/json, text/plain, */*',
    'x-from': 'oa',
    'authorization': 'Bearer <YOUR_AUTHORIZATION_TOKEN>',
    'x-dmp': 'u=lknr8x8&c=qggaa&url=%2FhomePage%2Fcolumn%2FcolumnList&chl=gxh',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wx393fa15d9a499597.wx.ckjr001.com/',
    'Cookie': 'HWWAFSESID=<YOUR_SESSION_ID>; HWWAFSESTIME=<YOUR_SESSION_TIME>'
}

list_response = requests.request("GET", url1, headers=headers1)
list_data = list_response.json()
extracted_data = [{"name": item["name"], "columnId": item["columnId"]} for item in list_data["data"]["data"]]

def downloader():
    # Initialize the progress bar
    pbar = tqdm(total=len(extracted_data), desc="Downloading assets", unit="asset")
    for item in extracted_data:
        folder_name = item["name"]
        os.makedirs(folder_name, exist_ok=True)  # create the folder if it doesn't exist
        response_json = requests.get(url2_1 + str(item["columnId"]) + url2_2, headers=headers2).json()
        # Iterate over each item in the assets
        for asset in response_json["data"]["data"]:
            for content in asset["assets"]["items"]:
                file_name = content.get("videoName") or content.get("audioName")
                file_url = content.get("videoMp4Url") or content.get("mp3Url")
                file_path = os.path.join(folder_name, file_name)
                # Use ffmpeg to download and save the file
                command = ['ffmpeg', '-i', file_url, '-c', 'copy', '-nostdin', file_path]
                try:
                    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(f"Downloaded and saved {file_name} to {folder_name}")
                except subprocess.CalledProcessError as e:
                    print(f"An error occurred while downloading {file_name}: {e}")
        # Update the progress bar after each asset is processed
        pbar.update(1)
    # Close the progress bar after all downloads are complete
    pbar.close()
downloader()