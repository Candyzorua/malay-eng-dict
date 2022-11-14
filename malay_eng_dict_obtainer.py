#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 00:03:54 2022

@author: jiayingong
"""
from bs4 import BeautifulSoup
import requests
import re
import json

#This program outputs a .json file of Malay words and corresponding 
#English translations obtained from Dr. Bhanot's Malay-English
#Cyber Dictionary, http://dictionary.bhanot.net

#Getting data from page and turning into soup object
URL = "http://dictionary.bhanot.net/b.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#Getting list of Malay words
def get_words(soup: BeautifulSoup) -> list[str]:
    words_raw = soup.find_all("b")
    words_raw.pop(0)
    words = [w.get_text().strip(':') for w in words_raw] 
    return words

#Getting list of English translations
def get_tns(soup: BeautifulSoup) -> list[str]:
    tns_raw = soup.find_all("dd")
    tns = []
    for w in tns_raw:
        while True:
            try:
                w.b.decompose() #destroying <b> tag
            except AttributeError:
                break
        pattern = r'<br/>'
        mod_w = re.sub(pattern, '~', str(w)) 
        mod_w = mod_w.replace('<dd>', '') 
        mod_w = mod_w.replace('</dd>', '') 
        for t in (mod_w.split('~')): 
            t = t.strip() 
            if t != '':
                tns.append(t) 
    return tns

#Combining words and translations into a dict
def get_dict(letter: str, wrds_to_remove: list[str], 
             tns_to_remove: list[str]) -> dict():
    #Getting page content and making BeautifulSoup object
    URL = f"http://dictionary.bhanot.net/{letter}.html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    words = get_words(soup)
    tns = get_tns(soup)
    
    words_dict = {}
    if wrds_to_remove != []: #remove words with no translations
        for wrd in wrds_to_remove:
            words.remove(wrd)
    if tns_to_remove != []: #remove translations with no words
        for tn in tns_to_remove:
            tns.remove(tn)
    for indx in range(0, len(words)):
        words_dict[words[indx]] = tns[indx]
    return words_dict

#Cleaning up dicts for each letter and combining into 1 main dict
def get_main_dict() -> dict:
    a_dict = (get_dict('a', [], ['mengajukan: to propose; to put forward for discussion']))
    b_dict = (get_dict('b', [], []))
    c_dict = (get_dict('c', [], ['bercawat: to wear a loincloth',
                              'mencebur: to plunge',
                              'menceburi: to get involved in; to plunge into',
                              'menceburkan: to plunge into; to get involved in']))
    d_dict = (get_dict('d', [], []))
    e_dict = (get_dict('e', [], []))
    f_dict = (get_dict('f', [], []))
    g_dict = (get_dict('g', [], ['bergelumang: dirty']))
    h_dict = (get_dict('h', [], []))
    i_dict = (get_dict('i', [], []))
    j_dict = (get_dict('j', ['juruukur'], []))
    k_dict = (get_dict('k', ['glossy;'], ["kacang bendi: lady's fingers", 
                                  'kekasaran: coarseness; rudeness; roughness',
                                  'menguap: to yawn',
                                  'terkuap-kuap: yawning repeatedly']))
    l_dict = (get_dict('l', [], []))
    m_dict = (get_dict('m', [], []))
    n_dict = (get_dict('n', [], []))
    o_dict = (get_dict('o', [], []))
    p_dict = (get_dict('p', [], []))
    q_dict = (get_dict('q', [], []))
    r_dict = (get_dict('r', [], []))
    s_dict = (get_dict('s', [], []))
    t_dict = (get_dict('t', [], []))
    u_dict = (get_dict('u', [], ['(2) comment']))
    v_dict = (get_dict('v', [], []))
    w_dict = (get_dict('w', ['sewajarnya', 'berwaspada'], []))
    w_dict = {'walau' if k == '\nwalau' else k:v for k,v in w_dict.items()} #replacing bad word
    x_dict = (get_dict('x', [], []))
    y_dict = (get_dict('y', [], []))
    z_dict = (get_dict('z', [], []))
    
    main_dict = {}
    list_of_letterdicts = [a_dict, b_dict, c_dict, d_dict, e_dict, f_dict, g_dict,
                           h_dict, i_dict, j_dict, k_dict, l_dict, m_dict, n_dict,
                           o_dict, p_dict, q_dict, r_dict, s_dict, t_dict, u_dict,
                           v_dict, w_dict, x_dict, y_dict, z_dict]
    
    for d in list_of_letterdicts:
        main_dict.update(d)
        
    return main_dict

#Serializing main dict to json and writing to file
def get_json(main_dict) -> None:
    json_dict = json.dumps(main_dict, indent=4)
    with open("malay-eng-dict.json", "w") as outfile:
        outfile.write(json_dict)
        
main_dict = get_main_dict()
get_json(main_dict)
    



    



