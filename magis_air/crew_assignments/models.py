from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

class CrewMember(models.Model):
    CAPTAIN = 'Captain'
    FIRST_OFFICER = 'First Officer'
    FLIGHT_ATTENDANT = 'Flight Attendant'
    FLIGHT_ENGINEER = 'Flight Engineer'
    
    CREW_ROLE_CHOICES = [
        (CAPTAIN, 'Captain'),
        (FIRST_OFFICER, 'First Officer'),
        (FLIGHT_ATTENDANT, 'Flight Attendant'),
        (FLIGHT_ENGINEER, 'Flight Engineer'),
    ]

    first_name = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True)
    crew_id = models.CharField(primary_key=True, max_length=6, unique=True)
    role = models.CharField(max_length=100, choices=CREW_ROLE_CHOICES, blank=False)  
    flight_schedules = models.ManyToManyField('flight_schedules.FlightSchedule', related_name='crew_members_in_schedule')

    def save(self, *args, **kwargs):
        if not self.crew_id:
            last_crew = CrewMember.objects.all().order_by('crew_id').last()
            if last_crew:
                last_id = int(last_crew.crew_id)
                new_id = last_id + 1
            else:
                new_id = 1
            self.crew_id = f"{new_id:06d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.crew_id} - {self.role}"

class FlightSchedule(models.Model):
    schedule_id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()
    crew_members = models.ManyToManyField(CrewMember, related_name='flight_schedule_crew_members')

    def save(self, *args, **kwargs):
        if not self.schedule_id:
            today = datetime.today()
            yy = today.strftime('%y')  
            mmdd = today.strftime('%m%d')  
            last_schedule = FlightSchedule.objects.all().order_by('-schedule_id').first()
            last_seq_num = int(last_schedule.schedule_id.split('-')[-1]) if last_schedule else 0
            new_seq_num = last_seq_num + 1
            self.schedule_id = f"SCH-{yy}{mmdd}-{str(new_seq_num).zfill(6)}"
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.schedule_id
