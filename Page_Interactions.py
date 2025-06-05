from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DropdownElement:
    def __init__(self, driver):
        self.driver = driver

    def change_theme_to_material_main(self):
        change_theme_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[3]/div[3]/button/div/div[2]")
        change_theme_button.click()

        material_main_option = self.driver.find_element(By.XPATH, "//div[@style='background-color: rgb(101, 85, 143); z-index: 2;']")
        material_main_option.click()

class ContextMenu:
    def __init__(self, driver):
        self.driver = driver

    def apply_underline_style(self):
        
        iframe = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/iframe")
        self.driver.switch_to.frame(iframe)

        target_element = self.driver.find_element(By.XPATH, "/html/body/my-app/div")
        ActionChains(self.driver).context_click(target_element).perform()

        menu_style_option = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/ul/li[5]")
        ActionChains(self.driver).move_to_element(menu_style_option).perform()

        submenu_underline_option = self.driver.find_element(By.XPATH, "//li[@aria-label='Underline']")
        submenu_underline_option.click()
