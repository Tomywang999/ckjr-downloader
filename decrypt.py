import requests
import os
import subprocess
from tqdm import tqdm
from Crypto.Cipher import AES
import base64
from concurrent.futures import ThreadPoolExecutor

key_url = "https://kpapiop.ckjr001.com/api/company/share?reservedRefereeId=9zvg2r9&protectRefereeId=9zvg2r9&fromApp=oa"
key_headers = {
    'Host': 'kpapiop.ckjr001.com',
    'accept': 'application/json, text/plain, */*',
    'x-from': 'oa',
    'authorization': 'Bearer <YOUR_AUTHORIZATION_TOKEN>',
    'x-dmp': 'u=p3842xp&c=nkz9&url=%2F%3FfromQr%3D1%26refereeId%3D9zvg2r9&chl=gxh',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/6.8.0(0x16080000) MacWechat/3.8.8(0x13080812) XWEB/1216 Flue',
    'origin': 'https://wx8a386e8fb04db387.wx.ckjr001.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wx8a386e8fb04db387.wx.ckjr001.com/',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"49dbc684be54d8e466d803345765e0a0de191edc"',
    'Cookie': 'HWWAFSESID=<YOUR_SESSION_ID>; HWWAFSESTIME=<YOUR_SESSION_TIME>'
}
courselist_url = "https://kpapiop.ckjr001.com/api/courses?name=&type=3&page=1&limit=1000&isVip=&catId=&sort=&p=&sortType=1&fromApp=oa"
courselist_headers = {
    'Host': 'kpapiop.ckjr001.com',
    'accept': 'application/json, text/plain, */*',
    'x-from': 'oa',
    'authorization': 'Bearer <YOUR_AUTHORIZATION_TOKEN>',
    'x-dmp': 'u=p3842xp&c=nkz9&url=%2FhomePage%2Fcourse%2FcourseList%3Ftype%3D0%26sortType%3D1&chl=gxh',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/6.8.0(0x16080000) MacWechat/3.8.8(0x13080812) XWEB/1216 Flue',
    'origin': 'https://wx8a386e8fb04db387.wx.ckjr001.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wx8a386e8fb04db387.wx.ckjr001.com/',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"a1e3d4baad1a3c93a905a3d8006c3d6d1b5688fa"',
    'Cookie': 'HWWAFSESID=<YOUR_SESSION_ID>; HWWAFSESTIME=<YOUR_SESSION_TIME>'
}
getcourse_url1 = "https://kpapiop.ckjr001.com/api/courses/"
getcourse_url2 = "/dirs?page=1&limit=1000&courseType=0&hasPermission=false&fromApp=oa"
getcourse_headers = {
    'Host': 'kpapiop.ckjr001.com',
    'accept': 'application/json, text/plain, */*',
    'x-from': 'oa',
    'authorization': 'Bearer <YOUR_AUTHORIZATION_TOKEN>',
    'x-dmp': 'u=p3842xp&c=nkz9&url=%2FhomePage%2Fcourse%2Fvideo%3FcourseId%3D3738411%26ckFrom%3D5%26extId%3D-1&chl=gxh',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/6.8.0(0x16080000) MacWechat/3.8.8(0x13080812) XWEB/1216 Flue',
    'origin': 'https://wx8a386e8fb04db387.wx.ckjr001.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wx8a386e8fb04db387.wx.ckjr001.com/',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"9a66d8b2c37b6b557760cd36e302cdea416741eb"',
    'Cookie': 'HWWAFSESID=<YOUR_SESSION_ID>; HWWAFSESTIME=<YOUR_SESSION_TIME>'
}
list_response = requests.request("GET", courselist_url, headers=courselist_headers)
list_data = list_response.json()
extracted_data = [{"name": item["name"], "courseId": item["courseId"]} for item in list_data["data"]["data"]]
def decrypt_aes_cbc_nopad(encrypted_data, key, iv):
    # Convert the base64 encoded string to bytes
    encrypted_data = base64.b64decode(encrypted_data)
    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    # Decrypt the encrypted data
    decrypted_data = cipher.decrypt(encrypted_data)
    # Decode the decrypted data from base64 to plain text
    plain_text = decrypted_data.decode('utf-8')
    return plain_text.replace('\n', '')

# Get key from the API
key_response = requests.request("GET", key_url, headers=key_headers).json()
key = key_response['data']['passKey']['key'].encode()
vi = key_response['data']['passKey']['vi'].encode()
#key = 'ckjrTheKey!@##@!'.encode()
#iv = '9NONwyJtHesysWpN'.encode()
enc_test = 'A01BofK8icuTYAHuJ9GitUwzHeovgePKWDvyiafFJh7dYEpLSZ3B/RgptlwMnyLPjxfm2ygbvmZh1t66z2STRig4opkRGUtOOxxzAnJhx/MTyTaeaJwAWFXu9wS5IWFNZPjNF6VyH4nYA0dhqelDVz4LZ5GMrG3vCAnhKQlZ2rBcnJuRZoa4DTv1UDWDR3oAmWD5Iq9Bw0SNyuDHndDqA/V7m7f4dfy3/EcKYOvUQHc='
#print(decrypt_aes_cbc_nopad(enc_test,key,vi))

def download_asset(asset, folder_name):
    file_name = asset.get("videoName")
    if not file_name.endswith('.mp4'):
        file_name += ".mp4"
    enc_url = asset.get("videoUrlEncode")
    file_url = decrypt_aes_cbc_nopad(enc_url,key,vi)
    file_path = os.path.join(folder_name, file_name)
    # Use ffmpeg to download and save the file with maximum threads
    command = ['ffmpeg', '-i', file_url, '-c', 'copy', '-threads', '0', '-nostdin', file_path]
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Downloaded and saved {file_name} to {folder_name}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading {file_name}: {e}")

def downloader():
    # Initialize the progress bar
    pbar = tqdm(total=len(extracted_data), desc="Downloading assets", unit="asset")
    with ThreadPoolExecutor(max_workers=5) as executor:
        for item in extracted_data:
            folder_name = item["name"]
            os.makedirs(folder_name, exist_ok=True)  # create the folder if it doesn't exist
            response_json = requests.get(getcourse_url1 + str(item["courseId"]) + getcourse_url2, headers=getcourse_headers).json()
            # Iterate over each item in the assets
            for asset in response_json["data"]:
                executor.submit(download_asset, asset, folder_name)
            # Update the progress bar after each asset is processed
            pbar.update(1)
    # Close the progress bar after all downloads are complete
    pbar.close()

downloader()