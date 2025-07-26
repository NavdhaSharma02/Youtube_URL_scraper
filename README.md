# Youtube_URL_scraper
This project collects podcast video URLs from YouTube using **YouTube Data API v3** via Google Cloud.

It also includes a script to remove duplicate URLs, making the final dataset clean and usable for ML/data tasks.

The original project was done on google colab.
---

## Project Motivation

While working on a podcast discovery project, I needed to collect video links from multiple podcast channels on YouTube and saving them onto a csv file.

Challenges I tackled:
- The 10,000 units/day API quota limit.
- Duplicate entries from overlapping results.
- The need to automate and clean the scraping pipeline.

 Although the final dataset is not included, this repo contains everything needed to regenerate it.

---

## Tools & Technologies

- **Python**
- **YouTube Data API v3** (Google Cloud)
- **Custom duplicate remover**
- **dotenv** for API key management



