serve: install
	bundle exec jekyll serve --livereload

install:
	bundle install

build: install
	bundle exec jekyll build

check_links: build
	# FreeRTOS section of --swap_urls is used to check FreeRTOS base links, 
	# but not the # (hash) sections, since those are handled dynamically after the website has loaded.
	bundle exec htmlproofer --allow_missing_href true --ignore_missing_alt true --swap_urls '^\/ComputingBootCamp:,freertos\.org([^\x23]*)\x23.*:https://www.freertos.org\1' --ignore-status-codes "0,301,302,403,429,500,503" --enforce_https false ./_site



