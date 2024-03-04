# pyvigate
Pyvigate: A Python framework that combines headless browsing with LLMs that assists you in your data solutions, product tours, building RAG applications, web automation, functional testing, and many more!

[![Downloads](https://static.pepy.tech/badge/pyvigate/week)](https://pepy.tech/project/pyvigate)[![Downloads](https://static.pepy.tech/badge/pyvigate)](https://pepy.tech/project/pyvigate) [![Documentation](https://img.shields.io/badge/docs-readthedocs-blue)](https://pyvigate.readthedocs.io/en/latest/)


## Installation

Pyvigate can be installed using pip or directly from the source for the latest version.

### Using pip

`pip install pyvigate`

### Installing from source
```
git clone https://github.com/kindsmiles/pyvigate.git
cd pyvigate
pip install .
```

## Components

Pyvigate consists of several key components designed to work together seamlessly for web automation tasks.

### PlayWrightEngine:

PlayWright is one library we use for headless browsing and other browser automation tasks.

```
from pyvigate.core.engine import PlaywrightEngine

engine = PlaywrightEngine(headless=True)
await engine.start_browser()
```


### QueryEngine (with Azure OpenAI)
QueryEngine incorporates AI to dynamically detect web page elements,
significantly improving the efficiency and reliability of automated interactions.
It also can help the user navigate and also create their own applications, which involve curating data, creating RAG applications, product tour, functional testing, etc.

```
from pyvigate.ai.query_engine import QueryEngine

query_engine = QueryEngine(
    api_key=os.getenv("OPENAI_API_KEY"),
    azure_api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    azure_llm_deployment_name=os.getenv("LLM_DEPLOYMENT_NAME"),
    azure_embedding_deployment_name=os.getenv("EMBEDDING_DEPLOYMENT_NAME")
)

```

### Login

Some products can be accessed by the browser only after the login. We can do this either manually identifying the login selectors or letting the AI detect the UI elements where the credentials can be passed.The Login component utilizes QueryEngine to intelligently identify login forms and fields, streamlining the login process.

```
from pyvigate.core.login import Login

login = Login(query_engine)
await login.perform_login(engine.page, "https://example.com/login", "username", "password")
```


### Scraping

With Scraping, Pyvigate offers powerful data extraction capabilities, enabling the collection of content from web pages post-login or navigation.

```
from pyvigate.services.scraping import Scraping

scraping = Scraping(engine.page, data_dir="data")
content = await scraping.extract_data_from_page()
print("Scraped content:", content)
```


### Caching

The Caching component allows for the local storage of web page content, facilitating offline analysis and reducing bandwidth usage.
```
from pyvigate.services.caching import Caching

caching = Caching(cache_dir="html_cache")
await caching.cache_page_content(engine.page, "https://example.com/page")
```


### Full Example

Bringing it all together, here's how you can use Pyvigate to login, scrape content, and cache it:


```
import asyncio
from dotenv import load_dotenv
from pyvigate.core.engine import PlaywrightEngine
from pyvigate.core.login import Login
from pyvigate.services.scraping import Scraping
from pyvigate.services.caching import Caching
from pyvigate.ai.query_engine import QueryEngine
import os

load_dotenv()

async def login_and_scrape():
    engine = PlaywrightEngine(headless=True)
    await engine.start_browser()

    query_engine = QueryEngine(api_key=os.getenv("OPENAI_API_KEY"))
    login = Login(query_engine)
    await login.perform_login(engine.page, "https://example.com/login", os.getenv("USERNAME"), os.getenv("PASSWORD"))

    scraping = Scraping(engine.page, data_dir="data")
    content = await scraping.extract_data_from_page()
    print("Scraped content:", content)

    caching = Caching(cache_dir="html_cache")
    await caching.cache_page_content(engine.page, "https://example.com/dashboard")

    await engine.stop_browser()

if __name__ == "__main__":
    asyncio.run(login_and_scrape())
```

## Donations
We are looking to cover some of our API costs, so we accept any donations that you can make:

[![Sponsor me on Buy Me a Coffee](https://cdn.buymeacoffee.com/buttons/default-orange.png)](https://www.buymeacoffee.com/abhijithneilabr)
