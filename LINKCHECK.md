# Installing for Link Checking


## Mac OS X Instructions
* Start with https://www.supertechcrew.com/jekyll-check-for-broken-links/
    * But, installation of nokogiri fails
    * I found a solution for Mac OS X at: https://www.reddit.com/r/ruby/comments/b0wtav/why_does_bundle_install_always_fail_to_install/ where they said to do this first:

```
_LIBS="$( xcrun --sdk macosx --show-sdk-path )/usr/include/"
bundle config build.nokogiri \
            "--use-system-libraries \
            --with-xml2-include=$_LIBS/libxml2 \
            --with-xslt-include=$_LIBS/libxslt \
            --with-exslt-include=$_LIBS/libexslt"
```
* Then, you can do `bundle install` and it will work
* But, then, it failed because I have moved `_site` to `_0site` to get it out of the middle of my editable files.
    * So, I had to change the commands in my Makefile to:
```
bundle exec htmlproofer ./_0site
```

## Linux Instructions
* Does someone want to try to follow the instructions below at https://www.supertechcrew.com/jekyll-check-for-broken-links/ and see if it works?  
    * May have to follow some instructions at https://www.reddit.com/r/ruby/comments/b0wtav/why_does_bundle_install_always_fail_to_install/ as well if it fails on the nokogiri stuff.

## Makefile Modifications for Link Checking
Once link checking is installed, here is the target for link checking in the Makefile:
```
checklinks: 
	bundle exec htmlproofer ./_0site
```

