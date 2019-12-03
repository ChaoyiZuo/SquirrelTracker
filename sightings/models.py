from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    lon = models.FloatField(
        help_text = _('Longitude'),
    )
    
    lat = models.FloatField(
        help_text = _('Latitude'),
    )
    
    squirrel_id = models.CharField(
        max_length = 20,
        help_text = _('Unique Squirrel ID'),
    )

    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = (
        (PM,'PM'),
        (AM,'AM'),
    )
    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        default=AM,
    )
    
    date = models.DateField(
        help_text = _('Date'),
    )
    
    ADULT = 'adult'
    JUVENILE = 'juvenile'
    OTHER = 'other' 
    
    AGE_CHOICES = (
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
        (OTHER,'Other'),
    )
    
    age = models.CharField(
        max_length=20,
        choices=AGE_CHOICES,
        default=OTHER,
    )
    
    GRAY = 'gray'
    CINNAMON = 'cinnamon'   
    BLACK = 'black'
    
    FUR_COLOR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black' ),
        (OTHER,'Other'),
    )

    pri_fur_color = models.CharField(
        max_length=20,
        choices=FUR_COLOR_CHOICES,
        default=OTHER,
        help_text = _('Primary Fur Color')
    )
    
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    LOCATION_CHOICES = (
        (GROUND_PLANE,'Ground Plane'),
        (ABOVE_GROUND,'Above Ground'),
        (OTHER,'Other'),
    )
    
    location = models.CharField(
        max_length=50,
        choices=LOCATION_CHOICES,
        default=OTHER,
        
    )
    
    specific_location=models.CharField(
        max_length = 1000,
        help_text = _('Specific location'),
    )
    
    running = models.BooleanField(
        help_text = _('Squirrel was seen running or not'),
        default=False,
    )
    
    chasing = models.BooleanField(
        help_text = _('Squirrel was seen chasing another squirrel or not'),
        default=False,
    )
    
    climbing = models.BooleanField(
        help_text = _('Squirrel was seen climbing a tree or not'),
        default=False,
    )
    
    eating = models.BooleanField(
        help_text = _('Squirrel was seen eating or not'),
        default=False,
    )
    
    foraging = models.BooleanField(
        help_text = _('Squirrel was seen foraging for food or not'),
        default=False,
    )
    
    other_activities = models.CharField(
        max_length = 1000,
        help_text = _('Other behaviors of squirrels'),
    )
    
    kuks = models.BooleanField(
        help_text = _('Squirrel was heard kukking or not (a chirpy vocal communication)'),
        default=False,
    )
    
    quaas = models.BooleanField(
        help_text = _('Squirrel was heard Quaaing or not (an elongated vocal communication)'),
        default=False,
    )
    
    moans = models.BooleanField(
        help_text = _('Squirrel was heard Moaning or not (a high-pitched vocal communication)'),
        default=False,
    )
    
    tail_flags = models.BooleanField(
        help_text = _('Squirrel was seen flaging its tail or not'),
        default=False,
    )
    
    tail_twitches = models.BooleanField(
        help_text = _('Squirrel was seen twitching its tail or not'),
        default=False,
    )
    
    approaches = models.BooleanField(
        help_text = _('Squirrel was seen approaching human or not'),
        default=False,
    )
    
    indifferent = models.BooleanField(
        help_text = _('Squirrel was indifferent to human presence or not'),
        default=False,
    )
    
    runs_from = models.BooleanField(
        help_text = _('Squirrel was seen running from humans or not'),
        default=False,
    )
    
    def __str__(self):
        return self.squirrel_id
