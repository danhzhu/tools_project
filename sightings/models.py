from django.db import models

class Squirrel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    unique_squirrel_id = models.CharField(max_length = 255)

    AM = 'AM'
    PM = 'PM'
    OTHER = ''

    shift_choices = ((AM, 'AM'),
                     (PM, 'PM'),
                     (OTHER, ''),
                     )

    shift = models.CharField(
              max_length = 5,
              choices = shift_choices,
              default = OTHER,)

    date = models.CharField(max_length = 255, null = True, blank = True)

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    age_choices = ((ADULT, 'Adult'),
                   (JUVENILE, 'Juvenile'),
                   (OTHER, ''),
                   )

    age = models.CharField(
            max_length = 8,
            choices = age_choices,
            default = OTHER,
            null = True,
            blank = True,)
      

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    color_choices = ((GRAY, 'Gray'),
                     (CINNAMON, 'Cinnamon'),
                     (BLACK, 'Black'),
                     (OTHER,''),
                    )
    primary_fur_color = models.CharField(
                          max_length = 8,
                          choices = color_choices,
                          default = OTHER,
                          null = True,
                          blank = True,)

    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'

    location_choices = ((GROUND, 'Ground Plane'),
                        (ABOVE, 'Above Ground'),
                        (OTHER, ''),
                       )

    location = models.CharField(
                 max_length = 15,
                 choices = location_choices,
                 default = OTHER,
                 null = True,
                 blank = True,)

    specific_location = models.CharField(max_length = 255, null = True, blank = True)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length = 255, null = True, blank = True)
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
