from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Oi, eu sou um bot feito em Python!"
        self.grupos = ["Gabi"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def enviarmensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(12)
        for user in self.grupos:
            grupo = self.driver.find_element_by_xpath('//span[@title="{user}"]')
            time.sleep(3)
            grupo.click()
            texto = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            texto.click()
            texto.send_keys(self.mensagem)
            botao = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao.click()
            time.sleep(3)


bot = WhatsappBot()
bot.enviarmensagens()
