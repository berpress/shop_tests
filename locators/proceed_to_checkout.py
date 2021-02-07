from selenium.webdriver.common.by import By


class ProceedToCheckoutLocators:
    SUMMARY_PROCEED_TO_CHECKOUT = (
        By.XPATH,
        '//a[@class="button btn btn-default standard-checkout button-medium"]',
    )
    ADDRESS_SELECT = (By.XPATH, '//select[@id="id_address_delivery"]')
    DELIVERY_ADDRESS_INFO = (By.XPATH, '//ul[@id="address_delivery"]')
    ADDRESS = (
        By.XPATH,
        '//button[@class="button btn btn-default button-medium"]',
    )
    CHECKBOX_SHIPPING = (By.XPATH, '//input[@type="checkbox"]')
    SHIPPING = (
        By.XPATH,
        '//button[@class="button btn btn-default standard-checkout ' 'button-medium"]',
    )
    PAYMENT_INFO = (By.XPATH, "//tbody")
    PAY_BY_BANK_WIRE = (By.XPATH, '//a[@class="bankwire"]')
    CONFIRM_MY_ORDER = (
        By.XPATH,
        '//button[@class="button btn btn-default button-medium"]',
    )
    MY_STORE_COMPLETE = (By.XPATH, '//div[@class="box"]')
