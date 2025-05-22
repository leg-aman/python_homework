from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

# Set up headless Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Target URL
url = "https://owasp.org/www-project-top-ten/"
top_10_vulnerabilities = []

try:
    driver.get(url)
    link_elements = driver.find_elements(
        By.XPATH,
        "//h2[@id='top-10-web-application-security-risks']/following-sibling::ul[1]/li/a"
    )

    print(f"Found {len(link_elements)} top 10 vulnerabilities:\n")

    for link in link_elements:
        title = link.text.strip()
        href = link.get_attribute("href")
        print(f"{title}: {href}")
        top_10_vulnerabilities.append({"title": title, "url": href})

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

# Save to CSV
df = pd.DataFrame(top_10_vulnerabilities)
df.to_csv("owasp_top_10.csv", index=False)
print("\nExtracted OWASP Top 10 Vulnerabilities:")
print(df)