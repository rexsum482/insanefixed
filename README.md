# InstaInsane Fixed v1.0
## Author: https://github.com/rexsum482
## IG: instagram.com/rexsum420
## Credit to: https://github.com/umeshshinde19
Instainsane is an Shell Script to perform multi-threaded brute force attack against Instagram, this script can bypass login limiting and it can test infinite number of passwords with a rate of about 1000 passwords/min with 100 attemps at once.
Fixed handling errors smoothly so that program doesn't exit on an error/bad api call. Created a password generator that creates passwords that fit modern requirements of minimum 8 characters, 1 uppercase, 1 lowercase, 1 symbol. Edit however you like.

## Legal disclaimer:
Usage of InstaInsane for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program 

![insane](https://user-images.githubusercontent.com/34893261/38772658-97646698-4012-11e8-9b5e-65596e70a5ff.png)

### Features
- Multi-thread (100 attempts at once)
- Save/Resume sessions
- Anonymous attack through TOR
- Check valid usernames
- Default password list (best +39k 8 letters)
- Check and Install all dependencies

### Usage:
```
git clone https://github.com/rexsum482/insanefixed.git
cd insanefixed
chmod +x instainsane.sh
sudo ./instainsane.sh
```

### Install requirements (Curl, Tor, Openssl):

```
chmod +x install.sh
sudo ./install.sh
```

### How it works?

Script uses an Android ApkSignature to perform authentication in addition using TOR instances to avoid blocking. 
The script uses Instagram-py algorithm (Python), see the project at: https://github.com/antony-jr/instagram-py
Thanks to: @umeshshinde19 https://github.com/umeshshinde19

### Donate!
Support the authors:

<noscript><a href="https://liberapay.com/umeshshinde19/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>
