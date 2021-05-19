VERSION := 1.0

.PHONY: A couple of words

readme.txt:
	echo Version: $(VERSION) > readme.txt

readme_copy.txt: readme.txt
	cat readme.txt > readme_copy.txt

requisites.txt: A couple of words
	echo $^ > $@

A couple of words:
