import pytest

from final_project.components.bonus_page import BonusPage
from final_project.components.promocode import Promocode
from final_project.components.slider import Slider
from final_project.components.product_page import ProductPage
from final_project.components.cart_icon import CartIcon
from final_project.components.menu_page import MenuPage
from final_project.components.cart_page import CartPage
from final_project.components.place_order_page import PlaceOrderPage
from final_project.components.my_account_page import MyAccountPage
from final_project.data.invalid_data import InvalidData
from final_project.data.valid_data import ValidData


class BaseTest:

    valid_data: ValidData
    invalid_data: InvalidData

    slider: Slider
    product_page: ProductPage
    cart_icon: CartIcon
    menu_page: MenuPage
    cart_page: CartPage
    place_order_page: PlaceOrderPage
    my_account_page: MyAccountPage
    promocode: Promocode
    bonus_page: BonusPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.valid_data = ValidData()
        request.cls.invalid_data = InvalidData()
        request.cls.slider = Slider(driver)
        request.cls.product_page = ProductPage(driver)
        request.cls.cart_icon = CartIcon(driver)
        request.cls.menu_page = MenuPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.place_order_page = PlaceOrderPage(driver)
        request.cls.my_account_page = MyAccountPage(driver)
        request.cls.promocode = Promocode(driver)
        request.cls.bonus_page = BonusPage(driver)
