from django.db import models

class Squirrel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    unique_squirrel_id = models.CharField(max_length = 255)

    AM = 'am'
    PM = 'pm'
    OTHER = ''

    shift_choices = ((AM, 'AM'),
                     (PM, 'PM'),
                     (OTHER, ''),
                     )

    shift = models.CharField(
              max_length = 5,
              choices = shift_choices,
              default = OTHER,)

    date = models.CharField(max_length = 255)

    ADULT = 'adult'
    JUVENILE = 'juvenile'

    age_choices = ((ADULT, 'Adult'),
                   (JUVENILE, 'Juvenile'),
                   (OTHER, ''),
                   )

    age = models.CharField(
            max_length = 8,
            choices = age_choices,
            default = OTHER,)

    GRAY = 'gray'
    CINNAMON = 'cinnamon'
    BLACK = 'black'

    color_choices = ((GRAY, 'Gray'),
                     (CINNAMON, 'Cinnamon'),
                     (BLACK, 'Black'),
                     (OTHER,''),
                    )
    primary_fur_color = models.CharField(
                          max_length = 8,
                          choices = color_choices,
                          default = OTHER,)

    GROUND = 'ground plane'
    ABOVE = 'above ground'

    location_choices = ((GROUND, 'Ground Plane'),
                        (ABOVE, 'Above Ground'),
                        (OTHER, ''),
                       )

    location = models.CharField(
                 max_length = 15,
                 choices = location_choices,
                 default = OTHER,)

    specific_location = models.CharField(max_length = 255)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length = 255)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
    
    def __str__(self):
        return self.unique_squirrel_id
