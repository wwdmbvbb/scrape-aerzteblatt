import re

base_url = 'https://www.aerzteblatt.de'
search = '/suche'
parameter_name_search = 's'
parameter_name_filter = 'wo'
parameter_name_page = 'page'
search_row_regex = re.compile('jsHitlistData.*')

date_to_number = {
    'Januar': 1,
    'Februar': 2,
    'März': 3,
    'April': 4,
    'Mai': 5,
    'Juni': 6,
    'Juli': 7,
    'August': 8,
    'September': 9,
    'Oktober': 10,
    'November': 11,
    'Dezember': 12
}

text = """

<!DOCTYPE html>
<html lang="de" class="adaptive">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
        <meta name="author" content="Deutscher &Auml;rzteverlag GmbH, Redaktion Deutsches &Auml;rzteblatt" />
        <meta name="copyright" content="Deutscher &Auml;rzteverlag GmbH, Redaktion Deutsches &Auml;rzteblatt" />
        <meta name="keywords" content="" />
        <meta name="description" content="" />
        <meta name="verify-v1" content="XOK8yVksrkFRVF+7jBHYbBywfCaZ4HgxPUSPZUwvrlA=" />
        <meta name="google-site-verification" content="bWBDc3TZMhLPCj_JIFBi_f9FXvnZyWEZteCNEaICuew" />
        <meta name="apple-itunes-app" content="app-id=436133387" />
        <meta name="google-play-app" content="app-id=de.aerzteblatt" />
        <meta name="msvalidate.01" content="08AE601A86529B016B07785C1C3AA891" />
        <meta name="userid" content="0" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=0" />
        <meta property="og:site_name" content="Deutsches Ärzteblatt" />
        <meta name="format-detection" content="telephone=no" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="black" />
        <meta http-equiv="Content-Security-Policy" data-timestamp="20191115085200" content="
    default-src
        'self' *.aerzteblatt.de *.googlesyndication.com
    ;         
    script-src 
        'self' 'unsafe-inline' 'unsafe-eval' *.aerzteblatt.de *
    ;
    style-src
        'self' 'unsafe-inline' *.aerzteblatt.de *.cloudflare.com *.googleapis.com
    ; 
    media-src 
        *
    ; 
    img-src
        data: *
    ; 
    font-src
        'self' *.aerzteblatt.de *.gstatic.com cdnjs.cloudflare.com
    ; 
    connect-src
        'self' *.aerzteblatt.de *.doubleclick.net *.gstatic.com *.googleapis.com *.googlesyndication.com *.meetrics.net *.ioam.de
        *.adscale.de *.teads.tv *.google-analytics.com  *.adform.net bs.serving-sys.com
    ; 
    object-src
        'self'
    ; 
    frame-src 
        'self' *.aerzteblatt.de *.civey.com *.youtube.com *.vimeo.com *.google.com *.adition.com datawrapper.dwcdn.net 
        *.googlesyndication.com *.online-divi.de object.center *.flashtalking.com *.2mdn.net *.doubleclick.net
        *.teads.tv *.teads.mgr.consensu.org daev.jobiqo.com *.serving-sys.com *.googleapis.com       
    ;
" />

        <title>Suche</title>
        <meta property="fb:app_id" content="407569295946749" />

        <link rel="shortcut icon" type="image/x-icon" href="https://cdn.aerzteblatt.de/_icons/favicon.ico">
        <link rel="icon" type="image/x-icon" href="https://cdn.aerzteblatt.de/_icons/favicon.ico">
        <link rel="icon" type="image/gif" href="https://cdn.aerzteblatt.de/_icons/favicon.gif">
        <link rel="icon" type="image/png" href="https://cdn.aerzteblatt.de/_icons/favicon.png">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon.png">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-57x57.png" sizes="57x57">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-60x60.png" sizes="60x60">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-72x72.png" sizes="72x72">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-76x76.png" sizes="76x76">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-114x114.png" sizes="114x114">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-120x120.png" sizes="120x120">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-128x128.png" sizes="128x128">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-144x144.png" sizes="144x144">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-152x152.png" sizes="152x152">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-180x180.png" sizes="180x180">
        <link rel="apple-touch-icon" href="https://cdn.aerzteblatt.de/_icons/apple-touch-icon-precomposed.png">
        <link rel="icon" type="image/png" href="https://cdn.aerzteblatt.de/_icons/favicon-16x16.png" sizes="16x16">
        <link rel="icon" type="image/png" href="https://cdn.aerzteblatt.de/_icons/favicon-32x32.png" sizes="32x32">
        <link rel="icon" type="image/png" href="https://cdn.aerzteblatt.de/_icons/favicon-96x96.png" sizes="96x96">
        <link rel="icon" type="image/png" href="https://cdn.aerzteblatt.de/_icons/favicon-160x160.png" sizes="160x160">
        <link rel="icon" type="image/png" href="https://cdn.aerzteblatt.de/_icons/favicon-192x192.png" sizes="192x192">
        <link rel="icon" type="image/png" href="https://cdn.aerzteblatt.de/_icons/favicon-196x196.png" sizes="196x196">        
        <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css?_lnsXts=20181114135829" />
        <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css?_lnsXts=20181114135654" />
        <link rel="stylesheet" type="text/css" href="/css/font-awesome.min.css?_lnsXts=20190411084109" />
        <link rel="stylesheet" type="text/css" href="/css/dae-responsive.css?_lnsXts=20200513132549" />
        <link rel="alternate" type="application/rss+xml" title="Deutsches Ärzteblatt - Aktuelles" href="/rss/news.asp?_lnsXts=20200213123600" />

        <script src="https://cdn.aerzteblatt.de/inc/js/jquery-3.3.1.min.js"></script>
        <script src="https://cdn.aerzteblatt.de/inc/js/jquery-ui.min.js"></script>
        <script src="https://cdn.aerzteblatt.de/inc/js/bootstrap.min.js"></script>
        <script data-cms="remove" src="//script.ioam.de/iam.js"></script>
        <script src="https://www.gstatic.com/firebasejs/6.0.4/firebase-app.js"></script>
        <script src="https://www.gstatic.com/firebasejs/6.0.4/firebase-messaging.js"></script>
        <script src="https://cdn.aerzteblatt.de/inc/js/dae-responsive.js"></script>

        <script data-cms="remove" src="https://www.googletagservices.com/tag/js/gpt.js"></script>
        <script data-cms="remove">
            var rubrik = ('startseite');
            // Konfigurationsblock im Seitenkopf vor Verlinkung der adlib.js
            var Ads_BA_ADIDsite = 'aerzteblatt.de';
            var Ads_BA_ADIDsection = rubrik;        // Rubrikkuerzel
            var Ads_BA_keyword = '';    // Targeting-Kriterium
            //Ads_BA_ADIDsection = 'test';
        </script>
        <script data-cms="remove" src="https://storage.googleapis.com/adlib/arzt_adlib.js"></script>
        <script>
            document.cookie = "screenwidth=" + screen.width + "; path=/";
            document.cookie = "screenheight=" + screen.height + "; path=/";
            document.cookie = "width=" + window.innerWidth + "; path=/";
            document.cookie = "height=" + window.innerHeight + "; path=/";
            document.cookie = "screendensity=" + ((typeof(window.devicePixelRatio) != "undefined") ? window.devicePixelRatio : "1") + "; path=/";
            document.cookie = "screentouch=" + ((typeof(window.ontouchstart) != "undefined") ? "true" : "false") + "; path=/";
        </script>
    </head>
    <body class="aerzteblattResponsive.htm loggedout  " id="top" data-pagekey="/suche" data-hefttyp="">
        <div id="modalDarker"></div>
        <!-- SZM VERSION="2.0" -->
<script id="SZM">
var iam_data = {
"st":"aerztebl",
"cp":"Suche",
"sv":"i2",
"sc":"yes",
"co":""
}
iom.c(iam_data, 1);
</script>
<noscript>
<!-- SZM VERSION="2.0" -->
<img src="https://de.ioam.de/tx.io?st=aerztebl&np=Suche&mo=0" width="1" height="1" style="position:absolute;top:0;left:0" alt="szmtag" />
<!--/SZM -->
</noscript>
<!--/SZM -->


        <section id="DAEpage">
            <div class="container-fluid">

                <div class="BAad" id="Ads_BA_BS"><script>Ads_BA_AD('BS')</script></div>

                <header id="head" class="head">
                    <div class="area_wrapper area_full">
                        <div class="area_container container">
                            <div class="area area_full">
                            	<div id="DAEmetanavi-area">
                                    <div class="metanavi">
                                        <ul class="aerzteblattResponsive.htm">
                                            <li data-lang="de" class="hidden-md underline hidden-sm-down"><a title="Hinweise f&uuml;r Autoren, Interessenkonflikte, Checkliste, Rechtseinr&auml;umung" href="/archiv/fuer-autoren">
                                                <i class="icon-pencil"></i> <span class="hidden-xl-down">F&uuml;r Autoren</span>
                                            </a></li>
                                            <li data-lang="de" class="hidden-md underline hidden-sm-down"><a title="Deutsches &Auml;rzteblatt ePaper" href="/epaper">
                                                <i class="icon-book2"></i> <span class="hidden-xl-down">ePaper</span>
                                            </a></li>
                                            <li data-lang="de" class="hidden-md underline hidden-sm-down"><a title="Kontakt, Datenschutz, Mediadaten, Abo, CD-ROM, Impressum" href="/service">
                                                <i class="icon-folder-open-alt"></i> <span class="hidden-xl-down">Service</span>
                                            </a></li>
                                            <li data-lang="de" class="hidden-md underline hidden-sm-down"><a title="Anzeigen" href="/anzeigen">
                                                <i class="icon-image"></i> <span class="hidden-xl-down">Anzeigen</span>
                                            </a></li>
                                            <li data-lang="de" class="meinDAE-login clickanchor">
                                                <a title="Login „Mein DÄ“" onclick="meinDAE(); return false;"><i class="icon-user"></i> <span class="hidden-sm-down">Mein DÄ</span></a>
                                            </li>
                                            <li data-lang="de" class="DAE-search bg-daecolor"><a title="Suche" class="sucheButton" id="sucheButton1" href="javascript:;">
                                                <i class="icon-line-search white"></i> <span class="white hidden-sm-down">Suche</span>
                                            </a></li>

                                            <li data-lang="en" class="hidden-md underline hidden-sm-down"><a title="For authors" href="/int/for-authors">
                                                <i class="icon-pencil"></i> <span class="hidden-xl-down">For authors</span>
                                            </a></li>
                                            <li data-lang="en" class="hidden-md underline hidden-sm-down"><a title="Deutsches &Auml;rzteblatt International ePaper" href="/int/archive/epaper">
                                                <i class="icon-book2"></i> <span class="hidden-xl-down">ePaper</span>
                                            </a></li>
                                            <li data-lang="en" class="DAE-search bg-daecolor"><a title="Suche" class="sucheButton" id="sucheButton2" href="/int/archive">
                                                <i class="icon-line-search white"></i> <span class="white hidden-sm-down">Search</span>
                                            </a></li>


                                        </ul>
                                        <div class="clear"></div>
                                    </div>
                                </div>

                                <div id="suche" class="dialog">
                                    <h2>Suche</h2>
                                    <form action="/suche">
                                        <div class="input">
                                            <input type="search" name="s" autofocus required />
                                            <div class="active-border"></div>
                                        </div>

                                        <div class="buttons">
                                            <button><i class="icon-line2-magnifier"></i></button>
                                            <!--input type="submit" value="Suchen" autofocus /-->
                                            <!--input type="button" data-fancybox-close value="Schließen" /-->
                                        </div>

                                        <div class="filters">
                                            <div class="row">
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_16" name="wo" value="16">
                                                    <label for="sf_key_16">Deutsches Ärzteblatt</label>
                                                </div>
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_32" name="wo" value="32">
                                                    <label for="sf_key_32">Deutsches Ärzteblatt PP</label>
                                                </div>
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_256" name="wo" value="256">
                                                    <label for="sf_key_256">Perspektiven</label>
                                                </div>
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_64" name="wo" value="64">
                                                    <label for="sf_key_64">Medizin studieren</label>
                                                </div>
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_1" name="wo" value="1">
                                                    <label for="sf_key_1">News</label>
                                                </div>
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_2" name="wo" value="2">
                                                    <label for="sf_key_2">Blogs</label>
                                                </div>
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_4" name="wo" value="4">
                                                    <label for="sf_key_4">Foren</label>
                                                </div>
                                                <div class="col col-12 col-sm-6 col-md-4 col-lg-3 col-xl-3">
                                                    <input type="checkbox" id="sf_key_8" name="wo" value="8">
                                                    <label for="sf_key_8">Preise</label>
                                                </div>
                                            </div>
                                        </div>
                                    </form>
                                </div>

                                <div id="DAElogo">
                                    <a href="/"><img class="DAElogo" src="https://cdn.aerzteblatt.de/img/layout/aerzteblattResponsive/aerzteblatt_logo.svg" alt="Deutsches &Auml;rzteblatt" /></a>
                                    <div class="fgname fachgruppe "></div>
                                    <div class="fgname international" data-lang="en">INTERNATIONAL</div>
                                    <div class="fgname studieren">STUDIEREN</div>
                                </div>

                                <div id="homepages1" class="hidden-md-down">
                                    <ul>
                                        <li class="aerzteblattResponsive.htm aerzteblatt"><a href="/">Ärzteblatt</a></li>
                                        <li class="aerzteblattResponsive.htm cme"><a href="/cme">cme</a></li>
                                        <li class="aerzteblattResponsive.htm aerztestellen"><a href="/anzeigen">Ärztestellen</a></li>
                                        <li class="aerzteblattResponsive.htm studieren"><a href="/studieren">Studieren</a></li>
                                        <li class="aerzteblattResponsive.htm international"><a href="/int">English <span class="hidden-xs-down">Edition</span></a></li>
                                    </ul>
                                    <div class="clear"></div>
                                </div>
                            </div>
                        </div>

                        <div class="ico-menue"></div>

                        <nav id="DAEmainmenu">
                            <div id="nav" class="container">
                                <div id="DAElogo-inside" class="col-lg-0 col-xl-0">
                                    <a href="/"><img class="DAElogo-inside" src="https://cdn.aerzteblatt.de/img/layout/aerzteblattResponsive/aerzteblatt-logo.svg" alt="Deutsches &Auml;rzteblatt" /></a>
                                    <div id="homepages2">
                                        <ul>
                                            <li class="aerzteblattResponsive.htm aerzteblatt"><a href="/">Ärzteblatt</a></li>
                                            <li class="aerzteblattResponsive.htm cme"><a href="/cme">CME</a></li>
                                            <li class="aerzteblattResponsive.htm aerztestellen"><a href="/anzeigen">Ärztestellen</a></li>
                                            <li class="aerzteblattResponsive.htm studieren"><a href="/studieren">Studieren</a></li>
                                            <li class="aerzteblattResponsive.htm international"><a href="/int">English <span class="hidden-xs-down">Edition</span></a></li>
                                        </ul>
                                        <div class="clear"></div>
                                    </div>
                                </div>
                                <ul class="menuNav">
<li class="dropanchor menu235"><a href="/">Home
 <span class="sep">|</span></a></li>
<li class="dropanchor menu236"><a href="/archiv">Archiv
 <span class="sep">|</span></a><div class="sub dropdown"><div class="container">
    <div class="row">
        <div class="col-12 col-12 col-xs-12 col-lg-4">
            <h2 class="d-none d-lg-block">Rubriken</h2>
            <div class="subnavi multi-column">
                <ul>
<li class="dropanchor"><a href="/archiv/suche" class="" >Recherche</a></li>
<li class="dropanchor"><a href="/archiv/daetitel" class="" >DÄ-Titel</a></li>
<li class="dropanchor"><a href="/archiv/pptitel" class="" >PP-Titel</a></li>
<li class="dropanchor"><a href="/archiv/perspektiven" class="" >Perspektiven</a></li>
<li class="dropanchor"><a href="/epaper" class="" >ePaper</a></li>
<li class="dropanchor"><a href="/archiv/zeitreise" class="" >Zeitreise</a></li>
<li class="dropanchor"><a href="/archiv/kommentare" class="" >Kommentare</a></li>
<li class="dropanchor"><a href="/meinDAE#clipboards" class="" >Merkliste</a></li>
</ul>

            </div>                        
        </div>
        <div class="col-8 d-none d-lg-block">
            <h2>DÄ-Titel</h2>
            <div class="row ausgaben"><div class="col">
    <a href="/archiv/inhalt?heftid=6451"><img alt="Ausgabe 21/2020" loading="lazy" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDIxLmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6ODAw
fX19" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDIxLmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6MTQw
MH19fQ==" data-fullurl="https://cdn.aerzteblatt.de/titel/117/titel21.jpg" /></a>
</div>
<div class="col">
    <a href="/archiv/inhalt?heftid=6452"><img alt="Ausgabe 20/2020" loading="lazy" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDIwLmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6ODAw
fX19" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDIwLmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6MTQw
MH19fQ==" data-fullurl="https://cdn.aerzteblatt.de/titel/117/titel20.jpg" /></a>
</div>
<div class="col">
    <a href="/archiv/inhalt?heftid=6453"><img alt="Ausgabe 19/2020" loading="lazy" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE5LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6ODAw
fX19" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE5LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6MTQw
MH19fQ==" data-fullurl="https://cdn.aerzteblatt.de/titel/117/titel19.jpg" /></a>
</div>
<div class="col">
    <a href="/archiv/inhalt?heftid=6454"><img alt="Ausgabe 18/2020" loading="lazy" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE4LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6ODAw
fX19" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE4LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6MTQw
MH19fQ==" data-fullurl="https://cdn.aerzteblatt.de/titel/117/titel18.jpg" /></a>
</div>
<div class="col">
    <a href="/archiv/inhalt?heftid=6455"><img alt="Ausgabe 17/2020" loading="lazy" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE3LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6ODAw
fX19" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE3LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6MTQw
MH19fQ==" data-fullurl="https://cdn.aerzteblatt.de/titel/117/titel17.jpg" /></a>
</div>
<div class="col">
    <a href="/archiv/inhalt?heftid=6456"><img alt="Ausgabe 16/2020" loading="lazy" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE2LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6ODAw
fX19" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJ0aXRlbFwvMTE3XC90aXRl
bDE2LmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJpbnNpZGUiLCJ3aWR0aCI6MTQw
MH19fQ==" data-fullurl="https://cdn.aerzteblatt.de/titel/117/titel16.jpg" /></a>
</div></div>
        </div>
    </div>
    <div class="row themen d-none d-xl-block">
        <div class="col-12 col-12 col-xs-12">
            <h2>Aktuell</h2>
            <ul><li><a href="/archiv/213829/Coronakrise-Kinder-haben-das-Recht-auf-Bildung">Coronakrise</a></li>

<li><a href="/archiv/213869/Neurologische-Manifestationen-Wie-COVID-19-die-Nerven-tangiert">Neurologische Manifestationen</a></li>

<li><a href="/archiv/213772/Herzinsuffizienz-Lebensstilbedingte-Faktoren-erhoehen-das-Risiko-bei-Frauen-staerker-als-bei-Maennern">Herzinsuffizienz</a></li>

<li><a href="/archiv/213808/Medizinische-Rehabilitation-Einrichtungen-in-der-Coronakrise">Medizinische Rehabilitation</a></li>

<li><a href="/archiv/214060/Zoeliakie-Das-Sterberisiko-ist-trotz-besserer-Diagnostik-und-glutenfreier-Lebensmittel-erhoeht">Zoeliakie</a></li>

<li><a href="/archiv/213807/Sterblichkeitsrisiko-bei-Herz-Kreislauf-Erkrankungen-Renin-Angiotensin-Blockade-auch-bei-Verschlechterung-der-Nierenfunktion-sinnvoll">Sterblichkeitsrisiko bei Herz-Kreislauf-Erkrankungen</a></li>

<li><a href="/archiv/214065/Rueckkehr-zur-Regelversorgung-Chronische-Krankheiten-machen-keine-Coronapause">Rückkehr zur Regelversorgung</a></li>

<li><a href="/archiv/213787/Neurologie-Leitlinie-zu-Gedaechtnisstoerungen-bei-neurologischen-Erkrankungen-aktualisiert">Neurologie</a></li>

<li><a href="/archiv/213769/SARS-CoV-2-Triage-fuer-den-Impfstoff">SARS-CoV-2</a></li>

<li><a href="/archiv/214063/Rheuma-amp-Co-COVID-19-bei-Immunsuppression">Rheuma &amp; Co</a></li>
</ul>
        </div>
    </div>
    <div class="clear"></div>
</div></div></li>
<li class="dropanchor menu237"><a href="/nachrichten">News
 <span class="sep">|</span></a><div class="sub dropdown"><div class="container">
    <div class="row">
        <div class="col-12 col-12 col-xs-12 col-lg-4">
            <h2 class="d-none d-lg-block">Rubriken</h2>
            <div class="subnavi multi-column">
                <ul>
<li class="dropanchor"><a href="/nachrichten/politik" class="" >Politik</a></li>
<li class="dropanchor"><a href="/nachrichten/medizin" class="" >Medizin</a></li>
<li class="dropanchor"><a href="/nachrichten/aerzteschaft" class="" >Ärzteschaft</a></li>
<li class="dropanchor"><a href="/nachrichten/ausland" class="" >Ausland</a></li>
<li class="dropanchor"><a href="/nachrichten/vermischtes" class="" >Vermischtes</a></li>
<li class="dropanchor"><a href="/nachrichten/hochschulen" class="" >Hochschulen</a></li>
<li class="dropanchor"><a href="/nachrichten/sw" class="" >Themen</a></li>
<li class="dropanchor"><a href="/nachrichten/bildergalerien" class="" >Bildergalerien</a></li>
<li class="dropanchor"><a href="/nachrichten/videos" class="" >Videos</a></li>
<li class="dropanchor"><a href="/nachrichten/kommentare" class="" >Kommentare</a></li>
<li class="dropanchor"><a href="/meinDAE#clipboards" class="" >Merkliste</a></li>
</ul>

            </div>                        
        </div>
        <div class="col-8 d-none d-lg-block">
            <h2>Aktuell</h2>
            <div class="row menunews">

<div class="col-4 col">
    <a href="/nachrichten/SARS-CoV-2">
    <div><img loading="lazy"  src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzAz
XC9pbWcyMjg1NTg0NzIuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzAz
XC9pbWcyMjg1NTg0NzIuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2020/03/img228558472.jpg" alt="" alt="" /></div>
    <div class="rubrik">Coronavirus</div>
    <div class="titel">Aktueller Stand zu<br/>SARS-CoV-2, COVID-19</div>
</a>
</div>

                <div class="col-4 col">
    <a href="/nachrichten/113034/COVID-19-Folgen-Weniger-Herzinfarktpatienten-und-geringere-Impfquote">
    <div><img loading="lazy"  src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzA1
XC9pbWcyNDM0MzUyODMuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzA1
XC9pbWcyNDM0MzUyODMuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2020/05/img243435283.jpg" alt="COVID-19-Folgen: Weniger Herzinfarktpatienten und geringere Impfquote" alt="" alt="" /></div>
    <div class="rubrik">Medizin</div>
    <div class="titel">COVID-19-Folgen: Weniger Herzinfarktpatienten und geringere Impfquote</div>
</a>
</div>
<div class="col-4 col">
    <a href="/nachrichten/113064/COVID-19-Hohe-Sterberate-unter-Intensivpatienten-in-New-York">
    <div><img loading="lazy"  src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzA1
XC9pbWcyNDM0MzYxNjAuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzA1
XC9pbWcyNDM0MzYxNjAuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2020/05/img243436160.jpg" alt="COVID-19: Hohe Sterberate unter Intensivpatienten in New York" alt="" alt="" /></div>
    <div class="rubrik">Medizin</div>
    <div class="titel">COVID-19: Hohe Sterberate unter Intensivpatienten in New York</div>
</a>
</div>
            </div>
        </div>
    </div>
    <div class="row themen d-none d-xl-block">
        <div class="col-12 col-12 col-xs-12">
            <h2>Themen</h2>
            <ul><li><a href="/nachrichten/sw/COVID%2D19">COVID-19</a></li>

<li><a href="/nachrichten/sw/Infektionen">Infektionen</a></li>

<li><a href="/nachrichten/sw/Virologie">Virologie</a></li>

<li><a href="/nachrichten/sw/Infektionsschutz">Infektionsschutz</a></li>

<li><a href="/nachrichten/sw/Impfen">Impfen</a></li>

<li><a href="/nachrichten/sw/Berufe%20im%20Gesundheitswesen">Berufe im Gesundheitswesen</a></li>

<li><a href="/nachrichten/sw/Nephrologie">Nephrologie</a></li>

<li><a href="/nachrichten/sw/Grippe%2FInfluenza">Grippe/Influenza</a></li>

<li><a href="/nachrichten/sw/Hygiene">Hygiene</a></li>

<li><a href="/nachrichten/sw/Europ%E4ische%20Union">Europäische Union</a></li>

<li><a href="/nachrichten/sw/Psychische%20Erkrankungen">Psychische Erkrankungen</a></li>

<li><a href="/nachrichten/sw/Kindergesundheit">Kindergesundheit</a></li>

<li><a href="/nachrichten/sw/Radiologie">Radiologie</a></li>

<li><a href="/nachrichten/sw/K%FCnstliche%20Intelligenz">Künstliche Intelligenz</a></li>

<li><a href="/nachrichten/sw/Schwangerschaft%20und%20Geburt">Schwangerschaft und Geburt</a></li>
</ul>
        </div>
    </div>
</div>
</div></li>
<li class="dropanchor menu335"><a href="/nachrichten/sw">Themen
 <span class="sep">|</span></a><div class="sub dropdown"><div class="container">
    <div class="row">
        <div class="col-12 col-12 col-xs-12 col-lg-4">
            <div class="subnavi">
                <h2>Rubriken</h2>
                <ul>
<li class="dropanchor"><a href="/nachrichten/sw" class="" >Aktuelle Themen</a></li>
<li class="dropanchor"><a href="/nachrichten/meinethemen" class="" >Meine Themen</a></li>
</ul>

            </div>                        
        </div>
        <div class="hidden col-8 d-none d-lg-block">
            <h2>Aktuell</h2>
            <div class="row menunews"><div class="col-4 col">
    <a href="/nachrichten/sw/COVID%2D19">
    <div><img src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzAx
XC9pbWcxOTg4ODY3ODIuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjozMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMjBcLzAx
XC9pbWcxOTg4ODY3ODIuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2020/01/img198886782.jpg" style="object-position:50% 50%   " alt="COVID-19" alt="" alt="" /></div>
    <div class="rubrik">COVID-19</div>
</a>
</div>
<div class="col-4 col">
    <a href="/nachrichten/sw/Infektionen">
    <div><img src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTJcLzEy
XC9pbWczMzk1NDMyNi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsiZml0IjoiaW5zaWRlIiwi
d2lkdGgiOjMwMH19fQ==" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTJcLzEy
XC9pbWczMzk1NDMyNi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsiZml0IjoiaW5zaWRlIiwi
d2lkdGgiOjE0MDB9fX0=" data-fullurl="https://cdn.aerzteblatt.de/bilder/2012/12/img33954326.jpg" style="object-position:50% 50%   " alt="Infektionen" alt="" alt="" /></div>
    <div class="rubrik">Infektionen</div>
</a>
</div>
<div class="col-4 col">
    <a href="/nachrichten/sw/Virologie">
    <div><img src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTVcLzA2
XC9pbWcxMjIzMTQyMDYuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjozMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTVcLzA2
XC9pbWcxMjIzMTQyMDYuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2015/06/img122314206.jpg" style="object-position:50% 50%   " alt="Virologie" alt="" alt="" /></div>
    <div class="rubrik">Virologie</div>
</a>
</div></div>
        </div>
    </div>
</div>
</div></li>
<li class="dropanchor menu238"><a href="/dae-plus">DÄ plus
 <span class="sep">|</span></a><div class="sub dropdown"><div class="container">
    <div class="row">
         <div class="col-12 col-12 col-xs-12 col-lg-4">
            <h2 class="d-none d-lg-block">Rubriken</h2>
            <div class="subnavi multi-column">
                <ul>
<li class="dropanchor"><a href="/foren" class="" >Foren</a></li>
<li class="dropanchor"><a href="/blogs" class="" >Blogs</a></li>
<li class="dropanchor"><a href="/dae-plus/zusatzinfo" class="" >Zusatzinfo</a></li>
<li class="dropanchor"><a href="/dae-plus/literaturverzeichnisse" class="" >Literatur</a></li>
<li class="dropanchor"><a href="/dae-plus/serien" class="" >Serien</a></li>
<li class="dropanchor"><a href="/dae-plus/bekanntgaben" class="" >Bekanntgaben</a></li>
<li class="dropanchor"><a href="/dae-plus/jahresinhaltsverzeichnisse" class="" >Jahresinhalt</a></li>
<li class="dropanchor"><a href="/foerderpreise" class="" >Förderpreise</a></li>
</ul>

            </div>                        
        </div>
        <div class="col-8 d-none d-lg-block">
            <h2>Aktuell</h2>
            <div class="row menunews"><div class="col">
    <a href="/blog/112154/Coronavirus-Versoehnlicher-Ausklang">
    <img loading="lazy" alt="" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTNcLzA1
XC9pbWc0OTg0OTc1Ni5naWYiLCJlZGl0cyI6eyJyZXNpemUiOnsiZml0IjoiaW5zaWRlIiwi
d2lkdGgiOjIwMH19fQ==" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTNcLzA1
XC9pbWc0OTg0OTc1Ni5naWYiLCJlZGl0cyI6eyJyZXNpemUiOnsiZml0IjoiaW5zaWRlIiwi
d2lkdGgiOjE0MDB9fX0=" data-fullurl="https://cdn.aerzteblatt.de/bilder/2013/05/img49849756.gif" />
    <div class="rubrik">Vom Arztdasein in Amerika</div>
    <div class="titel">Coronavirus: Versöhnlicher Ausklang</div>
    </a>
</div>

<div class="col">
    <a href="/forum/135312">
    <img loading="lazy" alt="" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMThcLzA2
XC9pbWcxMzg5ODkwMjkucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMThcLzA2
XC9pbWcxMzg5ODkwMjkucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2018/06/img138989029.png" />
    <div class="rubrik">Kommentare News</div>
    <div class="titel">Fachliche Diskussion</div>
    </a>
</div>

<div class="col">
    <a href="/dae-plus/zusatzinfo">
    <img loading="lazy" alt="" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTJcLzAx
XC9pbWcxNjAzMTYucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIsIndp
ZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTJcLzAx
XC9pbWcxNjAzMTYucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIsIndp
ZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2012/01/img160316.png" />
    <div class="rubrik">DÄ plus</div>
    <div class="titel">Zusatzinformationen, Literaturverzeichnisse</div>
    </a>
</div>
</div>
        </div>
    </div>
</div></div></li>
<li class="dropanchor menu239"><a href="/politik">Politik
 <span class="sep">|</span></a><div class="sub dropdown"><div class="container">
    <div class="row">
        <div class="col-12 col-12 col-xs-12 col-lg-4">
            <h2 class="d-none d-lg-block">Rubriken</h2>
            <div class="subnavi multi-column">
                <ul>
<li class="dropanchor"><a href="/nachrichten/politik" class="" >News (Online)</a></li>
<li class="dropanchor"><a href="/politik/politik" class="" >Gesundheitspolitik</a></li>
<li class="dropanchor"><a href="/politik/themen-der-zeit" class="" >Themen der Zeit</a></li>
<li class="dropanchor"><a href="/politik/management" class="" >Management</a></li>
<li class="dropanchor"><a href="/politik/apps" class="" >Apps</a></li>
<li class="dropanchor"><a href="/politik/personalien" class="" >Personalien</a></li>
</ul>

            </div>                        
        </div>
        <div class="col-8 d-none d-lg-block">
            <h2>Aktuell</h2>
            <div class="row menunews">
                <div class="col">
                    <a href="/politik/politik">
                    <img alt="Politik" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTVcLzA2
XC9pbWcxMjExODU1MTAuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTVcLzA2
XC9pbWcxMjExODU1MTAuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2015/06/img121185510.jpg" />
                    <div class="rubrik">Politik</div>
                    </a>
                </div>

                <div class="col">
                    <a href="/politik/themen-der-zeit">
                    <img alt="" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTZcLzEx
XC9pbWcxMzY2MDY2MjYuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTZcLzEx
XC9pbWcxMzY2MDY2MjYuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2016/11/img136606626.jpg" />
                    <div class="rubrik">Themen der Zeit</div>
                    </a>
                </div>

                <div class="col">
                     <a href="/nachrichten/politik/">
                     <img alt="" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTdcLzEw
XC9pbWcxMzc1ODA1NzguanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTdcLzEw
XC9pbWcxMzc1ODA1NzguanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2017/10/img137580578.jpg" />
                     <div class="rubrik">News</div>
                    </a>
                </div>

            </div>
        </div>
    </div>
    <div class="row themen d-none d-xl-block">
        <div class="col-12 col-12 col-xs-12">
            <h2>Themen</h2>
            <ul><li><a href="/archiv/213808/Medizinische-Rehabilitation-Einrichtungen-in-der-Coronakrise">Medizinische Rehabilitation</a></li>

<li><a href="/archiv/214065/Rueckkehr-zur-Regelversorgung-Chronische-Krankheiten-machen-keine-Coronapause">Rückkehr zur Regelversorgung</a></li>

<li><a href="/archiv/213770/Medizinstudium-in-Pandemiezeiten-Es-geht-weiter-trotzdem">Medizinstudium in Pandemiezeiten</a></li>

<li><a href="/archiv/213854/Coronaausbruch-im-Krankenhaus-Ein-Restrisiko-bleibt-bestehen">Coronaausbruch im Krankenhaus</a></li>

<li><a href="/archiv/213790/Krankenhaeuser-Rueckkehr-in-den-Regelbetrieb">Krankenhäuser</a></li>

<li><a href="/archiv/213861/Corona-Warn-App-Neustart-mit-dezentraler-Loesung">Corona-Warn-App</a></li>

<li><a href="/archiv/213758/Triage-bei-einer-Pandemie-Bislang-gesetzlich-ungeregelt">Triage bei einer Pandemie</a></li>

<li><a href="/archiv/213897/Zweites-Pandemiegesetz-Mehr-Meldepflichten-und-Tests">Zweites Pandemiegesetz</a></li>

<li><a href="/archiv/214045/Coronapandemie-Rolle-der-Zentralen-Notaufnahme">Coronapandemie</a></li>

<li><a href="/archiv/214125/Bundestag-Die-Folgen-der-Pandemie-abfedern">Bundestag</a></li>
</ul>
        </div>
    </div>
</div>
</div></li>
<li class="dropanchor menu240"><a href="/medizin">Medizin
 <span class="sep">|</span></a><div class="sub dropdown"><div class="container">
    <div class="row">
        <div class="col-12 col-12 col-xs-12 col-lg-4">
            <h2 class="d-none d-lg-block">Fachgebiete</h2>
            <div class="subnavi multi-column fachgebiete">
                <ul>
<li class="dropanchor"><a href="/nachrichten/medizin" class="" >News</a></li>
<li class="dropanchor"><a href="/medizin/medizinreport" class="" >Medizinreport</a></li>
<li class="dropanchor"><a href="/medizin/wissenschaft" class="" >Wissenschaft</a></li>
<li class="dropanchor"><a href="/fachgebiete/kardiologie" class="kardiologie" >Kardiologie</a></li>
<li class="dropanchor"><a href="/fachgebiete/Neurologie" class="neurologie" >Neurologie</a></li>
<li class="dropanchor"><a href="/fachgebiete/Urologie" class="urologie" >Urologie</a></li>
<li class="dropanchor"><a href="/fachgebiete/Onkologie" class="onkologie" >Onkologie</a></li>
<li class="dropanchor"><a href="/fachgebiete/Pneumologie" class="pneumologie" >Pneumologie</a></li>
</ul>

            </div>                        
        </div>
        <div class="col-8 d-none d-lg-block">
            <h2>Aktuell</h2>
            <div class="row menunews">

                <div class="col">
                    <a href="/medizin/wissenschaft">
                    <img alt="Wissenschaft" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTZcLzAz
XC9pbWcxMzU2NzM5OTYuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTZcLzAz
XC9pbWcxMzU2NzM5OTYuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2016/03/img135673996.jpg" />
                    <div class="rubrik">Wissenschaft</div>
                    </a>
                </div>

                <div class="col">
                    <a href="/medizin/medizinreport">
                    <img alt="Medizinreport" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTRcLzEy
XC9pbWcxMDQ3NDE4NjUuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMTRcLzEy
XC9pbWcxMDQ3NDE4NjUuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2014/12/img104741865.jpg" />
                    <div class="rubrik">Medizinreport</div>
                    </a>
                </div>

                <div class="col">
                     <a href="/archiv/perspektiven/">
                     <img alt="Perspektiven" style="object-position: top center" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMThcLzAy
XC9pbWcxMzc4Nzc4NDQuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMThcLzAy
XC9pbWcxMzc4Nzc4NDQuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2018/02/img137877844.jpg" />
                     <div class="rubrik">Perspektiven</div>
                    </a>
                </div>

                <div class="col">
                     <a href="/nachrichten/medizin/">
                     <img alt="News" src="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMThcLzAx
XC9pbWcxMzc3NzczMjkuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoyMDB9fX0=" data-bigsrc="https://img.aerzteblatt.de/eyJidWNrZXQiOiJjZG4uYWVyenRlYmxhdHQuZGUiLCJrZXkiOiJiaWxkZXJcLzIwMThcLzAx
XC9pbWcxMzc3NzczMjkuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7ImZpdCI6Imluc2lkZSIs
IndpZHRoIjoxNDAwfX19" data-fullurl="https://cdn.aerzteblatt.de/bilder/2018/01/img137777329.jpg" />
                     <div class="rubrik">News</div>
                    </a>
                </div>

            </div>
        </div>
    </div>
    <div class="row themen d-none d-xl-block">
        <div class="col-12 col-12 col-xs-12">
            <h2>Artikel</h2>
            <ul><li><a href="/archiv/213869/Neurologische-Manifestationen-Wie-COVID-19-die-Nerven-tangiert">Neurologische Manifestationen</a></li>

<li><a href="/archiv/213772/Herzinsuffizienz-Lebensstilbedingte-Faktoren-erhoehen-das-Risiko-bei-Frauen-staerker-als-bei-Maennern">Herzinsuffizienz</a></li>

<li><a href="/archiv/214060/Zoeliakie-Das-Sterberisiko-ist-trotz-besserer-Diagnostik-und-glutenfreier-Lebensmittel-erhoeht">Zoeliakie</a></li>

<li><a href="/archiv/213807/Sterblichkeitsrisiko-bei-Herz-Kreislauf-Erkrankungen-Renin-Angiotensin-Blockade-auch-bei-Verschlechterung-der-Nierenfunktion-sinnvoll">Sterblichkeitsrisiko bei...</a></li>

<li><a href="/archiv/214063/Rheuma-amp-Co-COVID-19-bei-Immunsuppression">Rheuma &amp; Co</a></li>

<li><a href="/archiv/214070/Umgang-mit-Corona-Toten-Obduktionen-sind-keinesfalls-obsolet">Umgang mit Corona-Toten</a></li>

<li><a href="/archiv/213627/Parosmie-als-fruehes-Symptom-bei-akuter-SARS-CoV-2-Infektion">Parosmie als frühes Symptom bei akuter...</a></li>

<li><a href="/archiv/213642/SARS-CoV-2-bei-Mitarbeitern-einer-grossen-Universitaetsklinik">SARS-CoV-2 bei Mitarbeitern einer großen...</a></li>

<li><a href="/archiv/213643/Geschaetzte-Nutzung-von-Intensivbetten-aufgrund-von-COVID-19-in-Deutschland-im-zeitlichen-Verlauf">Geschätzte Nutzung von Intensivbetten aufgrund von...</a></li>

<li><a href="/archiv/213644/Epidemiologische-Masszahlen-im-Rahmen-der-COVID-19-Pandemie">Epidemiologische Maßzahlen im Rahmen der...</a></li>
</ul>
        </div>
    </div>
</div>
</div></li>
<li class="dropanchor menu340"><a href="/cme">cme
 <span class="sep">|</span></a></li>
<li class="dropanchor menu241"><a href="/klinik">Klinik
 <span class="sep">|</span></a></li>
<li class="dropanchor menu242"><a href="/praxis">Praxis
 <span class="sep">&nbsp;</span></a></li>
</ul>

                                <div class="clear"></div>
                            </div>
                            <div class="clear"></div>
                        </nav>
                    </div>
                    <div class="clear"></div>
                </header>

                <section id="DAEcontent" data-pageid="2089">
                    <div class="area_wrapper area_full fachgruppeMenu">
                        <div class="area_container">
                            <div class="area area_full"></div>
                        </div>
                    </div>
                    <div class="area_wrapper area_full daebreadcrumb">
                        <div class="area_container">
                            <div class="area area_full daebreadcrumb">Suche</div>
                        </div>
                    </div>
                    <div class="clear"></div>
                    <div class="BAad hidden-md-down" id="Ads_BA_FLB"><!-- AdBusiness Flash-Bühne -->
                        <script>Ads_BA_AD('FLB')</script>
                    </div>                    

                   	<div class="area_wrapper  area area_left" id="p0000_a7665">
<div class="area_container ">
<div id="p2089_a7665" class="area area_left  row" data-pageid="2089" data-areaid="7665">
<div id="p2089_a7665_c47078" data-pageid="2089" data-areaid="7665" data-boxmeta="" data-boxid="47078" data-status="0" class="col col-12 col-12 col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"><!-- START ÄRZTEBLATT - Großer Titel -->
<div class="bigTitle adaptive-standard">
    <div class="subhead"></div>
    <h1 class="title"><span>Suchergebnisse</span></h1>
    <div class="message nr1"> 
 <!-- LINK --><!-- LINK -->

<div class="linkListe">


</div>
<div class="clear"></div></div>

</div>
<!-- END ÄRZTEBLATT - Großer Titel --></div>
<div id="p2089_a7665_c50258" data-pageid="2089" data-areaid="7665" data-boxmeta="" data-boxid="50258" data-status="0" class="col col-12 col-xs-12 col-sm-12 col-md-12 col-lg-0 col-xl-0 noprint search-filter"><!-- START ÄRZTEBLATT - Suchbox -->
<div>
   <div class="searchbox">
<div class="bg-daecolor">
       <div class="message nr1">
<div class="subhead"></div>


<div class="text"><div class="suchfilter">
<div class="suchMaske"><form action="/suche"><div class="label">Suchbegriff(e)</div><input type="search" name="s" value="klimawandel" /><div class="label">Suchen in</div><ul class="filters"><li><input checked type="checkbox" id="sf_key_16" name="wo" value="16" /><label for="sf_key_16">Deutsches Ärzteblatt</label></li><li><input  type="checkbox" id="sf_key_32" name="wo" value="32" /><label for="sf_key_32">Deutsches Ärzteblatt PP</label></li><li><input  type="checkbox" id="sf_key_256" name="wo" value="256" /><label for="sf_key_256">Perspektiven</label></li><li><input  type="checkbox" id="sf_key_128" name="wo" value="128" /><label for="sf_key_128">PRAXiS</label></li><li><input  type="checkbox" id="sf_key_64" name="wo" value="64" /><label for="sf_key_64">Medizin studieren</label></li><li><input  type="checkbox" id="sf_key_1" name="wo" value="1" /><label for="sf_key_1">News</label></li><li><input  type="checkbox" id="sf_key_2" name="wo" value="2" /><label for="sf_key_2">Blogs</label></li><li><input  type="checkbox" id="sf_key_4" name="wo" value="4" /><label for="sf_key_4">Foren</label></li><li><input  type="checkbox" id="sf_key_8" name="wo" value="8" /><label for="sf_key_8">Preise</label></li></ul><input type="submit" value="Suchen" /> <input type="button" value="Zur erweiterten Suche" onclick="location='/archiv/suche'"/></form></div>
</div>
</div>
<div class="clear"></div></div>

       <div class="clear"></div>
   </div>
</div>
</div>
<!-- END ÄRZTEBLATT - Suchbox--></div>
<div id="p2089_a7665_c50320" data-pageid="2089" data-areaid="7665" data-boxmeta="" data-boxid="50320" data-status="0" class="col col-12 col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"><!-- START ÄRZTEBLATT - Standard (ohne Linien) -->
<div>
   <div class="adaptive-standard without-all">
       <div class="message nr1">
<div class="subhead"></div>


<div class="text"><div class="rechercheinfos">Ihre Suche ergab 100 Treffer<div class="restrictions"><div class="restriction"><span class="field">Volltext</span> <span class="operator">=</span> <span class="value">klimawandel</span></div></div></div> <!-- LINK --><!-- LINK --></div>

<div class="linkListe">


</div>
<div class="clear"></div></div>

       <div class="clear"></div>
   </div>
</div>
<!-- END ÄRZTEBLATT - Standard (ohne Linien) --></div>
<div id="p2089_a7665_c50322" data-pageid="2089" data-areaid="7665" data-boxmeta="" data-boxid="50322" data-status="0" class="col col-12 col-xs-12 col-sm-12 col-md-12 col-lg-0 col-xl-0"><!-- START ÄRZTEBLATT - Suchbox -->
<div>
   <div class="searchbox">
<div class="bg-daecolor">
       <div class="message nr1">
<div class="subhead"></div>
<h2>Ihre Suche eingrenzen</h2>

<div class="text"></div>
<div class="clear"></div></div>

       <div class="clear"></div>
   </div>
</div>
</div>
<!-- END ÄRZTEBLATT - Suchbox--></div>
<div id="p2089_a7665_c50321" data-pageid="2089" data-areaid="7665" data-boxmeta="" data-boxid="50321" data-status="0" class="col col-12 col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"><!-- START ÄRZTEBLATT - Standard (ohne Linien) -->
<div>
   <div class="adaptive-standard without-all">
       <div class="message nr1">
<div class="subhead"></div>


<div class="text"><br /> <!-- LINK --><!-- LINK --></div>

<div class="linkListe">


</div>
<div class="clear"></div></div>

       <div class="clear"></div>
   </div>
</div>
<!-- END ÄRZTEBLATT - Standard (ohne Linien) --></div>
<div id="p2089_a7665_c44544" data-pageid="2089" data-areaid="7665" data-boxmeta="" data-boxid="44544" data-status="0" class="col col-12 col-12 col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"><!-- START ÄRZTEBLATT - Standard (ohne Linie drunter) -->
<div>
   <div class="adaptive-standard standardbox">
       <div class="message nr1">
<div class="subhead"></div>


<div class="text"><div class="documentinfobar top"><div class="mid"><div class="navigator" data-pagecount="20"><a href="#" class="naviButton navigatorButtonLeftLeft"><div class="navigatorButton navigatorLeftLeft"><i class="fa fa-angle-double-left"></i></div></a><a href="#" class="naviButton navigatorButtonLeft"><div class="navigatorButton navigatorLeft"><i class="fa fa-angle-left"></i></div></a><span class="navigatorText">Seite <span class="page">1</span> von 20<span class="hidden-sm-down">, Treffer 1&ndash;5 von 100</span></span><a href="?s=klimawandel&wo=16&page=20" class="naviButton navigatorButtonRightRight"><div class="navigatorButton navigatorRightRight"><i class="fa fa-angle-double-right"></i></div></a><a href="?s=klimawandel&wo=16&page=2" class="naviButton navigatorButtonRight"><div class="navigatorButton navigatorRight"><i class="fa fa-angle-right"></i></div></a></div></div></div><div class="jsHitlist" id="jsHitlist-9c4b37ede922622b827a678d89132357">
<div class="jsHitlistRecord row" data-src="16"><div class="jsHitlistNr col col-1 ">1.</div><div class="jsHitlistData col col-11 col-md-8"><div class="jsHitlistCategory">BRIEFE</div><div class="jsHitlistTitle"><a href="treffer?mode=s&wo=16&typ=16&aid=214149&s=klimawandel">Klimawandel: Es geht nicht um die Ärzte</a></div><div class="jsHitlistAuthor"><span class="author">Barabasch, Richard</span></div><div class="jsHitlistSrc">Dtsch Arztebl 2020; 117(21): A-1128 / B-947</div></div><div class="jsHitlistImage col hidden-sm-down col-3"><div class="ratio ratio_16_9"><a href="treffer?mode=s&wo=16&typ=16&aid=214149&s=klimawandel"><img class="thumb-1" src="/pdf/117/21/a1128.jpg" alt="Klimawandel: Es geht nicht um die Ärzte" /></a></div></div></div>
<div class="jsHitlistRecord row" data-src="16"><div class="jsHitlistNr col col-1 ">2.</div><div class="jsHitlistData col col-11 col-md-8"><div class="jsHitlistCategory">SEITE EINS</div><div class="jsHitlistTitle"><a href="treffer?mode=s&wo=16&typ=16&aid=213849&s=klimawandel">Wissenschaftler: Keine Hellseher</a></div><div class="jsHitlistAuthor"><span class="author">Schmedt, Michael</span></div><div class="jsHitlistSrc">Dtsch Arztebl 2020; 117(19): A-973 / B-821</div></div><div class="jsHitlistImage col hidden-sm-down col-3"><div class="ratio ratio_16_9"><a href="treffer?mode=s&wo=16&typ=16&aid=213849&s=klimawandel"><img class="thumb-1" src="/pdf/117/19/a973.jpg" alt="Wissenschaftler: Keine Hellseher" /></a></div></div></div>
<div class="jsHitlistRecord row" data-src="16"><div class="jsHitlistNr col col-1 ">3.</div><div class="jsHitlistData col col-11 col-md-8"><div class="jsHitlistCategory">MEDIZINREPORT: Interview</div><div class="jsHitlistTitle"><a href="treffer?mode=s&wo=16&typ=16&aid=213763&s=klimawandel">Interview mit Prof. Dr. Dr. med. Sabine Gabrysch, Professorin für Klimawandel und Gesundheit an der Charité – Universitätsmedizin Berlin und Ko-Leiterin der Abteilung für Klimaresilienz am Potsdam-Institut für Klimafolgenforschung: „Ärzte könnten zu wichtigen Akteuren des Wandels werden“</a></div><div class="jsHitlistAuthor"><span class="author">Eckert, Nadine</span>; <span class="author">Maibach-Nagel, Egbert</span></div><div class="jsHitlistSrc">Dtsch Arztebl 2020; 117(18): A-934 / B-789</div></div><div class="jsHitlistImage col hidden-sm-down col-3"><div class="ratio ratio_16_9"><a href="treffer?mode=s&wo=16&typ=16&aid=213763&s=klimawandel"><img class="thumb-1" src="/pdf/117/18/a934.jpg" alt="Interview mit Prof. Dr. Dr. med. Sabine Gabrysch, Professorin für Klimawandel und Gesundheit an der Charité – Universitätsmedizin Berlin und Ko-Leiterin der Abteilung für Klimaresilienz am Potsdam-Institut für Klimafolgenforschung: „Ärzte könnten zu wichtigen Akteuren des Wandels werden“" /></a></div></div></div>
<div class="jsHitlistRecord row" data-src="16"><div class="jsHitlistNr col col-1 ">4.</div><div class="jsHitlistData col col-11 col-md-8"><div class="jsHitlistCategory">BRIEFE</div><div class="jsHitlistTitle"><a href="treffer?mode=s&wo=16&typ=16&aid=213378&s=klimawandel">Green Hospitals: Ohne Verstand</a></div><div class="jsHitlistAuthor"><span class="author">Nolte, Stephan Heinrich</span></div><div class="jsHitlistSrc">Dtsch Arztebl 2020; 117(14): A-724 / B-613</div></div><div class="jsHitlistImage col hidden-sm-down col-3"><div class="ratio ratio_16_9"><a href="treffer?mode=s&wo=16&typ=16&aid=213378&s=klimawandel"><img class="thumb-1" src="/pdf/117/14/a724.jpg" alt="Green Hospitals: Ohne Verstand" /></a></div></div></div>
<div class="jsHitlistRecord row" data-src="16"><div class="jsHitlistNr col col-1 ">5.</div><div class="jsHitlistData col col-11 col-md-8"><div class="jsHitlistCategory">MEDIZINREPORT</div><div class="jsHitlistTitle"><a href="treffer?mode=s&wo=16&typ=16&aid=212983&s=klimawandel">Green Hospitals: Klimaschutz im Krankenhaus</a></div><div class="jsHitlistAuthor"><span class="author">Litke, Nicola</span>; <span class="author">Szecsenyi, Joachim</span>; <span class="author">Wensing, Michel</span>; <span class="author">Weis, Aline</span></div><div class="jsHitlistSrc">Dtsch Arztebl 2020; 117(11): A-544 / B-468</div></div><div class="jsHitlistImage col hidden-sm-down col-3"><div class="ratio ratio_16_9"><a href="treffer?mode=s&wo=16&typ=16&aid=212983&s=klimawandel"><img class="thumb-1" src="/pdf/117/11/a544.jpg" alt="Green Hospitals: Klimaschutz im Krankenhaus" /></a></div></div></div>
</div>
<div class="documentinfobar bottom"><div class="mid"><div class="navigator" data-pagecount="20"><a href="#" class="naviButton navigatorButtonLeftLeft"><div class="navigatorButton navigatorLeftLeft"><i class="fa fa-angle-double-left"></i></div></a><a href="#" class="naviButton navigatorButtonLeft"><div class="navigatorButton navigatorLeft"><i class="fa fa-angle-left"></i></div></a><span class="navigatorText">Seite <span class="page">1</span> von 20<span class="hidden-sm-down">, Treffer 1&ndash;5 von 100</span></span><a href="?s=klimawandel&wo=16&page=20" class="naviButton navigatorButtonRightRight"><div class="navigatorButton navigatorRightRight"><i class="fa fa-angle-double-right"></i></div></a><a href="?s=klimawandel&wo=16&page=2" class="naviButton navigatorButtonRight"><div class="navigatorButton navigatorRight"><i class="fa fa-angle-right"></i></div></a></div></div></div> <!-- LINK --><!-- LINK --></div>


<div class="clear"></div></div>

       <div class="clear"></div>
   </div>
</div>
<!-- END ÄRZTEBLATT - Standard (ohne Linie drunter) --></div>
<div class="clear"></div></div><!-- /area -->
</div><!-- /area_container -->
</div><!-- /area_wrapper -->
<div class="area_wrapper  area area_right" id="p0000_a7666">
<div class="area_container ">
<div id="p2089_a7666" class="area area_right  row" data-pageid="2089" data-areaid="7666">
<div id="p2089_a7666_c44546" data-pageid="2089" data-areaid="7666" data-boxmeta="" data-boxid="44546" data-status="0" class="col col-xs-0 col-sm-0 col-md-0 col-lg-12 col-xl-12"><!-- START ÄRZTEBLATT - Suchbox -->
<div>
   <div class="searchbox">
<div class="bg-daecolor">
       <div class="message nr1">
<div class="subhead"></div>


<div class="text"><div class="suchfilter">
<h2>Ihre Suche eingrenzen</h2>
<div class="suchMaske"><form action="/suche"><div class="label">Suchbegriff(e)</div><input type="search" name="s" value="klimawandel" /><div class="label">Suchen in</div><ul class="filters"><li><input checked type="checkbox" id="sf_key_16" name="wo" value="16" /><label for="sf_key_16">Deutsches Ärzteblatt</label></li><li><input  type="checkbox" id="sf_key_32" name="wo" value="32" /><label for="sf_key_32">Deutsches Ärzteblatt PP</label></li><li><input  type="checkbox" id="sf_key_256" name="wo" value="256" /><label for="sf_key_256">Perspektiven</label></li><li><input  type="checkbox" id="sf_key_128" name="wo" value="128" /><label for="sf_key_128">PRAXiS</label></li><li><input  type="checkbox" id="sf_key_64" name="wo" value="64" /><label for="sf_key_64">Medizin studieren</label></li><li><input  type="checkbox" id="sf_key_1" name="wo" value="1" /><label for="sf_key_1">News</label></li><li><input  type="checkbox" id="sf_key_2" name="wo" value="2" /><label for="sf_key_2">Blogs</label></li><li><input  type="checkbox" id="sf_key_4" name="wo" value="4" /><label for="sf_key_4">Foren</label></li><li><input  type="checkbox" id="sf_key_8" name="wo" value="8" /><label for="sf_key_8">Preise</label></li></ul><input type="submit" value="Suchen" /> <input type="button" value="Zur erweiterten Suche" onclick="location='/archiv/suche'"/></form></div>
</div>
</div>
<div class="clear"></div></div>

       <div class="clear"></div>
   </div>
</div>
</div>
<!-- END ÄRZTEBLATT - Suchbox--></div>
<div id="p2089_a7666_c55002" data-pageid="2089" data-areaid="7666" data-boxmeta="" data-boxid="55002" data-status="0" class="col col-12 col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"><!-- START ÄRZTEBLATT - Anzeigenbox -->
<div>
   <div class="anzeigenbox">
       <div class="message nr1">
<div class="subhead"></div>


<div class="text"><div id="Ads_BA_BUT"><div style="font-size:11px;padding-left:4px">Anzeige</div><script>Ads_BA_AD('BUT');</script></div>
 <!-- LINK --><!-- LINK --></div>
<div class="clear"></div></div>

       <div class="clear"></div>
   </div>
</div>
<!-- END ÄRZTEBLATT - Anzeigenbox --></div>
<div class="clear"></div></div><!-- /area -->
</div><!-- /area_container -->
</div><!-- /area_wrapper -->
<div class="clear"></div>


                    <div id="prevPageButton" class="browseButton" data-url=""></div>
                    <div id="nextPageButton" class="browseButton" data-url="?s=klimawandel&wo=16&page=2"></div>

                </section>


                <footer id="DAEfooter">
                    <div class="area_wrapper area_full">
                        <div class="area_container">
                                <div class="area area_full">
                                	<div class="row">
                                        <div class="col col-12 col-sm-12 col-md-5 col-lg-5 col-xl-5">
                                            <div id="company1">Deutsches Ärzteblatt</div>
                                            <div id="company2"><a href="http://www.aerzteverlag.de" target="_blank">Deutscher Ärzteverlag GmbH</a></div>
                                            <div id="company3">Redaktion</div>
                                            <p>Reinhardtstr. 34 &middot; 10117 Berlin<br />
                                            Telefon: +49 (0) 30 246267 - 0<br />
                                            Telefax: +49 (0) 30 246267 - 20<br />
                                            E-Mail: <a href="mailto:aerzteblatt@aerzteblatt.de">aerzteblatt@aerzteblatt.de</a></p>
                                            <p>entwickelt von <a href="http://www.schaffrath-digital.de">L.N. Schaffrath DigitalMedien GmbH</a></p>
                                        </div>
                                        <div class="col col-12 col-sm-12 col-md-7 col-lg-7 col-xl-7">
                                            <div class="homepages">
                                                <ul>
                                                    <li><a href="/anzeigen">Ärztestellen</a></li>
                                                    <li><a href="/">Ärzteblatt</a></li>
                                                    <li><a href="/cme">CME</a></li>
                                                    <li><a href="/studieren">Studieren</a></li>
                                                </ul>
                                                <div class="clear"></div>
                                            </div>

                                            <div class="general">
                                                <div class="row">
                                                    <div>
                                                        <ul>
                                                            <li><a href="/">Home</a></li>
                                                            <li><a href="/archiv">Archiv</a></li>
                                                            <li><a href="/nachrichten">News</a></li>
                                                            <li><a href="/nachrichten/sw">Themen</a></li>
                                                            <li><a href="/dae-plus">DÄ plus</a></li>
                                                        </ul>
                                                    </div>
                                                    <div>
                                                        <ul>
                                                            <li><a href="/anzeigen">Jobs</a></li>
                                                            <li><a href="/anzeigen/aufgabe">Anzeigen&shy;aufgabe</a></li>
                                                            <li><a href="/service/mediadaten">Media&shy;daten</a></li>
                                                            <li><a href="/service/abo">Abon&shy;nement</a></li>
                                                            <li><a href="/ePaper">ePaper</a></li>
                                                        </ul>
                                                    </div>
                                                    <div>
                                                        <ul>
                                                            <li><a href="/service/impressum">Impressum</a></li>
                                                            <li><a href="/service/kontakt">Kontakt</a></li>
                                                            <li><a href="https://www.aerzteverlag.de/datenschutz" target="_blank">Daten&shy;schutz &amp; Daten&shy;sicherheit</a></li>
                                                            <li><a href="https://www.aerzteverlag.de/agb" target="_blank">AGB</a></li>
                                                            <li class="hidden-md-up"><a href="/archiv/fuer-autoren" target="_self">Für Autoren</a></li>
                                                            <li class="hidden-md-up"><a href="/service" target="_self">Service</a></li>
                                                            <li class="hidden-md-up"><a href="/anzeigen" target="_self">Anzeigen</a></li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                            <hr />
                                            <div class="row">
                                                <div class="col col-12 col-sm-4 col-md-5 col-lg-5 col-xl-4">
                                                    <p>Sie finden uns auch auf:</p>
                                                    <a href="https://www.facebook.com/aerzteblatt/" target="_blank" class="social-icon si-small si-light si-facebook">
                                                        <i class="icon-facebook"></i>
                                                        <i class="icon-facebook"></i>
                                                    </a>
                                                    <a href="https://twitter.com/dt_aerzteblatt" target="_blank" class="social-icon si-small si-light si-twitter">
                                                        <i class="icon-twitter"></i>
                                                        <i class="icon-twitter"></i>
                                                    </a>
                                                </div>
                                                <div class="col col-12 col-sm-8 col-md-7 col-lg-7 col-xl-8">
                                                    <p>RSS-Feed abonnieren:</p>
                                                    <a href="/service/rss" target="_blank" class="social-icon si-small si-light si-rss">
                                                        <i class="icon-rss"></i>
                                                        <i class="icon-rss"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            <div class="scrollup"><i class="icon-angle-up"></i></div>
                        </div>
                    </div>
                </footer>

            </div>

            <div id="sky" class="hidden-lg-down BAad"><div class="BAad" id="Ads_BA_SKY"><script>Ads_BA_AD('SKY')</script></div></div>
            <div class="afs_ads">&nbsp;</div>
        </section>

        <script src="https://cdn.aerzteblatt.de/inc/js/google-analytics.js" defer></script>
        <script>
            // Fachgruppen-Tracking
            jsTrackPageImpression('Suche');
        </script>
    </body>
</html>
"""