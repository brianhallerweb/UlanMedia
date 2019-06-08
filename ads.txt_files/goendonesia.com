"<!DOCTYPE HTML>\n<html lang=\"en-US\">\n    <head>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\"\n    content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\"\n    content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\" />\n        <title>Waiting for the redirectiron...</title>\n        <style type=\"text/css\">\n            body {background-color: #ffffff; font-family: \"Helvetica Neue\", Helvetica,Arial,sans-serif;}\n            html, body {width: 100%; height: 100%; margin: 0; padding: 0;}\n            span {color: #878787; font-size: 12pt;  text-align: center;}\n            h1 {color: #878787; font-size: 18pt; text-align: center;}\n            .link {margin-top: 40px;}\n            .sk-circle {margin: 80px auto;width: 100px;height: 100px;position: relative;}\n            .sk-circle .sk-child {width: 100%;height: 100%;position: absolute;left: 0;top: 0;}\n            .sk-circle .sk-child:before {content: '';display: block;margin: 0 auto;width: 15%;height: 15%;background-color: #666666;border-radius: 100%;-webkit-animation: sk-circleBounceDelay 1.2s infinite ease-in-out both;animation: sk-circleBounceDelay 1.2s infinite ease-in-out both;}\n            .sk-circle .sk-circle2 {-webkit-transform: rotate(30deg);-ms-transform: rotate(30deg);transform: rotate(30deg); }\n            .sk-circle .sk-circle3 {-webkit-transform: rotate(60deg);-ms-transform: rotate(60deg);transform: rotate(60deg); }\n            .sk-circle .sk-circle4 {-webkit-transform: rotate(90deg);-ms-transform: rotate(90deg);transform: rotate(90deg); }\n            .sk-circle .sk-circle5 {-webkit-transform: rotate(120deg);-ms-transform: rotate(120deg);transform: rotate(120deg); }\n            .sk-circle .sk-circle6 {-webkit-transform: rotate(150deg);-ms-transform: rotate(150deg);transform: rotate(150deg); }\n            .sk-circle .sk-circle7 {-webkit-transform: rotate(180deg);-ms-transform: rotate(180deg);transform: rotate(180deg); }\n            .sk-circle .sk-circle8 {-webkit-transform: rotate(210deg);-ms-transform: rotate(210deg);transform: rotate(210deg); }\n            .sk-circle .sk-circle9 {-webkit-transform: rotate(240deg);-ms-transform: rotate(240deg);transform: rotate(240deg); }\n            .sk-circle .sk-circle10 {-webkit-transform: rotate(270deg);-ms-transform: rotate(270deg);transform: rotate(270deg); }\n            .sk-circle .sk-circle11 {-webkit-transform: rotate(300deg);-ms-transform: rotate(300deg);transform: rotate(300deg); }\n            .sk-circle .sk-circle12 {-webkit-transform: rotate(330deg);-ms-transform: rotate(330deg);transform: rotate(330deg); }\n            .sk-circle .sk-circle2:before {-webkit-animation-delay: -1.1s;animation-delay: -1.1s; }\n            .sk-circle .sk-circle3:before {-webkit-animation-delay: -1s;animation-delay: -1s; }\n            .sk-circle .sk-circle4:before {-webkit-animation-delay: -0.9s;animation-delay: -0.9s; }\n            .sk-circle .sk-circle5:before {-webkit-animation-delay: -0.8s;animation-delay: -0.8s; }\n            .sk-circle .sk-circle6:before {-webkit-animation-delay: -0.7s;animation-delay: -0.7s; }\n            .sk-circle .sk-circle7:before {-webkit-animation-delay: -0.6s;animation-delay: -0.6s; }\n            .sk-circle .sk-circle8:before {-webkit-animation-delay: -0.5s;animation-delay: -0.5s; }\n            .sk-circle .sk-circle9:before {-webkit-animation-delay: -0.4s;animation-delay: -0.4s; }\n            .sk-circle .sk-circle10:before {-webkit-animation-delay: -0.3s;animation-delay: -0.3s; }\n            .sk-circle .sk-circle11:before {-webkit-animation-delay: -0.2s;animation-delay: -0.2s; }\n            .sk-circle .sk-circle12:before {-webkit-animation-delay: -0.1s;animation-delay: -0.1s; }\n            @-webkit-keyframes sk-circleBounceDelay {0%, 80%, 100% {-webkit-transform: scale(0);transform: scale(0);}40% {-webkit-transform: scale(1);transform: scale(1);}}\n            @keyframes sk-circleBounceDelay {0%, 80%, 100% {-webkit-transform: scale(0);transform: scale(0);}40% {-webkit-transform: scale(1);transform: scale(1);}}\n\n        </style>\n\n        <script type=\"text/javascript\">\n            //<![CDATA[\n            function startCountdown() {\n                setInterval(function () {\n                    var $secondsElement = document.getElementById('seconds');\n                    var seconds = parseInt($secondsElement.innerHTML);\n                    if (seconds > 0) {\n                        seconds--;\n                        $secondsElement.innerHTML = seconds;\n                    }\n                }, 1000);\n            }\n            function browserIntegrityCheck() {\n                w = window.innerWidth;\n                h = window.innerHeight;\n                arr = [w, h, Math.floor((Math.random() * 9) + 1)];\n                arr.push(arr[0] * arr[1] * arr[2]);\n                d = new Date().getTime();\n                arr = [];\n                b = navigator.appName;\n                div1 = document.createElement('div');\n                div1.style.display = 'none';\n                div2 = document.createElement('div');\n                div2.style.display = 'none';\n                div3 = document.createElement('div');\n                div3.style.display = 'none';\n                c = document.getElementById('content');\n                c.appendChild(div1);\n                div1.appendChild(div2);\n                div2.appendChild(div3);\n                div1.removeChild(div2);\n                r = genRandString();\n                if (r.search('asd')) {\n                    r.replace('asd', 'bsd');\n                }\n            }\n\n            function redirect() {\n                setTimeout(function () {\n                    f = document.getElementById('challenge-form');\n                    f.submit();\n                }, 4000);\n            }\n            function genRandString() {\n                var text = \"\";\n                var possible = \"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\";\n\n                for (var i = 0; i < 5; i++)\n                    text += possible.charAt(Math.floor(Math.random() * possible.length));\n\n                return text;\n            }\n            \n            (function () {\n                var a = function () {\n                    try {\n                        return !!window.addEventListener\n                    } catch (e) {\n                        return !1\n                    }\n                },\n                        b = function (b, c) {\n                            a() ? document.addEventListener(\"DOMContentLoaded\", b, c) : document.attachEvent(\"onreadystatechange\", b)\n                        };\n                b(function () {\n                    var a = document.getElementById('content').style.display = 'block';\n\n                    setTimeout(startCountdown(), 0);\n                    setTimeout(browserIntegrityCheck(), 0);\n                    setTimeout(redirect(), 0);\n\n\n                }, false);\n            })();\n            //]]>\n        </script>\n\n\n    </head>\n    <body>\n        <table width=\"100%\" height=\"100%\" cellpadding=\"20\">\n            <tr>\n                <td align=\"center\" valign=\"middle\">\n                    <div>\n                        <noscript>\n                        <h1 style=\"color:#990000;\">Please, turn Javascript on in your browser then reload the page.</h1>\n                        </noscript>\n                        <div id=\"content\" style=\"display:none\">\n\n                            <div class=\"sk-circle\">\n                                <div class=\"sk-circle1 sk-child\"></div>\n                                <div class=\"sk-circle2 sk-child\"></div>\n                                <div class=\"sk-circle3 sk-child\"></div>\n                                <div class=\"sk-circle4 sk-child\"></div>\n                                <div class=\"sk-circle5 sk-child\"></div>\n                                <div class=\"sk-circle6 sk-child\"></div>\n                                <div class=\"sk-circle7 sk-child\"></div>\n                                <div class=\"sk-circle8 sk-child\"></div>\n                                <div class=\"sk-circle9 sk-child\"></div>\n                                <div class=\"sk-circle10 sk-child\"></div>\n                                <div class=\"sk-circle11 sk-child\"></div>\n                                <div class=\"sk-circle12 sk-child\"></div>\n                            </div>\n                            <h1>Accessing http://goendonesia.com/ads.txt securely\u00e2\u20ac\u00a6</h1>\n\n                            <span>This is an automatic process.  Your browser will redirect to your requested content in <span id=\"seconds\">5</span> seconds.</span>\n                        </div>\n\n                        <form id=\"challenge-form\" action=\"/verify.php\" method=\"post\">\n                            <input type=\"hidden\" name=\"hash\" value=\"b61e2c4d85f10c0731970d64a98658cac3e4f43f\"/>\n                            <input type=\"hidden\" name=\"origin_url\" value=\"http://goendonesia.com/ads.txt\"/>\n                        </form>\n                    </div>\n\n\n                    <div class=\"link\">\n                        <a href=\"https://bitninja.io\" target=\"_blank\" style=\"font-size: 12px;\">Security check by BitNinja.IO</a>\n                    </div>\n                </td>\n\n            </tr>\n        </table>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php?param=honey\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php?param=honey\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php?param=honey\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php?param=honey\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php?param=honey\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php?param=honey\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php?param=honey\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/?GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>"