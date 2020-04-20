#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
from collections import defaultdict
import time
from multiprocessing import Process, Manager, Pool
import requests


# In[2]:


button_dict = {'mail' : 'ejmi65789@google.com',
        'phone' : '01044444444',
        'name' : '이조용',
         'pw' : 'Kus410028!',
         'last_n' : 'lee',
         'first_n' : 'chong',
         'year' : '1994',
         'day' : '21',
         'month' : '6',
         'username' : 'dlckdtn901256',
         'confirm' : 'Kus410028!'}

next_word = ['다음', 'next', '시작', 'over', 'Next', 'NEXT', 'OVER', 'Over', '계속', 'continue', 'Continue', 'CONTINUE', 'Verify', 'VERIFY', 'verify', 'Start', 'START', 'start']
banner = ['cookie', 'Cookie', '쿠키', 'COOKIE']
for_cookie = ['ACCEPT', 'Accept', 'Agree', 'Agree', '계속', 'OK', 'Ok', 'ok', 'Continue', 'CONTINUE', 'continue', 'Get', 'Got', 'get', 'got', 'GOT', 'GET']
#accept_word = ['accept', '동의', 'consent', 'sign up', 'register', '수락', 'ACCEPT', 'Accept', 'create', 'Create', 'CREATE', 'Sign Up', 'SIGN UP', '코드', 'code', 'CODE', 'Code', 'agree', 'Agree', 'AGREE', 'Sign up', 'Submit', 'SUBMIT', 'submit', '등록', '계정 생성', '계정생성', '회원가입', '회원 가입']
sign_up_word = ['회원가입', 'sign up', 'Sign UP', 'SIGN UP', 'create', 'CREATE', 'Create', 'Join', 'join', 'JOIN', 'signup', '계정 만들기', '등록', 'Sign up', 'SignUp', 'Try', 'TRY', 'try', 'register', 'Register', 'REGISTER', 'Get Start', 'GET START', 'get start', '가입', 'Sign Up']
privacy = ['privacy', '개인정보', '데이터정책', 'PRIVACY', 'Privacy', '프라이버시']
terms_of_use = ['use', 'agreement', '약관', 'Use', 'USE', 'AGREEMENT', 'Agreement', 'Terms', 'terms', 'TERMS']
total = list()
true_banner = list()
for p in privacy:
    for u in terms_of_use:
        total.append((p, u))
for p in banner:
    for u in for_cookie:
        true_banner.append((p, u))


# In[5]:

def link_check(tag, option):
    result = dict()
    if 'tag' in str(type(tag)).lower():
        if 'href' in tag.attrs:
            print(tag, option)
            result[option+'_link']  = 'O'
        else:
            result[option+'_link']  = 'X'
        return result
    
    result[option+'_link'] = 'X'
    return result

def check_box(tag, option):
    result = dict()
    if 'tag' in str(type(tag)).lower():
        if tag.find_all('input', attrs = {'type' : 'checkbox'}):
            result[option+'_check_box'] = 'O'
            return result
        if tag.find_all('i'):
            result[option+'_check_box'] = 'O'
            return result
        for_siblings = [i for i in list(tag.previous_siblings) if 'tag' in str(type(i)).lower()]
        if len(for_siblings)>0:
            previous = for_siblings[-1]
            if previous.find_all('input', attrs = {'type' : 'checkbox'}):
                result[option+'_check_box'] = 'O'
                return result
            if previous.find_all('i'):
                result[option+'_check_box'] = 'O'
                return result
    result[option+'_check_box'] = 'X'
    return result

def refine(tag, string):
    temporary = str(tag)
    if 'class="' in str(tag):
        temporary = temporary.split('class="')[1]
        temporary = temporary.split('"')
        string['class'] = temporary[0]
    temporary = str(tag)
    if 'id="' in str(tag):
        temporary = temporary.split('id="')[1]
        temporary = temporary.split('"')
        string['id'] = temporary[0]
    temporary = str(tag)
    if 'name="' in str(tag):
        temporary = temporary.split('name="')[1]
        temporary = temporary.split('"')
        string['name'] = temporary[0]
    temporary = str(tag)
    if 'href="' in str(tag):
        temporary = temporary.split('href="')[1]
        temporary = temporary.split('"')
        string['href'] = temporary[0]
        
def finally_refined(object_list):
    result = list()
    for obj in object_list:
        if obj not in result:
            result.append(obj)
    return result

def switch(driver):
    if 1<len(driver.window_handles):
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

