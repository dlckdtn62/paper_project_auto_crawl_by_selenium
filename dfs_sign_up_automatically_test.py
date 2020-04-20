from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
from collections import defaultdict
import numpy as np
import time
from multiprocessing import Process, Manager, Pool
from 최종테스트 import *
import requests
import copy

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
skip = ['skip', 'Skip', 'SKIP']
        
def practice(url):
    
    print(url, end = ' ')
    result_dictionary = defaultdict(dict)
    if 'netflix' in url or 'google' in url or 'openload' in url or 'vk' in url or 'hulu' in url or 'xfinity' in url or 'canva' in url or 'quora' in url or 'quizlet' in url or 'medium' in url or 'twitter' in url or 'zendesk' in url:
        result_dictionary[url]['link_term'] = 'test on mechanic'
        result_dictionary[url]['term_check_box'] = 'test on mechanic'
        result_dictionary[url]['link_privacy'] = 'test on mechanic'
        result_dictionary[url]['privacy_check_box'] = 'test on mechanic'
        result_dictionary[url]['exist_check_box'] = 'test on mechanic'
        result_dictionary[url]['direct'] = 'test on mechanic'
        print(result_dictionary)
        return result_dictionary

    driver = webdriver.Chrome('C:\\Users\\dlckd\\onedrive\\Desktop\\chromedriver.exe')
    driver.get('https://www.vpnbook.com/webproxy')
    driver.implicitly_wait(20)
    time.sleep(20)
    driver.find_element_by_xpath('//*[@id="input"]').send_keys('www.google.com')
    driver.find_element_by_xpath('//*[@id="webproxylocation"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="webproxyform"]/input[2]').click()
    driver.implicitly_wait(20)
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('www.'+url+' create account')
    except:
        driver.quit()
        return url
    try:
        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
    except:
        driver.quit()
        return url
    driver.implicitly_wait(20)
    time.sleep(20)
