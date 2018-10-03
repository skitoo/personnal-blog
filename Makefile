
build:
	docker-compose run --rm blog pelican content -o docs/ -s pelicanconf.py && echo "www.skitoo.net" >> docs/CNAME
