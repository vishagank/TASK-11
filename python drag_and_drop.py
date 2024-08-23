from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get('https://jqueryui.com/droppable/')

# Switch to the iframe that contains the drag-and-drop elements
iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)

# Locate the draggable element (the white rectangle)
draggable = driver.find_element(By.ID, "draggable")

# Locate the droppable element (the yellow rectangle)
droppable = driver.find_element(By.ID, "droppable")

# Perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()


time.sleep(3)


driver.quit()
