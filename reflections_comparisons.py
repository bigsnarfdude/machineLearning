#! /usr/bin/env python
# encoding: utf-8

import sys, os
import re, string

from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


############################################################
#
# this is the section that takes the data and process the
# incoming data in a selection of features and category
#
############################################################

feature_count = {}
category_count = {}
    

def train_from_data(data):
    for category, documents in data.items():
        for doc in documents.split():
            train(doc, category)
    #print feature_count

def train(item, category):
    features = get_features(item)
    for f in features:
        increment_feature(f, category)
    increment_cat(category)

def increment_feature(feature, category):
    feature_count.setdefault(feature,{})
    feature_count[feature].setdefault(category, 0)
    feature_count[feature][category] += 1

def increment_cat(category):
    category_count.setdefault(category, 0)
    category_count[category] += 1
    


############################################################
#
# calculating scores functions below
#
############################################################

def probability(item, category):
    """
    probability: prob that an item is in a category
    """
    category_prob = get_category_count(category) / sum(category_count.values())
    return document_probability(item, category) * category_prob

def get_category_count(category):
    if category in category_count:
        return float(category_count[category])
    else:
        return 0.0

def document_probability(item, category):
    features = get_features(item)
    p = 1
    for feature in features:
        print "%s - %s - %s" % (feature, category, weighted_prob(feature, category))
        p *= weighted_prob(feature, category)
    return p
    
#def get_features(document):
 #   all_words = word_tokenize(document)
  #  all_words_freq = FreqDist(all_words)         
  #  print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
  #  return all_words_freq

def get_features(document):
    document = re.sub('[%s]' % re.escape(string.punctuation), '', document) # removes punctuation
    document = document.lower() # make everything lowercase
    all_words = [w for w in word_tokenize(document) if len(w) > 3 and len(w) < 16]
    p = PorterStemmer()
    all_words = [p.stem(w) for w in all_words]
    all_words_freq = FreqDist(all_words)
    print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
    return all_words_freq
    
def get_feature_count(feature, category):
    if feature in feature_count and category in feature_count[feature]:
        return float(feature_count[feature][category])
    else:
        return 0.0
        
def feature_prob(f, category): # Pr(A|B)
    if get_category_count(category) == 0:
        return 0
    return (get_feature_count(f, category) / get_category_count(category))
    
def weighted_prob(f, category, weight=1.0, ap=0.5):
    basic_prob = feature_prob(f, category)
    totals = sum([get_feature_count(f, category) for category in category_count.keys()])
    w_prob = ((weight*ap) + (totals * basic_prob)) / (weight + totals)
    return w_prob
        


