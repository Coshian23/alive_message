import twitter

def lambda_handler(event, context):

    # doc twitter account
    CK = "AbZQOQfJhhepEf29CvqGiuglS"
    CS = "VqyXmtDlaZnKy9WkHDtq0Raioe71fH317Iwi4isjg4SAGN5zqD"
    AT = "1166294649364860928-8qvnfDAF0uKkrpHEyKNIDUwj1NgEaq"
    ATS = "O87jotf4uYXrZRt6FdQsNA4bVA8U9b5IFv2LfvuKXR2Ho"

    api = twitter.Api(CK,CS,AT,ATS)
    # api.PostUpdates("ラーメン食べて和香枠")
    json = api.PostDirectMessage('@snowwhite202003', 'Hello World!', return_json=True)
    print(json)

    # grumpy twitter account
    CONSUMER_KEY = "yLIi0DRVcq0EmM9aqBfKuMGlt"
    CONSUMER_SECRET = "vxgoBxh9vTi0rexMMWVZfitzQxq4QIDR04MqUoVnMOwI6yr741"
    ACCESS_TOKEN = "1225580764789497857-iIIzE0LP09szc2OCQ68MjvDrr2HMTD"
    ACCESS_SECRET = "HG7A7txr2AqDF7qfviFK1NiR71J2druFT3F5MrgH442Di"

lambda_handler("","")