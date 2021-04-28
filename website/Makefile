develop:
	docker run --rm --volume="$$PWD:/srv/jekyll" -p 4001:4000 -p 35729:35729 -it jekyll/jekyll:4.0 jekyll serve --livereload
	
dbuild:
	docker run --rm --volume="$$PWD:/srv/jekyll" -it jekyll/jekyll:4.0 jekyll build

#checklinks: 
#	bundle exec htmlproofer --alt_ignore="*" --empty_alt_ignore --allow-hash-href ./_0site

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve

checks:
	make build
	make checklinks

