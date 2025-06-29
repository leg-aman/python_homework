from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
robots_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
results = []
try:
    driver.get(robots_url)
    
    # li = driver.find_elements(By.CSS_SELECTOR, ".cp-search-results-item")
    li = driver.find_elements(By.CSS_SELECTOR, ".results-list li")
    print(f"Number of li elements: {len(li)}")
    for item in li:
        try:
            title = item.find_element(By.CSS_SELECTOR, ".title-content").text
            author = item.find_element(By.CSS_SELECTOR, ".author-link").text
            year = item.find_element(By.CSS_SELECTOR, ".display-info-primary").text
            if len(author) > 1:
                #  If you find more than one author, you want to join the author names with a semicolon ; between each.  
                author = "; ".join([a.text for a in item.find_elements(By.CSS_SELECTOR, ".author-link")])
            else:
                author = item.find_element(By.CSS_SELECTOR, ".author-link").text
            results.append({
                "title": title,
                "author": author,
                "Format-Year": year
            })
            # print(f"Title: {title}, Author: {author}, Format-Year : {year}")
        except Exception as e:
            print(f"Error occurred while processing an item: {e}")
except Exception as e:
    print(f"Error occurred while accessing the website: {e}")
    print(f"Exception: {type(e).__name__}{e}")
finally:
    driver.quit()

df = pd.DataFrame(results)
print(df)
# Save the DataFrame to a CSV file
df.to_csv("books.csv", index=False)
# Save the DataFrame to a JSON file
df.to_json("books.json", orient="records", lines=True)