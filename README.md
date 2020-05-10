# openvpn-test
A script to test openvpn connections

## Installation

- install [speedtest (R) CLI](https://beta.speedtest.net/apps/cli)
- install openvpn-test: `sudo pip install git+git://github.com/ilyaukin/openvpn-test.git#egg=openvpn-test`

## Sample usage
```
sudo openvpn-test --config-dir /etc/openvpn/ovpn_tcp/ --config-mask=^tw26 --auth-user-pass .openvn-auth
```

## Customization
You can write python module containing function  
`test()` which does your custom test
and pass it in `--test` parameter.
