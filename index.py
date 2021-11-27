import seleniumConfig
import test
import coso
import khuvuc
def main():
    print("=======Main========")
    while(1):
        choose=input('Nhap chuong trinh: ')
        driver= seleniumConfig.login(5)
        coso.addCoSo(driver)
        coso.editCoSo(driver)
        coso.xoaCoso(driver)
        coso.timCoso(driver)
        # test.testFC(driver)
        # test.testJson(driver)
        khuvuc.addKhuvuc(driver)
        khuvuc.addFastKhuvuc(driver)
        khuvuc.editKhuvuc(driver)
        khuvuc.xoaKhuvuc(driver)
        khuvuc.timKhuvuc(driver)
        if(choose=='1'):
            print("___Looping<3___")
main()
