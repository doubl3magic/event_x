from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            # Invalid case
            raise ValidationError('Value must contain only letters')


class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(self.max_size))


def validate_image_size(image):
    file_size = image.file.size
    max_size = 8

    if file_size > max_size * 1024 * 1024:
        raise ValidationError(f"Max file size is {max_size}MB")


