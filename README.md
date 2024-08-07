# Xử lý ngôn ngữ tự nhiên 
---------------------------------------
## Yêu cầu: 
1. Đếm và hiển thị ra màn hình bộ vựng trong file text đầu vào
2. HIển thị ra màn hình tần suất xuất hiện của từng từ đơn theo chiều giảm dần
3. HIển thị ra màn hình tần suất xuất hiện của các cặp 2 từ đơn theo chiều giảm dần
4. Xóa bỏ các ký tự đặc biệt (#,%,&,”,..). Chuyển đổi văn bản sang ký tự Hoa và ngược lại
## Luyện tập: 
- Ghi đọc file tex
- List, array, dict
- Xử lý văn bản
## Code
```py
import re

import numpy as np

def doc_file_text():
    with open('D:/Du_lieu_tong_hop/Hoc AI/Doc_tai_lieu.txt', 'r', encoding = 'utf-8') as file :
        content = file.read()
        words = content.split()
        return words

def dem_hien_thi():
    words = doc_file_text()
    a = []
    for word in words:
        if word not in a:
            a.append(word)
    return a

def tan_xuat_tu_don():
    count = {}
    words = doc_file_text()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

def tan_xuat_tu_doi():
    words = doc_file_text()
    count = {}
    for i in range (len(words) - 1):
        tu_doi = (words[i], words[i+1])
        if tu_doi in count:
            count[tu_doi] += 1
        else:
            count[tu_doi] = 1
    return count

def xoa_ky_tu_dac_biet():
    words = doc_file_text()
    delet_word = []
    for word in words:
        delet_words = re.sub(r'[^a-zA-Z0-9\s\u00C0-\u1EF9]', '', word, flags=re.UNICODE).upper()
        delet_word.append(delet_words)
    return delet_word

def main():
    a = dem_hien_thi()
    word_count = tan_xuat_tu_don()
    tu_doi = tan_xuat_tu_doi()
    viet_hoa = xoa_ky_tu_dac_biet()
    print('Chuoi co',len(a),'tu vung')
    print('\nCac tu vung cua chuoi la: ',a)
    print('\nTan xuat xuat hien cua tung tu la: ')
    for word, count in word_count.items():
        print(f'{word}: {count}')
    print('\nTan xuat xuat hien cua tung tu la: ')
    for word, count in tu_doi.items():
        print(f'{word[0]} {word[1]}: {count}')
    print('Xoa ky tu dac biet va viet hoa no: ')
    print(viet_hoa)
if __name__ == '__main__':
    main()
```
## Kết quả: 
Cac tu vung cua chuoi la:  ['Các', 'kiểu', 'dữ', 'liệu', 'cơ', 'bản', 'chỉ', 'chứa', 'một', 'giá', 'trị', 'mỗi', 'biến', '(số,', 'chuỗi),', 'tuy', 'nhiên', 'nhiều', 'lúc', 'mình', 'cần', 'trị,', 'ví', 'dụ', 'tên', 'học', 'sinh', 'trong', 'lớp', 'có', '100', 'bạn']

Tan xuat xuat hien cua tung tu la: 
Các: 1
kiểu: 1
dữ: 1
liệu: 1
cơ: 1
bản: 1
chỉ: 1
chứa: 3
một: 2
giá: 2
trị: 1
mỗi: 1
biến: 1
(số,: 1
chuỗi),: 1
tuy: 1
nhiên: 1
nhiều: 2
lúc: 1
mình: 1
cần: 1
trị,: 1
ví: 1
dụ: 1
tên: 1
học: 1
sinh: 1
trong: 1
lớp: 1
có: 1
100: 1
bạn: 2

Tan xuat xuat hien cua tung tu la: 
Các kiểu: 1
kiểu dữ: 1
dữ liệu: 1
liệu cơ: 1
cơ bản: 1
bản chỉ: 1
chỉ chứa: 1
chứa một: 1
một giá: 1
giá trị: 1
trị mỗi: 1
mỗi biến: 1
biến (số,: 1
(số, chuỗi),: 1
chuỗi), tuy: 1
tuy nhiên: 1
nhiên nhiều: 1
nhiều lúc: 1
lúc mình: 1
mình cần: 1
cần chứa: 1
chứa nhiều: 1
nhiều giá: 1
giá trị,: 1
trị, ví: 1
ví dụ: 1
dụ chứa: 1
chứa tên: 1
tên học: 1
học sinh: 1
sinh trong: 1
trong một: 1
một lớp: 1
lớp có: 1
có 100: 1
100 bạn: 1
bạn bạn: 1
Xoa ky tu dac biet va viet hoa no: 
['CÁC', 'KIỂU', 'DỮ', 'LIỆU', 'CƠ', 'BẢN', 'CHỈ', 'CHỨA', 'MỘT', 'GIÁ', 'TRỊ', 'MỖI', 'BIẾN', 'SỐ', 'CHUỖI', 'TUY', 'NHIÊN', 'NHIỀU', 'LÚC', 'MÌNH', 'CẦN', 'CHỨA', 'NHIỀU', 'GIÁ', 'TRỊ', 'VÍ', 'DỤ', 'CHỨA', 'TÊN', 'HỌC', 'SINH', 'TRONG', 'MỘT', 'LỚP', 'CÓ', '100', 'BẠN', 'BẠN']
![image](https://github.com/user-attachments/assets/576c916c-8824-4dee-8767-709420547149)
