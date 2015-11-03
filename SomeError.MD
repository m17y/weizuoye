1:Database returned an invalid value in QuerySet.datetimes(). Are time zone definitions for your datab
    
    修正seting中配置
    USE_TZ = False

    LANGUAGE_CODE = ‘zh-cn‘

    TIME_ZONE = ‘Asia/Chongqing‘