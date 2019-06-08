"<!DOCTYPE html>\n<html>\n<head>\n    <meta charset=\"utf-8\">\n\t<meta name=\"viewport\" content=\"width=device-width\">\n    <title>NWC3L - New WarCraft 3 League</title>\n\t<link rel=\"icon\" type=\"image/x-icon\" href=\"/favicon.ico\">\n\t<link rel=\"stylesheet\" href=\"//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css\">\n\t<link rel=\"stylesheet\" href=\"//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css\">\n\t<script type=\"text/javascript\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\" ></script>\n<link type=\"text/css\" href=\"/css/tooltipster.bundle.min.css\" rel=\"stylesheet\">\n<link type=\"text/css\" href=\"/css/plugins/tooltipster/sideTip/themes/tooltipster-sideTip-borderless.min.css\" rel=\"stylesheet\">\n<script type=\"text/javascript\" src=\"/js/tooltipster.bundle.min.js\" defer></script>\n<script type=\"text/javascript\" src=\"/js/ffw.js\" defer></script>\n<script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js\" defer></script>\n<script type=\"text/javascript\" src=\"/js/fancybox/jquery.fancybox.pack.js\" defer></script>\n<link type=\"text/css\" href=\"/js/fancybox/jquery.fancybox.css\" rel=\"stylesheet\">\n<script type=\"text/javascript\">$(document).ready(function(){\n\n\t\t$(\".fancybox\").fancybox({\n\t\t\thelpers: {\n\t\t\t\toverlay: {\n\t\t\t\t\tlocked: false\n\t\t\t\t}\n\t\t\t},\n\t\t});\n\t\t$(\".fancybox-ajax\").fancybox({\n\t\t\ttype: \"iframe\",\n\t\t\thelpers: {\n\t\t\t\toverlay: {\n\t\t\t\t\tlocked: false\n\t\t\t\t}\n\t\t\t},\n\t\t});\n\t\n\t$('.fancybox-w-content').click(function(ev){\n\t    ev.preventDefault();\n\t    var $link = $(this);\n\t    $.fancybox({\n\t\t    'title': $link.attr('data-name'),\n\t\t    'content': '<div style=\"text-align:center\"><img src=\"'+$link.attr('href')+'\"></div><br><div style=\"max-width:400px\">'+$link.next().html()+'</div>',\n\t\t    helpers: {\n\t\t\t   overlay: {\n\t\t\t      locked: false\n\t\t\t   }\n\t\t\t}\n\t\t});\n\t});\n\t});\n</script>\n\t<script src=\"//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js\"></script>\n    <link href=\"/css/stylesheet.css\" rel=\"stylesheet\">\n</head>\n<body>\n\t<!-- Yandex.Metrika counter -->\n\t<script type=\"text/javascript\">\n\t\t(function (d, w, c) {\n\t\t\t(w[c] = w[c] || []).push(function() {\n\t\t\t\ttry {\n\t\t\t\t\tw.yaCounter26161809 = new Ya.Metrika({id:26161809,\n\t\t\t\t\t\twebvisor:true,\n\t\t\t\t\t\tclickmap:true,\n\t\t\t\t\t\ttrackLinks:true,\n                    accurateTrackBounce:true});\n\t\t\t\t} catch(e) { }\n\t\t\t});\n\t\t\t\n\t\t\tvar n = d.getElementsByTagName(\"script\")[0],\n\t\t\ts = d.createElement(\"script\"),\n\t\t\tf = function () { n.parentNode.insertBefore(s, n); };\n\t\t\ts.type = \"text/javascript\";\n\t\t\ts.async = true;\n\t\t\ts.src = (d.location.protocol == \"https:\" ? \"https:\" : \"http:\") + \"//mc.yandex.ru/metrika/watch.js\";\n\t\t\t\n\t\t\tif (w.opera == \"[object Opera]\") {\n\t\t\t\td.addEventListener(\"DOMContentLoaded\", f, false);\n\t\t\t} else { f(); }\n\t\t})(document, window, \"yandex_metrika_callbacks\");\n\t</script>\n\t<noscript><div><img src=\"//mc.yandex.ru/watch/26161809\" style=\"position:absolute; left:-9999px;\" alt=\"\" /></div></noscript>\n\t<!-- /Yandex.Metrika counter -->\n<div class=\"full-screen\"></div>\n<div id=\"wrapper\">\n\t<nav class=\"navbar navbar-default\">\n\t\t<div class=\"container\">\n\t\t\t<div class=\"navbar-header\">\n\t\t\t\t<button data-target=\".navbar-collapse\" data-toggle=\"collapse\" class=\"navbar-toggle\" type=\"button\">\n\t\t\t\t\t<span class=\"sr-only\">Toggle navigation</span>\n\t\t\t\t\t<span class=\"icon-bar\"></span>\n\t\t\t\t\t<span class=\"icon-bar\"></span>\n\t\t\t\t\t<span class=\"icon-bar\"></span>\n\t\t\t\t</button>\n\t\t\t\t<a href=\"/\" class=\"navbar-brand\">NWC3L</a>\n\t\t\t</div>\n\t\t\t<div class=\"navbar-collapse collapse\">\n\t\t\t\t<ul class=\"nav navbar-nav\">\n\t\t\t<!--<li><a class=\"fs-login\" href=\"#login\">Log in</a></li>-->\n\t<!--<li class=\"active\"><a href=\"/rules\">Rules</a></li>-->\n\t<!--<li><a href=\"/schedule\">Schedule</a></li>-->\n\t<li class=\"dropdown\">\n\t\t<a data-toggle=\"dropdown\" class=\"dropdown-toggle\" href=\"#\">Leagues<span class=\"caret\"></span></a>\n\t\t<ul role=\"menu\" class=\"dropdown-menu\">\n\t\t\t\t\t\t\t<li><a href=\"/seasons\">NWC3L</a></li>\n\t\t\t\t<li><a href=\"/rules\">Rules</a></li>\n\t\t\t\t<li><a href=\"/winners\">Winners</a></li>\n\t\t\t\t<li><a href=\"/statistic\">Statistic</a></li>\n\t\t\t<li role=\"separator\" class=\"divider\"></li>\t\t\t\t<li><a href=\"/league/nwl/seasons/\">NWL</a></li>\n\t\t\t\t<li><a href=\"/league/nwl/rules/\">Rules</a></li>\n\t\t\t\t<li><a href=\"/league/nwl/winners/\">Winners</a></li>\n\t\t\t\t<li><a href=\"/league/nwl/statistic/\">Statistic</a></li>\n\t\t\t\t\t\t<li role=\"separator\" class=\"divider\"></li>\n\t\t\t<li><a href=\"/teams\">Teams</a></li>\n\t\t\t<li><a href=\"/maps\">Maps</a></li>\n\t\t\t\t\t</ul>\n\t</li>\n\t<!--\n\t<li class=\"dropdown\">\n\t\t<a data-toggle=\"dropdown\" class=\"dropdown-toggle\" href=\"#\">League<span class=\"caret\"></span></a>\n\t\t<ul role=\"menu\" class=\"dropdown-menu\">\n\t\t\t<li><a href=\"/seasons\">Seasons</a></li>\n\t\t\t<li><a href=\"/rules\">Rules</a></li>\n\t\t\t<li><a href=\"/results\">Statistic</a></li>\n\t\t\t<li><a href=\"/winners\">Winners</a></li>\n\t\t\t\t\t\t<li><a href=\"/teams\">Teams</a></li>\n\t\t\t\t\t\t<li><a href=\"/maps\">Maps</a></li>\n\t\t</ul>\n\t</li>\n\t-->\n\t\t<li class=\"dropdown\">\n\t\t<a data-toggle=\"dropdown\" class=\"dropdown-toggle\" href=\"#\">Tournaments<span class=\"caret\"></span></a>\n\t\t<ul role=\"menu\" class=\"dropdown-menu\">\n\t\t\t\t\t\t\t\t\t\t<li><a href=\"/cups/nwc3l_series\">NWC3L Series</a></li>\n\t\t\t\t\t\t\t<li><a href=\"/cups/random_heroes\">Random Heroes</a></li>\n\t\t\t\t\t\t\t<li><a href=\"/cups/nwc3l_2x2_series\">NWC3L 2x2 Series</a></li>\n\t\t\t\t\t\t\t<li><a href=\"/cups/lw_cup\">LW Cup</a></li>\n\t\t\t\t\t\t\t<li><a href=\"/cups/show_match_wolves\">Show Match Wolves</a></li>\n\t\t\t\t\t\t\t<li><a href=\"/cups/lsl\">LSL</a></li>\n\t\t\t\t\t\t\t<li><a href=\"/cups/america_warcraft_league\">America Warcraft League</a></li>\n\t\t\t\t\t\t\t<li><a href=\"/cups/umad_cup\">uMaD Cup</a></li>\n\t\t\t\t\t\t\t\t</ul>\n\t</li>\n\t\t<!--<li><a href=\"https://www.dropbox.com/sh/a3de6d08q32ctjv/AADk__oPjoa9EgQDSXyqJ8sHa?dl=0\" target=\"_blank\">Replays</a></li>-->\n\t<li><a href=\"/replays\">Replays</a></li>\n\t<li><a href=\"/videos\">Video archive</a></li>\n\t\t\t\t<li class=\"dropdown\">\n\t\t\t<a data-toggle=\"dropdown\" class=\"dropdown-toggle\" href=\"#\">Broadcasts<span class=\"caret\"></span></a>\n\t\t\t<ul role=\"menu\" class=\"dropdown-menu\">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=12\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ru.png\" alt=\"\">\t\t\t\t\t\t\t\tag3nt\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=24\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tBack2Warcraft\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=35\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tbadkiwi\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=2\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/kz.png\" alt=\"\">\t\t\t\t\t\t\t\tDV\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=16\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/al.png\" alt=\"\">\t\t\t\t\t\t\t\tEna1337\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=32\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tEnTe\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=18\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/fr.png\" alt=\"\">\t\t\t\t\t\t\t\tFeartheG0lem\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=9\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ru.png\" alt=\"\">\t\t\t\t\t\t\t\tHexStmopCrit\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=26\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/nl.png\" alt=\"\">\t\t\t\t\t\t\t\tHI2Chaco\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=28\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/pe.png\" alt=\"\">\t\t\t\t\t\t\t\tHunterD\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=22\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ru.png\" alt=\"\">\t\t\t\t\t\t\t\tImperius\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=17\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tJehu\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=33\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tkevinwc3\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=34\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/kr.png\" alt=\"\">\t\t\t\t\t\t\t\tKimchoonsam\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=29\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/se.png\" alt=\"\">\t\t\t\t\t\t\t\tMaDFroG\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=15\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ch.png\" alt=\"\">\t\t\t\t\t\t\t\tmasaa\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=7\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tMentalGame\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=1\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ru.png\" alt=\"\">\t\t\t\t\t\t\t\tMorozov\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=30\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/fr.png\" alt=\"\">\t\t\t\t\t\t\t\tNeSH\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=36\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/kr.png\" alt=\"\">\t\t\t\t\t\t\t\tNorukill\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=6\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ca.png\" alt=\"\">\t\t\t\t\t\t\t\tOrange\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=10\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/hr.png\" alt=\"\">\t\t\t\t\t\t\t\tp1nke\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=14\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ru.png\" alt=\"\">\t\t\t\t\t\t\t\tReyenir\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=37\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ru.png\" alt=\"\">\t\t\t\t\t\t\t\tShaDai\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=19\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/se.png\" alt=\"\">\t\t\t\t\t\t\t\tSkutt\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=21\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ua.png\" alt=\"\">\t\t\t\t\t\t\t\tSonik\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=25\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tSpatenHTK\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=31\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/fr.png\" alt=\"\">\t\t\t\t\t\t\t\tSyDe\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=8\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/ru.png\" alt=\"\">\t\t\t\t\t\t\t\tTGW\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=11\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/fr.png\" alt=\"\">\t\t\t\t\t\t\t\tToD\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=23\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/de.png\" alt=\"\">\t\t\t\t\t\t\t\tToX\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<a href=\"/stream?show=20\">\n\t\t\t\t\t\t\t\t<img src=\"/upload/flags/us.png\" alt=\"\">\t\t\t\t\t\t\t\tWackedStrats\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t</li>\n\t\t</ul>\n\n<ul class=\"nav navbar-nav navbar-right\">\n\t\t\t\t\t\t<li><a href=\"/login?b=L2Fkcy50eHQ=\">Login</a></li>\n\t\t<li><a href=\"/register\">Registration</a></li>\n\t\t\t<li class=\"dropdown\">\n\t\t<a data-toggle=\"dropdown\" class=\"dropdown-toggle\" href=\"#\">Choose Your Language <span class=\"caret\"></span></a>\n\t\t<ul role=\"menu\" class=\"dropdown-menu\">\n\t\t\t<li><a href=\"/change_lang?lang=en\"><img src=\"/upload/flags/gb.png\" alt=\"\"> English</a></li>\n\t\t\t<li><a href=\"/change_lang?lang=de\"><img src=\"/upload/flags/de.png\" alt=\"\"> Deutsch</a></li>\n\t\t\t<li><a href=\"/change_lang?lang=fr\"><img src=\"/upload/flags/fr.png\" alt=\"\"> Fran\u00e7ais</a></li>\n\t\t\t<li><a href=\"/change_lang?lang=ru\"><img src=\"/upload/flags/ru.png\" alt=\"\"> \u0420\u0443\u0441\u0441\u043a\u0438\u0439</a></li>\n\t\t\t<li><a href=\"/change_lang?lang=kr\"><img src=\"/upload/flags/kr.png\" alt=\"\"> \ud55c\uad6d\uc5b4</a></li>\n\t\t</ul>\n\t</li>\n</ul>\n\t\t\t</div><!--/.nav-collapse -->\n\t\t</div>\n\t</nav>\n\t<div class=\"bs-docs-header\">\n\t\t<div class=\"container\">\n\t\t\t<h1 style=\"font-size:8em\">404</h1>\n\t\t\t<p>not found :(</p>\n\t\t</div>\n\t</div>\n\t<div class=\"container\">\n\t\t<div class=\"row\">\n\t\t\t<section id=\"content\">\n\t\t\t</section>\n\t\t</div>\n\n\t</div>\n\t<div class=\"for-footer\"></div>\n</div>\n<footer class=\"footer\">\n\t<div class=\"container\">\n\t\t<p class=\"text-muted\">&copy; All rights reserved. Page generation time: 0.02737, sql queries: 5</p>\n\t</div>\n</footer>\n<a class=\"scroll-to-top\" href=\"#\"></a>\n</body>\n</html>"