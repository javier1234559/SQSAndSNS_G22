

# Đề tài: Tìm hiểu Amazon SQS , SNS và viết ứng dụng minh họa

## Nhóm 22
- Nguyễn Bùi Minh Nhật - 20161347
- Đỗ Vũ Hưng    - 20110499
- Định Quân  - 20110043

Link ggdrive : https://drive.google.com/drive/folders/1BvBhw59NpnVoV3PGAxgstgiNPDPyS55w?usp=sharing

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
git clone https://github.com/javier1234559/LightSail_G22.git
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
:wq
```
Khởi chạy ứng dụng

```
python3 run.py
```