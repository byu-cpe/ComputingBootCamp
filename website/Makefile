develop:
	docker run --rm --volume="$$PWD:/srv/jekyll" -p 4000:4000 -p 35729:35729 -it jekyll/jekyll:4.0 jekyll serve --livereload
	
dbuild:
	docker run --rm --volume="$$PWD:/srv/jekyll" -it jekyll/jekyll:4.0 jekyll build

check_links: build
	bundle exec htmlproofer --allow_missing_href --ignore_missing_alt --swap_urls "^\/ComputingBootCamp:" --ignore-status-codes "0,301,302,403,429,500", --enforce_https false ./_site

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve


