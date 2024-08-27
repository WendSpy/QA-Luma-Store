from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# Configurando o WebDriver (exemplo com Chrome)
driver = webdriver.Chrome()

try:
    # 1. Acessar a Home Page
    driver.get("https://magento.softwaretestingboard.com/")

    # Verificar se a página inicial carregou corretamente (checar por algum elemento específico da página)
    assert "Home Page" in driver.title, "Página inicial não carregou corretamente"

    # 2. Buscar por "shirt" no campo de busca no menu superior
    search_box = driver.find_element(By.NAME, "q")  # Encontre o campo de busca pelo nome ou outro identificador
    search_box.send_keys("shirt")
    search_box.send_keys(Keys.RETURN)  # Simular a tecla "Enter"
    time.sleep(2) 

    # Esperar até que a página de resultados carregue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "page-title"))  # Altere o localizador para um elemento específico da página de resultados
    )
    assert "Search results for: 'shirt'" in driver.page_source, "Página de resultados não carregou corretamente"
    time.sleep(2) 

    # 3. Adicionar um produto no carrinho
    product = driver.find_element(By.CLASS_NAME, "product-item-link") 
    product.click()  # Clicar no produto para ir para a página de detalhes
    time.sleep(2) 
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "product-addtocart-button"))  # Esperar que o botão de adicionar ao carrinho seja visível
    )

    size = driver.find_element(By.ID, "option-label-size-143-item-168") # Seleciona o tamanho do produto
    size.click()
    time.sleep(1) 

    color = driver.find_element(By.ID, "option-label-color-93-item-50") # Seleciona a cor do produto
    color.click()
    time.sleep(1) 

    add_minicart = driver.find_element(By.ID, "product-addtocart-button")  # Adiciona o produto ao carrinho
    add_minicart.click()
    time.sleep(2) 

    # 4. Realizar checkout
    WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, "top-cart-btn-checkout"))  # Esperar que o botão de checkout seja visível
    )
    time.sleep(2) 

    minicart = driver.find_element(By.CLASS_NAME, "minicart-wrapper") #Clica no carrinho 
    minicart.click()
    time.sleep(1) 

    checkout_button = driver.find_element(By.ID, "top-cart-btn-checkout") # Clica no checkout
    checkout_button.click()
    time.sleep(2) 

    # Verificar se a página de checkout carregou corretamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "step-title"))
    )
    assert "i18n: 'Shipping Address'" in driver.page_source, "Página de checkout não carregou corretamente"

    email = driver.find_element(By.ID, "customer-email")  
    email.send_keys("gordon.fernandez@example.com")
    email.send_keys(Keys.RETURN)
    time.sleep(2) 

    first_name = driver.find_element(By.NAME, "firstname")  
    first_name.send_keys("Gordon")
    time.sleep(2) 

    last_name = driver.find_element(By.NAME, "lastname")  
    last_name.send_keys("Fernandez")
    time.sleep(2)

    element = driver.find_element(By.NAME, "company")
    driver.execute_script("arguments[0].scrollIntoView();", element)

    address  = driver.find_element(By.NAME, "street[0]")  
    address.send_keys("5415 Northaven Rd")
    time.sleep(2) 

    city = driver.find_element(By.NAME, "city")  
    city.send_keys("Dallas")
    time.sleep(2) 

    #clica na box state
    state = driver.find_element(By.CLASS_NAME, "select")
    state.click()
    time.sleep(2) 

    texas_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//option[@data-title='Texas']"))
)

# Realizar o scroll até a opção "Texas" (se necessário)
    driver.execute_script("arguments[0].scrollIntoView();", texas_option)

# Selecionar a opção "Texas"
    texas_option.click()

    time.sleep(2)

    postal_code = driver.find_element(By.NAME, "postcode")  
    postal_code.send_keys("12345")
    time.sleep(2) 

    #Clica na pox country
    country = driver.find_element(By.NAME, "country_id")
    country.click()
    time.sleep(2) 

    united_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//option[@data-title='United States']"))
)

# Realizar o scroll até a opção "United States"
    driver.execute_script("arguments[0].scrollIntoView();", united_option)
# Selecionar a opção "United States"
    united_option.click()
    time.sleep(2)

    phone_number = driver.find_element(By.NAME, "telephone")  
    phone_number.send_keys("(374) 393-4118")
    time.sleep(2) 

    element2 = driver.find_element(By.NAME, "postcode")
    driver.execute_script("arguments[0].scrollIntoView();", element2)

    methods = driver.find_element(By.NAME, "ko_unique_5")
    methods.click()
    time.sleep(2) 

    button_next = driver.find_element(By.CSS_SELECTOR, "button[data-role='opc-continue']")
    button_next.click() 

    # Verificar se a página de checkout carregou corretamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout-payment-method-load"))
    )
    assert "Payment Method" in driver.page_source, "Página de checkout não carregou corretamente"
    time.sleep(4)
    
    final = driver.find_element(By.CSS_SELECTOR, "button[title='Place Order']")
    final.click()

    time.sleep(10) 

finally:
    # Fechar o navegador
    driver.quit()
