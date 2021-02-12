develop:
	docker run --rm --volume="$$PWD:/srv/jekyll" -p 4000:4000 -p 35729:35729 -it jekyll/jekyll:4.0 jekyll serve --livereload
	
dbuild:
	docker run --rm --volume="$$PWD:/srv/jekyll" -it jekyll/jekyll:4.0 jekyll build

checklinks: 
	bundle exec htmlproofer --alt_ignore="*" --empty_alt_ignore --allow-hash-href ./_0site

serve:
	bundle exec jekyll serve

build:
	bundle exec jekyll build

dist: 
	bundle exec jekyll build
	cd _0site; scp -r * ssh.et.byu.edu:groups/immersewiki/www

checks:
	make build
	make checklinks
