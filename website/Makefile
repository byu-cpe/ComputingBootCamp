develop:
	docker run --rm --volume="$$PWD:/srv/jekyll" -p 4000:4000 -p 35729:35729 -it jekyll/jekyll:4.0 jekyll serve --livereload
	
dbuild:
	docker run --rm --volume="$$PWD:/srv/jekyll" -it jekyll/jekyll:4.0 jekyll build

check_links: build
	bundle exec htmlproofer --empty_alt_ignore --url-swap "^\/ComputingBootCamp:" ./_0site

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve


