# GNews API Integration

## 1. Overview

GNews API is used to collect technology-related news articles from different news sources.

The application retrieves news in JSON format and passes the articles to the processing pipeline.

## 2. API Provider

- Service: GNews API
- API documentation: https://gnews.io/docs/v4
- Endpoint: `/api/v4/search`
- Search query: `technology`
- Language: English
- Maximum articles per request: 10

## 3. API Configuration

The API key is stored in an environment variable:

`GNEWS_API_KEY`

The key must never be hardcoded or committed to GitHub.

## 4. Request Parameters

The application uses the following parameters:

| Parameter | Value | Purpose |
|---|---|---|
| q | technology | Search for technology news |
| lang | en | Retrieve English articles |
| max | 10 | Limit the number of results |

## 5. News Data

The API response provides article information such as:

- Article ID
- Title
- Description
- Content
- URL
- Image
- Publication date
- Language
- Source name
- Source URL
- Source country

## 6. Data Processing

After retrieving the response:

1. Check whether the API request succeeded.
2. Read the returned JSON data.
3. Extract the article information.
4. Pass the articles to the next pipeline stage.
5. Preserve the raw response for S3 storage.

## 7. Error Handling

The application should handle common API errors, including:

- Invalid API key
- HTTP request failures
- Network connection problems
- Empty API responses
- API rate limits

API credentials must remain private when troubleshooting.

## 8. Result

GNews API provides the news articles required for sentiment analysis and storage in the AWS data pipeline.