default:

publish:
	@ echo "Checking HTML..."
	@ gsutil -m rsync -rdx 'static/dictionary/pages/*|\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' build/  gs://jastrow.semitics-archive.org/
	@ echo "Checking CSS and JS..."
	@ gsutil -m rsync -rdx 'pages/*|\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' static/dictionary/  gs://jastrow.semitics-archive.org/static/dictionary/
	@ echo "Checking Images..."
	@ gsutil -m rsync -rdx '\..*|.*/\.[^/]*$|.*/\..*/.*$|_.*' static/dictionary/pages/  gs://jastrow.semitics-archive.org/static/dictionary/pages
	@ echo "Done."

build:
	@ echo "Building  Site..."
	@ python3 manage.py build --skip-static
	@ cp static/dictionary/styles.css build/static/dictionary.styles.css
	@ cp static/dictionary/scripts.js build/static/dictionary.scripts.js

build-css:
	@echo "Pushing CSS..."
	gsutil cp static/dictionary/styles.css gs://jastrow.semitics-archive.org/static/dictionary/styles.css