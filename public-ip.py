import requests
import time

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        ip_data = response.json()
        public_ip = ip_data['ip']
        return public_ip
    except Exception as e:
        return str(e)

log_file = 'ip.log'
sec_interval = 7200

while True:
    public_ip = get_public_ip()

    with open(log_file, 'a') as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f'{timestamp} - IP Público: {public_ip}\n')

    time.sleep(sec_interval)

  
# LINHA DE COMANDO NOHUP
# nohup python3 script.py > script.log 2>&1 &
# Depois valide o PID que aparecer com "htop" 
