from selenium import webdriver
from cookies import save_cookie

browser = webdriver.Chrome(executable_path=r"C:\Users\Itay\OneDrive\OneDrive - Technion\Documents\computer science\python\Horizon\chromedriver.exe")
browser.get("https://web.me.app/")

foo = input()

save_cookie(browser, r'C:\Users\Itay\OneDrive\OneDrive - Technion\Documents\computer science\python\Horizon\Caller Identifier\cookie')