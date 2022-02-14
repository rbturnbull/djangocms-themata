from django.db import models

class Stylesheet(models.Model):
    name = models.CharField(max_length=1023, help_text="A name for this stylesheet.")
    active = models.BooleanField(default=False, help_text="Whether or not this stylesheet ought to be linked to.")
    href = models.CharField(max_length=1023, help_text="The URL to the stylesheet.")
    static = models.BooleanField(default=False, help_text="Whether or not this stylesheet URL is relative .")
    integrity = models.CharField(max_length=1023, default="", blank=True, help_text="The Subresource Integrity (SRI) for this stylesheet (if applicable).")
    category = models.CharField(max_length=1023, default="", blank=True, help_text="A category for this stylesheet (e.g. 'bootstrap').")

    def __str__(self):
        return self.name