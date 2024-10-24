import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf"

# RESTCONF HTTP headers
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070147",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.147.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }

    resp = requests.put(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070147",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if 200 <= resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070147 is created successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070147",
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if 200 <= resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return "Loopback 65070147 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


# Uncomment and implement these functions as needed

def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070147",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        }
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070147",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if 200 <= resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070147 is enabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))



def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070147",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        }
    }
    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070147",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False
    )
    if 200 <= resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070147 is disabled"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback65070147"
    resp = requests.get(
        api_url_status,
        auth=basicauth,
        headers=headers,
        verify=False
    )
    if 200 <= resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback65070147 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback65070147 is disabled"
    elif resp.status_code == 404:
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No interface Loopback65070147"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
