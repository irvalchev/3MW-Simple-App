from django.db import models


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)

    class Meta:
        db_table = "sites"

    @classmethod
    def create(cls, name):
        site = cls(name=name)
        return site

    def __str__(self):
        return self.name


class SiteEntry(models.Model):
    id = models.AutoField(primary_key=True)
    site = models.ForeignKey(Site)
    date = models.DateTimeField('date')
    a_value = models.FloatField()
    b_value = models.FloatField()

    class Meta:
        db_table = "site_entries"
        verbose_name_plural = "Site entries"

    @classmethod
    def create(cls, site, date, a_value, b_value):
        entry = cls(site=site, date=date, a_value=a_value, b_value=b_value)
        return entry

    def __str__(self):
        return "Site: {}, date: {}, A: {}, B: {}".format(self.site, self.date, self.a_value, self.b_value)


