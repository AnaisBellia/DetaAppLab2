from flask import Flask, Response, redirect, Request
import sys
import logging

app = Flask(__name__)

@app.route('/', methods=["GET"])

def hello_world():
    prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250432838-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' UA-250432838-1');
</script>
 """
    return prefix_google + "LAB 2 "

### Prints a log on python
logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
#log.warning('I print to stderr by default')
print('hello world in python console from Anaïs Bellia')


### deta login, deta deploy in terminal, then lab2micro in deta / inspecter in outil de dev
@app.route('/Logger',methods=['GET'])
def logger():
    page="""
    <script> console.log('message de la console') </script>"""
    return "voir console" + page

# 3. Activate logger on Deta
# aller dans lab2_micro, visor, et rentrer dans console deta visor enable puis deta visor open
# dans deta/visor le log s'affichera dans la console