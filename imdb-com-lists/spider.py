#!/usr/bin/env python

import scrapy


class IMDBListSpider(scrapy.Spider):
    name = "fellow-kids-spider"
    out = open("quotes", "w")

    @staticmethod
    def get_start_urls():
        with open("results") as f:
            return f.read().splitlines()
        return []

    start_urls = get_start_urls.__func__()

    def parse(self, response):
        quotes = response.xpath(
            '//div[@class="list-description"]//p[contains(text(),\'"\')]/text()'
        )

        if not quotes:
            return

        IMDBListSpider.out.write("\n".join(quotes.getall()))
