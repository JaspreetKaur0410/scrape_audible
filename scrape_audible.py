from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time

# Initialize Chrome options
options = Options()
options.headless = False
options.add_experimental_option("detach", True)

# Website URL
website = "https://www.audible.com/search"

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.get(website)

pagination=driver.find_element(By.XPATH,'//ul[contains(@class,"pagingElements")]')
pages=pagination.find_elements(By.TAG_NAME,'li')
last_page=int(pages[-2].text)
current_page=1

# Initialize lists to store book details
titles = []
authors = []
narrators = []
lengths = []

# Define the number of pages to scrape
pages_to_scrape = last_page
current_page = 1

while current_page <= pages_to_scrape:
    time.sleep(5)  # Wait for the page to load completely

    # Get all books on the current page
    list_of_books = driver.find_elements(By.XPATH, "//li[contains(@class, 'productListItem')]")

    for book in list_of_books:
        try:
            title = book.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]/a").text
            titles.append(title)
        except:
            titles.append("N/A")

        try:
            author = book.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]//a").text
            authors.append(author)
        except:
            authors.append("N/A")

        try:
            narrator = book.find_element(By.XPATH, ".//li[contains(@class, 'narratorLabel')]//a").text
            narrators.append(narrator)
        except:
            narrators.append("N/A")

        try:
            length = book.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text
            lengths.append(length)
        except:
            lengths.append("N/A")

    # Move to the next page
    try:
        next_button = driver.find_element(By.XPATH, '//span[contains(@class,"nextButton")]/a')
        next_button.click()
        current_page += 1
    except:
        print("No more pages available or an error occurred.")
        break

# Close the browser
driver.quit()

# Save data to CSV
df_books = pd.DataFrame({
    'Title': titles,
    'Author': authors,
    'Narrator': narrators,
    'Length': lengths
})

df_books.to_csv('./data_exported/books_pagination.csv', index=False)
print("Data exported to './data_exported/books_pagination.csv'")
