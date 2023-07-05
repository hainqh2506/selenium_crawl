from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def download_pdf(url, download_path):
    # Khởi tạo tùy chọn cho trình duyệt Chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    options.add_argument('--no-sandbox')
    options.add_argument('--verbose')
    options.add_experimental_option("prefs", {     #đổi đường dẫn download
        "profile.default_content_setting_values.automatic_downloads": 1,
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    #options.add_argument("--headless")  # Chạy trình duyệt ở chế độ headless, không hiển thị giao diện trực tiếp
    
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome(options=options) 
    driver.get(url)
    time.sleep(2)  # Chờ trang web tải xong nội dung
    # chon muc can tai
    i = 1  #chon i = 
    # 1, Dang ky moi ; 2, Dang ky thay doi ; 3, Thong bao thay doi ; 4,Vi pham / Thu hoi; 5, Giải thể ; 6, Loại khác
    new_page = driver.find_element(By.XPATH, f"//a[@id='LnkActiveAnnType' and contains(@href, \"javascript:__doPostBack('ctl00$C$RptProdGroups$ctl{i:02}$LnkActiveAnnType','')\")]")
    new_page.click()
    time.sleep(3)
    #down load page 1.
    for i in range(2,22):
        pdf_icon = driver.find_element(By.CSS_SELECTOR, f"#ctl00_C_CtlList_ctl{i:02}_LnkGetPDFActive")
        driver.execute_script("arguments[0].click();", pdf_icon)
        time.sleep(0.1)
    # download page 2-25
    for i in range(2,26):
        next_page = driver.find_element(By.XPATH, "//a[@href=\"javascript:__doPostBack('ctl00$C$CtlList','Page${}')\"]".format(i))
        next_page.click()
        time.sleep(0.1)
        
        for i in range(2,22):
            pdf_icon = driver.find_element(By.CSS_SELECTOR, f"#ctl00_C_CtlList_ctl{i:02}_LnkGetPDFActive")
            driver.execute_script("arguments[0].click();", pdf_icon)
            time.sleep(0.1)
            driver.execute_script("document.getElementById('return').style.display = 'none';")
#--------------------------------------------------------------------------------------------

url = "https://dichvuthongtin.dkkd.gov.vn/egazette/Forms/Egazette/DefaultAnnouncements.aspx"
download_path = "D:\crawl\Test"
download_pdf(url, download_path)

# for i in range(1,7):
#     new_page = driver.find_element(By.XPATH, f"//a[@id='LnkActiveAnnType' and contains(@href, \"javascript:__doPostBack('ctl00$C$RptProdGroups$ctl{i:02}$LnkActiveAnnType','')\")]")

#     new_page.click()
#     time.sleep(3)
