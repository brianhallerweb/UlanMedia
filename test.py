import requests
import json
import sys
import os
import re

import pprint
pp=pprint.PrettyPrinter(indent=2)

def test():
    
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads.txt/ads.txt_list.txt', 'r') as file:
        domains = file.read().split("\n")

    bad_domains = ['http://123rarbg.com/ads.txt', 'http://12postsv.com/ads.txt', 'http://247buzzfeed.com/ads.txt', 'http://2sht2tllk2.com/ads.txt', 'http://aankhodekhi.today/ads.txt', 'http://akclip.com/ads.txt', 'http://algebra.com/ads.txt', 'http://allfreepop.info/ads.txt', 'http://allinposters.ga/ads.txt', 'http://allthenews.co.za/ads.txt', 'http://alltunesfun.info/ads.txt', 'http://amandotusalud.info/ads.txt', 'http://anihd.net/ads.txt', 'http://animehasu.com/ads.txt', 'http://animmex.bid/ads.txt', 'http://animmex.trade/ads.txt', 'http://animmex.webcam/ads.txt', 'http://anlamlisozlerim.com/ads.txt', 'http://aprendevariado.com/ads.txt', 'http://bailamvan.com/ads.txt', 'http://bakchodiband.com/ads.txt', 'http://balita.news/ads.txt', 'http://ballph.com/ads.txt', 'http://bantincapnhat.com/ads.txt', 'http://bestmegabox.info/ads.txt', 'http://bestpartychart.info/ads.txt', 'http://bestpopparty.info/ads.txt', 'http://bikiniactress.com/ads.txt', 'http://bingwallpaper.com/ads.txt', 'http://blackmatterz.com/ads.txt', 'http://blewaah.com/ads.txt', 'http://boxmp3best.info/ads.txt', 'http://celebrattee.com/ads.txt', 'http://centronoticiasdigital-nw.com/ads.txt', 'http://cfapost.com/ads.txt', 'http://chamngoncuocsong.com/ads.txt', 'http://chinadeep.info/ads.txt', 'http://chosenfiles.com/ads.txt', 'http://clck.mgid.com/ads.txt', 'http://cloudypk.com/ads.txt', 'http://collectionsetc.com/ads.txt', 'http://contigoaldia.com/ads.txt', 'http://coorms.net/ads.txt', 'http://crocko.com/ads.txt', 'http://cuoivuive.com/ads.txt', 'http://curiosavida.com/ads.txt', 'http://curiosidadtotal.net/ads.txt', 'http://dailybuzzportal.com/ads.txt', 'http://dailytrend.mx/ads.txt', 'http://dainikonlinevideo.com/ads.txt', 'http://de-news.net/ads.txt', 'http://deimportancia.com/ads.txt', 'http://delcamposoy.com/ads.txt', 'http://denunciasbarranquilla.com/ads.txt', 'http://deskgram.net/ads.txt', 'http://deskgram.org/ads.txt', 'http://despiertard.info/ads.txt', 'http://diariolaprimeraperu.com/ads.txt', 'http://digongnews.info/ads.txt', 'http://directfootbol.com/ads.txt', 'http://doisongxahoi.info/ads.txt', 'http://downloadyoutubehd.net/ads.txt', 'http://dramacafe.in/ads.txt', 'http://dstvguide.co.za/ads.txt', 'http://du30news.net/ads.txt', 'http://du30newsglobal.com/ads.txt', 'http://du30socialinfo.com/ads.txt', 'http://duniabaca.com/ads.txt', 'http://duterteawesome.info/ads.txt']
    
    good_domains = []
    for domain in domains:
        if domain in bad_domains:
            continue
        else:
            good_domains.append(domain)

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/ads.txt/reduced.json", "w") as file:
        json.dump(good_domains, file)

test()




