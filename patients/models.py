from django.db import models
from django.contrib.auth import get_user_model


# also called Ticket table
# class Patients(models.Model):
#     class Meta:
#         unique_together = ('event', 'contacts')
#
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user',
#                              error_messages={"blank": "User ref field may not be blank.",
#                                              "required": "User ref is required."})
#
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event',
#                               error_messages={"blank": "Event field may not be blank.",
#                                               "required": "Event is required."})
#     contacts = models.ForeignKey(Contacts, default=None, null=True, on_delete=models.CASCADE, related_name='contacts',
#                                  error_messages={"blank": "Contacts field may not be blank.",
#                                                  "required": "Contacts is required."})
#     # null means not open , true means accept , false means decline
#     is_accepted = models.BooleanField(default=None, null=True)
#     # total member allow to with us
#     total_person = models.IntegerField(default=1, error_messages={"blank": "Total person field may not be blank.",
#                                                                   "required": "Total person is required."})
#     # if mail has been send invited is true , so user can track witch contacts is invited
#     is_invited = models.BooleanField(default=None, null=True)
#     is_ticket = models.BooleanField(default=False, null=False)
#     # ticket id
#     token = models.CharField(max_length=30, unique=True)
#     invite_type = models.CharField(max_length=6, default=None, null=True)
#     event_templates = models.ForeignKey(EventTemplates, on_delete=models.SET_NULL, null=True, related_name='event_templates',
#                                         error_messages={"blank": "Event card field may not be blank.",
#                                                         "required": "Event card is required."})
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