data = {'ruby': 'wanted learn more numpy when doing euler projects also learned about ipython today porting matlab python through numpy image project move maybe explore more imaging large part worked different ways convert images gray using different initially planned attend john resigs meeting morning then continue with suduko solver python suduko game lasted longer than expected greatlearned types functions objectslack classesuse this syntactic aspects browsers consolelocal file hosting learn about buttons pygame well manipulation certain areas also learn more about variables class which functions have access drawn numbers actual using knearest then flash these into cell also write sudoko generator which ability button process click highlights then click again removes learned more about object creation assist coding well lists which seem work like java arraylist started ability draw plan learn more pygame deal with action events within suduko move connect game mechanics start working generate puzzle with difficulty levels around with action events understanding deal with them learnt further structuring aspects classes developed further learning python hard like make solver have user would great turn this into would ideally like image processing suduko puzzle like robot then solve inform user incorrectcorrect moves maybe even make network tutorials finally imported library pygame tkinter sklearn started playing with these wrote suduko python more more python learn more python file openings also discuss java code with someone else help them going forward with thinking about packages focusing python more python variables file systems also helped with some more android opencv more work complete more scala python stated planned integrate into android well open also know opencv functionality stated yesterday learn more python scala well more python scala issue with regards google play being android emulator write some more regarding previous project projects onto github share with integrated successful read more about opencv understood sample code also some more python planned learn more scala implement some functions newly setup eclipse scala continuing with scalamaybe more pythonthought project gephi python script friendships well likes develop eventually twitter toofound python wrapper weeks function programming principles scala some lectures social network analysis created first network wrote more formalised goals with sunday group study concerning pentesting security systems fixed computer issues setup android environment split harddrive ubuntu continue studying python scala probabilistic graphical methods exactly what said would also advancing knowledge regards linux command learned some more implemented exercises from learning python hard planned start evolutionary using open source going start usinglearning implemented open source java code within eclipse learnt more about using debugger within eclipse solving issue through trial error completed palette library planned start cleaning kandid code which evolutionary generator learn cfdg from java scala 103012 finish afternoon clean kandid find interact with cfdg through java ended starting library reference when using cfdg hsbs learning more going complete watershed read about mean evolutionary finish watershed algorithm image segmentation finish atrous ittens colour start writing time table list todo things remainder both tasks need completion watershed simply changing implementation haralick texture descriptor symmetry implementations image descriptors edges finish implementation itten implementation haralick texture descriptor symmetry implementation ittens colour theory further tamura featuresusing watershed implementation colour translator implementation color polar coordinateshelp assist others with kmeansunderstanding fuzzy complete tasks initially able above ditracted implementing rgbtoyuv then kmeansdifferent from initial debugged some vtheoretical based codealso worked class arrays java libi repeated some code which wanted segmentation algorithms colour theory regards itten emotion implementation ittens colour theory further tamura features using watershed implementation colour translator implementation color polar coordinateshelp assist others with kmeansunderstanding fuzzy watershed read about ittens colour wheel determining emotions from image read learnt more about tamura texture features implemented color from vice versa color harmony relation image learned plan about applying wavelets images also about meaningful info from edge implementation attempt implement earth movers distance define colourfulness image look using symmetry detection well other employable some wavelets also meaningful info from edges through creating','vincent': 'wanted build server clients into fully deployable package service work machine learning part final project need stop worrying about work while makes unproductive worrying about stuff that really cant control right this moment while will gather bunch machine learning stuff will tackle next couple testing client server gathering exfiltration data from network traces captured over 10000 packets classification algorithm applied couple jobs dftp work putting markup images more late last night watching team jacob didnt enough sleep vampire zombies verbose tcpdump parser finished finished twisted server running with redirected traffic output napped when woke everything crystal clear lines code debug fixed after sleeping wanted learn more about sparse matrix machine learning learn basics pandas scipy numpy spent couple hours debugging navigator with corey dataset corey able sample dataset currently training full wanted machine learning today talk getting programming produced more than answers reality returning work doesnt seem exciting when prospects dftp detection sick most yesterday today built smtp server that does lookup record first before processing request mail server bouncing spoofing messages instead relying outside wanted build python network intrusion detection system with sklearn detect algorithm finish then will pickle bunch other algorithms against 1999 loaded dropped couple features first step fitting data several hours computation training still running logistical regression wanted make another feature dftp project wanted work sure have necessary libraries built more didnt work dftp just demod weekly show tell ended trying load 1999 dataset into pandas loaded found sklearn library wasnt properly installed rebuilt planned review code from other hsers bittorrent clients build domain name system client server coding like today awesome settling project last half makes coding easier when visualize project from start several versions dftp client server pushed code github plain text file transfer packet wireshark malformed packet checked twisted submission 5589 closed watched etsy security dude planned validate bittorrent client python write lexerparser sklearn make cheating domain name system transfer protocol will build bittorrentish file transfer server client learned about python networking found move data queries built small server that parse payloads tried explaining what working will build bittorrentish file transfer server client planned hold next project stuck choosing building lexerparser rule enforcement scikitlearn build visualization infosec build bittorrent client python nick said pick something that love work continue struggle will validate each paths plan next steps better picture each different projects value their pros cons their value overall programming effort python machine struggled continued struggle with committing final project worked closing twisted 5888 5589 tickets worked proxycaching select server worked kdd99 machine learning random forest anomaly detection planned learn stuff have more programming about magic decorators functions that like classes paired with julie scrapper investigated flask found basic methods return json restful returns demod ipython julie blogged going clojure recall think wanted tackle sklearn patch submission close twisted 5888 5889 tickets merge classes build dont know switched code coded really dont count getting whitespace trailing characters programming maybe similar editing proofreading then maybe code thru pep8py pushed github didnt touch open source software submissions didnt blog didnt really tweet much learn about rugged devops etsy devops velocity conference with issues 5888 5889 patch submissions twisted work proxy caching good stuff apart glue together again certain best refactoring session pushed code still apart scripts rewrote them simplehttp simpleproxycache refactored much lost select statements made functions proxy import script module class functions http missed twisted lurk around open hatch sympy brubeck twisted reports open tickets looking simple documentation type easy need patient with submitting patches just fixed away maybe best approach because submission looks half brained poorly submitted need have confidence contributions work even make patch issue 5888 twisted project blogged about because didnt realize that supposed update trunk prior submitting patch noticed patch using diff updated trunk seeing holman present twice decided would contribute open source navigated couple contributions with nimi corey time jump into contribution water also watch indie games with will keep hunting help with keep contributing weekend some contributions under belt github indie games movie ended finding documentation twisted ended patching request only find that there already submitted patch pending just catalogued maintainers ended filing report that found twisted with john twisted will have have more being lost lost over head johns talk seen some cool implementations javascript jquery jqueryui continue struggle with twisted learning have learned that struggling with decorators callbacks classes event build stuff will have seek help sooner started nice productive with http server crashed halt built simple http server progressed proxy server progressed proxy server with cache manage incoming data stream focused code learn small prototype where take data make decisions data planned integrate twisted into tictactoe network game cleaned code from thursday with nick feedback last weeks townhall meeting more about python sockets module hack yesterday with corey ruby great results good impacket module sockets select modified learned more about conversion filtering pattern matching built packet sniffer based impacket recommended planned work tictactoe winning even with sleeping issues with noisy roommates felt confident this week building different things would like leverage programs integrate them into objects classes moar jumped ahead build webserver with sockets working right browser talk server eventually should able talk browser correctly serve tictactoe built some tools slept times classes network communication build some parsers handling data stream home sleep until thursday bean slept chair learned about unittest built unit tests data stream parsers built network learn sleep more didnt have more control with sleeping getting because roomates effects design with john resig built server class game class network very satisfied with todays progress done week with playable about python network evar hope this productive everyday hacker school guess like building simple network things like port scanners grinders text browser simple chat servers that talk need relax more have like these programs github much shaving built bunch network programs simplechatserverpy dnsgrinderpy echoserverpy planned learn about bloom filters different hashing technology memcache implement these very productive morning will take advice from lisa apply recommendations lisa suggested that stop stressing about output comparison others just code have will give simple memcache python simple round robin tested different hashing algorithms didnt code much afternoon into sonali lisafrom previous batch going ikea took water taxi ikea different types bloom filters more sleep find quiet places study keep having while programming turn twitter facebook email phone distractions about different implementations built script demonstrate hashing 1000000 character passwords learned crypto murmurhash jenkins speed accuracy argument learned that hadoop cassandra bloom filters reduce tweets notes bryants talk code read code sleep code about bloom filters wrote python program specificially test murmurhash commutatieve monoids found stuff monads bloom filter implementation pthon finded webscraper that sings finish tweetradio script that reads tweets song lyrics want review data mining book dive deeper into machine hacker school back into fought with unicode parsing errors finally used regex replace data with clean data could parse html brought book reviewed chapter peters code review refactoring communitative wanted tackle pairing saturday night nimi worked issue openhatch corey lynch paired issue 1264 scikitlearn listened 2chainz choice barry white coreys choice meeting hopefully with more people north williamsburg hacker school more waiting pull request merge trunk couple lines issue 1264 scikit learn blogged parallel processing random forests monte carlo emergency water stashed around loft putting away candles that crazily found around whole planning anxiety took over most everyone freaked left loft spent worrying about hurricane flooding electricity twitter facebook lurked tweets stay busy activated distraction wanted player game completed first phase workable code generators solve problem with firewall pushed need back plan this thing gets implemented cleaned learned about generators created first chained generator allisons introspectionrb work learn implementation tracing module review python implementations trace traceback inspect builtins confused after talk wanted explore haskell clojure scala research need code everyday find book learning boring truthful follow lessons examples enough need strike balance between learning coding feel productive maybe just need enjoy more sans learned about bunch modules found good post python module series explanations each modules awesome side tracked with some generator object dict storage file processing needed planned learn about rubys implementation settrace maybe implement tracing objects functions more booked time with alex continue thru work alisons implementation with theyre ahead because this learning product development implementation settrace down huge rabbit hole where learn about debugging learn about ackgrep from alex payne going finish thats going figured moving parts just need duct tape them planned learn learn about debugging validate scope building online ruby doing hackday with hackerschoolers build twitter sentiment engine visualization upcoming productive research learning happy with outcome enjoyed talks today ossjulia nltk processing meetup pivotal been working learning code working have learned going write script test understanding code base back wanted review classes build bunch classes something interesting refactor some code into will continue using look implemented ruby great project keep presented blogged about setup review from n00bs point view steps getting into interesting project learned setup google engine into pgloggerpy changed localhost setup take inheritance class methods instance hoping work bunch classes interacting with each other like game jukebox would really like moment feel like productive need concentrate more focus more feel stalled without learned them built some classes override some methods still unclear most effective uses like would just rewrite bunch classes into your class instead nested planned learning decorators generators maybe reinforcing reduce filter think nice learn some interesting related topics saturday afternoon learning session still about caught memcache wanted come school today have will rest better mondays classes excited return will review generators learn about their practical uses would like learn about decorators rested most computer review functions that return values sure what practical uses funcs that return values data passed around initialized from function planned extend class process data using euclidean distance calculation determine pairing partners calculation planned build simple pairing program made classes with would like complete program program webscrape data push directly gephi will think about effectiveness time another class will interact with data objects will work storage data difficulty doing calculation because didnt have weightings peoples skill score learn program better dataset have been more productive start ended visualizing data node graph gephi blogged planned build simple pairing program made classes with will continue pair with someone nice have someone talk finish program close were able objects created into another objects talk each other information session data security extract data created objects dict longest time thought data structure json nope just exported just going learn about python review hard book dive into book going ensure understood concepts reduce filter will stick lessons books classes some interesting classes interacting with each other have done classes java ruby continue fall short implementing extended brain teaser learned about list comprehensions reduce filter lambda virtualenv damn xcode4 command line'}








train_from_data(data)

vincent = probability("Honolulu Brooklyn Perpetual student Python C Keen on machine learning NLP in sklearn pandas numpy joblib cython Kaggle cool stickers", "vincent")
ruby = probability("Honolulu Brooklyn Perpetual student Python C Keen on machine learning NLP in sklearn pandas numpy joblib cython Kaggle cool stickers", "ruby")

print "This is Corey scored against Vincent's reflections", vincent
print "This is Corey scored against Ruby's reflections", ruby