class find_values:
    def __init__(self, data_direction, driver, url):
        self.value = data_direction
        self.driver = driver
        self.url = url
        
    def return_text(self, child):
        try:
            return child.text
        except:
            return child.string
        
    def dfs(self, start, next_link_dict):
        visited = list()
        queue = list()
        queue.append(start)
        url = self.url
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                try:
                    for child in list(node.children):
                        text = self.return_text(child)
                        for word in self.value:
                            if word in text.lower():
                                print(word)
                                try:
                                    child.contents
                                    queue.append(child)
                                except:
                                    temporary = dict()
                                    refine(child.parent, temporary)
                                    refine(child, temporary)
                                    print(temporary, child, child.parent)
                                    if temporary:
                                        next_link_dict.append(temporary)
                                        #temporary['word'] = word
                                    
                        if 'value="' in str(child):
                            string = str(child).split('value="')[1]
                            string = string.split('"')[0]
                            for word in self.value:
                                if word in string.lower():
                                    try:
                                        child.contents
                                        queue.append(child)
                                    except:
                                        temporary = dict()
                                        refine(child.parent, temporary)
                                        refine(child, temporary)
                                        if temporary:
                                            next_link_dict.append(temporary)
                                            #temporary['word'] = word
                except : pass 
                
    def create_link(self, links):
        final_link =self.preprocessing(links)
        print(final_link)
        before = self.driver.current_url
        for link in final_link:
            trial(None, link, self.driver)
            time.sleep(5)
            after = self.driver.current_url
            if after != before:
                return True       
    
    def preprocessing(self, links):
        except_link = ['facebook', 'google', 'instagram', 'twitter', 'amazon', 'apple', 'help', 'support', 'forum']
        except_link = [u for u in except_link if u not in self.url]
        final_link = []
        ban_word = False
        for link in links:
            for y in link.values():
                for ban in except_link:
                    if ban in y.lower():
                        ban_word = True
                        break
                if ban_word == True:
                    break
            if ban_word != True:
                final_link.append(link)
        return final_link
        
        
    def policy_dfs(self, start, option):
        visited = list()
        for_footer = start.find('footer')
        queue = list()
        queue.append(start)
        count = 0
        if option == 1:
            while queue:
                node = queue.pop(0)
                if node not in visited:
                    visited.append(node)
                    try:
                        for child in list(node.children):
                            text = self.return_text(child)
                            for word_1, word_2 in self.value:
                                if word_1 in text and word_2 in text:
                                    queue.append(child)
                            if 'value="' in str(child):
                                string = str(child).split('value="')[1]
                                string = string.split('"')[0]
                                for word_1, word_2 in self.value:
                                    if word_1 in string and word_2 in string:
                                        queue.append(child)                                            
                    except: pass
        else:
            while queue:
                node = queue.pop(0)
                if node not in visited:
                    visited.append(node)
                    try:
                        for child in list(node.children):
                            text = self.return_text(child)
                            for word_1 in self.value:
                                if word_1 in text:
                                    queue.append(child)
                            if 'value="' in str(child):
                                string = str(child).split('value="')[1]
                                string = string.split('"')[0]
                                for word_1 in self.value:
                                    if word_1 in string:
                                        queue.append(child)
                    except: pass

        return visited, for_footer
    
    def find_tag(self, target, foot):
        driver = self.driver
        temp = target.pop()
        while 'NavigableString' in str(type(temp)) and target:
            temp = target.pop()
            if 'NavigableString' not in str(type(temp)):
                if temp in foot.contents:
                    continue
                else:
                    break
        return temp

def select(soup, driver):
    for sl in soup.find_all('select'):
        select_tags = {}
        select_check = str(sl).lower()
        if 'country' in select_check or '국가' in select_check:
            select_trial('country', sl, driver)
        elif '년' in select_check or 'year' in select_check or '해' in select_check:
            select_trial('year', sl, driver)
        elif '달' in select_check or 'month' in select_check or '월' in select_check:
            select_trial('month', sl, driver)
        elif 'day' in select_check or '일' in select_check or '날' in select_check:
            select_trial('day', sl, driver)
        elif 'city' in select_check or '도시' in select_check or '도' in select_check:
            select_trial('city', sl, driver)

def keywords(soup, check):
    result = []
    for ipt in soup.find_all(['input']):
        input_tags = {}
        for_input_value_count = {}
        for input_check in ipt.attrs.values():
            if type(input_check) == str:
                input_check = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', input_check).lower()
                if input_check not in for_input_value_count:
                    for_input_value_count[input_check] = 1
                else:
                    for_input_value_count[input_check]+=1
                
        input_check = ''
        max_value = 0
       # print(for_input_value_count)
        for key, value in for_input_value_count.items():
            if max_value<value and key in check:
                input_check = key
                max_value = value
        result.append(input_check.lower())  
    return result
            
            
