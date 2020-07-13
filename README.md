# GoogleScriptTrend
<h2>How to run:</h2>

```shell
$ python3 script.py -h
usage: script.py [-h] [-a A] [-b B] [-c C] [-d D] [-e E] [--geo GEO]
                 [--timeframe TIMEFRAME] [--cat CAT] [--gprop GPROP]

optional arguments:
  -h, --help            show this help message and exit
  -a A                  Primeiro valor de pesquisa
  -b B                  Segundo valor de pesquisa
  -c C                  Terceiro valor de pesquisa
  -d D                  Quarto valor de pesquisa
  -e E                  Quinto valor de pesquisa
  --geo GEO, -g GEO     Área geográfica
  --timeframe TIMEFRAME, -time TIMEFRAME
                        Intervalo temporal
  --cat CAT, -k CAT     Categoria
  --gprop GPROP, -gp GPROP
                        Serviço do google a fazer a pesquisa

```

## Installation

- Clone repo 
- Initialize libraries
- Add email on /Configuration/emailData.py

### Clone repo

> Clone this repo to your local machine 

```shell
$ git clone git@github.com:alkimo/GoogleScriptTrend.git
```

### Initialize libraries

> Initialize all libraries with pip install on requirements.txt

```shell
$ cd GoogleScriptTrend
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
```

### Add Email

> Add email configured with the proper google drive permissions 

![GIF](https://i.ibb.co/B3dQ1PH/ezgif-com-video-to-gif-1.gif)

### Run test

> Example: Search for COVID, VACCINE and TRUMP on America
```shell
# First you run the virtual env
$ source /env/bin/activate
# Now you run the script
(env) $ python3 script.py -a "COVID" -b "VACCINE" -c "TRUMP" -g "US"
```