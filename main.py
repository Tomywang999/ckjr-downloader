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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8va3BhcGlvcC5ja2pyMDAxLmNvbS9hcGkvbXAvYXV0aENhbGxiYWNrIiwiaWF0IjoxNzE5Mjg2NDAyLCJleHAiOjE3MjE4Nzg0MDIsIm5iZiI6MTcxOTI4NjQwMiwianRpIjoiYUNkMWxQZTdSclo0c0p0WiIsInN1YiI6bnVsbCwiYyI6InFnZ2FhIiwidSI6ImxrbnI4eDgiLCJhIjoxLCJsaXZlQXV0aElkIjowLCJpc21iIjowLCJwIjpudWxsLCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIiwic3lzIjoibWljcm8iLCJhdWkiOjEwMDI1LCJyZnQiOjE2MzUyMTE1NDUsInVpZCI6IjE0NDIyOTkyNDQ3NzI4NDM1MjIiLCJhcHBJZCI6IjE0NDIyOTkyNDMyODY4OTI1NDUiLCJsb2dpblVzZXJUeXBlIjoyLCJjdiI6MjAwLCJ1dHkiOjIsImFpZCI6IjE0ODIyMzcxODgwMTkxMjYyNzQiLCJjaWQiOiIxNDgyMjM3MTg2MTY1NTE0MjQxIiwiYWciOjkzMjcwOCwib3BJZCI6Imx6bjdwbjlvIiwianV0IjowLCJvcEFkbWluVXNlcklkIjowLCJqdW4iOiJcdTVmYzNcdTUxNDNcdTk3NTJcdTVjMTFcdTVlNzRcdTViYjZcdTVlYWRcdTYyMTBcdTk1N2ZcdTViNjZcdTk2NjIifQ.1qnjSJhqMDHSyMlCwSXJ3w9-pXm8NIcPtmnW5Qt_D3c',
    'x-dmp': 'u=lknr8x8&c=qggaa&url=%2FhomePage%2Fcolumn%2FcolumnList&chl=gxh',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wx393fa15d9a499597.wx.ckjr001.com/',
    'Cookie': 'HWWAFSESID=b614b19f88a0171114b; HWWAFSESTIME=1719287028153'
}

url2_1 = "https://kpapiop.ckjr001.com/api/column/getCourses/"
url2_2 = "?page=1&limit=100&sort=asc&name=&isCoursePage=0&columnPermission=0&fromApp=oa"
headers2 = {
    'Host': 'kpapiop.ckjr001.com',
    'accept': 'application/json, text/plain, */*',
    'x-from': 'oa',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8va3BhcGlvcC5ja2pyMDAxLmNvbS9hcGkvbXAvYXV0aENhbGxiYWNrIiwiaWF0IjoxNzE5Mjg2NDAyLCJleHAiOjE3MjE4Nzg0MDIsIm5iZiI6MTcxOTI4NjQwMiwianRpIjoiYUNkMWxQZTdSclo0c0p0WiIsInN1YiI6bnVsbCwiYyI6InFnZ2FhIiwidSI6ImxrbnI4eDgiLCJhIjoxLCJsaXZlQXV0aElkIjowLCJpc21iIjowLCJwIjpudWxsLCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIiwic3lzIjoibWljcm8iLCJhdWkiOjEwMDI1LCJyZnQiOjE2MzUyMTE1NDUsInVpZCI6IjE0NDIyOTkyNDQ3NzI4NDM1MjIiLCJhcHBJZCI6IjE0NDIyOTkyNDMyODY4OTI1NDUiLCJsb2dpblVzZXJUeXBlIjoyLCJjdiI6MjAwLCJ1dHkiOjIsImFpZCI6IjE0ODIyMzcxODgwMTkxMjYyNzQiLCJjaWQiOiIxNDgyMjM3MTg2MTY1NTE0MjQxIiwiYWciOjkzMjcwOCwib3BJZCI6Imx6bjdwbjlvIiwianV0IjowLCJvcEFkbWluVXNlcklkIjowLCJqdW4iOiJcdTVmYzNcdTUxNDNcdTk3NTJcdTVjMTFcdTVlNzRcdTViYjZcdTVlYWRcdTYyMTBcdTk1N2ZcdTViNjZcdTk2NjIifQ.1qnjSJhqMDHSyMlCwSXJ3w9-pXm8NIcPtmnW5Qt_D3c',
    'x-dmp': 'u=lknr8x8&c=qggaa&url=%2FhomePage%2Fcolumn%2FcolumnDetail%3FcId%3D-1%26ckFrom%3D9%26extId%3D135131&chl=gxh',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/6.8.0(0x16080000) MacWechat/3.8.8(0x13080812) XWEB/1216 Flue',
    'origin': 'https://wx393fa15d9a499597.wx.ckjr001.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wx393fa15d9a499597.wx.ckjr001.com/',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"ae56447b9305734cb0bc496b454ea42f9ccd4014"',
    'Cookie': 'HWWAFSESID=b614b19f88a0171114b; HWWAFSESTIME=1719287028153'
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