# How to regenerate web site

Get both Markdown source and previously generated html:
```
git clone https://github.com/ivannamik/ivannamik.github.io --branch master master
git clone https://github.com/ivannamik/ivannamik.github.io --branch source source
```

Prepare an environment:
```
virtualenv env
source env/bin/activate
pip install -r source/requirements.txt
```

Run Pelican generator:
```
cd source
pelican --output ../master
```

