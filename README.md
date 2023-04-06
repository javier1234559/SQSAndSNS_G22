

# Đề tài: Tìm hiểu Amazon SQS , SNS và viết ứng dụng minh họa

## Nhóm 22
- Nguyễn Bùi Minh Nhật - 20161347
- Đỗ Vũ Hưng    - 20110499
- Định Quân  - 20110043

> Link ggdrive : https://drive.google.com/drive/folders/1BvBhw59NpnVoV3PGAxgstgiNPDPyS55w?usp=sharing

> Link báo cáo lần 1 : https://www.youtube.com/watch?v=CqBgWT6eD0A

> Link báo cáo lần 2 : https://www.youtube.com/watch?v=PzCaUAxxQvo

## Deploy lên EC2
Update máy chủ ubutu EC2
```
sudo apt update
```
Cài đặt Python 3.8
```
sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt install python3.8

python3.8 --version

sudo apt-get install python3-pip
```
Cài đặt git

```
sudo apt install git
```
Clone repo về máy chủ EC2 vừa tạo
```
git clone https://github.com/javier1234559/SQSAndSNS_G22.git
```
Mở tường lửa cho port 5000

```
sudo ufw allow 5000
```
Truy cập vào thư mục và cài đặt các gói cần thiết
```
cd LightSail_G22

pip3 install -r requirements.txt

vi config.ini

```
>Copy Accesskey của Lab Learner và bấm lưu 

```
[default]
aws_access_key_id=ASIAV5W6YQ2GVOPR3ZWH
aws_secret_access_key=+w2/3AYrPMlDhJdUPiz4RxyE1iGFuEYG3djG/ZWL
aws_session_token=FwoGZXIvYXdzEGAaDLvaq083zIn57bk3EiLPAfrn0+v8iCEOux0VU+xtrooSO/Hue7132WKT5ruQqHCgilbAq84fWIkGssPCPAP/9TdPQdk33KsLtrZzT+ByxJUVz1SnDsvrmM+YWenSm5mc37gVNgkxHl71VL5dDOeRL5KJVPunf7XTbMzCoVIU5SfoOeh3ZIYukFYdcb18IsWsZOlNrfTCPeCXtN4OxTxaaSrPcp9KUU2mQ1NwkFBKcN6GyKckE3U+t8ujx6UkZ0aR3v+uyjZCVXblMCUlU0R3Tmpjox8USK49rXvtBGPowyiz3IqdBjItebFl9J4fLcIIfw6Aq+tg58zJzUFqW+9lgJ/HTyvjRdTgEdyFTIxny1el1CRD

```

```
:wq
```
Khởi chạy ứng dụng

```
python3 run.py
```
