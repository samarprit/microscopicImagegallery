# microscopicImagegallery
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# creating tiles folders for each of the large images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## import the os specific module and file handling and regular expression module\n",
    "import os,io,re"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### enter the file name of the file \n",
    "f_fullname=file(raw_input(\"Enter Filename: \"), 'r') \n",
    "###### removig the extension only the first part of the file name\n",
    "each_file=re.split('.',f_fullname)[0] \n",
    "###### load the image into openslide object\n",
    "    Op_object=op.Openslide(each_file)\n",
    "###### generating thumbnail object\n",
    "\timage=op_object.get_thumbnail(op_object.level_dimensions[op_object.level_count-1])\n",
    "##### \t\n",
    "    image.save(each_file+\".bmp\")\n",
    "######\n",
    "\timage.close()\n",
    "###### for creating smaller pic files\n",
    "\tos.system('python deepzoom.py %s' %f_fullname)\n",
    "###### generating deepzoom object\n",
    "\tdp_object=op.deepzoom.DeepZoomGenerator(op_object) \n",
    "###### extracting the content of the xml file\n",
    "\tdp_xml_tag=dp_object.get_dzi('jpeg')\n",
    "###### stroring name of the dazi file in a variable\n",
    "\tdzi_fname=each_file+\".dzi\" \n",
    "###### creating a dzi file AND OPENING\n",
    "\tf=open(dzi_fname,\"w+\") \n",
    "###### writing to a dzi file\n",
    "\tf.write(\"<?xml version='1.0' encoding='UTF-8'?>\"+dp_xml_tag)\n",
    "###### closing a dzi file\t\n",
    "    f.close() "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Do this for evey large tiff file in the folder. No need to mention the path of the folder."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### there is an alternative application vips.exe. \n",
    "##### its command is  vips.exe -copy --vips.progress '/path/to/input tiff file.tiff'  '/path/to/output.bmp' [layout=dz]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Django framework establishment for creating a photo gallery app"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "djanjo-admin startproject photo_gallery# gallery name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# starts a project with admin capacity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "cd photo_gallery"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "python manage.py migrate"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### for admin purposes like uploading images and editing images or handling web content from the backend of the software  \n",
    "python manage.py createsuperuser"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### create a new folder called media_files in this folder. these will be used for stroing the images\n",
    "#### go to the photo_gallery folderand open settings.py and add MEDIA.ROOT AND MEDIA.URL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# open urls.py and the ## lines into the script. This is for linking the mediafiles to the web application\n",
    "from django.conf import settings\n",
    "## ##from django.conf.urls.static import static\n",
    "## from django.conf.urls import url\n",
    "## from django.contrib import admin\n",
    "## from photos.views import photo_list\n",
    "\n",
    "## urlpatterns = [\n",
    "##    url(r'^admin/', admin.site.urls),\n",
    " \t]\n",
    "# ##if settings.DEBUG:\n",
    "# ##   urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# now we have to start an app for uploading and storing the images. Make sure you are in the folder where is manage.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    " python manage.py startapp photos # make sure you have Pillow it is a module which is used for veiwing imagefield."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# open settings.py inside photo_gallery folder and add the line as follows\n",
    "### INSTALLED_APPS = [\n",
    "###    'django.contrib.admin',\n",
    "###    'django.contrib.auth',\n",
    "###    'django.contrib.contenttypes',\n",
    "###    'django.contrib.sessions',\n",
    "###    'django.contrib.messages',\n",
    "###    'django.contrib.staticfiles',\n",
    "###    'photos',<--- add this line\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# open model.py in the photos app folder and add the following lines \n",
    "##### class Photo(models.Model):\n",
    "#####     title=models.CharField(max_length=50) #when uploading images enter the name of image\n",
    "#####     width=models.IntegerField(default=0) # automatically take in the dimension of the images \n",
    "#####    height=models.IntegerField(default=0)# automatically take in the dimension of the images\n",
    "#####    image=models.ImageField(null=False,blank=False,width_field='width',height_field='height') # pillow module will facilitate in uploading the images and storing the dimensions\n",
    "#####   timestamp=models.DateTimeField(auto_now_add=True,auto_now=False) # \n",
    "\n",
    "#####  def __unicode__(self): # web form for entering the title of the images\n",
    "######      return self.title\n",
    "###### class Meta:\n",
    "######            ordering=['-timestamp'] # this class will order or display images from recent to oldest"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# open admin.py for registering the database model for acessing the images and editing them.\n",
    "##### from .models import Photo\n",
    "##### class PhotoAdmin(admin.ModelAdmin)\n",
    "#####     list_display=['title','timestamp'] # it will show the name of the file and time of uploaded\n",
    "##### class Meta:\n",
    "#####     model=Photo\n",
    "##### admin.site.register(Photo, PhotoAdmin)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# go back to folder where manage.py is. \n",
    "#### python manage.py makemigrations\n",
    "#### python manage.py migrate"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# start the server python manage.py runserver \n",
    "###### open the broswer and go to 127.0.0.1/admin, then upload and save as many images you want to."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# open views.py and make the following changes\n",
    "#### from .models import Photo\n",
    "# #Create your views here.\n",
    "#### def photo_list(request):\n",
    "####    queryset = Photo.objects.all()\n",
    "####    context = {\n",
    "####            \"photos\" : queryset,\n",
    "####            }\n",
    "####    return render(request, \"photo.html\", context)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# CREATE A NEW FOLDER TEMPLATES WHERE YOU HAVE MANAGE.PY. GO INSIDE THE FOLDER AND CREATE A empty FILE NAMED photo.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# open the settings.py file in photos_gallery folder and insert the following line as shown below:\n",
    "###### TEMPLATES = [\n",
    "#####    {\n",
    "#####        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n",
    "#####         'DIRS': [os.path.join(BASE_DIR, 'templates')], <---this is the line you enter into this block\n",
    "#####        'APP_DIRS': True,\n",
    "#####        'OPTIONS': {\n",
    "#####            'context_processors': [\n",
    "#####                'django.template.context_processors.debug',\n",
    "#####                'django.template.context_processors.request',\n",
    "#####                'django.contrib.auth.context_processors.auth',\n",
    "#####                'django.contrib.messages.context_processors.messages',\n",
    "#####            ],\n",
    "#####        },\n",
    "#####    },\n",
    "##### ]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## open the photo.html file in editor#\n",
    "## go to browser and and open the source file of the web page and right click and open all link mentioned in between <link href=...> in seperate tabs\n",
    "### copy the address of those scripts and paste them in the <link ref=.... > in photo.html\n",
    "### substititute \"div=starter template>/div>\" with the following\n",
    "##### {% for photo in photos %}\n",
    "#####    {% if photo.image %}\n",
    "!# h1>{{photo.title}}</h1>   <img src='{{photo.image.url}}' class='image-responsive'   {% endif %}\n",
    "#####    {% endfor %}\n",
    "#### refresh the page and you will see the image\n",
    "#### go to http://127.0.0.1:8000/admin and upload images for the website\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## click on the visit site option at the right top corner to visit the site as a user."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "### for viewing a single slide in the page there is a script in the has to be changed in photo.html and slide-template.html\n",
    "### Then the model file has to be modified import deepzoom and then include the following lines.\n",
    "#### class MyImage(Photo.image):\n",
    "#####  '''\n",
    "######  Overrides UploadedImage base class.\n",
    "#####  '''\n",
    "######  pass"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "### in views.py make the following changes.\n",
    "from deepzoom.models import DeepZoom\n",
    "\n",
    "def deepzoom_view(request, passed_slug=None):\n",
    "  try:\n",
    "      _deepzoom_obj = DeepZoom.objects.get(slug=passed_slug)\n",
    "  except DeepZoom.DoesNotExist:\n",
    "      raise Http404\n",
    "  return render_to_response('deepzoom.html',\n",
    "                            {'deepzoom_obj': _deepzoom_obj},\n",
    "                            context_instance=RequestContext(request))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
