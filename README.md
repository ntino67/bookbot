# Bookbot

Bookbot is a simple command-line tool for analyzing text files, such as books. It counts characters, words, and provides word frequency statistics, making it a helpful tool for anyone interested in basic text analysis.

## Features

- Counts the total number of words in a text file
- Counts the total number of characters
- Displays how many times each word appears, sorted by frequency
- Easy to use from the command line

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/YOUR-GITHUB-USERNAME/bookbot.git
    cd bookbot
    ```

2. Run Bookbot on your chosen book/text file:

    ```bash
    python main.py books/frankenstein.txt
    ```

    Replace `books/frankenstein.txt` with the path to your own text file.

3. View the output in your terminal!

## Example Output
```
--- Begin report of books/frankenstein.txt ---
88764 words found in the document
The 'e' character was found 45000 times
The 't' character was found 32000 times
...
The 'the' word appeared 5300 times
The 'and' word appeared 4900 times
...
--- End report ---
```


## Requirements

- Python 3.x

No additional dependencies required.

## License

MIT License
