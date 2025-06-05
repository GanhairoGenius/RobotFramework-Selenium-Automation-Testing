from SeleniumLibrary.base import LibraryComponent, keyword
from Page_Interactions import DropdownElement, ContextMenu

class CustomKeywords(LibraryComponent):
    
    @keyword
    def change_theme(self):
        dropdown = DropdownElement(self.seleniumlib.driver)
        dropdown.change_theme_to_material_main()

    @keyword
    def apply_underline(self):
        context_menu = ContextMenu(self.seleniumlib.driver)
        context_menu.apply_underline_style()
