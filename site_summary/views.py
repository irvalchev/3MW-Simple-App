from django.shortcuts import render
from site_summary.models import Site, SiteEntry


def sites(request):
    sites_list = Site.objects.all()

    context = {'sites_list': sites_list}
    return render(request, 'sites.html', context)


def site_details(request, site_id):
    site = Site.objects.filter(id=site_id)
    site_entries = None
    if site:
        site_entries = SiteEntry.objects.filter(site=site)

    context = {'site': site, 'site_entries': site_entries}
    return render(request, 'site_details.html', context)


def summary_sum(request):
    aggregation = "sum"
    all_entries = SiteEntry.objects.all()
    summary_entries = []

    for site in Site.objects.all():
        summary_entry = SiteEntry()
        summary_entry.site = site
        summary_entry.a_value = sum(entry.a_value for entry in
                                    all_entries if entry.site == site)
        summary_entry.b_value = sum(entry.b_value for entry in
                                    all_entries if entry.site == site)
        summary_entries.append(summary_entry)

    context = {'summary_entries': summary_entries, "aggregation": aggregation}
    return render(request, 'summary.html', context)


def summary_average(request):
    aggregation = "average"
    summary_entries = SiteEntry.objects.raw("""
        SELECT 0 as id, site_id, null as date, avg(a_value) a_value,
          avg(b_value) b_value
        FROM site_entries
        GROUP BY site_id""")

    context = {'summary_entries': summary_entries, "aggregation": aggregation}
    return render(request, 'summary.html', context)