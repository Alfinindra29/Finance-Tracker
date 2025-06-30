from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Inisialisasi opsi headless (tanpa GUI)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inisialisasi WebDriver
driver = webdriver.Chrome(options=options)

# Ganti URL dengan alamat publik Codespaces kamu
BASE_URL = "https://your-username-5000.app.github.dev"  # GANTI URL ini

try:
    # 1. Login
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "username").send_keys("demo")  # ganti sesuai user test
    driver.find_element(By.NAME, "password").send_keys("demo")  # ganti sesuai user test
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    time.sleep(2)

    # 2. Tambah Transaksi
    driver.get(f"{BASE_URL}/transactions")
    driver.find_element(By.NAME, "date").send_keys("2025-07-01")
    driver.find_element(By.NAME, "category").send_keys("Uji Otomatis")
    driver.find_element(By.NAME, "amount").send_keys("10000")
    driver.find_element(By.NAME, "payment_method").send_keys("Cash")
    driver.find_element(By.NAME, "notes").send_keys("Tes otomatis via Selenium")
    driver.find_element(By.XPATH, '//button[contains(text(), "Tambah")]').click()

    time.sleep(2)

    # 3. Logout
    driver.get(f"{BASE_URL}/logout")

    print("✅ TEST BERHASIL: Login → Tambah Transaksi → Logout")

except Exception as e:
    print("❌ TEST GAGAL:", e)

finally:
    driver.quit()
