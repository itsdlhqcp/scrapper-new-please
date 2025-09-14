# News Scraper

A simple Python news article scraper that extracts article information from web URLs using the `news-please` library.

## Features

- Extracts article titles, authors, publication dates, and main text
- Handles multiple URLs simultaneously
- Clean, formatted output with article summaries
- Error handling for failed extractions

## Prerequisites

- Python 3.6 or higher
- pip package manager

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install newspaper4k
```

**Note:** The original installation command in the code comments (`pip install newspaper4k`) is incorrect. This project uses `news-please`, not `newspaper4k`.

## Usage

1. Run the scraper:

```bash
python scraper.py
```

The script will extract information from the predefined URLs and display:
- Article URL
- Title
- Authors
- Publication date
- First 200 characters of the main text

## Code Structure

```
├── scraper.py          # Main scraper script
└── README.md          # This file
```

### scraper.py

The main script contains:
- `main()` function that processes a list of URLs
- URL list with sample news articles
- Article extraction and display logic
- Error handling for failed extractions

## Sample URLs

The script currently processes these URLs:
- BBC News article
- Inshorts news homepage

## Customization

### Adding New URLs

To scrape different articles, modify the `urls` list in the `main()` function:

```python
urls = [
    'https://example-news-site.com/article1',
    'https://another-news-site.com/article2',
    # Add more URLs here
]
```

### Adjusting Text Preview

To change the preview text length, modify the slice in the print statement:

```python
# Change 200 to desired character count
print(f"Text (first 200 chars): {article.maintext[:200]}...")
```

## Error Handling

The script includes basic error handling:
- If an article cannot be extracted, it displays an error message
- Processing continues for remaining URLs even if some fail

## Dependencies

- **news-please**: A news crawler that extracts structured information from news articles

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure `news-please` is installed correctly
   ```bash
   pip install news-please
   ```

2. **Network Issues**: Some websites may block automated requests. Try:
   - Different URLs
   - Adding delays between requests
   - Using different user agents

3. **Extraction Failures**: Some websites may not be compatible with the library's extraction methods

### Syntax Error in Original Code

**Important**: There's a syntax error in the original code. The line:
```python
if **name** == "__main__":
```

Should be:
```python
if __name__ == "__main__":
```

Make sure to fix this before running the script.

## Output Format

```
URL: https://example.com/article
Title: Article Title Here
Authors: ['Author Name']
Publish Date: 2024-01-01 12:00:00
Text (first 200 chars): This is the beginning of the article text that provides a preview of the content...
------------------------------
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Future Enhancements

Potential improvements for this scraper:
- Save articles to file (JSON, CSV, etc.)
- Add command-line arguments for custom URLs
- Implement rate limiting for respectful scraping
- Add support for RSS feeds
- Create a web interface
- Add data cleaning and preprocessing options
