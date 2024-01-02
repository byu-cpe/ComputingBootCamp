serve: install
	bundle exec jekyll serve --livereload

install:
	bundle install

build: install
	bundle exec jekyll build

check_links: build
	bundle exec htmlproofer --allow_missing_href true --ignore_missing_alt true --swap_urls "^\/ComputingBootCamp:" --ignore-status-codes "0,301,302,403,429,500,503", --enforce_https false ./_site



