*HashConnections*

HashConnections queries Cisco Umbrella Investigate for hashes from Threatgrid that are shown in Investigate to be associated to a domain. It prints each sha256 hash and all network connections that were observed when the hash was analyzed with the Threatgrid sandbox environment.

---
*Example*
---

```
connections.py google.com

Hash: fc26169f5ffc299c2d282b8d32ae1340169f90e9812a311b86437d641a1911c5

google.com
74.125.29.113
200.119.204.12
74.125.29.138
200.87.164.69
74.125.29.102
74.125.29.101
190.186.45.170
74.125.29.139
74.125.29.100

Hash: 133cf81a44fe871fa91be0291977804fc9b74ef5dc5b8cb364974b1cd86cc6e6

google.com
tvrstrynyvwstrtve.com
rtvwerjyuver.com
wqerveybrstyhcerveantbe.com
supnewdmn.com
91.233.244.106
66.175.212.197
109.74.196.143
69.164.203.105
172.217.2.14
```
---
*Requirements*
---
An Investigate API key: https://docs.umbrella.com/developer/investigate-api/

https://github.com/opendns/pyinvestigate
<br>
https://github.com/requests/requests
<br>
https://docs.python.org/2.7/library/argparse.html
<br>
https://docs.python.org/2/library/configparser.html
<br>

---
*Installation*
---

git clone https://github.com/anmisccali/HashConnections

pip install -r requirements.txt
<br>
Put your API key into the config.ini file

---
*Basic Help*
---

```
usage: connections.py [-h] [--limit LIMIT] domain

Pull in hash(es) from domain

positional arguments: domain Domain to look up

optional arguments: -h, --help show this help message and exit --limit LIMIT Limit number returned, default is 100
