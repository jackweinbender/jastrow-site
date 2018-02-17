default:

publish: build
	gsutil -m rsync -rdx '\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' build/  gs://jastrow.semitics-archive.org/

publish-with-images:
	gsutil -m rsync -rdx '\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' build/  gs://jastrow.semitics-archive.org/
	gsutil -m rsync -rdx '\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' static/dictionary/pages  gs://jastrow.semitics-archive.org/static/pages

build:
	python3 manage.py build --skip-static
	cp static/dictionary/styles.css build/static/dictionary/styles.css
	cp static/dictionary/script.js build/static/dictionary/script.js