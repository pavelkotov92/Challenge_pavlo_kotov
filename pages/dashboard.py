from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_selection_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_in_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    dev_team_contact_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    pass