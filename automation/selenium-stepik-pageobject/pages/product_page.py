from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket_product(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    
    def should_be_success_text(self):

        title_element = self.wait_for_element(ProductPageLocators.BOOK_TITILE)
        title_text = title_element.text

        success_element = self.wait_for_element(ProductPageLocators.SUCCESS_TEXT_BUSKET)
        success_text = success_element.text

        assert title_text == success_text,  f"Название товара '{title_text}' не совпадает с сообщением '{success_text}'" #проверяем что текст добавления в коризину совпадает с тайтлом товара 

    def should_be_equal_price(self):

        product_price = self.wait_for_element(ProductPageLocators.PRICE_TITLE)
        product_text = product_price.text
        
        busket_price = self.wait_for_element(ProductPageLocators.BUSKET_PRICE)
        busket_price_text = busket_price.text

        assert product_text == busket_price_text, f"Цена товара '{product_price}' не совпадает с уведомлением о цене в корзине '{busket_price_text}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_TEXT_BUSKET), "Success message is presented, but should not be"

    def should_be_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_TEXT_BUSKET), "Message isn't disappear, but should be"

    
