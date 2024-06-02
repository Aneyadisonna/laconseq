def info_panel_closer(driver):
    """Closes the info panel.

    Args:
        driver: Selenium WebDriver instance.
    """

    driver.execute_script('document.querySelector("div.info-panel").style.display = "none";')