def input_(soup, check, driver, count):
    for ipt in soup.find_all(['input']):
        input_tags = {}
        for_input_value_count = {}
        for input_check in ipt.attrs.values():
            if type(input_check) == str:
                input_check = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', input_check).lower()
                if input_check not in for_input_value_count:
                    for_input_value_count[input_check] = 1
                else:
                    for_input_value_count[input_check]+=1
                
        input_check = ''
        max_value = 0
       # print(for_input_value_count)
        for key, value in for_input_value_count.items():
            if max_value<value and key in check:
                input_check = key
                max_value = value
        print(input_check)    
        if 'phone' in str(input_check).lower() and check['phone']!=True:
            refine(ipt, input_tags)
            trial('phone', input_tags, driver)
            check['phone'] = True
        elif 'password' == str(input_check).lower() and check['password']!=True and count<2:
            refine(ipt, input_tags)
            trial('pw', input_tags, driver)
            if count == 0:
                check['password'] = False
            else:
                check['password'] = True
            count += 1
        elif 'username' in str(input_check).lower() and check['username']!= True:
            refine(ipt, input_tags)
            trial('username', input_tags, driver)
            check['username'] = True
        elif 'last' in str(input_check).lower() and check['last']!=True:
            refine(ipt, input_tags)
            trial('last_n', input_tags, driver)
            check['last'] = True
        elif 'first' in str(input_check).lower() and check['first']!=True or 'family' in str(input_check).lower():
            refine(ipt, input_tags)
            trial('first_n', input_tags, driver)
            check['first'] = True
        elif 'name' == str(input_check).lower() and check['name'] != True:
            refine(ipt, input_tags)
            trial('name', input_tags, driver)
            check['name'] = True    
        elif 'day' in str(input_check).lower() and check['day']!=True:
            check['day'] = True
            refine(ipt, input_tags)
            trial('day', input_tags, driver)
        elif 'month' in str(input_check).lower() and check['month']!=True:
            check['month'] = True
            refine(ipt, input_tags)
            trial('month', input_tags)
        elif 'year' in str(input_check).lower() and check['year']!=True:
            check['year'] = True
            refine(ipt, input_tags)
            trial('year', input_tags, driver)
        elif 'email' == str(input_check).lower() and check['email']!= True:
            refine(ipt, input_tags)
            trial('mail', input_tags, driver) 
            check['email'] = True
        elif 'confirm' in str(input_check).lower() and check['confirm'] != True:
            refine(ipt, input_tags)
            trial('confirm', input_tags, driver) 
            check['confirm'] = True
    return check, count

def select_trial(opt, string, driver):
    try:
        value = str(sl.find_all('option')[1]).split('value="')[1].split('">')[0]
    except: pass
    if opt == 'country':
        try:
            driver.find_element_by_xpath("//option[@value='"+'KR'+"']").click()
        except:
            pass
    elif opt == 'year':
        try:
            driver.find_element_by_xpath("//option[@value='"+'2000'+"']").click()
        except:
            pass
    elif opt == 'month':
        try:
            driver.find_element_by_xpath("//option[@value='"+'6'+"']").click()
        except : pass
    elif opt == 'day':
        try:
            driver.find_element_by_xpath("//option[@value='"+'20'+"']").click()
        except:
            pass
    elif opt == 'city':
        try:
            driver.find_element_by_xpath("//option[@value='"+value+"']").click()
        except: pass

def trial(attrs, string, driver):
    if attrs!=None:
        try:
            driver.find_element_by_id(string['id']).send_keys(button_dict[attrs])
        except:
            try:
                driver.find_element_by_name(string['name']).send_keys(button_dict[attrs])
            except:
                try:
                    driver.find_element_by_class_name(string['class']).send_keys(button_dict[attrs])
                except Exception as e:
                    return e
    else:
        try:
            driver.find_element_by_class_name(string['class']).click()
        except:
            try: 
                driver.find_element_by_class_name(string['id']).click()
            except:
                try:
                    driver.find_element_by_class_name(string['name']).click()
                   
                except Exception as e:
                    return 'error'

def p_length(paragraph):
    result = ''
    for p in paragraph:
        result+= p.text
    return result

def still_exist(soup, tags_dictionary):
    if 'class' in tags_dictionary:
        if soup.find_all(class_ = tags_dictionary['class']):
            return False
    if 'id' in tags_dictionary:
        if soup.find_all(id_ = tags_dictionary['id']):
            return False
    if 'name' in tags_dictionary:
        if soup.find_all(name = tags_dictionary['name']):
            return False

    return True

def button_(tag, temporary):
    temporary = refine(tag, temporary)
    return temporary
    