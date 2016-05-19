#!/usr/bin/python
from gmusicapi import Mobileclient
import sys
sys.path.insert( 0 , '/home/sarah/Desktop' )
import secretLogin

api = Mobileclient()

usernameX = secretLogin.getEmail()
passwordX = secretLogin.getPass()

api.login( usernameX , passwordX , Mobileclient.FROM_MAC_ADDRESS )

library = api.get_all_songs()

