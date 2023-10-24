from miio.integrations import vacuum 
import time
import token_extractor
import pandas as pd

username = 'your_username' #mi account username

password = 'your_password' #mi account password

floor_area = 56  #unless the vacuum cleaner dont sweep this much area at least , the cleaning would not end

connector = token_extractor.XiaomiCloudConnector(username,password)

if connector.login() :

    servers = ["cn", "de", "us", "ru", "tw", "sg", "in", "i2",'tr']

    for server in servers:
        try :
            devices = connector.get_devices(server)
            if len(devices['result']['list']):
                break
        except:
            pass


    my_devices = {'Device_name':[],'Token':[],'local_ip':[]}

    for i in range(len(devices['result']['list'])):
        my_devices['Device_name'].append(devices['result']['list'][i]['name'])
        my_devices['Token'].append(devices['result']['list'][i]['token'])
        my_devices['local_ip'].append(devices['result']['list'][i]['localip'])


    my_devices = pd.DataFrame(my_devices)
    ip = my_devices[my_devices['Device_name'].str.contains('vacuum',case=False)]['local_ip'].iloc[0]
    token = my_devices[my_devices['Device_name'].str.contains('vacuum',case=False)]['Token'].iloc[0]

    myvac= vacuum.RoborockVacuum(ip, token)


    while (myvac.status().clean_area<floor_area) & (myvac.status().battery >20):
        myvac.resume_or_start()
        time.sleep(10)
            
    while myvac.status().state != 'Charging':     
        myvac.home()
        time.sleep(20)

    print('Cleaning is finished')

else:
    print('mi account login failed')

