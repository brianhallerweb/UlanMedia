"<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\" />\n<title>Estrenos10</title> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n<link rel=\"manifest\" href=\"https://estrenos10.com/manifest/manifest.json\" />\n<meta name=\"theme-color\" content=\"#364863\" />\n<link rel=\"stylesheet\" href=\"https://estrenos10.com/themes/blue/css/style.css?v=beta2-0\" />\n<link rel=\"stylesheet\" href=\"https://estrenos10.com/themes/fonts/style.css?v=beta2-0\" />\n<link rel=\"stylesheet\" href=\"https://estrenos10.com/build/css/app.css?v=beta2-0\" />\n<script type=\"text/javascript\" src=\"https://estrenos10.com/themes/js/cropper.min.js\"></script>\n<script type=\"text/javascript\" src=\"https://estrenos10.com/themes/js/sidenav.min.js\"></script>\n<style>\r\n\r\n.DvrTop>figure,\r\n[class*=section-] {\r\n    margin-bottom: 2rem\r\n}\r\n\r\n[class*=Dvr-] {\r\n    margin: 0 auto 2rem;\r\n    text-align: center\r\n}\r\n\r\n.Dvr-728 {\r\n    max-width: 728px\r\n}\r\n\r\n.Dvr-300 {\r\n    max-width: 300px\r\n}\r\n\r\n.DvrTop .Dvr-728,\r\n[class*=Dvr-]:last-child,\r\n.DvrTop.Dvr-728,\r\n.Dvr-A>figure:last-child,\r\n.NewsBx,\r\n.thumb,\r\n.NewsBx .Dvr-300 {\r\n    margin-bottom: 0\r\n}\r\n\r\n.NewsBx,\r\n.thumb {\r\n    overflow: hidden;\r\n    font-size: 0\r\n}\r\n\r\n.NewsBx .Dvr-300 {\r\n    margin-right: 1px\r\n}\r\n\r\n.NewsBx .News.a {\r\n    padding-top: 250px;\r\n    width: 300px\r\n}\r\n\r\n.News .Title {\r\n    font-size: .875rem;\r\n    font-weight: 700;\r\n    margin-bottom: 0\r\n}\r\n\r\n.News.a .Title a,\r\n.Event .Title a,\r\n.Event {\r\n    color: #fff\r\n}\r\n\r\n.News.a {\r\n    position: relative;\r\n    margin-right: 1px;\r\n    margin-bottom: 1px\r\n}\r\n\r\n.News.a .thumb,\r\n.News.a .thumb img,\r\n.News.b .thumb,\r\n.News.b .thumb img,\r\n.Review .thumb img,\r\n.Event .thumb img,\r\n.event-single .thumb img {\r\n    position: absolute;\r\n    left: 0;\r\n    top: 0;\r\n    width: 100%;\r\n    height: 100%;\r\n    object-fit: cover\r\n}\r\n\r\n.News.a header,\r\n.Event header {\r\n    position: absolute;\r\n    left: 0;\r\n    bottom: 0;\r\n    right: 0;\r\n    padding: 3rem 1rem 1rem;\r\n    white-space: normal;\r\n    z-index: 1;\r\n    background: -moz-linear-gradient(top, rgba(87, 24, 69, 0) 0%, rgba(87, 24, 69, 0.5) 100%);\r\n    background: -webkit-linear-gradient(top, rgba(87, 24, 69, 0) 0%, rgba(87, 24, 69, 0.5) 100%);\r\n    background: linear-gradient(to bottom, rgba(87, 24, 69, 0) 0%, rgba(87, 24, 69, 0.5) 100%)\r\n}\r\n\r\n.Content,\r\n.Content>main,\r\n.Content>aside,\r\n.gallery {\r\n    padding-top: 1rem;\r\n    padding-bottom: 1rem\r\n}\r\n\r\n.main {\r\n    margin-bottom: 2rem\r\n}\r\n\r\n.main:last-child {\r\n    margin-bottom: 0\r\n}\r\n\r\n.main>.HdTop:first-child {\r\n    padding-top: 0\r\n}\r\n\r\naside.stck>div {\r\n    position: sticky;\r\n    top: 2rem\r\n}\r\n\r\n.thumb img {\r\n    transition: .2s\r\n}\r\n\r\n.thumb {\r\n    background: -moz-linear-gradient(top, #fff 0%, #ff5733 100%);\r\n    background: -webkit-linear-gradient(top, #fff 0%, #ff5733 100%);\r\n    background: linear-gradient(to bottom, #fff 0%, #ff5733 100%);\r\n    position: relative\r\n}\r\n\r\n.News:hover .thumb img,\r\n.Review:hover .thumb img,\r\n.Event:hover .thumb img {\r\n    opacity: .8;\r\n    transform: scale(1.1)\r\n}\r\n\r\n.cate-link {\r\n    display: inline-block;\r\n    vertical-align: top;\r\n    margin-bottom: 5px;\r\n    padding: 0 .5rem;\r\n    font-weight: 700;\r\n    text-transform: uppercase;\r\n    color: #571845;\r\n    line-height: 1.25rem;\r\n    background-color: #ffc300;\r\n    font-size: .75rem;\r\n    border-radius: 10px 0 10px 0\r\n}\r\n\r\n.cate-link:hover {\r\n    background-color: #c70039;\r\n    color: #fff\r\n}\r\n\r\n\r\n@media(max-width:992px) {\r\n\r\n    .NewsTop {\r\n        max-width: none\r\n    }\r\n    .NewsBx {\r\n        overflow: auto;\r\n        white-space: nowrap\r\n    }\r\n    .NewsBx>.lg,\r\n    .NewsBx>ul,\r\n    .NewsBx>ul>li {\r\n        display: inline-block;\r\n        vertical-align: top;\r\n        min-width: 301px\r\n    }\r\n    .News.b .thumb {\r\n        max-width: 270px;\r\n        margin-left: auto;\r\n        margin-right: auto\r\n    }\r\n    .Events {\r\n        overflow: auto\r\n    }\r\n\r\n}\r\n\r\n@media (min-width: 992px){\r\n\t.NewsBx>.lg {\r\n\t    width: calc(100% - 603px);\r\n\t}\r\n\t.NewsBx>ul>li, .NewsBx>.lg {\r\n\t    float: left;\r\n\t}\r\n\t.NewsBx>ul {\r\n\t    float: right;\r\n\t    width: 602px;\r\n\t}\r\n\t.NewsBx>.lg .News.a {\r\n\t    width: 100%;\r\n\t    padding-top: 501px;\r\n\t    margin-bottom: 0;\r\n\t}\r\n\t.NewsBx>.lg .News .Title {\r\n\t    font-size: 1.7rem;\r\n\t    line-height: 1.2;\r\n\t}\r\n}\r\n.Ul{\r\n    padding: 0;\r\n    margin: 0;\r\n    list-style-type: none\r\n}\r\n.NewsBx *:hover{\r\n\ttext-decoration: none;\t\r\n}\r\n</style>\n</head>\n<body>\n<script>\r\n\t\tvar appId = '151698755041135';\r\n\t</script>\n<div id=\"fb-root\"></div>\n<script>(function(d, s, id) {\r\n\tvar js, fjs = d.getElementsByTagName(s)[0];\r\n\tif (d.getElementById(id)) return;\r\n\tjs = d.createElement(s); js.id = id;\r\n\tjs.src = 'https://connect.facebook.net/en_US/sdk/xfbml.customerchat.js#xfbml=1&version=v3.0&appId=151698755041135&autoLogAppEvents=1';\r\n\tfjs.parentNode.insertBefore(js, fjs);\r\n\t}(document, 'script', 'facebook-jssdk'));</script>\n<div id=\"app\">\n<div>\n<nav class=\"navbar navbar-expand-lg navbar-dark bg-dark fixed-top\">\n<div class=\"container position-relative\">\n<button id=\"menu-toggle\" class=\"navbar-toggler position-absolute\" type=\"button\" style=\"top: 0.34687rem;\" aria-label=\"Toggle navigation\">\n<span class=\"navbar-toggler-icon\"></span>\n</button>\n<a class=\"navbar-brand mr-auto mr-lg-0 logo-nav\" href=\"/\" title=\"Estrenos10\">\n<img src=\"https://estrenos10.com/assets/logo.png\" alt=\"Estrenos10 Logo\" height=\"35\">\n</a>\n<button class=\"navbar-toggler position-absolute\" type=\"button\" style=\"top: 0.34687rem; right: 0;\" aria-label=\"Toggle navigation\" v-on:click=\"showSearchMovil\">\n<span class=\"navbar-search-icon\"></span>\n</button>\n<div class=\"collapse navbar-collapse\" id=\"navbarsExampleDefault\">\n<ul class=\"navbar-nav mr-auto\">\n<li class=\"nav-item\">\n<a class=\"nav-link\" href=\"/peliculas/estrenos-2018\">Estrenos 2018</a>\n</li>\n<li class=\"nav-item\">\n<a class=\"nav-link\" href=\"/peliculas/estrenos-2019\">Estrenos 2019</a>\n</li>\n<li class=\"nav-item dropdown\">\n<a class=\"nav-link dropdown-toggle\" href=\"#\" id=\"navbarDropdown\" role=\"button\" data-toggle=\"dropdown\" aria-haspopup=\"true\" aria-expanded=\"false\">\nG\u00e9neros\n</a>\n<div class=\"dropdown-menu\" aria-labelledby=\"navbarDropdown\">\n<a class=\"dropdown-item\" href=\"/peliculas/genero-accion\">Pel\u00edculas de acci\u00f3n</a>\n<a class=\"dropdown-item\" href=\"/peliculas/genero-animacion\">Pel\u00edculas animadas</a>\n<a class=\"dropdown-item\" href=\"/peliculas/genero-terror\">Pel\u00edculas de Terror</a>\n<a class=\"dropdown-item\" href=\"/peliculas/genero-comedia\">Pel\u00edculas graciosas</a>\n<a class=\"dropdown-item\" href=\"/peliculas/genero-romance\">Pel\u00edculas rom\u00e1nticas</a>\n</div>\n</li>\n<li class=\"nav-item dropdown\">\n<a class=\"nav-link dropdown-toggle\" href=\"#\" id=\"navbarDropdown\" role=\"button\" data-toggle=\"dropdown\" aria-haspopup=\"true\" aria-expanded=\"false\">\nRanking\n</a>\n<div class=\"dropdown-menu\" aria-labelledby=\"navbarDropdown\">\n<a class=\"dropdown-item\" href=\"/peliculas/mejores-del-2018\">Mejores pel\u00edculas del 2018</a>\n<a class=\"dropdown-item\" href=\"/peliculas/mejores-del-2017\">Mejores pel\u00edculas del 2017</a>\n<a class=\"dropdown-item\" href=\"/peliculas/mejores-del-2016\">Mejores pel\u00edculas del 2016</a>\n<a class=\"dropdown-item\" href=\"/peliculas/mejores-del-2015\">Mejores pel\u00edculas del 2015</a>\n</div>\n</li>\n<li class=\"nav-item\">\n<a class=\"nav-link\" href=\"/listas/lista-76\">Anime</a>\n</li>\n</ul>\n<search-form></search-form>\n<auth-nav class=\"d-none d-lg-block\"></auth-nav>\n</div>\n</div>\n</nav>\n<search-form-movil></search-form-movil>\n</div>\n<main class=\"bg-lightx\">\n<div class=\"container text-center\">\n<h1>Se produjo un error 404</h1>\n<h2>Page not found.</h2>\n<p>The requested URL could not be matched by routing.</p>\n</div>\n</main>\n<footer class=\"footer\">\n<div class=\"FooterBot\">\n<div class=\"container text-center text-lg-left\">\n<div class=\"row\">\n<div class=\"col-lg-8\">\n<div class=\"text-white\">Estrenos10 \u00a9 2018 - Este sitio no almacena ning\u00fan video en sus servidores.</div>\n</div>\n<div class=\"col-lg-4\">\n<ul class=\"d-block m-0 p-0\">\n<li><a href=\"/dmca\" rel=\"nofollow\">DMCA <span class=\"icon-pin\"></span></a></li>\n<li><a href=\"/privacy-policy\" rel=\"nofollow\">Privacy <span class=\"icon-pin\"></span></a></li>\n<li><a href=\"/contact\" rel=\"nofollow\">Contact <span class=\"icon-pin\"></span></a></li>\n<li><a href=\"//fb.com/Estrenos10-255608948309946/\" target=\"_blank\" rel=\"noreferrer\">Facebook <span class=\"icon-pin\"></span></a></li>\n</ul>\n</div>\n</div>\n</div>\n</div>\n</footer>\n<div style=\"background: url(https://goo.gl/epZPX6); display: none;\"></div>\n<auth-modal></auth-modal>\n<global-alert></global-alert>\n<div id=\"sidenav\" style=\"transform: translate3d(-380px, 0px, 0px);\">\n<div class=\"sidenav\">\n<side-nav></side-nav>\n<ul class=\"d-block list-unstyled\">\n<li><a class=\"subheader\">Explorar sitio</a></li>\n<li><a href=\"/peliculas/estrenos-2018\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/ticket.svg\" /> Estrenos 2018</a></li>\n<li><a href=\"/peliculas/estrenos-2019\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/ticket.svg\" /> Estrenos 2019</a></li>\n<li><a href=\"/peliculas\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/movie_star.svg\" /> Novedades</a></li>\n<li><a class=\"subheader\">G\u00e9neros</a></li>\n<li><a href=\"/listas/lista-76\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/list.svg\" /> Anime</a></li>\n<li><a href=\"/peliculas/genero-accion\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/list.svg\" /> Pel\u00edculas de Acci\u00f3n</a></li>\n<li><a href=\"/peliculas/genero-animacion\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/list.svg\" /> Pel\u00edculas Animadas</a></li>\n<li><a href=\"/peliculas/genero-terror\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/list.svg\" /> Pel\u00edculas de Terror</a></li>\n<li><a href=\"/peliculas/genero-comedia\"><img class=\"md-icon\" alt=\"icon\" src=\"/assets/svg/list.svg\" /> Pel\u00edculas de Comedia</a></li>\n</ul>\n</div>\n</div>\n<div id=\"backdrop\"></div>\n</div>\n<script>\r\n\t/*if ('serviceWorker' in navigator) {\r\n\t\twindow.addEventListener('load', function() {\r\n\t\t\tnavigator.serviceWorker.register('/sw.js').then(function(registration) {\r\n\t\t\t\treturn;\r\n\t\t\t}, function(err) {\r\n\t\t\t\tconsole.log('Fail sw:', err);\r\n\t\t\t});\r\n\t\t});\r\n\t}*/\r\n\t</script>\n<script src=\"https://estrenos10.com/build/js/manifest.js?v=beta2-0\"></script>\n<script src=\"https://estrenos10.com/build/js/vendor.js?v=beta2-0\"></script>\n<script src=\"https://estrenos10.com/build/js/app.js?v=beta2-0\"></script>\n<script>\r\n\t\"use strict\";\r\n\tvar sidenav=new Sidenav({\r\n\t\tcontent:document.getElementById(\"app\"),\r\n\t\tsidenav:document.getElementById(\"sidenav\"),\r\n\t\tbackdrop:document.getElementById(\"backdrop\")\r\n\t});\r\n\tdocument.getElementById(\"menu-toggle\").addEventListener(\"click\",function(){\r\n\t\tsidenav.open();\r\n\t});\r\n\t</script>\n<script type=\"text/javascript\" src=\"https://estrenos10.com/themes/js/jquery-3.3.1.slim.min.js\"></script>\n<script type=\"text/javascript\" src=\"https://estrenos10.com/themes/js/popper.min.js\"></script>\n<script type=\"text/javascript\" src=\"https://estrenos10.com/themes/js/bootstrap.min.js\"></script>\n<script>\r\n\t$(function () {\r\n\t\t$('[data-toggle=\"tooltip\"]').tooltip();\r\n\t\t$('[data-toggle=\"popover\"]').popover();\r\n\t})\r\n\t</script>\n</body>\n</html>\n"