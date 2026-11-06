# VADER Sentiment Analysis

## 1. Overview

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a rule-based sentiment analysis tool used to identify the emotional tone of text.

In this project, VADER analyzes news article content and classifies each article as positive, negative, or neutral.

## 2. Python Library

The project uses:

`vaderSentiment`

Install it using:

```powershell
pip install vaderSentiment
```

## 3. Sentiment Analysis Process

1. Retrieve an article from the GNews API.
2. Extract its title, description, and available content.
3. Prepare the text for analysis.
4. Pass the text to the VADER sentiment analyzer.
5. Retrieve the compound sentiment score.
6. Assign a sentiment label based on the score.

## 4. Sentiment Classification

| Compound Score | Sentiment |
|---|---|
| Greater than or equal to 0.05 | Positive |
| Less than or equal to -0.05 | Negative |
| Between -0.05 and 0.05 | Neutral |

## 5. Compound Score

The compound score is a normalized value ranging from -1.0 to +1.0.

- -1.0 represents the most negative score.
- 0.0 represents a neutral score.
- +1.0 represents the most positive score.

## 6. Empty Text Handling

If an article has no usable text, the project assigns:

- Sentiment: `neutral`
- Sentiment score: `0.0`

This prevents missing article content from causing unnecessary processing errors.

## 7. Database Integration

The sentiment label and compound score are stored alongside the article information in PostgreSQL.

This allows the dashboard to display and analyze news sentiment.

## 8. Result

VADER transforms collected news text into structured sentiment information that can be stored, queried, and displayed in the dashboard.