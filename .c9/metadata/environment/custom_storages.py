{"filter":false,"title":"custom_storages.py","tooltip":"/custom_storages.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":43},"action":"remove","lines":["from django.conf import settings","from storages.backends.s3boto3 import S3Boto3Storage","","","class StaticStorage(S3Boto3Storage):","    location = settings.STATICFILES_LOCATION","","","class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":33},{"start":{"row":0,"column":0},"end":{"row":10,"column":19},"action":"insert","lines":["from django.conf import settings","from storages.backends.s3boto3 import S3Boto3Storage","","","class StaticStorage(S3Boto3Storage):","    location = settings.STATICFILES_LOCATION","","","class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION","© 2019 GitHub, Inc."]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":19},"action":"remove","lines":["© 2019 GitHub, Inc."],"id":34}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":0},"end":{"row":10,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567286364569,"hash":"16d5013d8203c8d661f1e5064f6c8bb799533df9"}