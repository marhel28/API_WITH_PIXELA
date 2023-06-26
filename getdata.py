import datetime as dt
from CTkMessagebox import CTkMessagebox
import random
import string
import requests
import json
import convertapi
import webview

time = dt.datetime.now()
real_time = time.__str__().split()[0]
real_time = real_time.replace("-", '')

url_endpoint = "https://pixe.la/v1/users"

responses = None


class CData:
    count = 16
    combine = string.ascii_lowercase + string.digits
    token = ''.join(random.choices(combine, k=count))

    def __init__(self, username: str, graphid, color="momiji", type_data="int", unit="km", name_graphs="try"):
        self.name = username
        self.name_graphs = name_graphs
        self.graphid = graphid
        self.data_ = real_time
        self.unit = unit
        self.color = color
        self.Token = self.token
        self.type = type_data
        self.headers = {
            "X-USER-TOKEN": self.Token
        }

    def creat_user(self):
        param_creat = {
            "token": self.Token,
            "username": self.name,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        creat_userdata = requests.post(f"{url_endpoint}", json=param_creat)
        print(creat_userdata.status_code)

    def creat_graphs(self):
        param_creat = {
            "id": self.graphid,
            "name": self.name_graphs,
            "unit": self.unit,
            "type": self.type,
            "color": self.color
        }
        creat_data = requests.post(f"{url_endpoint}/{self.name}/graphs", json=param_creat, headers=self.headers)
        print(creat_data.status_code)
        print(creat_data.text)

    def save_data(self):
        with open("secret.json", "r") as file:
            data = json.load(file)
        data[f"{self.name}"] = {
            "name_graph": self.name_graphs,
            "X-USER-TOKEN": self.Token,
            "id_user": self.graphid
        }
        with open("secret.json", 'w') as file:
            json.dump(data, file, indent=4)


def massageError():
    CTkMessagebox(title="ERROR", message="password or username is filed")


class Data:
    def __init__(self, username: str, graphid: str, quantity: str):
        self.name = username
        self.quantity = quantity
        self.graphid = graphid
        self.token_x = {
            "X-USER-TOKEN": ""
        }
        self.response = f"{url_endpoint}/{self.name}"
        self.__ok = False
        self.__ok2 = False
        self.get_token()

    def get_token(self):
        with open("secret.json", 'r') as file:
            file = json.load(file)
            try:
                if self.name in file:
                    self.__ok = True
                    print(file[f"{self.name}"]["id_user"])
                    if self.graphid == file[f"{self.name}"]["id_user"]:
                        self.token_x["X-USER-TOKEN"] = file[f"{self.name}"]["X-USER-TOKEN"]
                        self.__ok2 = True
                    else:
                        massageError()
                        self.__ok2 = False
                else:
                    self.__ok = False
                    massageError()

            except:
                self.__ok = False

    def data_return_checkmark_id(self, getpass):
        if self.__ok2:
            getpass.select()
        else:
            getpass.deselect()

    def data_return_checkmark(self, getclass):
        if self.__ok:
            getclass.select()
        else:
            getclass.deselect()

    def add_pixel(self):
        param_pixel = {
            "date": real_time,
            "quantity": self.quantity
        }
        print("ok")
        response = requests.post(f"{self.response}/graphs/{self.graphid}", json=param_pixel, headers=self.token_x)
        print(response)
        self.update_realtime()

    def execus(self):
        if self.__ok and self.__ok2:
            return True
        else:
            return False

    def dwonload_pixel(self):
        file_path = "D:/Documents/programming/100days/day 37 API/image"
        params = {
            "appearance": "light"
        }
        response = requests.get(f"{self.response}/graphs/{self.graphid}", params=params)
        print(response.status_code)
        if response.status_code == 200:
            with open(f"{file_path}/python.svg", 'wb') as file:
                file.write(response.content)
                print("file svg telah diunduh")
                convertapi.api_secret = 'pLUpPYKCKuWLCOyc'
                parameters = {
                    'File': f'{file_path}/python.svg'
                }
                convertapi.convert('png', parameters, from_format='svg').save_files(file_path)
        else:
            pass

    def delete_pixel(self, time_pixel: str):
        response = requests.delete(f"{self.response}/graphs/{self.graphid}/{time_pixel}")
        print(response)

    def delete_data_acc(self):
        with open("secret.json", 'r') as file:
            data = json.load(file)
        del data[f"{self.name}"]
        with open("secret.json", 'w') as file:
            json.dump(data, file, indent=4)
        response = requests.delete(url=self.response, headers=self.token_x)
        print(response.text)

    def get_nominal(self):
        response = requests.get(url=f"{self.response}/graphs", headers=self.token_x)
        response = response.content
        print(response)
        data = json.loads(response)
        graphs = data['graphs']
        graphs = graphs[0]
        for k, v in graphs.items():
            with open('secret.json', 'r') as file:
                file_ = json.load(file)
            with open('secret.json', 'w') as file:
                file_[f"{self.name}"][f"{k}"] = f"{v}"
                json.dump(file_, file, indent=4)

    def get_data_all(self):
        response = requests.get(url=f"{self.response}/graphs/{self.graphid}/stats", headers=self.token_x)
        response_ = response.content
        data = json.loads(response_)
        with open("secret.json", 'r') as file:
            file_ = json.load(file)
            for k, v in data.items():
                file_[f"{self.name}"][f"{k}"] = v
        with open('secret.json', 'w') as file:
            json.dump(file_, file, indent=4)

    def update_realtime(self):
        tanggal_obj = dt.datetime.strptime(real_time, "%Y%m%d")
        tanggal_terformat = tanggal_obj.strftime("%Y-%m-%d")
        with open('secret.json', 'r') as file:
            file_ = json.load(file)

        file_[f"{self.name}"][f"update_time "] = tanggal_terformat
        with open('secret.json', 'w') as file:
            json.dump(file_, file, indent=4)

    # def get_retina(self):
    #     response = requests.get(url=f"{self.response}/graphs/{self.graphid}/{real_time}/retina")
    #     webbrowser.open(url=f"{self.response}/graphs/{self.graphid}/{real_time}/retina")
    #     file_path = "D:/Documents/programming/100days/day 37 API/image"
    #     if response.status_code == 200:
    #         with open(f"{file_path}/retina.svg", 'wb') as file:
    #             file.write(response.content)
    #             print("file svg telah diunduh")
    #             convertapi.api_secret = 'pLUpPYKCKuWLCOyc'
    #             parameters = {
    #                 'File': f'{file_path}/retina.svg'
    #             }
    #             convertapi.convert('png', parameters, from_format='svg').save_files(file_path)
    #             self.check_time(real_time)
    #     else:
    #         pass

    def openweb(self):
        return f"{self.response}/graphs/{self.graphid}"

    def getdata_graph(self):
        pass

    @staticmethod
    def check_time(check: str):
        return check

    def website(self):
        response = f"{self.response}/graphs/{self.graphid}.html"
        massage = CTkMessagebox(title="Info", message="close dulu klo mau klik !")
        webview.create_window(title="Habbit Track", url=response)
        webview.start()
