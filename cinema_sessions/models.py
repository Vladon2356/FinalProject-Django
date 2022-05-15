from django.db import models
from django.urls import reverse

from movies.models import Movies
from halls.models import Halls
from users.models import CustomUser


class Sessions(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name="Movie")
    hall = models.ForeignKey(Halls, on_delete=models.CASCADE, verbose_name="Hall")
    date = models.DateField(verbose_name="Date")
    start_at = models.TimeField(verbose_name="Start at")
    end_at = models.TimeField(verbose_name="End at")
    ticket_price = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)

    def generate_tickets(self):
        for row in range(self.hall.rows):
            for column in range(self.hall.columns):

                ticket = Tickets(
                    session_id=self.pk,
                    column=column + 1,
                    row=row + 1,
                    ticket_price=self.ticket_price,
                )
                ticket.save()
        return 200

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_tickets()

    def get_absolute_url(self):
        return reverse("session_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"


class Tickets(models.Model):
    session = models.ForeignKey(
        Sessions, on_delete=models.CASCADE, related_name="tickets"
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="tickets",
        null=True,
        blank=True,
        default=None,
    )
    column = models.SmallIntegerField(null=False)
    row = models.SmallIntegerField(null=False)
    sold = models.BooleanField(default=False, null=True, blank=True)
    ticket_price = models.SmallIntegerField(null=False)
    is_active = models.BooleanField(default=True)

    @classmethod
    def buy_ticket(cls, row, column, session_id, owner_id):
        ticket = Tickets.objects.filter(
            session_id=session_id, row=row, column=column
        ).first()
        if ticket:
            if ticket.sold:
                return "Ticket already sold"
            ticket.sold = True
            ticket.owner_id = owner_id
            ticket.save()
            return "Bought"
        return "Ticket not found"

    def __str__(self):
        return f"Session :{self.session.pk}, row :{self.row}, column :{self.column}"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
