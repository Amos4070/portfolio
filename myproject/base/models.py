from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # ✅ Correct import
from ckeditor_uploader.fields import RichTextUploadingField







class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)  # ✅ Correct
    slug = models.SlugField(null=True, blank=True)


    thumbnail= models.ImageField(null=True, blank=True, upload_to="media", default= "placeholder.jpg")


    def __str__(self):
        return self.headline




    def save(self, *args, **kwargs):
        if self.slug is None:  # ✅ Correct check for None
            slug = slugify(self.headline)  # ✅ Generate base slug
            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1

            while has_slug:  # ✅ Ensure slug uniqueness
                count += 1
                slug = f"{slugify(self.headline)}-{count}"
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug  # ✅ Assign final slug

        super().save(*args, **kwargs)  # ✅ Always call super().save()










        

    # def save(self, *args, **kwargs):
    #     if self.slug ==None:
    #         slug = slugify(self.headline)
    #         has_slug = Post.objects.filter(slug=slug).exists()
    #         count =1
    #         while has_slug:
    #             count +=1
    #             slug = slugify(self.headline) + '-' + str(count)
    #             has_slug = Post.objects.filter(slug=slug).exists()
    #         self.slug = slug



    #     super().save(*args, **kwargs)

    
  