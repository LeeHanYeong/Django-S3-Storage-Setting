from storages.backends.s3boto3 import S3Boto3Storage


class DefaultFileStorage(S3Boto3Storage):
    location = 'media'


class StaticFilesStorage(S3Boto3Storage):
    location = 'static'
    file_overwrite = True
