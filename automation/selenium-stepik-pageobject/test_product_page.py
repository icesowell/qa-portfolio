from pages.product_page import ProductPage



def  test_guest_can_add_product_to_basket(browser):
    product_link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

    product_page = ProductPage(browser, product_link)

    product_page.open()

    product_page.add_to_basket_product_and_solve()
    
    product_page.should_be_success_text()
    product_page.should_be_equal_price()
    