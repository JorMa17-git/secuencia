from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def procesar_enlace(driver, enlace):
    try:
        print(f"\n🔁 Procesando enlace: {enlace}")
        driver.get(enlace)
        
        # Intenta hacer clic en el botón de ataque
        try:
            boton_ataque = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btnFury"))
            )
            boton_ataque.click()
            print("✅ ¡Ataque realizado con éxito!")
            return True
        except:
            print("⚠️ Botón no encontrado o no clickeable")
            return False
    
    except Exception as e:
        print(f"🚨 Error procesando enlace: {str(e)}")
        return False

def main():
    # Lista de 15 enlaces (ejemplo)
    enlaces = [
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/vIusly5nEpb7zahlllXBhpbwNgzh4bPD/h/17e35cb667a22ff94fec48a479c52c8d/t/1752357190/linkDefense/289d39241bb2e453d3bbe8d1282a280a3eb9e867",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/eBEAXZq6Rnq64W8DarhmZXjJpG5shyQg/h/4ee086db816ccd546413e20b400d9f8a/t/1752357455/linkDefense/9a3702b7ec0df2dbb37c73f49b792c4c8a0835d2",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/iO3FFDfVCcfJIH1s7zIwkb977PUoy9za/h/d67bf10147e0fd79e7aa8b9857c14d1a/t/1752357610/linkDefense/0de6422ca9b01189b1a9ad09e80024476cbc0a22",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/iHcEw1aS33fid9REFizb6omNKcGwwhFV/h/f96ac502d54edc4f501b1c5ad9867bb5/t/1752357843/linkDefense/e490fea8710c5079349157f6ddf4387fc2157bc0",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/rZPk1lALdK2g8U5sTUH6KDZHkeVpHYUi/h/58b99d8d18d2aaf52fd935916e6be6cd/t/1752358024/linkDefense/1f3ffc0d486f4afe0d3963454142ea51fda1193d",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/4IKe9feaV3rurxbneanpZxS4dq2Xz5lV/h/b46a3c072b92818c2a3173e7da62447f/t/1752358199/linkDefense/3508895f70c33666069b8db6c2bfa275fb8897d4",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/WrCR1UpaY7GKNmZl66SiCM16jnp2iHaC/h/c782c9bc8481da22056c2b7c3170fc41/t/1752358304/linkDefense/d74f2ac20c2c63a4dd228af466b0aaf1c734d6d9",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/PebMjE9UciCXiqKchvbVY7ekyYTu1oVX/h/5ff44409e4a7ece1ee57a65e0beaa9ba/t/1752358428/linkDefense/86d702e65a0e71aea1e009e4c0528c2c3f69592d",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/QRSUys7TUo71EzWadUK2QaTqX8F49pRx/h/caec9dea3746a67a6428077f18dc7a5a/t/1752358525/linkDefense/5ba247732d48c93ccaeffedf19d69f4a241704d2",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/h1SrvsO7F7wpVQSWwV6SCzk8QVYdfhfq/h/63fee575f1563aa419683eb1884fb263/t/1752358622/linkDefense/29a842acdbfbdaf9e85054017f49ed71d05528e4",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/7YxS1WI5xsE3DelGY9s6LfrJJeoNhGkG/h/6a9893c76184958276f236d830443fb5/t/1752358759/linkDefense/23fb55fbfed5263e373ed455b7ce3515da0df708",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/DtnAOg8GpIZ9jDvTurkz9pOeGLOGhP6B/h/663cb99c9fa62029d3c2d4d194880983/t/1752358982/linkDefense/501a2aefaddb0c3e0b69efe6b0bfaa5410d59cc0",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/9fRXWrnMxEu4JXv34YJCFWTqgpla8pFV/h/2f11a49f1a1433a010e6e468ad8f1d31/t/1752359174/linkDefense/37e10daf4b6b64f233308156a6023c9fe42b380b",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/keK8qRfdmylpNdD43XsniLyHmnUFXDGx/h/613ebaf9341c90c0c33381129c086656/t/1752359390/linkDefense/8344f73ba8a3765558a6e729631a4806a54b624f",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/n4KdXuwtSBbW7dBuGwLwUDPXkUStLyMr/h/8013b70e52f0b600d352520c1153dfab/t/1752359580/linkDefense/d07d2fe130d6e647717931ca3a6b56b6cbe0b2e4",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/TfPwWGMas9Z77IUQputGhMQEknOSjtkl/h/057472ce76e617793473b2419e408d7d/t/1752359761/linkDefense/09cdcb3967050a4a40891870d868fdc51b9009b9",
        "https://wargameserver3.evilgrog.com/profile/index/id/109336/i/3MpGGmbcFsCDTVghi1qkdN9Yflgf62EH/h/12119121a96752efac7099a1218e28d8/t/1752359928/linkDefense/65d690e3a9277e190a83d23a6b0bf7b4e1dbfe30"
        
    ]
    
    # Configuración del navegador
    servicio = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless=new")
    
    with webdriver.Chrome(service=servicio, options=options) as driver:
        driver.implicitly_wait(5)
        
        for i, enlace in enumerate(enlaces):
            print(f"\n🔗 Procesando enlace {i+1}/{len(enlaces)}")
            procesar_enlace(driver, enlace)
            
            # Espera 30 segundos excepto después del último enlace
            if i < len(enlaces) - 1:
                print("⏳ Esperando 30 segundos para el próximo enlace...")
                time.sleep(30)
    
    print("\n🎯 Todos los enlaces procesados!")

if __name__ == "__main__":
    main()
