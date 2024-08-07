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