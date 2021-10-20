# URLExtractor

Information gathering & website reconnaissance

## Screenshot
![Screenshot](Screenshot.jpg?raw=ture "Screenshot")

------

**Usage:**
`./extractor.sh http://www.target.org/`


Features:
------

* IP and hosting info like city and country (using [FreegeoIP](http://freegeoip.net/))
* DNS servers (using [dig](http://packages.ubuntu.com/precise/dnsutils))
* ASN, Network range, ISP name (using [RISwhois](https://www.ripe.net/analyse/archived-projects/ris-tools-web-interfaces/riswhois))
* Load balancer test
* Whois for abuse mail (using [Spamcop](https://www.spamcop.net/))
* PAC (Proxy Auto Configuration) file
* Compares hashes to diff code
* robots.txt (recursively looking for hidden stuff)
* Source code (looking for passwords and users)
* External links (frames from other websites)
* Directory FUZZ (like Dirbuster and Wfuzz - using [Dirbuster](https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)) directory list)
* [URLvoid](http://www.urlvoid.com/) API - checks Google page rank, Alexa rank and possible blacklists 
* Provides useful links at other websites to correlate with IP/ASN
* Option to open ALL results in browser at the end

Changelog to version 0.1.9:
------

* Abuse mail using lynx istead of ~~curl~~
* Target server name parsing fixed
* More verbose about HTTP codes and directory discovery
* MD5 collection for IP fixed
* Links found now show unique URLs from array
* [New feature] **Google** results
* [New feature] **Bing** IP check for other hosts/vhosts
* [New feature] Opened ports from **Shodan**
* [New feature] **VirusTotal** information about IP
* [New feature] **Alexa Rank** information about $TARGET_HOST

Requirements:
------

Tested on Kali light mini AND OSX 10.11.3 with brew
```
sudo apt-get install bc curl dnsutils libxml2-utils whois md5sha1sum lynx -y
```

**Configuration file:**
```
CURL_TIMEOUT=15 #timeout in --connect-timeout
CURL_UA=Mozilla #user-agent (keep it simple)
INTERNAL=NO #YES OR NO (show internal network info)
URLVOID_KEY=your_API_key #using API from http://www.urlvoid.com/
FUZZ_LIMIT=10 #how many lines it will read from fuzz file
OPEN_TARGET_URLS=NO #open found URLs at the end of script
OPEN_EXTERNAL_LINKS=NO #open external links (frames) at the end of script
```

Todo list:
------

* [x] Upload to github :)
* [ ] Integration with other APIs
* [ ] Add  host regex validation
* [ ] Use GNU parallel to fuzz URLs
* [ ] Export to CSV
* [ ] Possible migration to python
* [ ] Integration with JoomScan/WPScan/CMSmap
* [ ] Integration with CipherScan
* [ ] Check for installed packages

## Download and Clone
> Download: Click [Here](https://github.com/The404Hacking/URLExtractor/archive/master.zip) (URLExtractor-master.zip)

> Clone: git clone [https://github.com/The404Hacking/URLExtractor.git](https://github.com/The404Hacking/URLExtractor.git)

## The404Hacking | Digital Security ReSearch Group
[The404Hacking](https://T.me/The404Hacking)

## Follow us !
[The404Hacking](https://T.me/The404Hacking) - [The404Cracking](https://T.me/The404Cracking)

[Instagram](https://instagram.com/The404Hacking) - [GitHub](https://github.com/The404Hacking)

[YouTube](http://yon.ir/youtube404) - [Aparat](http://www.aparat.com/The404Hacking)

[Weblog](http://the404hacking.blogsky.com) - [Email](mailto:The404Hacking.Team@Gmail.Com)
