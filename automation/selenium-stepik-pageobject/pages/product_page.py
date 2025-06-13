from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def add_to_basket_product_and_solve(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
    
    def should_be_success_text(self):
        wait = WebDriverWait(self.browser, 10)
        title_element = wait.until(EC.visibility_of_element_located(ProductPageLocators.BOOK_TITILE))

        title_text = title_element.text

        success_element = wait.until(EC.visibility_of_element_located(ProductPageLocators.SUCCESS_TEXT_BUSKET))
        success_text = success_element.text

        assert title_text in success_text,  f"Название товара '{title_text}' не совпадает с сообщением '{success_text}'" #проверяем что текст добавления в коризину совпадает с тайтлом товара 

    def should_be_equal_price(self):
        wait = WebDriverWait(self.browser, 10)

        product_price = wait.until(EC.visibility_of_element_located(ProductPageLocators.PRICE_TITLE))
        product_text = product_price.text
        
        busket_price = wait.until(EC.visibility_of_element_located(ProductPageLocators.BUSKET_PRICE))
        busket_price_text = busket_price.text

        assert product_text == busket_price_text, f"Цена товара '{product_price}' не совпадает с уведомлением о цене в корзине '{busket_price_text}'"

