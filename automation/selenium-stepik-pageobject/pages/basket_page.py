from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_text_basket(self):
        
        basket_notice = self.wait_for_element(BasketPageLocators.EMPTY_BASKET_NOTICE)
        basket_empty_text = basket_notice.text
        assert "Ваша корзина пуста" in basket_empty_text 
    
    def should_be_not_include_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_COUNTER_ITEMS)