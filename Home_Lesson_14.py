import requests
import json
import random


def sort_authors(item: dict):
    data = item["quoteAuthor"].split()[-1]
    return data


class Quotes:
    def __init__(self, quotes_count: int, filename: str, file_format: str = "json"):
        self.filename = f"{filename}.{file_format}"
        self.format = file_format
        self.quotes_count = quotes_count
        self.local_url = "http://api.forismatic.com/api/1.0/"
        self.local_quotes = []


    def get_quotes(self):
        for quote_num in range(self.quotes_count):
            self.local_quotes += [self.get_quote()]


    def get_quote(self):
        params = {
            "method": "getQuote",
            "format": self.format,
            "key": random.randint(0, 999999),
            "lang": "en"
        }
        response = requests.get(self.local_url, params=params)
        try:
            if response.json()["quoteAuthor"] == "":
                return self.get_quote()
            else:
                return response.json()
        except json.decoder.JSONDecodeError:
            return self.get_quote()


    def print_quotes(self):
        for quote in self.local_quotes:
            quote_text = quote["quoteText"]
            quote_author = quote["quoteAuthor"]
            print(f"\"{quote_text}\" - {quote_author}.")


    def save_quotes(self):
        with open(self.filename, "w") as json_file:
            json.dump(sorted(self.local_quotes, key=sort_authors), json_file)



number_of_citations = 10
file_name = "test"
file_format = "json"
test = Quotes(quotes_count=number_of_citations, filename=file_name, file_format=file_format)
test.get_quotes()
test.print_quotes()
test.save_quotes()



