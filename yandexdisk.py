import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {
            "Content-Type" : "application/json",
            "Authorization" : f"OAuth {self.token}"
        }
    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path" : file_path, "overwrite" : "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str, file_name: str):
        href_dict = self._get_upload_link(file_path=file_path)
        href = href_dict.get("href")
        response = requests.put(href, data=open(file_name, "rb"))
        response.raise_for_status()


if __name__ == '__main__':
    file = "homework.txt"
    yadisk_path = "netology_homework/homework.txt"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(yadisk_path, file)