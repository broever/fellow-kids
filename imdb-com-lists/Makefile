quotes: results spider.py
	./get-quotes

results: queries
	./get-lists

.PHONY: clean
clean:
	rm -f results
	rm -f quotes

.PHONY: all
all: quotes
