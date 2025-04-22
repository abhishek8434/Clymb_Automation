import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from collections import Counter
import openai
from openai import OpenAI
import os

# === CONFIG ===
openai_api_key ="Enter your OpenAI API key here"
DUMMY_KEYWORDS = ['lorem ipsum', 'dummy']
# DUMMY_KEYWORDS = ['lorem ipsum', 'dummy', 'test', 'abc', 'xyz', '123', 'sample', 'testing', 'placeholder']

URLS = [
    "https://dev.creativerunr.com/se/ios-app-development-services/",
    "https://dev.creativerunr.com/se/flutter-app-development-company/",
    "https://dev.creativerunr.com/se/android-app-development-services/",
    "https://dev.creativerunr.com/se/react-native-app-development-services/",
    "https://dev.creativerunr.com/se/mern-stack-development-services/",
    "https://dev.creativerunr.com/se/search-engine-optimization-services/",
    "https://dev.creativerunr.com/se/social-media-marketing-services/",
    "https://dev.creativerunr.com/se/content-marketing-services/",
    "https://dev.creativerunr.com/se/pay-per-click-advertising/",
    "https://dev.creativerunr.com/se/app-store-optimization-services/",
    "https://dev.creativerunr.com/se/email-marketing-services/",
    "https://dev.creativerunr.com/se/ecommerce-website-development-services/",
    "https://dev.creativerunr.com/se/ecommerce-app-development-company/",
    "https://dev.creativerunr.com/se/headless-commerce-development-services/",
    "https://dev.creativerunr.com/se/shopify-development-services/",
    "https://dev.creativerunr.com/se/magento-development-services/",
    "https://dev.creativerunr.com/se/wordpress-development-services/",
    "https://dev.creativerunr.com/se/woo-commerce-development-services/",
    "https://dev.creativerunr.com/se/migration-services-provider-company/",
    "https://dev.creativerunr.com/se/nop-commerce-development-services/",
    "https://dev.creativerunr.com/se/iot-solution-development-company/",
    "https://dev.creativerunr.com/se/ai-solution-development/",
    "https://dev.creativerunr.com/se/machin-learning-development-services/",
    "https://dev.creativerunr.com/se/chatbot-development-services/",
    "https://dev.creativerunr.com/se/nlp-software-development-services/",
    "https://dev.creativerunr.com/se/marketing-collateral-design-services/",
    "https://dev.creativerunr.com/se/responsive-website-design-company/",
    "https://dev.creativerunr.com/se/mobile-ui-ux-design-services/",
    "https://dev.creativerunr.com/se/bootstrap-development-services/",
    "https://dev.creativerunr.com/se/headless-cms/",
    "https://dev.creativerunr.com/se/web-maintainence-and-support/",
    "https://dev.creativerunr.com/se/webflow-development-services/",
    "https://dev.creativerunr.com/se/custom-cms-website-development-company/",
    "https://dev.creativerunr.com/se/theme-based-website-development/"
]

# === Setup OpenAI Client ===
client = OpenAI(api_key=openai_api_key)

# === Setup Selenium Driver ===
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# === Helper to count dummy keywords ===
def count_dummy_keywords(text):
    counter = Counter()
    for keyword in DUMMY_KEYWORDS:
        count = text.lower().count(keyword)
        if count > 0:
            counter[keyword] = count
    return counter

# === GPT Analysis ===
def gpt_check(content):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Detect any signs of placeholder or dummy content in the following web content."},
                {"role": "user", "content": content[:3000]}  # truncate for safety
            ],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI error: {e}"

# === Main Check Loop ===
for url in URLS:
    print(f"\n🔗 Checking: {url}")
    try:
        driver.get(url)
        time.sleep(3)
        text = driver.find_element(By.TAG_NAME, "body").text

        dummy_counts = count_dummy_keywords(text)
        total = sum(dummy_counts.values())

        if total > 0:
            print(f"❌ Found {total} dummy data items:")
            for k, v in dummy_counts.items():
                print(f"   - {k}: {v}")
        else:
            print("✅ No rule-based dummy keywords found.")

        print("🧠 GPT Feedback:")
        print(gpt_check(text))

    except Exception as e:
        print(f"⚠️ Error checking {url}: {e}")

driver.quit()
