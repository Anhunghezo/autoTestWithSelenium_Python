import time
import json
from coso import addCoSo
import help
from help import check_btn_nextpage

def testFC(driver):
  print('___TESTING!!___')
  driver.get ("https://banhang.upgo.vn/#/area/collection")
  time.sleep(3)
  # help.getByClass(driver,"p-button-label").click()
  # time.sleep(1) 
  print('find tpCS')
  # print(len(help.getsByClass(driver, 'ng-dirty')))
  help.getsByClass(driver,"p-button-label")[1].click()
  time.sleep(3)
  print(len(help.getsByClass(driver, 'float-right')))
  xxx =help.getsByClass(driver, 'float-right')
  for x in xxx:
    print(x)
  time.sleep(2)
  help.getsByClass(driver, 'pi-chevron-down')[0].click()
  time.sleep(2)
  help.getsByClass(driver, 'p-autocomplete-item')[2].click()
  # help.getById(driver, 'area_no').send_keys('Da click')
  # time.sleep(2)
  # help.getById(driver, 'integeronly').send_keys('1')
  # time.sleep(2)
  # help.getsByClass(driver, 'pi-chevron-down')[0].click()
  # time.sleep(2)
  # 
  # #XONG
  # time.sleep(4)
  # help.getsByClass(driver, 'fa-check-square')[0].click()
  # help.getByName(driver, 'area_no').send_keys("da click")

def testJson(driver):
  f = open('./dataH.json', encoding='utf-8')  
  list = json.load(f)
  newCoso = list['newCoso']
  addCosoMPTY = list['addCosoMPTY']
  editCoso = list['editCoso']
  newKhuvuc = list['newKhuvuc']
  newFastKhuvuc = list['newFastKhuvuc']
  newFastKhuvucMPTY = list['newFastKhuvucMPTY']
  editKhuvucXX = list['editKhuvucXX']
  print('List Json: ', list)
  print('New coso: ', newCoso)
  print('AddCS EMPTY: ', addCosoMPTY)
  print('EditCS: ', editCoso)
  print('New khuvuc: ', newKhuvuc)
  print('NewF KV: ', newFastKhuvuc)
  print('NewF KV Empty: ',newFastKhuvucMPTY)
  print('Edit KV: ', editKhuvucXX)

