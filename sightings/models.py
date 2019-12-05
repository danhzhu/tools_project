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

    running = models.NullBooleanField()
    chasing = models.NullBooleanField()
    climbing = models.NullBooleanField()
    eating = models.NullBooleanField()
    foraging = models.NullBooleanField()
    other_activities = models.CharField(max_length = 255)
    kuks = models.NullBooleanField()
    quaas = models.NullBooleanField()
    moans = models.NullBooleanField()
    tail_flags = models.NullBooleanField()
    tail_twitches = models.NullBooleanField()
    approaches = models.NullBooleanField()
    indifferent = models.NullBooleanField()
    runs_from = models.NullBooleanField()

    def __str__(self):
        return self.unique_squirrel_id
