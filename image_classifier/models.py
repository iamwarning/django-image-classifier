import uuid

from django.db import models
from keras_preprocessing.image import load_img, img_to_array
from PIL import Image as sec
import numpy as np
from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input, decode_predictions
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import MediaCloudinaryStorage
from classifier import settings

# Create your models here.
class Image(models.Model):
    picture = models.ImageField(upload_to="classifier", storage=MediaCloudinaryStorage())
    # picture = CloudinaryField("Image", resource_type='image')
    classified = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank=True)

    def __str__(self):
        return "Image classified at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M:%S'))



    def save(self, *args, **kwargs):
        try:
            print('URL build --> ', self.picture.file)
            # image = sec.frombytes('RGBA', (299,299), self.picture.file.read(), 'raw')
            image = load_img(self.picture.url, target_size=(299,299))
            image_array = img_to_array(image)
            to_pred = np.expand_dims(image_array, axis=0)
            prep = preprocess_input(to_pred)
            model = InceptionResNetV2(weights='imagenet')
            prediction = model.predict(prep)
            decoded = decode_predictions(prediction)[0][0][1]
            self.classified = str(decoded)
            Image.objects.filter(pk=self.id).update(classified=self.classified)
            print(str(decoded))
            print('Success')
        except Exception as ex:
            print('Error --> ', ex)
            self.classified = 'Failed to classify'
        super().save(*args, **kwargs)

