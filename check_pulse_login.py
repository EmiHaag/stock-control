import requests.exceptions
def check_pulse_conn():
    try:
        r = requests.get('http://fls.ncr.com/cgi-bin/global.pl?country=6905&ce=ar903e46&report=OH&B1=Submit+Query')
        r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return False
    except requests.exceptions.HTTPError:
        return False
    else:
        return True # Proceed to do stuff with `r` 

""" status = check_pulse_conn() """
""" if status:
    print("Pulse connection good.")
else:
    print("Error al conectarse a Pulse") """