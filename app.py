from selenium import webdriver
from bs4 import BeautifulSoup
import time
import concurrent.futures

def scrape_page(page):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)

    url = f"https://www.dineout.co.in/chennai-restaurants?p={page}"
    driver.get(url)
    
    time.sleep(5)  

    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")
    restaurants = soup.find_all("a", class_="restnt-name ellipsis")

    restaurant_names = []
    for restaurant in restaurants:
        name = restaurant.get_text(strip=True)
        if name:
            restaurant_names.append(name)

    driver.quit()

    return restaurant_names

def main():
    with open("good_restaurant.txt", "w", encoding="utf-8") as f:
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            
            futures = [executor.submit(scrape_page, page) for page in range(1, 301)]
            
            
            for future in concurrent.futures.as_completed(futures):
                restaurant_names = future.result()
                for name in restaurant_names:
                    print("Found restaurant:", name)
                    f.write(name + "\n")

if __name__ == "__main__":
    main()
