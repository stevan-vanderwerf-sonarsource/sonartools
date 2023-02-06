#!/usr/bin/env python3
import argparse
import json
import requests

#from https://github.com/axil/docker-registry-list/blob/master/docker-registry-list.py - public domain

""" Curl examples
curl 'https://auth.docker.io/token?service=registry.docker.io&scope=repository:library/registry:pull'
curl -v https://index.docker.io/v2/library/registry/tags/list -i -H 'Authorization: Bearer {}'
"""


def get_token(auth_url, image_name):
    payload = {
        'service': 'registry.docker.io',
        'scope': 'repository:{image}:pull'.format(image=image_name)
    }

    auth = ()
    r = requests.get(auth_url + '/token', params=payload, auth=auth)
    if not r.status_code == 200:
        print("Error status {}".format(r.status_code))
        raise Exception("Could not get auth token")

    j = r.json()
    return j['token']


def fetch_versions(index_url, token, image_name):
    h = {'Authorization': "Bearer {}".format(token)}
    r = requests.get('{}/v2/{}/tags/list'.format(index_url, image_name),
                     headers=h)
    return r.json()

def update_tags():
    index_url = 'https://index.docker.io'
    token = get_token(auth_url='https://auth.docker.io', image_name='library/sonarqube')
    versions = fetch_versions(index_url, token, image_name='library/sonarqube')
    with open('sqtagmaster.json', 'w') as sqtagmaster:
        sqtagmaster.write(json.dumps(versions))