#     driver = webdriver.Chrome('C:\\Users\\quadratic_fuction2\\Desktop\\chromedriver.exe')
#     driver.get('https://www.vpnbook.com/webproxy')
#     driver.implicitly_wait(20)
#     time.sleep(20)
#     driver.find_element_by_xpath('//*[@id="input"]').send_keys('https://www.google.co.uk/webhp?hl=en')
#     driver.find_element_by_xpath('//*[@id="webproxylocation"]/option[3]').click()
#     driver.find_element_by_xpath('//*[@id="webproxyform"]/input[2]').click()
#     driver.implicitly_wait(20)
#     driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(url+' create account, sign up')
#     driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
#     driver.implicitly_wait(20)
#     time.sleep(20)

    try:
        driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3').click()
    except:
        try:
            driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/a/h3').click()
        except:
            try:
                driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div/div[1]/a/h3').click()
            except:
                try:
                    driver.find_element_by_xpath('//*[@id="rso"]/div/div[1]/div/div[1]/a/h3').click()
                except:
                    try:
                        driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div[1]/a/h3').click()
                    except:
                        try:
                            driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3').click()
                        except:
                            result_dictionary[url]['direct'] = 'xpath-check'
                            result_dictionary[url]['link_term'] = 'xpth-check'
                            result_dictionary[url]['term_check_box'] = 'xpth-check'
                            result_dictionary[url]['link_privacy'] = 'xpth-check'
                            result_dictionary[url]['privacy_check_box'] = 'xpth-check'
                            result_dictionary[url]['exist_check_box'] = 'xpth-check'
                            driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
                            driver.quit()
                            print(result_dictionary)
                            return result_dictionary
    try:       
        response = requests.get(driver.current_url)
    except requests.exceptions.ConnectionError as e:
        result_dictionary[url]['direct'] = e
        result_dictionary[url]['link_term'] = e
        result_dictionary[url]['term_check_box'] = e
        result_dictionary[url]['link_privacy'] = e
        result_dictionary[url]['privacy_check_box'] = e
        result_dictionary[url]['exist_check_box'] = e
        driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
        driver.quit()
        return result_dictionary
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
            
    driver.implicitly_wait(20)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    find_join_link = find_values(sign_up_word, driver, url)
    join_link = list()
    for x in soup.body.contents:
        find_join_link.dfs(x, join_link)
    join_link = finally_refined(join_link)
    print(join_link)
    for_link_check = find_join_link.create_link(join_link)
    print('join')
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:       
        response = requests.get(driver.current_url)
    except requests.exceptions.ConnectionError as e:
        result_dictionary[url]['direct'] = e
        result_dictionary[url]['link_term'] = e
        result_dictionary[url]['term_check_box'] = e
        result_dictionary[url]['link_privacy'] = e
        result_dictionary[url]['privacy_check_box'] = e
        result_dictionary[url]['exist_check_box'] = e
        driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
        driver.quit()
        return result_dictionary
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    if len(driver.window_handles)>1:
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:       
        response = requests.get(driver.current_url)
    except requests.exceptions.ConnectionError as e:
        result_dictionary[url]['direct'] = e
        result_dictionary[url]['link_term'] = e
        result_dictionary[url]['term_check_box'] = e
        result_dictionary[url]['link_privacy'] = e
        result_dictionary[url]['privacy_check_box'] = e
        result_dictionary[url]['exist_check_box'] = e
        driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
        driver.quit()
        return result_dictionary
    soup = BeautifulSoup(driver.page_source, 'lxml')
    continue_email = find_values(['continue with email', 'sign up with email'], driver, url)
    continue_list = []
    for x in soup.body.contents:
        continue_email.dfs(x, continue_list)
    continue_list = finally_refined(continue_list)
    for_continue = continue_email.create_link(continue_list)
    try:       
        response = requests.get(driver.current_url)
    except requests.exceptions.ConnectionError as e:
        result_dictionary[url]['direct'] = e
        result_dictionary[url]['link_term'] = e
        result_dictionary[url]['term_check_box'] = e
        result_dictionary[url]['link_privacy'] = e
        result_dictionary[url]['privacy_check_box'] = e
        result_dictionary[url]['exist_check_box'] = e
        driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
        driver.quit()
        return result_dictionary
    
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print(len(soup.find_all('body')))

    check_soup = 1
    count = 1

    input_check = {'phone' : False,
     'password' : False,
     'last' : False,
     'first' : False,
     'day' : False,
     'month' : False,
     'year' : False,
     'name' : False,
     'email' : False,
     'Username' : False,
     'confirm' : False}
    
    except_link = ['facebook', 'google', 'instagram', 'twitter', 'amazon', 'apple', 'help', 'yahoo']
    except_link = [u for u in except_link if u not in url]
    print('link')
    count_ = 0
    before_check = input_check
    while check_soup !=soup and 7>=count:
        before = []
        test = find_values(next_word, driver, url)
        temp = soup.body
        link_next = list()
        for x in temp.contents:
            test.dfs(x, link_next)
        if not link_next or len(link_next) == 0:
            break
        link_next = finally_refined(link_next)
        if check_soup != 1:
            soup = check_soup
        if soup.find(['select']):
            select(soup, driver)
        if soup.find(['input']):
            before = keywords(soup, input_check)
            input_check, count_ = input_(soup, input_check, driver, count_)
        check = True
        if 1<len(driver.window_handles):
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
        for link in link_next:
            trial(None, link, driver)
            result = keywords(soup, input_check)
            if before!=result:
                break
        check_soup = BeautifulSoup(driver.page_source, 'lxml')
        count +=1
        time.sleep(7)
        
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:       
        response = requests.get(driver.current_url)
    except requests.exceptions.ConnectionError as e:
        result_dictionary[url]['direct'] = e
        result_dictionary[url]['link_term'] = e
        result_dictionary[url]['term_check_box'] = e
        result_dictionary[url]['link_privacy'] = e
        result_dictionary[url]['privacy_check_box'] = e
        result_dictionary[url]['exist_check_box'] = e
        driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
        driver.quit()

    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #print(input_check)
    
#     accept_find = find_values(accept_word, driver, url)
#     accept_list = list()
#     accept_find.dfs(soup, accept_list)
#     accept_list = finally_refined(accept_list)

