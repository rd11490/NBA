from BasketballReferenceBoxScoreParser import BasketballReferenceBoxScoreParser

__author__ = 'Ryan'
import unittest
from bs4 import BeautifulSoup

class testBoxScoreParser(unittest.TestCase):

    def setUp(self):
        #<editor-fold desc="Test Page">
        self.page = """<!DOCTYPE html><html data-version="the-magglio-475" itemscope itemtype="http://schema.org/website" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://opengraphprotocol.org/schema/" lang="en"><head><title>Cleveland Cavaliers at Golden State Warriors Box Score, June 19, 2016 | Basketball-Reference.com</title><link rel="dns-prefetch" href="http://d2ft4b0ve1aur1.cloudfront.net" /><link rel="dns-prefetch" href="http://m.bkref.com" />
        <link rel=subresource href="http://d2ft4b0ve1aur1.cloudfront.net/js-475/sr-bbr-min.js.jgz" /><script type="text/javascript">var sr_gzipEnabled = false; var sr_js_loader = new Array();</script><script type="text/javascript" src="http://d2ft4b0ve1aur1.cloudfront.net/js-100/sr.gzipcheck.js.jgz"></script><noscript><link type="text/css" rel="stylesheet" href="http://d2ft4b0ve1aur1.cloudfront.net/css-475/sr-bbr-min.css"></noscript><script type="text/javascript">
        (function () {var sr_css_file = 'http://d2ft4b0ve1aur1.cloudfront.net/css-475/sr-bbr-min.css';if (sr_gzipEnabled) {sr_css_file = 'http://d2ft4b0ve1aur1.cloudfront.net/css-475/sr-bbr-min-gz.css';}var head = document.getElementsByTagName("head")[0];if (head) {var scriptStyles = document.createElement("link");scriptStyles.rel = "stylesheet";scriptStyles.type = "text/css";scriptStyles.href = sr_css_file;head.appendChild(scriptStyles);}}());</script><!-- tiles, touch, favicons --><link rel="apple-touch-icon-precomposed" sizes="152x152" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/apple-touch-icon-152x152-bbr-precomposed.png"><link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/apple-touch-icon-144x144-bbr-precomposed.png"><link rel="apple-touch-icon-precomposed" sizes="120x120" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/apple-touch-icon-120x120-bbr-precomposed.png"><link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/apple-touch-icon-114x114-bbr-precomposed.png"><link rel="apple-touch-icon-precomposed" sizes="76x76" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/apple-touch-icon-76x76-bbr-precomposed.png"><link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/apple-touch-icon-72x72-bbr-precomposed.png"><link rel="apple-touch-icon-precomposed" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/apple-touch-icon-bbr-precomposed.png"><link rel=icon href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/favicon_bbr.png"><!--[if IE]><link rel="shortcut icon" href="http://d2ft4b0ve1aur1.cloudfront.net/images-475/favicon_bbr.ico"><![endif]--><meta name="msapplication-TileColor" content="#ffffff"/><meta name="msapplication-TileImage" content="http://d2ft4b0ve1aur1.cloudfront.net/images-475/ms-tile-144-bbr.png" /><link rel=search        type="application/opensearchdescription+xml" href="http://d2ft4b0ve1aur1.cloudfront.net/os-475/opensearch-bbr.xml" title="B-Ref Search"><!--[if lte IE 7 ]><style type="text/css">
        .uni_holder { display: none; }
        </style><![endif]--><!--[if lte IE 6]><style type="text/css">
        .hovermenu,.hovermenu_ajax,.sub_index,#quick_index {display:none!important}
        </style><![endif]-->
        <!--  ASYNCHRONOUS:googletag --><script type='text/javascript'>
        var googletag = googletag || {};googletag.cmd = googletag.cmd || [];(function() {var gads = document.createElement('script');gads.async = true;gads.type = 'text/javascript';var useSSL = 'https:' == document.location.protocol;gads.src = (useSSL ? 'https:' : 'http:') + '//www.googletagservices.com/tag/js/gpt.js';var node = document.getElementsByTagName('script')[0];node.parentNode.insertBefore(gads, node);})();</script><meta name=keywords content="box score, play-by-play, shot chart, June 19, 2016, Cleveland Cavaliers, Golden State Warriors"><meta property="fb:admins"     content="34208645"><meta property="fb:page_id"    content="35120246404"><meta property="og:description" content="Box Score"><meta property="og:title" content="Cavaliers (93) at Warriors (89), Jun 19, 2016"><meta property="og:url" content="http://www.basketball-reference.com/boxscores/201606190GSW.html"><meta property="og:type" content="sports_game"><meta itemprop=name content="Cavaliers (93) at Warriors (89), Jun 19, 2016"><meta itemprop=description content="Box Score"><meta property="og:site_name"  content="Basketball-Reference.com"><meta property="og:image"      content="http://d2ft4b0ve1aur1.cloudfront.net/images-434/apple-touch-icon-152x152-bbr-precomposed.png"><meta itemprop=image         content="http://d2ft4b0ve1aur1.cloudfront.net/images-434/apple-touch-icon-152x152-bbr-precomposed.png"><meta name="twitter:card"         content="summary"><meta name="twitter:site"         content="@bball_ref"><meta name="twitter:creator"      content="@bball_ref"><meta name="twitter:title"        content="Cleveland Cavaliers at Golden State Warriors Box Score, June 19, 2016 | Basketball-Reference.com"><meta name="twitter:description"  content="Stats and results for players, teams, leaders and scores from the first game ever to yesterday"><meta name="twitter:image"        content=""><meta name="twitter:url"          content="http://www.basketball-reference.com"><meta name="twitter:domain"       content="Basketball-Reference.com"></head><body onload=""><div id=page_container><div id=top_nav><!--BEGIN QUALTRICS SITE INTERCEPT-->
        <script type='text/javascript'>
        (function(){var g=function(e,h,f,g){
        this.get=function(a){for(var a=a+"=",c=document.cookie.split(";"),b=0,e=c.length;b<e;b++){for(var d=c[b];" "==d.charAt(0);)d=d.substring(1,d.length);if(0==d.indexOf(a))return d.substring(a.length,d.length)}return null};
        this.set=function(a,c){var b="",b=new Date;b.setTime(b.getTime()+6048E5);b="; expires="+b.toGMTString();document.cookie=a+"="+c+b+"; path=/; "};
        this.check=function(){var a=this.get(f);if(a)a=a.split(":");else if(100!=e)"v"==h&&(e=Math.random()>=e/100?0:100),a=[h,e,0],this.set(f,a.join(":"));else return!0;var c=a[1];if(100==c)return!0;switch(a[0]){case "v":return!1;case "r":return c=a[2]%Math.floor(100/c),a[2]++,this.set(f,a.join(":")),!c}return!0};
        this.go=function(){if(this.check()){var a=document.createElement("script");a.type="text/javascript";a.src=g+ "&t=" + (new Date()).getTime();document.body&&document.body.appendChild(a)}};
        this.start=function(){var a=this;window.addEventListener?window.addEventListener("load",function(){a.go()},!1):window.attachEvent&&window.attachEvent("onload",function(){a.go()})}};
        try{(new g(100,"r","QSI_S_SI_3CWPKrI10k7ANBX","//zncvfm2dltswdzell-farris.siteintercept.qualtrics.com/WRSiteInterceptEngine/?Q_SIID=SI_3CWPKrI10k7ANBX&Q_LOC="+encodeURIComponent(window.location.href))).start()}catch(i){}})();
        </script><div id='SI_3CWPKrI10k7ANBX'><!--DO NOT REMOVE-CONTENTS PLACED HERE--></div>
        <!--END SITE INTERCEPT-->

        <div id="sr_site_dir">
         <a href="http://www.sports-reference.com">Sports-Reference</a>:
         <a href="http://www.baseball-reference.com">Baseball</a> &#183;
         <span class="bold_text">Basketball</span>
        (<a href="http://www.sports-reference.com/cbb/">college</a>) &#183;
         <a href="http://www.pro-football-reference.com">Football</a>
        (<a href="http://www.sports-reference.com/cfb/">college</a>) &#183;
         <a href="http://www.hockey-reference.com/">Hockey</a> &#183;
         <a href="http://www.sports-reference.com/olympics/">Olympics</a> &#183;
         <a href="http://www.sports-reference.com/blog/">S-R Blog</a> &#183;
         <a href="http://www.sports-reference.com/feedback/">Question or Comment?</a>
        </div><!-- div#sr_site_dir -->

        <div id=site_header>
         <div id=sr_header>
          <div id=sr_header_right_float class="float_right clear_right">
           <div class="float_right">
            <div id="welcome" class="margin0 padding_bottom_half float_right poptip" tip="Review the details of your account"><span class="greeting"></span><a class="acct_external" href="/my/auth.cgi"></a>&nbsp;</div>
            <div class="clear_both padding_bottom_half">
             <span class="badge ui-corner-all         colors         like_a logged_out"  onclick="return sr_login_popup();" id="login_placeholder" style="display:none;"                                      >LOGIN<span id="loginform_container"></span></span>
             <span class="badge ui-corner-all         colors         like_a logged_in"   onclick="return sr_logout();"                                                                                        >LOGOUT</span>
             <span class="badge ui-corner-all tooltip disabled_badge like_a is_sponsor"  onclick="document.location.href='/my/auth.cgi?do=sponsor'"          tip="Sponsor a page on Basketball-Reference.com" >SPONSOR</span>
             <span class="badge ui-corner-all tooltip disabled_badge like_a ad_free"     onclick="document.location.href='/my/auth.cgi?do=ad_free_browsing'" tip="Surf Sports Reference Ad Free">AD FREE</span>
            <span>&nbsp;</span>
            </div>
           </div>

           <div class="clearfix float_right clear_both">
            <div class="padding_left_half float_right"><a class="sprite-twitter" title="Follow us on Twitter" href="http://twitter.com/bball_ref"></a><a class="sprite-facebook" title="Become a Fan on FaceBook" href="http://www.facebook.com/Basketball.Reference"></a><a class="sprite-youtube" title="Sports Reference Instructional Videos" href="http://www.youtube.com/user/sportsreference"></a></div>

            <div class=float_right>
             <form  id="f" name="f" action="/search/search.fcgi">
              <input x-webkit-speech type="search" placeholder="click 'Tips' for shortcuts" id="search" name="search" class="search long typeahead">
              <input type="hidden" name="results" value="" data-search-id>
              <input type=submit value="Search" class="submit">
              <a class="padding_left_half small_text" href="/about/findstuff.shtml?lid=homepage_tips">Tips</a>
             </form>
            </div>
           </div>

          </div><!-- div#sr_header_right_float -->
         </div><!-- div#sr_header -->

         <div class="float_left">
          <div class="clear_left float_left padding_top padding_bottom_half"><a href="/?lid=homepage_logo"><img src="http://d2ft4b0ve1aur1.cloudfront.net/images-370/Basketball-Ref.png" width=464 height=73 border="0" alt="Basketball-Reference.com"></a>
        </div>
         </div>

        </div><!-- div#site_header -->


        <div id=quick_index><ul class="hovermenu_ajax navbar"><li><a href="/play-index/">play index</a><ul class=li_margin id="header_playindex"></ul></li><li class=active><a href="/boxscores/">box scores</a><ul id=header_boxscores></ul></li><li><a href="/players/">players</a><ul class=li_margin id="header_players"></ul></li><li><a href="/teams/">teams</a><ul id=header_teams></ul></li><li><a href="/leagues/">seasons</a><ul class=li_margin id="header_leagues"></ul></li><li><a href="/coaches/">coaches</a><ul class=li_margin id="header_coaches"></ul></li><li><a href="/leaders/">leaders</a><ul class=li_margin id="header_leaders"></ul></li><li><a href="/awards/">awards</a><ul class=li_margin id="header_awards"></ul></li><li><a href="/playoffs/">playoffs</a><ul class=li_margin id="header_playoffs"></ul></li><li><a href="/draft/">draft</a><ul class=li_margin id="header_draft"></ul></li><li><a href="/euro/">euro</a><ul class=li_margin id="header_euro"></ul></li><li><a href="/dleague/">d-lg</a><ul class=li_margin id="header_dlg"></ul></li><li><a href="/olympics/">olympics</a><ul class=li_margin id="header_olympics"></ul></li><li><a href="#">more [+]</a><ul class=li_margin id="header_more_links"></ul></li></ul></div><!-- div#quick_index --><div id=you_are_here><p class=padding_left0><a class=mobile_link href="http://m.bkref.com/m?p=XXboxscoresXX201606190GSW.html">Mobile Site</a> <span class=bold_text>You Are Here</span> &gt; <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop=url href="/"><span itemprop=title>BBR Home</span></a></span> &gt; <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop=url href="/boxscores/index.cgi?month=6&amp;day=19&amp;year=2016"><span itemprop=title>Box Scores</span></a></span> &gt; <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><span class=bold_text><span itemprop=title>Cleveland Cavaliers at Golden State Warriors Box Score, June 19, 2016</span></span></span></p></div><!-- div#quick_index --><div class="site_news"><p><span class="bold_text">News:</span> <span class="poptip" tip="If you follow me on twitter, you know that this work has been a long time coming. Starting last summer, Adam Wodon, Adam Darowski, and I started throwing around ideas for a more mobile-friendly version of our sites. Our mobile experience is probably charitably described as limited and functional and with now over 2/3rd's of [&#8230;]">s-r blog:<a onClick="try { pageTracker._trackEvent('blog','click','area-yah'); } catch (err) {};"
         href="http://www.sports-reference.com/blog/2016/07/sports-reference-to-launch-redesigned-sites-this-summer/">Sports Reference to Launch Redesigned Sites this Summer</a> <span class="small_text"></span></span></p></div>
        </div><!-- div#top_nav -->
        <div class='width100 overflow_hidden'><div class='float_left'><!-- div.#restofsite_728x90_atf1.advert728x90 -->
        <script type="text/javascript">
        googletag.cmd.push(function() {
        googletag.defineSlot('/20893548/yb/sportsreference', [728,90], 'restofsite_728x90_atf1').addService(googletag.pubads());

        googletag.enableServices();
        googletag.pubads().setTargeting('site', ['bbr']);
        });
        </script>
        <div id="restofsite_728x90_atf1" class="advert728x90">
        <script type="text/javascript">
        googletag.cmd.push(function() { googletag.display('restofsite_728x90_atf1'); });
        </script>
        </div>
        <!-- /div.#restofsite_728x90_atf1.advert728x90 -->

        </div>
        <div class='float_right padding_top margin_top'></div>
        </div><div id="page_content">
        <table class="margin_top width100">
        <tr class="valign_top">
        <td>
        <h1>Cleveland Cavaliers at Golden State Warriors Box Score, June 19, 2016</h1>
        <div class='clear_both width100 overflow_hidden'><div class='float_left'><table class="nav_table no_highlight stats_table">
        <tr>
        <td class="align_right padding_half"><strong>2016 Finals</strong><br><br><a href="/playoffs/2016-nba-finals-cavaliers-vs-warriors.html">Series Summary</a></td><td>
        <table>
        <tr>
        <td colspan="2" class="align_center bold_text">Game 1</td>
        </tr>
        <tr>
        <td><a href="/boxscores/201606020GSW.html">CLE<br>GSW</a></td>
        <td class="align_right"><a href="/boxscores/201606020GSW.html">89<br>104</a></td>
        </tr>
        <tr>
        <td colspan="2" class="align_center">GSW 1-0</td></tr>
        </table>
        </td>
        <td>
        <table>
        <tr>
        <td colspan="2" class="align_center bold_text">Game 2</td>
        </tr>
        <tr>
        <td><a href="/boxscores/201606050GSW.html">CLE<br>GSW</a></td>
        <td class="align_right"><a href="/boxscores/201606050GSW.html">77<br>110</a></td>
        </tr>
        <tr>
        <td colspan="2" class="align_center">GSW 2-0</td></tr>
        </table>
        </td>
        <td>
        <table>
        <tr>
        <td colspan="2" class="align_center bold_text">Game 3</td>
        </tr>
        <tr>
        <td><a href="/boxscores/201606080CLE.html">GSW<br>CLE</a></td>
        <td class="align_right"><a href="/boxscores/201606080CLE.html">90<br>120</a></td>
        </tr>
        <tr>
        <td colspan="2" class="align_center">GSW 2-1</td></tr>
        </table>
        </td>
        <td>
        <table>
        <tr>
        <td colspan="2" class="align_center bold_text">Game 4</td>
        </tr>
        <tr>
        <td><a href="/boxscores/201606100CLE.html">GSW<br>CLE</a></td>
        <td class="align_right"><a href="/boxscores/201606100CLE.html">108<br>97</a></td>
        </tr>
        <tr>
        <td colspan="2" class="align_center">GSW 3-1</td></tr>
        </table>
        </td>
        <td>
        <table>
        <tr>
        <td colspan="2" class="align_center bold_text">Game 5</td>
        </tr>
        <tr>
        <td><a href="/boxscores/201606130GSW.html">CLE<br>GSW</a></td>
        <td class="align_right"><a href="/boxscores/201606130GSW.html">112<br>97</a></td>
        </tr>
        <tr>
        <td colspan="2" class="align_center">GSW 3-2</td></tr>
        </table>
        </td>
        <td>
        <table>
        <tr>
        <td colspan="2" class="align_center bold_text">Game 6</td>
        </tr>
        <tr>
        <td><a href="/boxscores/201606160CLE.html">GSW<br>CLE</a></td>
        <td class="align_right"><a href="/boxscores/201606160CLE.html">101<br>115</a></td>
        </tr>
        <tr>
        <td colspan="2" class="align_center">Tied 3-3</td></tr>
        </table>
        </td>
        <td class="background_yellow">
        <table>
        <tr>
        <td colspan="2" class="align_center bold_text">Game 7</td>
        </tr>
        <tr>
        <td><a href="/boxscores/201606190GSW.html">CLE<br>GSW</a></td>
        <td class="align_right"><a href="/boxscores/201606190GSW.html">93<br>89</a></td>
        </tr>
        <tr>
        <td colspan="2" class="align_center">CLE 4-3</td></tr>
        </table>
        </td>
        </tr>
        </table>
        <table>
        <tr>
        <td><table class="border_gray">
        <tr class="valign_top">
        <td class="align_center padding">
        <span class="bold_text large_text"><a href="/teams/CLE/2016.html">Cleveland Cavaliers</a><br>93</span><br><span class="x_small_text"><a href="/boxscores/201606160CLE.html" class="bold_text">&lArr; Prev Game</a></span>
        </td>
        <td class="align_center padding">
        <span class="bold_text large_text"><a href="/teams/GSW/2016.html">Golden State Warriors</a><br>89</span><br><span class="x_small_text"><a href="/boxscores/201606160CLE.html" class="bold_text">&lArr; Prev Game</a></span>
        </td>
        </tr>
        <tr>
        <td class="align_center padding_bottom small_text" colspan="2">8:00 PM, June 19, 2016<br>Oracle Arena, Oakland, California</td>
        </tr>
        </table>
        </td>
        </tr>
        </table>
        <table>
        <tr>
        <td><table class="nav_table stats_table">
        <tr>
        <th>&nbsp;</th>
        <th colspan="5">Scoring</th>
        </tr>
        <tr>
        <th>&nbsp;</th>
        <th class="align_right">1</th>
        <th class="align_right">2</th>
        <th class="align_right">3</th>
        <th class="align_right">4</th>
        <th class="align_right">T</th>
        </tr>
        <tr>
        <td><a href="/teams/CLE/2016.html">CLE</a></td>
        <td class="align_right">23</td>
        <td class="align_right">19</td>
        <td class="align_right">33</td>
        <td class="align_right">18</td>
        <td class="align_right bold_text">93</td>
        </tr>
        <tr>
        <td><a href="/teams/GSW/2016.html">GSW</a></td>
        <td class="align_right">22</td>
        <td class="align_right">27</td>
        <td class="align_right">27</td>
        <td class="align_right">13</td>
        <td class="align_right bold_text">89</td>
        </tr>
        </table>
        </td>
        <td class="valign_middle"><div class="table_container" id="div_four_factors">
        <table data-freeze="1" class=" nav_table stats_table" id="four_factors">
        <colgroup><col><col><col><col><col><col><col></colgroup>
        <thead>
        <tr class=" over_header">
          <th data-stat="" align="CENTER" colspan=2  class=" over_header" ></th>
          <th data-stat="header_tmp" align="center" colspan=4  class="bold_text over_header" >Four Factors</th>
          <th></th>
        </tr>
        <tr class="">
          <th data-stat="team_id" align="left"  class=" sort_default_asc"  tip="Team"></th>
          <th data-stat="pace" align="right"  class=""  tip="<b>Pace Factor</b>: An estimate of possessions per 48 minutes">Pace</th>
          <th data-stat="efg_pct" align="right"  class=""  tip="<strong>Effective Field Goal Percentage</strong><br>This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.">eFG%</th>
          <th data-stat="tov_pct" align="right"  class=" sort_default_asc"  tip="<b>Turnover Percentage</b><br>An estimate of turnovers committed per 100 plays.">TOV%</th>
          <th data-stat="orb_pct" align="right"  class=""  tip="<b>Offensive Rebound Percentage</b><br>An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.">ORB%</th>
          <th data-stat="ft_rate" align="right"  class=""  tip="Free Throws Per Field Goal Attempt">FT/FGA</th>
          <th data-stat="off_rtg" align="right"  class=""  tip="<b>Offensive Rating</b><br>An estimate of points produced (players) or scored (teams) per 100 possessions">ORtg</th>
        </tr>
        </thead>
        <tbody>
        <tr  class="">
           <td align="left" ><a href="/teams/CLE/2016.html">CLE</a></td>
           <td align="right" >90.7</td>
           <td align="right" >.439</td>
           <td align="right" >10.6</td>
           <td align="right"  class=" background_yellow">22.0</td>
           <td align="right"  class=" background_yellow">.256</td>
           <td align="right"  class=" background_yellow">102.5</td>
        </tr>
        <tr  class="">
           <td align="left" ><a href="/teams/GSW/2016.html">GSW</a></td>
           <td align="right" >90.7</td>
           <td align="right"  class=" background_yellow">.476</td>
           <td align="right"  class=" background_yellow">10.1</td>
           <td align="right" >15.2</td>
           <td align="right" >.120</td>
           <td align="right" >98.1</td>
        </tr>
        </tbody>
        </table>
        </div><!-- div.table_container#div_xxxx -->
        </td>
        </tr>
        </table>
        <div class="bold_text overflow_auto small_text">
        <div class="border_gray_double float_left margin_right padding background_gray"><span class="bold_text color_white">Box Score</span></div>
        <div class="border_gray_double float_left margin_right padding"><a href="/boxscores/pbp/201606190GSW.html">Play-By-Play</a></div>
        <div class="border_gray_double float_left margin_right padding"><a href="/boxscores/shot-chart/201606190GSW.html">Shot Charts</a></div>
        <div class="border_gray_double float_left margin_right padding"><a href="/boxscores/plus-minus/201606190GSW.html">Plus/Minus</a></div>
        </div>
        </div><div class='float_right'>
        <div class="margin_bottom padding_bottom"><!-- div.#restofsite_300x250_atf1.advert300x250 -->
        <script type="text/javascript">
        googletag.cmd.push(function() {
        googletag.defineSlot('/20893548/yb/sportsreference', [300,250], 'restofsite_300x250_atf1').addService(googletag.pubads());

        googletag.enableServices();
        googletag.pubads().setTargeting('site', ['bbr']);
        });
        </script>
        <div class="clear_both x_small_text align_right"><a href="/my/auth.cgi?do=ad_free_browsing">Support us without the ads? Go Ad-Free.</a></div>
        <div id="restofsite_300x250_atf1" class="advert300x250">
        <script type="text/javascript">
        googletag.cmd.push(function() { googletag.display('restofsite_300x250_atf1'); });
        </script>
        </div>
        <!-- /div.#restofsite_300x250_atf1.advert300x250 -->

        </div>
        <div class=""><!-- div.#restofsite_300x250_atf2.advert300x250 -->
        <script type="text/javascript">
        googletag.cmd.push(function() {
        googletag.defineSlot('/20893548/yb/sportsreference', [300,250], 'restofsite_300x250_atf2').addService(googletag.pubads());

        googletag.enableServices();
        googletag.pubads().setTargeting('site', ['bbr']);
        });
        </script>
        <div class="clear_both x_small_text align_right"><a href="/my/auth.cgi?do=ad_free_browsing">Support us without the ads? Go Ad-Free.</a></div>
        <div id="restofsite_300x250_atf2" class="advert300x250">
        <script type="text/javascript">
        googletag.cmd.push(function() { googletag.display('restofsite_300x250_atf2'); });
        </script>
        </div>
        <!-- /div.#restofsite_300x250_atf2.advert300x250 -->

        </div>
        </div>
        </div><div class='clear_both width100'><div class="table_heading">
        <h2 data-mobile-header="" style="color:white;background-color:rgb(139,0,0)!important">Cleveland Cavaliers (4-3)</h2>
        <div class="table_heading_text"></div>
        </div>
        <div class="table_container" id="div_CLE_basic">
        <table data-freeze="1"  class="sortable  stats_table" id="CLE_basic">
        <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
        <thead>
        <tr class=" over_header">
          <th></th>
          <th data-stat="header_tmp" align="center" colspan=20  class="bold_text over_header" >Basic Box Score Stats</th>
        </tr>
        <tr class="">
          <th data-stat="player" align="left"  class="tooltip sort_default_asc" >Starters</th>
          <th data-stat="mp" align="right"  class="tooltip"  tip="Minutes Played">MP</th>
          <th data-stat="fg" align="right"  class="tooltip"  tip="Field Goals">FG</th>
          <th data-stat="fga" align="right"  class="tooltip"  tip="Field Goal Attempts">FGA</th>
          <th data-stat="fg_pct" align="right"  class="tooltip"  tip="Field Goal Percentage">FG%</th>
          <th data-stat="fg3" align="right"  class="tooltip"  tip="3-Point Field Goals">3P</th>
          <th data-stat="fg3a" align="right"  class="tooltip"  tip="3-Point Field Goal Attempts">3PA</th>
          <th data-stat="fg3_pct" align="right"  class="tooltip"  tip="3-Point Field Goal Percentage">3P%</th>
          <th data-stat="ft" align="right"  class="tooltip"  tip="Free Throws">FT</th>
          <th data-stat="fta" align="right"  class="tooltip"  tip="Free Throw Attempts">FTA</th>
          <th data-stat="ft_pct" align="right"  class="tooltip"  tip="Free Throw Percentage">FT%</th>
          <th data-stat="orb" align="right"  class="tooltip"  tip="Offensive Rebounds">ORB</th>
          <th data-stat="drb" align="right"  class="tooltip"  tip="Defensive Rebounds">DRB</th>
          <th data-stat="trb" align="right"  class="tooltip"  tip="Total Rebounds">TRB</th>
          <th data-stat="ast" align="right"  class="tooltip"  tip="Assists">AST</th>
          <th data-stat="stl" align="right"  class="tooltip"  tip="Steals">STL</th>
          <th data-stat="blk" align="right"  class="tooltip"  tip="Blocks">BLK</th>
          <th data-stat="tov" align="right"  class="tooltip"  tip="Turnovers">TOV</th>
          <th data-stat="pf" align="right"  class="tooltip"  tip="Personal Fouls">PF</th>
          <th data-stat="pts" align="right"  class="tooltip"  tip="Points">PTS</th>
          <th data-stat="plus_minus" align="right"  class="tooltip"  tip="Plus/Minus">+/-</th>
        </tr>
        </thead>
        <tbody>
        <tr  class="">
           <td align="left"  csk="James,LeBron"><a href="/players/j/jamesle01.html">LeBron James</a></td>
           <td align="right"  csk="2809">46:49</td>
           <td align="right" >9</td>
           <td align="right" >24</td>
           <td align="right" >.375</td>
           <td align="right" >1</td>
           <td align="right" >5</td>
           <td align="right" >.200</td>
           <td align="right" >8</td>
           <td align="right" >10</td>
           <td align="right" >.800</td>
           <td align="right" >1</td>
           <td align="right" >10</td>
           <td align="right" >11</td>
           <td align="right" >11</td>
           <td align="right" >2</td>
           <td align="right" >3</td>
           <td align="right" >5</td>
           <td align="right" >1</td>
           <td align="right" >27</td>
           <td align="right" >+4</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Irving,Kyrie"><a href="/players/i/irvinky01.html">Kyrie Irving</a></td>
           <td align="right"  csk="2580">43:00</td>
           <td align="right" >10</td>
           <td align="right" >23</td>
           <td align="right" >.435</td>
           <td align="right" >2</td>
           <td align="right" >5</td>
           <td align="right" >.400</td>
           <td align="right" >4</td>
           <td align="right" >4</td>
           <td align="right" >1.000</td>
           <td align="right" >3</td>
           <td align="right" >3</td>
           <td align="right" >6</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >3</td>
           <td align="right" >26</td>
           <td align="right" >+10</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Smith,J.R."><a href="/players/s/smithjr01.html">J.R. Smith</a></td>
           <td align="right"  csk="2335">38:55</td>
           <td align="right" >5</td>
           <td align="right" >13</td>
           <td align="right" >.385</td>
           <td align="right" >2</td>
           <td align="right" >8</td>
           <td align="right" >.250</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >0</td>
           <td align="right" >4</td>
           <td align="right" >4</td>
           <td align="right" >2</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >3</td>
           <td align="right" >12</td>
           <td align="right" >+7</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Thompson,Tristan"><a href="/players/t/thomptr01.html">Tristan Thompson</a></td>
           <td align="right"  csk="1909">31:49</td>
           <td align="right" >3</td>
           <td align="right" >3</td>
           <td align="right" >1.000</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >3</td>
           <td align="right" >4</td>
           <td align="right" >.750</td>
           <td align="right" >0</td>
           <td align="right" >3</td>
           <td align="right" >3</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >0</td>
           <td align="right" >4</td>
           <td align="right" >9</td>
           <td align="right" >+2</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Love,Kevin"><a href="/players/l/loveke01.html">Kevin Love</a></td>
           <td align="right"  csk="1802">30:02</td>
           <td align="right" >3</td>
           <td align="right" >9</td>
           <td align="right" >.333</td>
           <td align="right" >0</td>
           <td align="right" >3</td>
           <td align="right" >.000</td>
           <td align="right" >3</td>
           <td align="right" >4</td>
           <td align="right" >.750</td>
           <td align="right" >4</td>
           <td align="right" >10</td>
           <td align="right" >14</td>
           <td align="right" >3</td>
           <td align="right" >2</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >9</td>
           <td align="right" >+19</td>
        </tr>
        <tr class="no_ranker thead">
          <th data-stat="player" align="left"  class=" sort_default_asc" >Reserves</th>
          <th data-stat="mp" align="right"  class=""  tip="Minutes Played">MP</th>
          <th data-stat="fg" align="right"  class=""  tip="Field Goals">FG</th>
          <th data-stat="fga" align="right"  class=""  tip="Field Goal Attempts">FGA</th>
          <th data-stat="fg_pct" align="right"  class=""  tip="Field Goal Percentage">FG%</th>
          <th data-stat="fg3" align="right"  class=""  tip="3-Point Field Goals">3P</th>
          <th data-stat="fg3a" align="right"  class=""  tip="3-Point Field Goal Attempts">3PA</th>
          <th data-stat="fg3_pct" align="right"  class=""  tip="3-Point Field Goal Percentage">3P%</th>
          <th data-stat="ft" align="right"  class=""  tip="Free Throws">FT</th>
          <th data-stat="fta" align="right"  class=""  tip="Free Throw Attempts">FTA</th>
          <th data-stat="ft_pct" align="right"  class=""  tip="Free Throw Percentage">FT%</th>
          <th data-stat="orb" align="right"  class=""  tip="Offensive Rebounds">ORB</th>
          <th data-stat="drb" align="right"  class=""  tip="Defensive Rebounds">DRB</th>
          <th data-stat="trb" align="right"  class=""  tip="Total Rebounds">TRB</th>
          <th data-stat="ast" align="right"  class=""  tip="Assists">AST</th>
          <th data-stat="stl" align="right"  class=""  tip="Steals">STL</th>
          <th data-stat="blk" align="right"  class=""  tip="Blocks">BLK</th>
          <th data-stat="tov" align="right"  class=""  tip="Turnovers">TOV</th>
          <th data-stat="pf" align="right"  class=""  tip="Personal Fouls">PF</th>
          <th data-stat="pts" align="right"  class=""  tip="Points">PTS</th>
          <th data-stat="plus_minus" align="right"  class=""  tip="Plus/Minus">+/-</th>
        </tr>
        <tr  class="">
           <td align="left"  csk="Jefferson,Richard"><a href="/players/j/jefferi01.html">Richard Jefferson</a></td>
           <td align="right"  csk="1530">25:30</td>
           <td align="right" >1</td>
           <td align="right" >4</td>
           <td align="right" >.250</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >1</td>
           <td align="right" >8</td>
           <td align="right" >9</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >-8</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Shumpert,Iman"><a href="/players/s/shumpim01.html">Iman Shumpert</a></td>
           <td align="right"  csk="1150">19:10</td>
           <td align="right" >1</td>
           <td align="right" >3</td>
           <td align="right" >.333</td>
           <td align="right" >1</td>
           <td align="right" >3</td>
           <td align="right" >.333</td>
           <td align="right" >3</td>
           <td align="right" >3</td>
           <td align="right" >1.000</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >6</td>
           <td align="right" >-9</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Williams,Mo"><a href="/players/w/willima01.html">Mo Williams</a></td>
           <td align="right"  csk="285">4:45</td>
           <td align="right" >1</td>
           <td align="right" >3</td>
           <td align="right" >.333</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >.000</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >-5</td>
        </tr>
        </tbody>
        <tfoot>
        <tr  class="bold_text stat_total">
           <td align="left" >Team Totals</td>
           <td align="right" >240</td>
           <td align="right" >33</td>
           <td align="right" >82</td>
           <td align="right" >.402</td>
           <td align="right" >6</td>
           <td align="right" >25</td>
           <td align="right" >.240</td>
           <td align="right" >21</td>
           <td align="right" >25</td>
           <td align="right" >.840</td>
           <td align="right" >9</td>
           <td align="right" >39</td>
           <td align="right" >48</td>
           <td align="right" >17</td>
           <td align="right" >7</td>
           <td align="right" >6</td>
           <td align="right" >11</td>
           <td align="right" >15</td>
           <td align="right" >93</td>
           <td align="right" ></td>
        </tr>
        </tfoot>
        </table>
        </div><!-- div.table_container#div_xxxx -->
        <div class="table_heading">

        <div class="table_heading_text"></div>
        </div>
        <div class="table_container" id="div_CLE_advanced">
        <table data-freeze="1"  class="sortable  stats_table" id="CLE_advanced">
        <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
        <thead>
        <tr class=" over_header">
          <th></th>
          <th data-stat="header_tmp" align="center" colspan=15  class="bold_text over_header" >Advanced Box Score Stats</th>
        </tr>
        <tr class="">
          <th data-stat="player" align="left"  class="tooltip sort_default_asc" >Starters</th>
          <th data-stat="mp" align="right"  class="tooltip"  tip="Minutes Played">MP</th>
          <th data-stat="ts_pct" align="right"  class="tooltip"  tip="<strong>True Shooting Percentage</strong><br>A measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.">TS%</th>
          <th data-stat="efg_pct" align="right"  class="tooltip"  tip="<strong>Effective Field Goal Percentage</strong><br>This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.">eFG%</th>
          <th data-stat="fg3a_per_fga_pct" align="right"  class="tooltip"  tip="<strong>3-Point Attempt Rate</strong><br>Percentage of FG Attempts from 3-Point Range">3PAr</th>
          <th data-stat="fta_per_fga_pct" align="right"  class="tooltip"  tip="<strong>Free Throw Attempt Rate</strong><br>Number of FT Attempts Per FG Attempt">FTr</th>
          <th data-stat="orb_pct" align="right"  class="tooltip"  tip="<b>Offensive Rebound Percentage</b><br>An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.">ORB%</th>
          <th data-stat="drb_pct" align="right"  class="tooltip"  tip="<b>Defensive Rebound Percentage</b><br>An estimate of the percentage of available defensive rebounds a player grabbed while he was on the floor.">DRB%</th>
          <th data-stat="trb_pct" align="right"  class="tooltip"  tip="<b>Total Rebound Percentage</b><br>An estimate of the percentage of available rebounds a player grabbed while he was on the floor.">TRB%</th>
          <th data-stat="ast_pct" align="right"  class="tooltip"  tip="<b>Assist Percentage</b><br>An estimate of the percentage of teammate field goals a player assisted while he was on the floor.">AST%</th>
          <th data-stat="stl_pct" align="right"  class="tooltip"  tip="<b>Steal Percentage</b><br>An estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor.">STL%</th>
          <th data-stat="blk_pct" align="right"  class="tooltip"  tip="<b>Block Percentage</b><br>An estimate of the percentage of opponent two-point field goal attempts blocked by the player while he was on the floor.">BLK%</th>
          <th data-stat="tov_pct" align="right"  class="tooltip sort_default_asc"  tip="<b>Turnover Percentage</b><br>An estimate of turnovers committed per 100 plays.">TOV%</th>
          <th data-stat="usg_pct" align="right"  class="tooltip"  tip="<b>Usage Percentage</b><br>An estimate of the percentage of team plays used by a player while he was on the floor.">USG%</th>
          <th data-stat="off_rtg" align="right"  class="tooltip"  tip="<b>Offensive Rating</b><br>An estimate of points produced (players) or scored (teams) per 100 possessions">ORtg</th>
          <th data-stat="def_rtg" align="right"  class="tooltip sort_default_asc"  tip="<b>Defensive Rating</b><br>An estimate of points allowed per 100 possessions">DRtg</th>
        </tr>
        </thead>
        <tbody>
        <tr  class="">
           <td align="left"  csk="James,LeBron"><a href="/players/j/jamesle01.html">LeBron James</a></td>
           <td align="right"  csk="2809">46:49</td>
           <td align="right" >.475</td>
           <td align="right" >.396</td>
           <td align="right" >.208</td>
           <td align="right" >.417</td>
           <td align="right" >2.5</td>
           <td align="right" >22.3</td>
           <td align="right" >13.0</td>
           <td align="right" >47.4</td>
           <td align="right" >2.3</td>
           <td align="right" >7.3</td>
           <td align="right" >15.0</td>
           <td align="right" >32.9</td>
           <td align="right" >98</td>
           <td align="right" >92</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Irving,Kyrie"><a href="/players/i/irvinky01.html">Kyrie Irving</a></td>
           <td align="right"  csk="2580">43:00</td>
           <td align="right" >.525</td>
           <td align="right" >.478</td>
           <td align="right" >.217</td>
           <td align="right" >.174</td>
           <td align="right" >8.2</td>
           <td align="right" >7.3</td>
           <td align="right" >7.7</td>
           <td align="right" >5.1</td>
           <td align="right" >1.2</td>
           <td align="right" >2.7</td>
           <td align="right" >7.5</td>
           <td align="right" >28.7</td>
           <td align="right" >106</td>
           <td align="right" >102</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Smith,J.R."><a href="/players/s/smithjr01.html">J.R. Smith</a></td>
           <td align="right"  csk="2335">38:55</td>
           <td align="right" >.462</td>
           <td align="right" >.462</td>
           <td align="right" >.615</td>
           <td align="right" >.000</td>
           <td align="right" >0.0</td>
           <td align="right" >10.7</td>
           <td align="right" >5.7</td>
           <td align="right" >9.2</td>
           <td align="right" >1.4</td>
           <td align="right" >0.0</td>
           <td align="right" >13.3</td>
           <td align="right" >17.8</td>
           <td align="right" >85</td>
           <td align="right" >103</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Thompson,Tristan"><a href="/players/t/thomptr01.html">Tristan Thompson</a></td>
           <td align="right"  csk="1909">31:49</td>
           <td align="right" >.945</td>
           <td align="right" >1.000</td>
           <td align="right" >.000</td>
           <td align="right" >1.333</td>
           <td align="right" >0.0</td>
           <td align="right" >9.8</td>
           <td align="right" >5.2</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >7.2</td>
           <td align="right" >0.0</td>
           <td align="right" >6.9</td>
           <td align="right" >194</td>
           <td align="right" >101</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Love,Kevin"><a href="/players/l/loveke01.html">Kevin Love</a></td>
           <td align="right"  csk="1802">30:02</td>
           <td align="right" >.418</td>
           <td align="right" >.333</td>
           <td align="right" >.333</td>
           <td align="right" >.444</td>
           <td align="right" >15.6</td>
           <td align="right" >34.7</td>
           <td align="right" >25.7</td>
           <td align="right" >17.0</td>
           <td align="right" >3.5</td>
           <td align="right" >0.0</td>
           <td align="right" >8.5</td>
           <td align="right" >18.1</td>
           <td align="right" >104</td>
           <td align="right" >91</td>
        </tr>
        <tr class="no_ranker thead">
          <th data-stat="player" align="left"  class=" sort_default_asc" >Reserves</th>
          <th data-stat="mp" align="right"  class=""  tip="Minutes Played">MP</th>
          <th data-stat="ts_pct" align="right"  class=""  tip="<strong>True Shooting Percentage</strong><br>A measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.">TS%</th>
          <th data-stat="efg_pct" align="right"  class=""  tip="<strong>Effective Field Goal Percentage</strong><br>This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.">eFG%</th>
          <th data-stat="fg3a_per_fga_pct" align="right"  class=""  tip="<strong>3-Point Attempt Rate</strong><br>Percentage of FG Attempts from 3-Point Range">3PAr</th>
          <th data-stat="fta_per_fga_pct" align="right"  class=""  tip="<strong>Free Throw Attempt Rate</strong><br>Number of FT Attempts Per FG Attempt">FTr</th>
          <th data-stat="orb_pct" align="right"  class=""  tip="<b>Offensive Rebound Percentage</b><br>An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.">ORB%</th>
          <th data-stat="drb_pct" align="right"  class=""  tip="<b>Defensive Rebound Percentage</b><br>An estimate of the percentage of available defensive rebounds a player grabbed while he was on the floor.">DRB%</th>
          <th data-stat="trb_pct" align="right"  class=""  tip="<b>Total Rebound Percentage</b><br>An estimate of the percentage of available rebounds a player grabbed while he was on the floor.">TRB%</th>
          <th data-stat="ast_pct" align="right"  class=""  tip="<b>Assist Percentage</b><br>An estimate of the percentage of teammate field goals a player assisted while he was on the floor.">AST%</th>
          <th data-stat="stl_pct" align="right"  class=""  tip="<b>Steal Percentage</b><br>An estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor.">STL%</th>
          <th data-stat="blk_pct" align="right"  class=""  tip="<b>Block Percentage</b><br>An estimate of the percentage of opponent two-point field goal attempts blocked by the player while he was on the floor.">BLK%</th>
          <th data-stat="tov_pct" align="right"  class=" sort_default_asc"  tip="<b>Turnover Percentage</b><br>An estimate of turnovers committed per 100 plays.">TOV%</th>
          <th data-stat="usg_pct" align="right"  class=""  tip="<b>Usage Percentage</b><br>An estimate of the percentage of team plays used by a player while he was on the floor.">USG%</th>
          <th data-stat="off_rtg" align="right"  class=""  tip="<b>Offensive Rating</b><br>An estimate of points produced (players) or scored (teams) per 100 possessions">ORtg</th>
          <th data-stat="def_rtg" align="right"  class=" sort_default_asc"  tip="<b>Defensive Rating</b><br>An estimate of points allowed per 100 possessions">DRtg</th>
        </tr>
        <tr  class="">
           <td align="left"  csk="Jefferson,Richard"><a href="/players/j/jefferi01.html">Richard Jefferson</a></td>
           <td align="right"  csk="1530">25:30</td>
           <td align="right" >.250</td>
           <td align="right" >.250</td>
           <td align="right" >.000</td>
           <td align="right" >.000</td>
           <td align="right" >4.6</td>
           <td align="right" >32.7</td>
           <td align="right" >19.5</td>
           <td align="right" >0.0</td>
           <td align="right" >2.1</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >7.2</td>
           <td align="right" >69</td>
           <td align="right" >95</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Shumpert,Iman"><a href="/players/s/shumpim01.html">Iman Shumpert</a></td>
           <td align="right"  csk="1150">19:10</td>
           <td align="right" >.694</td>
           <td align="right" >.500</td>
           <td align="right" >1.000</td>
           <td align="right" >1.000</td>
           <td align="right" >0.0</td>
           <td align="right" >5.4</td>
           <td align="right" >2.9</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >10.4</td>
           <td align="right" >151</td>
           <td align="right" >108</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Williams,Mo"><a href="/players/w/willima01.html">Mo Williams</a></td>
           <td align="right"  csk="285">4:45</td>
           <td align="right" >.333</td>
           <td align="right" >.333</td>
           <td align="right" >.333</td>
           <td align="right" >.000</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >25.0</td>
           <td align="right" >38.9</td>
           <td align="right" >49</td>
           <td align="right" >109</td>
        </tr>
        </tbody>
        <tfoot>
        <tr  class="bold_text stat_total">
           <td align="left" >Team Totals</td>
           <td align="right" >240</td>
           <td align="right" >.500</td>
           <td align="right" >.439</td>
           <td align="right" >.305</td>
           <td align="right" >.305</td>
           <td align="right" >22.0</td>
           <td align="right" >84.8</td>
           <td align="right" >55.2</td>
           <td align="right" >51.5</td>
           <td align="right" >7.7</td>
           <td align="right" >14.3</td>
           <td align="right" >10.6</td>
           <td align="right" >100.0</td>
           <td align="right" >102.5</td>
           <td align="right" >98.1</td>
        </tr>
        </tfoot>
        </table>
        </div><!-- div.table_container#div_xxxx -->
        <div class="table_heading">
        <h2 data-mobile-header="" style="color:white;background-color:rgb(0,0,255)!important">Golden State Warriors (3-4)</h2>
        <div class="table_heading_text"></div>
        </div>
        <div class="table_container" id="div_GSW_basic">
        <table data-freeze="1"  class="sortable  stats_table" id="GSW_basic">
        <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
        <thead>
        <tr class=" over_header">
          <th></th>
          <th data-stat="header_tmp" align="center" colspan=20  class="bold_text over_header" >Basic Box Score Stats</th>
        </tr>
        <tr class="">
          <th data-stat="player" align="left"  class="tooltip sort_default_asc" >Starters</th>
          <th data-stat="mp" align="right"  class="tooltip"  tip="Minutes Played">MP</th>
          <th data-stat="fg" align="right"  class="tooltip"  tip="Field Goals">FG</th>
          <th data-stat="fga" align="right"  class="tooltip"  tip="Field Goal Attempts">FGA</th>
          <th data-stat="fg_pct" align="right"  class="tooltip"  tip="Field Goal Percentage">FG%</th>
          <th data-stat="fg3" align="right"  class="tooltip"  tip="3-Point Field Goals">3P</th>
          <th data-stat="fg3a" align="right"  class="tooltip"  tip="3-Point Field Goal Attempts">3PA</th>
          <th data-stat="fg3_pct" align="right"  class="tooltip"  tip="3-Point Field Goal Percentage">3P%</th>
          <th data-stat="ft" align="right"  class="tooltip"  tip="Free Throws">FT</th>
          <th data-stat="fta" align="right"  class="tooltip"  tip="Free Throw Attempts">FTA</th>
          <th data-stat="ft_pct" align="right"  class="tooltip"  tip="Free Throw Percentage">FT%</th>
          <th data-stat="orb" align="right"  class="tooltip"  tip="Offensive Rebounds">ORB</th>
          <th data-stat="drb" align="right"  class="tooltip"  tip="Defensive Rebounds">DRB</th>
          <th data-stat="trb" align="right"  class="tooltip"  tip="Total Rebounds">TRB</th>
          <th data-stat="ast" align="right"  class="tooltip"  tip="Assists">AST</th>
          <th data-stat="stl" align="right"  class="tooltip"  tip="Steals">STL</th>
          <th data-stat="blk" align="right"  class="tooltip"  tip="Blocks">BLK</th>
          <th data-stat="tov" align="right"  class="tooltip"  tip="Turnovers">TOV</th>
          <th data-stat="pf" align="right"  class="tooltip"  tip="Personal Fouls">PF</th>
          <th data-stat="pts" align="right"  class="tooltip"  tip="Points">PTS</th>
          <th data-stat="plus_minus" align="right"  class="tooltip"  tip="Plus/Minus">+/-</th>
        </tr>
        </thead>
        <tbody>
        <tr  class="">
           <td align="left"  csk="Green,Draymond"><a href="/players/g/greendr01.html">Draymond Green</a></td>
           <td align="right"  csk="2814">46:54</td>
           <td align="right" >11</td>
           <td align="right" >15</td>
           <td align="right" >.733</td>
           <td align="right" >6</td>
           <td align="right" >8</td>
           <td align="right" >.750</td>
           <td align="right" >4</td>
           <td align="right" >4</td>
           <td align="right" >1.000</td>
           <td align="right" >1</td>
           <td align="right" >14</td>
           <td align="right" >15</td>
           <td align="right" >9</td>
           <td align="right" >2</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >3</td>
           <td align="right" >32</td>
           <td align="right" >-1</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Thompson,Klay"><a href="/players/t/thompkl01.html">Klay Thompson</a></td>
           <td align="right"  csk="2537">42:17</td>
           <td align="right" >6</td>
           <td align="right" >17</td>
           <td align="right" >.353</td>
           <td align="right" >2</td>
           <td align="right" >10</td>
           <td align="right" >.200</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >2</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >3</td>
           <td align="right" >2</td>
           <td align="right" >14</td>
           <td align="right" >-11</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Curry,Stephen"><a href="/players/c/curryst01.html">Stephen Curry</a></td>
           <td align="right"  csk="2356">39:16</td>
           <td align="right" >6</td>
           <td align="right" >19</td>
           <td align="right" >.316</td>
           <td align="right" >4</td>
           <td align="right" >14</td>
           <td align="right" >.286</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >1.000</td>
           <td align="right" >0</td>
           <td align="right" >5</td>
           <td align="right" >5</td>
           <td align="right" >2</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >4</td>
           <td align="right" >4</td>
           <td align="right" >17</td>
           <td align="right" >-3</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Barnes,Harrison"><a href="/players/b/barneha02.html">Harrison Barnes</a></td>
           <td align="right"  csk="1764">29:24</td>
           <td align="right" >3</td>
           <td align="right" >10</td>
           <td align="right" >.300</td>
           <td align="right" >2</td>
           <td align="right" >4</td>
           <td align="right" >.500</td>
           <td align="right" >2</td>
           <td align="right" >2</td>
           <td align="right" >1.000</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >2</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >4</td>
           <td align="right" >10</td>
           <td align="right" >-6</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Ezeli,Festus"><a href="/players/e/ezelife01.html">Festus Ezeli</a></td>
           <td align="right"  csk="645">10:45</td>
           <td align="right" >0</td>
           <td align="right" >4</td>
           <td align="right" >.000</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >0</td>
           <td align="right" >-9</td>
        </tr>
        <tr class="no_ranker thead">
          <th data-stat="player" align="left"  class=" sort_default_asc" >Reserves</th>
          <th data-stat="mp" align="right"  class=""  tip="Minutes Played">MP</th>
          <th data-stat="fg" align="right"  class=""  tip="Field Goals">FG</th>
          <th data-stat="fga" align="right"  class=""  tip="Field Goal Attempts">FGA</th>
          <th data-stat="fg_pct" align="right"  class=""  tip="Field Goal Percentage">FG%</th>
          <th data-stat="fg3" align="right"  class=""  tip="3-Point Field Goals">3P</th>
          <th data-stat="fg3a" align="right"  class=""  tip="3-Point Field Goal Attempts">3PA</th>
          <th data-stat="fg3_pct" align="right"  class=""  tip="3-Point Field Goal Percentage">3P%</th>
          <th data-stat="ft" align="right"  class=""  tip="Free Throws">FT</th>
          <th data-stat="fta" align="right"  class=""  tip="Free Throw Attempts">FTA</th>
          <th data-stat="ft_pct" align="right"  class=""  tip="Free Throw Percentage">FT%</th>
          <th data-stat="orb" align="right"  class=""  tip="Offensive Rebounds">ORB</th>
          <th data-stat="drb" align="right"  class=""  tip="Defensive Rebounds">DRB</th>
          <th data-stat="trb" align="right"  class=""  tip="Total Rebounds">TRB</th>
          <th data-stat="ast" align="right"  class=""  tip="Assists">AST</th>
          <th data-stat="stl" align="right"  class=""  tip="Steals">STL</th>
          <th data-stat="blk" align="right"  class=""  tip="Blocks">BLK</th>
          <th data-stat="tov" align="right"  class=""  tip="Turnovers">TOV</th>
          <th data-stat="pf" align="right"  class=""  tip="Personal Fouls">PF</th>
          <th data-stat="pts" align="right"  class=""  tip="Points">PTS</th>
          <th data-stat="plus_minus" align="right"  class=""  tip="Plus/Minus">+/-</th>
        </tr>
        <tr  class="">
           <td align="left"  csk="Iguodala,Andre"><a href="/players/i/iguodan01.html">Andre Iguodala</a></td>
           <td align="right"  csk="2273">37:53</td>
           <td align="right" >2</td>
           <td align="right" >6</td>
           <td align="right" >.333</td>
           <td align="right" >0</td>
           <td align="right" >3</td>
           <td align="right" >.000</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >.000</td>
           <td align="right" >2</td>
           <td align="right" >7</td>
           <td align="right" >9</td>
           <td align="right" >4</td>
           <td align="right" >2</td>
           <td align="right" >2</td>
           <td align="right" >0</td>
           <td align="right" >3</td>
           <td align="right" >4</td>
           <td align="right" >+3</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Livingston,Shaun"><a href="/players/l/livinsh01.html">Shaun Livingston</a></td>
           <td align="right"  csk="964">16:04</td>
           <td align="right" >3</td>
           <td align="right" >7</td>
           <td align="right" >.429</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >2</td>
           <td align="right" >2</td>
           <td align="right" >1.000</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >8</td>
           <td align="right" >+8</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Varejao,Anderson"><a href="/players/v/varejan01.html">Anderson Varejao</a></td>
           <td align="right"  csk="509">8:29</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >.000</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >.500</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >3</td>
           <td align="right" >1</td>
           <td align="right" >-9</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Speights,Marreese"><a href="/players/s/speigma01.html">Marreese Speights</a></td>
           <td align="right"  csk="274">4:34</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >.000</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >.000</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >2</td>
           <td align="right" >2</td>
           <td align="right" >4</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >2</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >+3</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Barbosa,Leandro"><a href="/players/b/barbole01.html">Leandro Barbosa</a></td>
           <td align="right"  csk="264">4:24</td>
           <td align="right" >1</td>
           <td align="right" >2</td>
           <td align="right" >.500</td>
           <td align="right" >1</td>
           <td align="right" >1</td>
           <td align="right" >1.000</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" ></td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >0</td>
           <td align="right" >1</td>
           <td align="right" >3</td>
           <td align="right" >+5</td>
        </tr>
        </tbody>
        <tfoot>
        <tr  class="bold_text stat_total">
           <td align="left" >Team Totals</td>
           <td align="right" >240</td>
           <td align="right" >32</td>
           <td align="right" >83</td>
           <td align="right" >.386</td>
           <td align="right" >15</td>
           <td align="right" >41</td>
           <td align="right" >.366</td>
           <td align="right" >10</td>
           <td align="right" >13</td>
           <td align="right" >.769</td>
           <td align="right" >7</td>
           <td align="right" >32</td>
           <td align="right" >39</td>
           <td align="right" >22</td>
           <td align="right" >7</td>
           <td align="right" >5</td>
           <td align="right" >10</td>
           <td align="right" >23</td>
           <td align="right" >89</td>
           <td align="right" ></td>
        </tr>
        </tfoot>
        </table>
        </div><!-- div.table_container#div_xxxx -->
        <div class="table_heading">

        <div class="table_heading_text"></div>
        </div>
        <div class="table_container" id="div_GSW_advanced">
        <table data-freeze="1"  class="sortable  stats_table" id="GSW_advanced">
        <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
        <thead>
        <tr class=" over_header">
          <th></th>
          <th data-stat="header_tmp" align="center" colspan=15  class="bold_text over_header" >Advanced Box Score Stats</th>
        </tr>
        <tr class="">
          <th data-stat="player" align="left"  class="tooltip sort_default_asc" >Starters</th>
          <th data-stat="mp" align="right"  class="tooltip"  tip="Minutes Played">MP</th>
          <th data-stat="ts_pct" align="right"  class="tooltip"  tip="<strong>True Shooting Percentage</strong><br>A measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.">TS%</th>
          <th data-stat="efg_pct" align="right"  class="tooltip"  tip="<strong>Effective Field Goal Percentage</strong><br>This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.">eFG%</th>
          <th data-stat="fg3a_per_fga_pct" align="right"  class="tooltip"  tip="<strong>3-Point Attempt Rate</strong><br>Percentage of FG Attempts from 3-Point Range">3PAr</th>
          <th data-stat="fta_per_fga_pct" align="right"  class="tooltip"  tip="<strong>Free Throw Attempt Rate</strong><br>Number of FT Attempts Per FG Attempt">FTr</th>
          <th data-stat="orb_pct" align="right"  class="tooltip"  tip="<b>Offensive Rebound Percentage</b><br>An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.">ORB%</th>
          <th data-stat="drb_pct" align="right"  class="tooltip"  tip="<b>Defensive Rebound Percentage</b><br>An estimate of the percentage of available defensive rebounds a player grabbed while he was on the floor.">DRB%</th>
          <th data-stat="trb_pct" align="right"  class="tooltip"  tip="<b>Total Rebound Percentage</b><br>An estimate of the percentage of available rebounds a player grabbed while he was on the floor.">TRB%</th>
          <th data-stat="ast_pct" align="right"  class="tooltip"  tip="<b>Assist Percentage</b><br>An estimate of the percentage of teammate field goals a player assisted while he was on the floor.">AST%</th>
          <th data-stat="stl_pct" align="right"  class="tooltip"  tip="<b>Steal Percentage</b><br>An estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor.">STL%</th>
          <th data-stat="blk_pct" align="right"  class="tooltip"  tip="<b>Block Percentage</b><br>An estimate of the percentage of opponent two-point field goal attempts blocked by the player while he was on the floor.">BLK%</th>
          <th data-stat="tov_pct" align="right"  class="tooltip sort_default_asc"  tip="<b>Turnover Percentage</b><br>An estimate of turnovers committed per 100 plays.">TOV%</th>
          <th data-stat="usg_pct" align="right"  class="tooltip"  tip="<b>Usage Percentage</b><br>An estimate of the percentage of team plays used by a player while he was on the floor.">USG%</th>
          <th data-stat="off_rtg" align="right"  class="tooltip"  tip="<b>Offensive Rating</b><br>An estimate of points produced (players) or scored (teams) per 100 possessions">ORtg</th>
          <th data-stat="def_rtg" align="right"  class="tooltip sort_default_asc"  tip="<b>Defensive Rating</b><br>An estimate of points allowed per 100 possessions">DRtg</th>
        </tr>
        </thead>
        <tbody>
        <tr  class="">
           <td align="left"  csk="Green,Draymond"><a href="/players/g/greendr01.html">Draymond Green</a></td>
           <td align="right"  csk="2814">46:54</td>
           <td align="right" >.955</td>
           <td align="right" >.933</td>
           <td align="right" >.533</td>
           <td align="right" >.267</td>
           <td align="right" >2.2</td>
           <td align="right" >34.9</td>
           <td align="right" >17.6</td>
           <td align="right" >44.4</td>
           <td align="right" >2.3</td>
           <td align="right" >0.0</td>
           <td align="right" >10.7</td>
           <td align="right" >19.4</td>
           <td align="right" >172</td>
           <td align="right" >97</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Thompson,Klay"><a href="/players/t/thompkl01.html">Klay Thompson</a></td>
           <td align="right"  csk="2537">42:17</td>
           <td align="right" >.412</td>
           <td align="right" >.412</td>
           <td align="right" >.588</td>
           <td align="right" >.000</td>
           <td align="right" >2.5</td>
           <td align="right" >2.8</td>
           <td align="right" >2.6</td>
           <td align="right" >9.0</td>
           <td align="right" >1.3</td>
           <td align="right" >0.0</td>
           <td align="right" >15.0</td>
           <td align="right" >23.0</td>
           <td align="right" >74</td>
           <td align="right" >109</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Curry,Stephen"><a href="/players/c/curryst01.html">Stephen Curry</a></td>
           <td align="right"  csk="2356">39:16</td>
           <td align="right" >.437</td>
           <td align="right" >.421</td>
           <td align="right" >.737</td>
           <td align="right" >.053</td>
           <td align="right" >0.0</td>
           <td align="right" >14.9</td>
           <td align="right" >7.0</td>
           <td align="right" >9.9</td>
           <td align="right" >1.3</td>
           <td align="right" >2.1</td>
           <td align="right" >17.1</td>
           <td align="right" >29.0</td>
           <td align="right" >72</td>
           <td align="right" >103</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Barnes,Harrison"><a href="/players/b/barneha02.html">Harrison Barnes</a></td>
           <td align="right"  csk="1764">29:24</td>
           <td align="right" >.460</td>
           <td align="right" >.400</td>
           <td align="right" >.400</td>
           <td align="right" >.200</td>
           <td align="right" >0.0</td>
           <td align="right" >8.0</td>
           <td align="right" >3.8</td>
           <td align="right" >6.0</td>
           <td align="right" >1.8</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >18.0</td>
           <td align="right" >96</td>
           <td align="right" >106</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Ezeli,Festus"><a href="/players/e/ezelife01.html">Festus Ezeli</a></td>
           <td align="right"  csk="645">10:45</td>
           <td align="right" >.000</td>
           <td align="right" >.000</td>
           <td align="right" >.000</td>
           <td align="right" >.000</td>
           <td align="right" >0.0</td>
           <td align="right" >10.9</td>
           <td align="right" >5.1</td>
           <td align="right" >14.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >18.1</td>
           <td align="right" >16</td>
           <td align="right" >109</td>
        </tr>
        <tr class="no_ranker thead">
          <th data-stat="player" align="left"  class=" sort_default_asc" >Reserves</th>
          <th data-stat="mp" align="right"  class=""  tip="Minutes Played">MP</th>
          <th data-stat="ts_pct" align="right"  class=""  tip="<strong>True Shooting Percentage</strong><br>A measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.">TS%</th>
          <th data-stat="efg_pct" align="right"  class=""  tip="<strong>Effective Field Goal Percentage</strong><br>This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.">eFG%</th>
          <th data-stat="fg3a_per_fga_pct" align="right"  class=""  tip="<strong>3-Point Attempt Rate</strong><br>Percentage of FG Attempts from 3-Point Range">3PAr</th>
          <th data-stat="fta_per_fga_pct" align="right"  class=""  tip="<strong>Free Throw Attempt Rate</strong><br>Number of FT Attempts Per FG Attempt">FTr</th>
          <th data-stat="orb_pct" align="right"  class=""  tip="<b>Offensive Rebound Percentage</b><br>An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.">ORB%</th>
          <th data-stat="drb_pct" align="right"  class=""  tip="<b>Defensive Rebound Percentage</b><br>An estimate of the percentage of available defensive rebounds a player grabbed while he was on the floor.">DRB%</th>
          <th data-stat="trb_pct" align="right"  class=""  tip="<b>Total Rebound Percentage</b><br>An estimate of the percentage of available rebounds a player grabbed while he was on the floor.">TRB%</th>
          <th data-stat="ast_pct" align="right"  class=""  tip="<b>Assist Percentage</b><br>An estimate of the percentage of teammate field goals a player assisted while he was on the floor.">AST%</th>
          <th data-stat="stl_pct" align="right"  class=""  tip="<b>Steal Percentage</b><br>An estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor.">STL%</th>
          <th data-stat="blk_pct" align="right"  class=""  tip="<b>Block Percentage</b><br>An estimate of the percentage of opponent two-point field goal attempts blocked by the player while he was on the floor.">BLK%</th>
          <th data-stat="tov_pct" align="right"  class=" sort_default_asc"  tip="<b>Turnover Percentage</b><br>An estimate of turnovers committed per 100 plays.">TOV%</th>
          <th data-stat="usg_pct" align="right"  class=""  tip="<b>Usage Percentage</b><br>An estimate of the percentage of team plays used by a player while he was on the floor.">USG%</th>
          <th data-stat="off_rtg" align="right"  class=""  tip="<b>Offensive Rating</b><br>An estimate of points produced (players) or scored (teams) per 100 possessions">ORtg</th>
          <th data-stat="def_rtg" align="right"  class=" sort_default_asc"  tip="<b>Defensive Rating</b><br>An estimate of points allowed per 100 possessions">DRtg</th>
        </tr>
        <tr  class="">
           <td align="left"  csk="Iguodala,Andre"><a href="/players/i/iguodan01.html">Andre Iguodala</a></td>
           <td align="right"  csk="2273">37:53</td>
           <td align="right" >.291</td>
           <td align="right" >.333</td>
           <td align="right" >.500</td>
           <td align="right" >.333</td>
           <td align="right" >5.5</td>
           <td align="right" >21.6</td>
           <td align="right" >13.1</td>
           <td align="right" >17.2</td>
           <td align="right" >2.8</td>
           <td align="right" >4.4</td>
           <td align="right" >0.0</td>
           <td align="right" >8.8</td>
           <td align="right" >96</td>
           <td align="right" >97</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Livingston,Shaun"><a href="/players/l/livinsh01.html">Shaun Livingston</a></td>
           <td align="right"  csk="964">16:04</td>
           <td align="right" >.508</td>
           <td align="right" >.429</td>
           <td align="right" >.000</td>
           <td align="right" >.286</td>
           <td align="right" >6.5</td>
           <td align="right" >0.0</td>
           <td align="right" >3.4</td>
           <td align="right" >25.9</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >11.3</td>
           <td align="right" >26.9</td>
           <td align="right" >104</td>
           <td align="right" >112</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Varejao,Anderson"><a href="/players/v/varejan01.html">Anderson Varejao</a></td>
           <td align="right"  csk="509">8:29</td>
           <td align="right" >.266</td>
           <td align="right" >.000</td>
           <td align="right" >.000</td>
           <td align="right" >2.000</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >17.7</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >10.8</td>
           <td align="right" >82</td>
           <td align="right" >112</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Speights,Marreese"><a href="/players/s/speigma01.html">Marreese Speights</a></td>
           <td align="right"  csk="274">4:34</td>
           <td align="right" >.000</td>
           <td align="right" >.000</td>
           <td align="right" >.500</td>
           <td align="right" >.000</td>
           <td align="right" >45.7</td>
           <td align="right" >51.3</td>
           <td align="right" >48.3</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >36.9</td>
           <td align="right" >0.0</td>
           <td align="right" >21.3</td>
           <td align="right" >62</td>
           <td align="right" >71</td>
        </tr>
        <tr  class="">
           <td align="left"  csk="Barbosa,Leandro"><a href="/players/b/barbole01.html">Leandro Barbosa</a></td>
           <td align="right"  csk="264">4:24</td>
           <td align="right" >.750</td>
           <td align="right" >.750</td>
           <td align="right" >.500</td>
           <td align="right" >.000</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >0.0</td>
           <td align="right" >22.1</td>
           <td align="right" >125</td>
           <td align="right" >112</td>
        </tr>
        </tbody>
        <tfoot>
        <tr  class="bold_text stat_total">
           <td align="left" >Team Totals</td>
           <td align="right" >240</td>
           <td align="right" >.502</td>
           <td align="right" >.476</td>
           <td align="right" >.494</td>
           <td align="right" >.157</td>
           <td align="right" >15.2</td>
           <td align="right" >78.0</td>
           <td align="right" >44.8</td>
           <td align="right" >68.8</td>
           <td align="right" >7.7</td>
           <td align="right" >8.8</td>
           <td align="right" >10.1</td>
           <td align="right" >100.0</td>
           <td align="right" >98.1</td>
           <td align="right" >102.5</td>
        </tr>
        </tfoot>
        </table>
        </div><!-- div.table_container#div_xxxx -->
        <table class="margin_top small_text">
        <tr><td class="bold_text">Inactive:</td><td>
        <span class="bold_text">CLE:&nbsp;</span><a href="/players/k/kaunsa01.html">Sasha Kaun</a>,&nbsp;<a href="/players/m/mcraejo01.html">Jordan McRae</a>&nbsp;&nbsp;&nbsp;<span class="bold_text">GSW:&nbsp;</span><a href="/players/b/bogutan01.html">Andrew Bogut</a>,&nbsp;<a href="/players/l/looneke01.html">Kevon Looney</a>&nbsp;&nbsp;&nbsp;</td></tr>
        <tr><td class="bold_text">Officials:</td><td><a href="/referees/callami99r.html">Mike Callahan</a>, <a href="/referees/crawfda99r.html">Dan Crawford</a>, <a href="/referees/mccutmo99r.html">Monty McCutchen</a></td></tr>
        <tr><td class="bold_text">Attendance:</td><td>19,596</td></tr>
        <tr><td class="bold_text">Time of Game:</td><td>2:26</td></tr>
        </table>
        </div></td>
        </tr>
        </table>
        </div>
        <!-- SR js files --><div id=sr_js></div><script type="text/javascript">
        (function () {var sr_js_file = 'http://d2ft4b0ve1aur1.cloudfront.net/js-475/sr-bbr-min.js';if (sr_gzipEnabled) {sr_js_file = 'http://d2ft4b0ve1aur1.cloudfront.net/js-475/sr-bbr-min.js.jgz';}var sr_script_tag = document.getElementById("sr_js");if (sr_script_tag) {var sr_script = document.createElement("script");sr_script.type = "text/javascript";sr_script.charset = "utf-8";sr_script.src = sr_js_file;sr_script_tag.appendChild(sr_script);}}());</script><!-- Google Analytics --><script>
        var sr_cookie = document.cookie;
        String.prototype.sr_isMatch = function(s){
         return this.match(s)!==null
        }
        function getCookie(name) {
         var prefix = name + "=";
         var begin = sr_cookie.indexOf("; " + prefix);
         if (begin == -1) {
         begin = sr_cookie.indexOf(prefix);
         if (begin != 0) return null;
         }
         else
         {
         begin += 2;
         var end = document.cookie.indexOf(";", begin);
         if (end == -1) {
         end = sr_cookie.length;
         }
         }
         return unescape(sr_cookie.substring(begin + prefix.length, end));
        }
        var sr_cookie = getCookie('SR_user') || '';
        var sr_is_ad_free = sr_cookie.sr_isMatch('Z6SON8tTdJid');
        var sr_is_user = sr_cookie !== null && sr_cookie !== '';
        var sr_seen_modal = getCookie('modal_ad') !== null;
        (function(i,s,o,g,r,a,m){
         i['GoogleAnalyticsObject']=r;
         i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();
         a=s.createElement(o),m=s.getElementsByTagName(o)[0];
         a.async=1;
         a.src=g;
         m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', 'UA-1890630-2', 'auto');
        ga('require', 'linkid', 'linkid.js');
        ga('require', 'ecommerce', 'ecommerce.js');
        ga('set', 'dimension2',sr_is_ad_free);
        ga('set', 'dimension3',sr_is_user);
        ga('set', 'dimension4',sr_seen_modal);
        ga('send', 'pageview');
        var trackOutboundLink = function(el, url) {
         ga('send', 'event', 'outbound', 'click', url, {'hitCallback':
         function () {
         if (el.target == '_blank') {
         return true;
         } else {
         setTimeout(function() { document.location = url; }, 50);
         return false;
         }
         }
         });
        }
        /**
         * Manual callback handler
         * false == no scroll to track from previous page
         */
        // The SR overall account.
        ga('create', 'UA-1890630-20', 'auto', {'name': 'combined_tracker', 'allowLinker': true });  // New tracker.
        ga('combined_tracker.send', 'pageview');
        // The SR overall account.
        ga('create', 'UA-1890630-9', 'auto', {'name': 'sr_tracker', 'allowLinker': true });  // New tracker.
        ga('sr_tracker.require', 'displayfeatures');
        ga('sr_tracker.set', 'dimension1','bbr');
        ga('sr_tracker.set', 'dimension2',sr_is_ad_free);
        ga('sr_tracker.set', 'dimension3',sr_is_user);
        ga('sr_tracker.set', 'dimension4',sr_seen_modal);
        ga('sr_tracker.send', 'pageview');
        var linker;
        // Cross browser way to listen for events.
        function addListener(element, type, callback) {
         if (element.addEventListener) element.addEventListener(type, callback);
         else if (element.attachEvent) element.attachEvent('on' + type, callback);
        }
        var sr_links = document.getElementsByClassName("sr_link");
        Array.prototype.forEach.call(sr_links, function(el) {
         // Do stuff with the element
         addListener(el, 'mousedown', decorateMe);
         addListener(el, 'keydown',   decorateMe);
        });
        function decorateMe(event) {
         event = event || window.event;                            // Cross browser hoops.
         var target = event.target || event.srcElement;
         if (target && target.href) {                              // Ensure this is a link.
         ga(function(tracker) {
         var linker = new window.gaplugins.Linker(tracker);
         var output = linker.decorate(target);
         });
         }
        }
        </script><!-- End Google Analytics --><!-- SLF: removed the facebook and google Plus buttons --><style>.social_media { display:none;}span#player_name { margin-left: 0.5em;}</style><script src="http://network.yardbarker.com/network/ybn_pixel/12488" type="text/javascript"></script><script type="text/javascript">
        (function () {if (document.getElementById('sr_suppress_ads')) { return false; }// Adiply rails ads
        var scr = document.createElement("script");scr.setAttribute('async', 'true');scr.type = "text/javascript";scr.src = "http://ad.adip.ly/dlvr/adiply_statmarg.min.js?site_id=SportsReference_AP&t=120";((document.getElementsByTagName('head') || [null])[0] ||
        document.getElementsByTagName('script')[0].parentNode).appendChild(scr);}());</script><script src="http://static.bbref.com/js/ads.js"></script><script type="text/javascript">
        if (typeof sr_test == 'undefined') {document.write('<img class=hidden src="http://static.spref.com/x.gif?obscured">');} else {document.write('<img class=hidden  src="http://static.spref.com/x.gif?seen">');}</script>

        <div id="site_footer">
        <div id="taboola-below-article-thumbnails"></div>
        <style type="text/css">#sr_pagebottom * { margin: 0px auto }</style>
        <script type="text/javascript">
        if ((/play-index/.test(location.pathname)) ||
           (document.getElementById('sr_suppress_ads')))
        {
        }
        else if (location.pathname != '/') {
           var choice = Math.random();
           var company = '';
           if (choice <= 0.10) {
               !function (e, f, u) {
               e.src = u;
               f.parentNode.insertBefore(e, f);
               }(document.createElement('script'),
             document.getElementById('taboola-below-article-thumbnails'),
             'http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js');

               (adsbygoogle = window.adsbygoogle || []).push({});

               //googletag.cmd.push(function() {
               // googletag.defineSlot('/117033896/sr_pagebottom', [[970, 90],[728, 90]], 'sr_pagebottom').addService(googletag.pubads());
               // googletag.pubads().set("adsense_channel_ids", "5516762052");
               // googletag.enableServices();
               // });
               company = 'google';
           } else {
               // taboola
               window._taboola = window._taboola || [];
               _taboola.push({article:'auto'});
               !function (e, f, u) {
               e.async = 1;
               e.src = u;
               f.parentNode.insertBefore(e, f);
               }(document.createElement('script'),
             document.getElementsByTagName('script')[0],
             'http://cdn.taboola.com/libtrc/sportsreference-network/loader.js');

               _taboola.push({
                   mode: 'thumbnails-b',
                   container: 'taboola-below-article-thumbnails',
                   placement: 'Below Article Thumbnails',
                   target_type: 'mix'
                   });
               _taboola.push({flush: true});
               company = 'taboola';
           }

           //document.write('<div class="xx_small_text">choice: '+choice+':'+company+'</div>');

        }
        else {
            // for the front page.
           googletag.cmd.push(function() {
              googletag.defineSlot('/5702/yb_Sports_Reference', [728,90], 'sr_pagebottom').addService(googletag.pubads());
              googletag.enableServices();
          });
        }
        </script>

        <ins class="adsbygoogle"
             style="display:inline-block;width:970px;height:90px"
             data-ad-client="ca-pub-5319453360923253"
             data-ad-slot="5975682851"></ins>

        <!-- sr_pagebottom -->
        <div id="sr_pagebottom" style="width:970px; height:90px;" class="margin_bottom">

        <script type="text/javascript">
        if ((/play-index/.test(location.pathname)) ||
           (document.getElementById('sr_suppress_ads')))
        {
        }
        else if (location.pathname == '/') {
           googletag.cmd.push(function() { googletag.display('sr_pagebottom'); });
        }
        </script>
        </div>


        <div id="sr_footer" class="margin_top">
        Copyright &copy; 2000-2016 <a href="http://www.sports-reference.com">Sports
        Reference LLC</a>. All rights reserved.

        <form class="inline margin_left" method="get" name="f_footer" action="/search/search.fcgi">
        <input x-webkit-speech type="text" id="search_footer" name="search" class="search long">
        <input type="submit" value="Search" class="submit">
        </form>

        <div class="margin_top large_text"><a href="http://www.sports-reference.com/feedback/">Question, Comment, Feedback or Correction?</a></div>

        <div class="margin_top">Tools: <a href="/linker/">Automatic Player Linker</a>&nbsp;|&nbsp;<a
        href="/friv/linkify.cgi">Basic Player Linker</a></div>

        <div class="center margin_top">
        <p>Current season data provided by SportsDirect Inc.</p>
        <a href="http://sportsdirectinc.com" rel="nofollow"><img alt="Sports Direct" src="http://d2ft4b0ve1aur1.cloudfront.net/images-436/sports-direct-275x35.png"></a>
        </div>

        <div class="blockquote clear_both margin_top">
        The NBA identifications are used with the permission of NBA Properties, Inc.
        </div>




        <div class="blockquote clear_both margin_top">
        <a href="http://www.sports-reference.com/">A Sports Reference Site</a>:
        <a href="/about/">About BBR</a>&nbsp;|
        <a href="http://www.sports-reference.com/privacy.shtml">Privacy Statement</a>&nbsp;|
        <a href="http://www.sports-reference.com/termsofuse.shtml">Conditions &amp; Terms of Service</a> |
        <a href="http://www.sports-reference.com/data_use.shtml">Use of Data</a>
        </div>
        <div class="clear_both align_center large_text bold_text margin">Part of the <a rel="nofollow" href="http://www.foxsports.com/"><img alt="Fox Sports Engage Network" align="top" border="0" width="300" src="http://d3k2oh6evki4b7.cloudfront.net/images-012/engage.gif" height="33"></a> Network</div>
        </div><!-- div#sr_footer -->
        </div><!-- div#site_footer -->


        </div><!-- div#page_container -->

        </body><!-- SR -->
        </html>"""
        #</editor-fold>
        self.BBRefBoxScoreParser = BasketballReferenceBoxScoreParser()

    def extractFinalScoresTest(self):
        soup = BeautifulSoup(self.page)
        finalScores = self.BBRefBoxScoreParser.extractFinalScores(soup)
        print(finalScores)
        self.assertEquals(True, True)
        #FIX GAMEID!


if __name__ == '__main__':
    unittest.main()