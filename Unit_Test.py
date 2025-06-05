import pytest
from Page_Interactions import ContextMenu, DropdownElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_change_theme_to_material_main(mocker):
    
    driver = mocker.Mock()
    change_theme_button = mocker.Mock()
    material_main_option = mocker.Mock()

    driver.find_element.side_effect = [change_theme_button, material_main_option]

    dropdown = DropdownElement(driver)
    dropdown.change_theme_to_material_main()

    change_theme_button.click.assert_called_once()
    material_main_option.click.assert_called_once()

def test_apply_underline_style(mocker):
    driver = mocker.Mock()
    iframe = mocker.Mock()
    target_element = mocker.Mock()
    menu_style_option = mocker.Mock()
    submenu_underline_option = mocker.Mock()

    mock_chain = mocker.Mock()
    mock_chain.context_click.return_value = mock_chain
    mock_chain.move_to_element.return_value = mock_chain
    mock_chain.perform.return_value = None

    mocker.patch('Page_Interactions.ActionChains', return_value=mock_chain)

    driver.find_element.side_effect = [
        iframe,            
        target_element,    
        menu_style_option,   
        submenu_underline_option   
    ]

    context = ContextMenu(driver)
    context.apply_underline_style()

    submenu_underline_option.click.assert_called_once()