#     if not accept_list:
#         result_dictionary[url]['direct'] = 'no-accept-button'
#         result_dictionary[url]['term_link'] = 'no-accept-button'
#         result_dictionary[url]['term_check_box'] = 'no-accept-button'
#         result_dictionary[url]['privacy_link'] = 'no-accept-button'
#         result_dictionary[url]['privacy_check_box'] = 'no-accept-button'
#         result_dictionary[url]['exist_check_box'] = 'no-accept-button'
#         driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
#         driver.quit()
#         return result_dictionary
    print('terms')
    privacy_find = find_values(privacy, driver, url)
    privacy_list, footer_y = privacy_find.policy_dfs(soup, 2)
    use_find = find_values(terms_of_use, driver, url)
    use_list, footer_z = use_find.policy_dfs(soup, 2)
    privacy_list = finally_refined(privacy_list)
    use_list = finally_refined(use_list)
    total_find = find_values(total, driver, url)
    total_list, footer_x = total_find.policy_dfs(soup, 1)
    x = finally_refined(total_list)
    y = privacy_find.find_tag(privacy_list, footer_y)
    z = use_find.find_tag(use_list, footer_z)
    x = total_find.find_tag(total_list, footer_x)
    privacy_in_total = find_values(privacy, driver, url)
    privacy_in_x, footer_privacy_x = privacy_in_total.policy_dfs(x, 2)
    privacy_in_x = finally_refined(privacy_in_x)
    xy = privacy_in_total.find_tag(privacy_in_x, footer_privacy_x)
    use_in_total = find_values(terms_of_use, driver, url)
    use_in_x, footer_use_x = use_in_total.policy_dfs(x, 2)
    use_in_x = finally_refined(use_in_x)
    xz = use_in_total.find_tag(use_in_x, footer_use_x)
    print(x)
    print(y)
    print(z)
    print(xy)
    print(xz)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    paragraph_length = len(p_length(soup.find_all('p')))

    if 10000<paragraph_length:
        result_dictionary[url]['direct'] = 'O'
        result_dictionary[url]['term_link'] = 'X'
        result_dictionary[url]['term_checkbox'] = 'X'
        result_dictionary[url]['privacy_link'] = 'X'
        result_dictionary[url]['privacy_check_box'] = 'X'
        result_dictionary[url]['exist_check_box'] = 'X'

    if 'direct' not in result_dictionary[url]:
        for_append = link_check(xy, 'privacy')
        for key, value in for_append.items():
            #print(key, value)
            result_dictionary[url][key] = value
        for_append = link_check(xz, 'term')
        for key, value in for_append.items():
            #print(key, value)
            result_dictionary[url][key] = value
        result_dictionary[url]['direct'] = 'X'

        if xy.parent != xz.parent:
            result_dictionary[url]['exist_check_box'] = 'X'
            for_append = check_box(xy.parent, 'privacy')
            for key, value in for_append.items():
                result_dictionary[url][key] = value
            for_append = check_box(xz.parent, 'term')
            for key, value in for_append.items():
                result_dictionary[url][key] = value
        else:
            for_append = check_box(x, 'exist')
            #print(for_append)
            for key, value in for_append.items():
                result_dictionary[url][key] = value
            result_dictionary[url]['privacy_check_box'] = 'X'
            result_dictionary[url]['term_check_box'] = 'X'

        if result_dictionary[url]['privacy_link'] == 'X' and result_dictionary[url]['privacy_check_box'] == 'X' and result_dictionary[url]['exist_check_box'] == 'X':
            for_append = check_box(y.parent, 'privacy')
            for key, value in for_append.items():
                result_dictionary[url][key] = value
            for_append = link_check(y, 'privacy')
            for key, value in for_append.items():
                result_dictionary[url][key] = value

        if result_dictionary[url]['term_link'] == 'X' and result_dictionary[url]['term_check_box'] == 'X' and result_dictionary[url]['exist_check_box'] == 'X':
            for_append = check_box(z.parent, 'term')
            for key, value in for_append.items():
                result_dictionary[url][key] = value
            for_append = link_check(z, 'term')
            for key, value in for_append.items():
                result_dictionary[url][key] = value

        if result_dictionary[url]['term_check_box'] == 'O' or result_dictionary[url]['privacy_check_box'] == 'O':
            result_dictionary[url]['exist_check_box'] = 'X'
                
    driver.save_screenshot('c:\\users\\dlckd\\onedrive\\desktop\\screenshot\\'+url+'.png')
    driver.quit()
    print(result_dictionary)
    print()
    print()
    return result_dictionary