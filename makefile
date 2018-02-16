default:

publish: build
	gsutil -m rsync -rdx '\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' build/  gs://jastrow.semitics-archive.org/

publish-no-images:
	rm -rf build/static/pages
	gsutil -m rsync -rx '\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' build/  gs://jastrow.semitics-archive.org/

build:
	python3 manage.py build