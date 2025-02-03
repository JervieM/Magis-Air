from django.db import models
from crew_assignments.models import CrewMember
from flight_routes.models import Flight

class FlightSchedule(models.Model):
    schedule_id = models.CharField(primary_key=True, max_length=17, unique=True)
    date = models.DateField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    crew_members = models.ManyToManyField(CrewMember, related_name="schedules_for_member")  

    def save(self, *args, **kwargs):
        YY = self.date.strftime('%y') 
        MM = self.date.strftime('%m')
        DD = self.date.strftime('%d')
        last_schedule = FlightSchedule.objects.filter(date=self.date).order_by('-schedule_id').first()
        last_seq_num = int(last_schedule.schedule_id.split('-')[-1]) if last_schedule else 0
        new_seq_num = last_seq_num + 1
        self.schedule_id = f"SCH-{YY}{MM}{DD}-{str(new_seq_num).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.schedule_id} - {self.flight.flight_id} on {self.date}"