** Settings ***
Library     SeleniumLibrary
Resource   Variables.robot

*** Test Case ***
Open Browser And Navigate
    Open Browser    ${URL}    ${BROWSER}    headless=${HEADLESS}
    Maximize Browser Window
    Set Selenium Speed    2s

Accepting Cookies
    Run Keyword And Ignore Error    Click Element    xpath=/html/body/div[2]/div[2]/div/div/div[2]/div/div/button[2]

Scrolling Down Webpage
    Wait Until Element Is Visible   xpath=/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/h1/a   timeout=10s
    Scroll Element Into View        xpath=/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/h1/a
    Execute Javascript              window.scrollTo(0,500)

Change Theme To Material_Main
    Wait Until Element Is Enabled   xpath=/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[3]/div[3]/button/div/div[2]  timeout=20s
    Click Element                   xpath=/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[3]/div[3]/button/div/div[2]
    Click Element                   xpath=//div[@style="background-color: rgb(101, 85, 143); z-index: 2;"]

Apply Underline Style
    Wait Until Element Is Visible   xpath=/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/iframe   timeout=29s
    Select Frame                    xpath=/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/iframe
    Open Context Menu               xpath=/html/body/my-app/div
    Wait Until Element Is Visible   xpath=//div[contains(@class, 'k-animation-container-shown')]   timeout=10s
    Mouse Over                      xpath=/html/body/div[1]/div/div/div/ul/li[5]
    Wait Until Element Is Visible   xpath=//li[@aria-label='Underline']   timeout=10s
    Click Element                   xpath=//li[@aria-label='Underline']

Capture Screenshot
    Capture Page Screenshot         ${SREENSHOT_PATH}
