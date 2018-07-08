import requests

url = "https://www.tuandai.com/user/checkPhoneNew"

querystring = {"a":"2491"}

payload = "sPhone=17513502491&aliyTicket=FFFF0000000001796346%3A1530946669408%3A0.7151143366758277&aliySessionId=0152JIZgtMjy7iQLwB8JakWTfmHJ1xfZUECwDeZnop5DVlOxJxjjapS8bujf1TwfERvuzMzUyWTQ5fkcKbLlFPm-nah9neI7tyalqC_cMqHnZYJhWU8_j0GwbPbMwAzE-0DH-fFh-C_QHjCuna6UwPZBZ3_D8I1SlwFh3bd5oKhE6uqiizQDkInowDBYya5j0To0hCr8l3zO2JoOz1oBiH5JCATC00fhQKDp1S8fgJoEqsKSI0isdCsaOq0YvILA_CCoty7V6GdlBXOy-Au4bu9je1GupHe4Tm19nmiWVQYVqy89_bozQjA3EZQUb_F4uRtOLQwid-VEoy3AUsfuLRnbZ1CNFAvD6KKeisk3rWS019blrKLMEsDxyHGtdbS8cH&aliySig=05a1C7nT4bR5hcbZlAujcdydL7Z_ZdHIqH90a0y5WDOAnaUECCBAbfTBkWJ69CTt98Lkr3ZOkU2X1NzVKIE9B565nnpd8jsy3H9RTa-8PaRe9iGp4-RSlo2wwzH2kqN58cZH69-GDjXpju4ucc8vFTecyF13GjDQABs0wYTtmTvLwIYjmHs9qIL4Xy2Q03S1tDG0BITLalbbcPYH9rQKfcxotPtvKoDJpXh35Px3tinmthScfK7YnqjybsdGstCfr6dxtZH6phFiO0XZQKvr4gug6O-7aynxTFHSwTMmvPHFEd9WZIkHWlGpdhVEBdPPkAagIORDqVJadUDU36BOJn74ni7rZGbSucHL1N3B5tTtkhsRdwkgTivwXgs7pC7yXWrkUZvGQVXrXNWyx06T_vLdR20VG0Mlh-gzN8WF4nAE8wM7-f6C7ypmnr5XKyVdCOgZTsUhJZ9C58mFesencdbVNe_rjHb9mgyCCZkWlrCAY3V6eW6Z_zRu3D8AiphlUV-IEFIWfj48anKTKXQ8818a7H-_N5pZctBfCtiLxlOpnWUqw_Rsc3BclCNgLSoq2rTJqOMNFdjYnTQ6u4BDmjUFKbFqZdAByUBbfrdQtA5_B3i4dZeDGwlQ617y04AePKURVBt9lQiJmjkIAkwyBHKOHBnJfxceV0K_YEdncrN8WL_uj6PPN7HuU4hVk-W9L4&aliyScene=register"
headers = {
    'cookie': "acw_tc=AQAAAPVmY0nzHAQAIxYRDqQKTEzFZPuF; td_visitorId=c514c424-ee16-f3a2-f18f-e23f038fd947; td_exit_flag=1; sajssdk_2015_cross_new_user=1; _uab_collina=153094666639867465162735; JSESSIONID=sC6YjsK2cvVTUC-tTZnptdE4BJdKIIh3R9BL78gd; tuandai005=x3arjnDqJrDeDWL2VceJ79sGbFcM9K12DyAUNykb3ohzX3lNfEAeIA%3D%3D; u_asec=099%23KAFE%2FGEKEcEEhYTLEEEEEpEQz0yFD6DhZcaMZ6g3Su9EW6VwZXw7G6f1DEFETcZdt9TXE7EFbOR5DFMTEEyP%2F9iSlllUE7TxYpgjD5GSLECq1nZW2h5IwqsM2e04IEWcvHNlUJ6%2F1HvkLHyU0HeqmdeI02HryIYRvFdlQwMZ1Vnyk8lDqw%2FMk6A0puGWoD4fB0ANtkj2Lmf3wHGTEELP%2F3kjCjWvmcQTEEy%2F%2F3ynScwbE7EUsyaSt3llsyaP%2F36alllr1rZddn3llu8FsyaaolllW2aP%2F36alllzOqMTEF2C36iq6wO3aUVEutxsrQdtaGuDZapGwwZpLy8krO4RivDcbf2SrodRiLZDALYdaql3aeXfNVX3LQdtU6kG6dbpwwZnZR2BlYFETIZ4gbq%3D; td_half_sessionId=e2a4ffc0-dcce-24fb-3cc1-cd62f032fed2; Hm_lvt_6dff67da4e4ef03cccffced8222419de=1530946666; Hm_lpvt_6dff67da4e4ef03cccffced8222419de=1530946669; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216473883f6f5cf-0923584bdaaaf4-474a0521-2073600-16473883f70d89%22%2C%22%24device_id%22%3A%2216473883f6f5cf-0923584bdaaaf4-474a0521-2073600-16473883f70d89%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22PlatformType%22%3A%22TDW%22%7D%7D; _umdata=0712F33290AB8A6DCD5C5D18AD736A658A35613E3E0B308B57901EEF435778A496CAD1B698B56207CD43AD3E795C914CF92D3862A2F9FD0D61831771662CC771",
    'origin': "https://www.tuandai.com",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'x-requested-with': "XMLHttpRequest",
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'cache-control': "no-cache",
    'authority': "www.tuandai.com",
    'referer': "https://www.tuandai.com/user/register.aspx",
    'postman-token': "1e9a28e6-9d6f-c206-4609-0e7a797d1319"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
