"<!doctype html>\n<html>\n<head>\n    <title>424 Failed Dependency</title>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width\">\n    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700&subset=latin,cyrillic' rel='stylesheet' type='text/css'>\n    <style>\n        body {\n            background-color: #f1f4f5;\n            color: #37474f;\n            line-height: 1.4;\n            font-family: 'Open Sans', sans-serif;\n            margin: 0;\n            padding: 0;\n            }\n        .error_code {\n            display: block;\n            font-size: 92px;\n            font-weight: 700;\n            margin-top: -25px;\n            }\n        .error_brief {\n            display: block;\n            font-size: 18px;\n            font-weight: 700;\n            margin-bottom: 15px;\n            }\n        .help_button, .fix_button {\n            background-color: #399bff;\n            color: #fff;\n            margin-top: 15px;\n            font-size: 14px;\n            padding: 7px 20px 7px 20px;\n            border: none;\n            border-radius: 3px;\n            vertical-align: middle;\n            cursor: pointer;\n            }\n        .fix_button {\n            background-color: #38ad41;\n            }\n        #fix_details {\n            margin-top: 40px;\n            visibility: hidden;\n            opacity: 0;\n            transition: visibility 0.3s, opacity 0.3s linear;\n            }\n    </style>\n\n    <script language=\"JavaScript\">\n        function toggleHelp() {\n            var e = document.getElementById(\"fix_details\");\n            if (e.style.visibility == 'visible') {\n                e.style.visibility = 'hidden';\n                e.style.opacity = 0;\n            } else {\n                e.style.visibility = 'visible';\n                e.style.opacity = 1;\n            }\n        }\n    </script>\n</head>\n<body>\n\n<div style=\"display: table; position: absolute; height: 100%; width: 100%;\">\n    <div style=\"display: table-cell; vertical-align: middle; padding: 0 40px;\">\n        <div style=\"margin-left: auto; margin-right: auto; width: 520px;\">\n            <div style=\"float:left; width:200px; text-align: center; padding-right: 20px;\">\n                <span class=\"error_code\">424</span>\n                <span class=\"error_description\">Failed Dependency</span>\n            </div>\n            <div style=\"float:left; width:300px;\">\n                <span class=\"error_brief\">\u00d0\u0097\u00d0\u00b0\u00d0\u00b1\u00d0\u00bb\u00d0\u00be\u00d0\u00ba\u00d0\u00b8\u00d1\u0080\u00d0\u00be\u00d0\u00b2\u00d0\u00b0\u00d0\u00bd\u00d0\u00be \u00d0\u00bf\u00d1\u0080\u00d0\u00b0\u00d0\u00b2\u00d0\u00b8\u00d0\u00bb\u00d0\u00b0\u00d0\u00bc\u00d0\u00b8 \u00d0\u00b1\u00d0\u00b5\u00d0\u00b7\u00d0\u00be\u00d0\u00bf\u00d0\u00b0\u00d1\u0081\u00d0\u00bd\u00d0\u00be\u00d1\u0081\u00d1\u0082\u00d0\u00b8</span>\n                <span class=\"error_detail\">\u00d0\u0097\u00d0\u00b0\u00d0\u00bf\u00d1\u0080\u00d0\u00be\u00d1\u0081 \u00d1\u0081\u00d0\u00be\u00d0\u00b4\u00d0\u00b5\u00d1\u0080\u00d0\u00b6\u00d0\u00b8\u00d1\u0082 \u00d0\u00bf\u00d1\u0080\u00d0\u00b8\u00d0\u00b7\u00d0\u00bd\u00d0\u00b0\u00d0\u00ba\u00d0\u00b8 \u00d0\u00bf\u00d0\u00be\u00d0\u00bf\u00d1\u008b\u00d1\u0082\u00d0\u00ba\u00d0\u00b8 \u00d0\u00b8\u00d1\u0081\u00d0\u00bf\u00d0\u00be\u00d0\u00bb\u00d1\u008c\u00d0\u00b7\u00d0\u00be\u00d0\u00b2\u00d0\u00b0\u00d0\u00bd\u00d0\u00b8\u00d1\u008f \u00d1\u0083\u00d1\u008f\u00d0\u00b7\u00d0\u00b2\u00d0\u00b8\u00d0\u00bc\u00d0\u00be\u00d1\u0081\u00d1\u0082\u00d0\u00b8 \u00d0\u00bd\u00d0\u00b0 \u00d1\u0081\u00d0\u00b0\u00d0\u00b9\u00d1\u0082\u00d0\u00b5</span>\n                <br>\n                <input type=\"button\" value=\"\u00d0\u009a\u00d0\u00b0\u00d0\u00ba \u00d1\u008d\u00d1\u0082\u00d0\u00be \u00d0\u00b8\u00d1\u0081\u00d0\u00bf\u00d1\u0080\u00d0\u00b0\u00d0\u00b2\u00d0\u00b8\u00d1\u0082\u00d1\u008c?\" class=\"help_button\" onclick=\"toggleHelp()\">\n            </div>\n            <div style=\"clear:both\"></div>\n            <div id=\"fix_details\">\n                \u00d0\u0095\u00d1\u0081\u00d0\u00bb\u00d0\u00b8 \u00d0\u0092\u00d1\u008b \u00d0\u00b0\u00d0\u00b4\u00d0\u00bc\u00d0\u00b8\u00d0\u00bd\u00d0\u00b8\u00d1\u0081\u00d1\u0082\u00d1\u0080\u00d0\u00b0\u00d1\u0082\u00d0\u00be\u00d1\u0080 \u00d1\u0081\u00d0\u00b0\u00d0\u00b9\u00d1\u0082\u00d0\u00b0, \u00d1\u0081\u00d0\u00b0\u00d0\u00bc\u00d1\u008b\u00d0\u00b9 \u00d0\u00b1\u00d1\u008b\u00d1\u0081\u00d1\u0082\u00d1\u0080\u00d1\u008b\u00d0\u00b9 \u00d1\u0081\u00d0\u00bf\u00d0\u00be\u00d1\u0081\u00d0\u00be\u00d0\u00b1 \u00d0\u00b8\u00d1\u0081\u00d0\u00bf\u00d1\u0080\u00d0\u00b0\u00d0\u00b2\u00d0\u00b8\u00d1\u0082\u00d1\u008c \u00d1\u008d\u00d1\u0082\u00d1\u0083 \u00d0\u00be\u00d1\u0088\u00d0\u00b8\u00d0\u00b1\u00d0\u00ba\u00d1\u0083 &mdash; \u00d0\u00b2\u00d0\u00be\u00d1\u0081\u00d0\u00bf\u00d0\u00be\u00d0\u00bb\u00d1\u008c\u00d0\u00b7\u00d0\u00be\u00d0\u00b2\u00d0\u00b0\u00d1\u0082\u00d1\u008c\u00d1\u0081\u00d1\u008f\n                \u00d0\u00a2\u00d0\u00b5\u00d1\u0085\u00d0\u00bd\u00d0\u00b8\u00d1\u0087\u00d0\u00b5\u00d1\u0081\u00d0\u00ba\u00d0\u00be\u00d0\u00b9 \u00d0\u00bf\u00d1\u0080\u00d0\u00be\u00d0\u00b2\u00d0\u00b5\u00d1\u0080\u00d0\u00ba\u00d0\u00be\u00d0\u00b9 \u00d1\u0081\u00d0\u00b0\u00d0\u00b9\u00d1\u0082\u00d0\u00b0 \u00d0\u00b2 \u00d0\u00bf\u00d0\u00b0\u00d0\u00bd\u00d0\u00b5\u00d0\u00bb\u00d0\u00b8 \u00d1\u0083\u00d0\u00bf\u00d1\u0080\u00d0\u00b0\u00d0\u00b2\u00d0\u00bb\u00d0\u00b5\u00d0\u00bd\u00d0\u00b8\u00d1\u008f \u00d1\u0085\u00d0\u00be\u00d1\u0081\u00d1\u0082\u00d0\u00b8\u00d0\u00bd\u00d0\u00b3\u00d0\u00be\u00d0\u00bc.\n                \n                <br>\n                <input type=\"button\" value=\"\u00d0\u00a2\u00d0\u00b5\u00d1\u0085\u00d0\u00bd\u00d0\u00b8\u00d1\u0087\u00d0\u00b5\u00d1\u0081\u00d0\u00ba\u00d0\u00b0\u00d1\u008f \u00d0\u00bf\u00d1\u0080\u00d0\u00be\u00d0\u00b2\u00d0\u00b5\u00d1\u0080\u00d0\u00ba\u00d0\u00b0 \u00d1\u0081\u00d0\u00b0\u00d0\u00b9\u00d1\u0082\u00d0\u00b0\" class=\"fix_button\" onclick=\"location.href = 'https://adm.tools/troubleshooting/?host=esokrat.com&error=424&request=XPp6qE2MJo4SGOHaXnDsrwAAANo&time=2019-06-07%2017:54:32'\">\n                <br><br>\n                <a href=\"https://www.ukraine.com.ua/faq/error-424.html\">\u00d0\u009f\u00d0\u00be\u00d0\u00b4\u00d1\u0080\u00d0\u00be\u00d0\u00b1\u00d0\u00bd\u00d0\u00b5\u00d0\u00b5 \u00d0\u00be \u00d0\u00b2\u00d0\u00be\u00d0\u00b7\u00d0\u00bc\u00d0\u00be\u00d0\u00b6\u00d0\u00bd\u00d1\u008b\u00d1\u0085 \u00d0\u00bf\u00d1\u0080\u00d0\u00b8\u00d1\u0087\u00d0\u00b8\u00d0\u00bd\u00d0\u00b0\u00d1\u0085 \u00d0\u00be\u00d1\u0088\u00d0\u00b8\u00d0\u00b1\u00d0\u00ba\u00d0\u00b8...</a>\n            </div>\n        </div>\n    </div>\n</div>\n\n</body>\n</html>"