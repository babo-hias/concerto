from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import Show
from .forms import ShowForm, TXTForm
from .functions import get_table_data, get_year_chart, get_artist_chart, get_location_chart
import csv
import codecs
import pandas as pd


def index(request):
  return render(request, 'index.html')


def start(request):
  shows = Show.objects.all().values()

  df_artists = pd.DataFrame(list(shows))
  df_artists = df_artists.groupby(['artist']).count().reset_index()
  df_artists = df_artists[['artist', 'id']].sort_values(by=['id'], ascending=False)

  df_locations = pd.DataFrame(list(shows))
  df_locations = df_locations.loc[df_locations['location'] != 'Festival']
  df_locations = df_locations.groupby(['location']).count().reset_index()
  df_locations = df_locations[['location', 'id']].sort_values(by=['id'], ascending=False)
  df_locations.rename(columns={'location': 'Location', 'id': '#'}, inplace=True)

  template = loader.get_template('start.html')
  context = {
    'artists': df_artists,
    'locations': df_locations,
    'header': ['Künstler', '#']
  }
  return HttpResponse(template.render(context, request))





def table(request):
  shows = Show.objects.all().values()

  ### create data for table
  db_columns = get_table_data()

  template = loader.get_template('table.html')
  context = {
    'shows': shows,
    'header': db_columns
  }
  return HttpResponse(template.render(context, request))


def timeline(request):
    shows = Show.objects.all().values()
    df = pd.DataFrame(list(shows))

    ### create data for year-chart
    year_chart_data = get_year_chart(df)

    template = loader.get_template('timeline.html')
    context = {
        'year_labels': year_chart_data[0],
        'year_data': year_chart_data[1],
    }
    return HttpResponse(template.render(context, request))


def artists(request):
  shows = Show.objects.all().values()
  df = pd.DataFrame(list(shows))

  ### create data for artist-chart
  artist_chart_data = get_artist_chart(df)

  template = loader.get_template('artists.html')
  context = {
    'artists_labels': artist_chart_data[0],
    'artists_data': artist_chart_data[1],
  }
  return HttpResponse(template.render(context, request))


def locations(request):
  shows = Show.objects.all().values()
  df = pd.DataFrame(list(shows))

  ### create data for location-chart
  location_chart_data = get_location_chart(df)

  template = loader.get_template('locations.html')
  context = {
    'locations_labels': location_chart_data[0],
    'locations_data': location_chart_data[1]
  }
  return HttpResponse(template.render(context, request))


def add(request):
  if request.method == 'POST':
    form = ShowForm(request.POST)
    if form.is_valid():
      form.cleaned_data
      return HttpResponseRedirect(reverse('table'))

  else:
    form = ShowForm()

  return render(request, 'add.html', {'form': form})


def addrecord(request):
  member = Show(
    kategorie = request.POST['kategorie'],
    genre=request.POST['genre'],
    artist=request.POST['artist'],
    ort=request.POST['ort'],
    location=request.POST['location'],
    kosten=request.POST['kosten'],
    jahr=request.POST['jahr']
  )
  member.save()

  return HttpResponseRedirect(reverse('table'))


def add_txt(request):
  if request.method == 'POST':
    form = ShowForm(request.POST)
    if form.is_valid():
      form.cleaned_data
      return HttpResponseRedirect(reverse('table'))

  else:
    form = TXTForm()

  return render(request, 'add_txt.html', {'form': form})


def addrecords_txt(request):
  db_entries = []
  txt_file = request.FILES['txt_file']
  txt_file_reader = csv.reader(codecs.iterdecode(txt_file, 'utf-8'), delimiter='\t')

  for line in txt_file_reader:
    # Create an empty instance of your model
    obj = Show()
    # Populate the fields of the model based on the record line of your file
    obj.kategorie = line[0]
    obj.genre = line[1]
    obj.artist = line[2]
    obj.ort = line[3]
    obj.location = line[4]
    obj.kosten = line[5]
    obj.jahr = line[6]
    # Add the model to the list of objects
    db_entries.append(obj)

  # Save all objects simultaniously, instead of saving for each line
  Show.objects.bulk_create(db_entries)

  return HttpResponseRedirect(reverse('table'))


def delete(request):
  shows = Show.objects.all().values()
  template = loader.get_template('delete.html')
  context = {
    'shows': shows,
  }
  return HttpResponse(template.render(context, request))


def deleted(request, id):
  show_to_delete = Show.objects.get(id=id)
  show_to_delete.delete()
  return HttpResponseRedirect(reverse('table'))