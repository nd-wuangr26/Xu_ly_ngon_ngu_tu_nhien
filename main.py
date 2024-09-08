import streamlit as st
import numpy as np
import pandas as pd
import re

st.title('CHƯƠNG TRÌNH XỬ LÝ NGÔN NGỮ TỰ NHIÊN')
file = st.file_uploader('Input file text cần xử lý')
#API xu ly ngon ngu
def input():
    if file is not None:
        content = file.read().decode('utf-8')
        words = content.split()
        return words
    return []

def dem_hien_thi():
    words = input()
    a = []
    for word in words:
        if word not in a:
            a.append(word)
    return a

def tan_xuat_tu_don():
    words = input()
    cout = {}
    for word in words:
        if word in cout:
            cout[word] += 1
        else:
            cout[word] = 1
    return cout

def tan_xuat_tu_doi():
    words = input()
    cout = {}
    if len(words) < 2:
        st.write('Khong du tu de xuat')
    for i in range(len(words) - 1):
        tu_doi = (words[i], words[i+1])
        if tu_doi in cout:
            cout[tu_doi] += 1
        else:
            cout[tu_doi] = 1
    return cout

def xoa_ky_tu_db():
    words = input()
    delete = []
    for word in words:
        delete_words = re.sub(r'[^a-zA-Z0-9\s\u00C0-\u1EF9]', '', word, flags=re.UNICODE).upper()
        delete.append(delete_words)
    return delete


# Design web
if st.button('Đếm số lượng từ xuất hiện'):
    st.write('So luong xuat hien la: ', len(dem_hien_thi()))

if st.button('Tần xuất xuất hiện từ đơn'):
    result = tan_xuat_tu_don()
    if isinstance(result, dict):
        st.write('Tần suất xuất hiện từ đơn là:')
        for word, freq in result.items():
            st.write(f'{word}: {freq}')
    else:
        st.write(result)

if st.button('Tần xuất xuất hiện từ đôi'):
    result = tan_xuat_tu_doi()
    if isinstance(result, dict):
        st.write('Tần suất xuất hiện từ đôi là:')
        for tu_doi, freq in result.items():
            st.write(f'{tu_doi}: {freq}')
    else:
        st.write(result)

if st.button('Xóa ký tự đặc biệt và viết hoa'):
    st.write('Kết quả: ', xoa_ky_tu_db())