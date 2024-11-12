from django.db import models
import datetime
import math
import plotly
import plotly.graph_objs as go

# Create your models here.

class Voter(models.Model):
    '''
    Store/represent voter data from the recent election.
    '''
    # identification
    last_name = models.TextField()
    first_name = models.TextField()
    
    
    street_number = models.IntegerField()
    street_name = models.TextField()
    apartment_number = models.TextField()
    
    zip_code = models.TextField()
    birth_date = models.DateField()
    register_date = models.DateField()
    
    party_affiliation = models.CharField(max_length=2)
    precient_number = models.CharField(max_length=5)
    
    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()
    
    voter_score = models.IntegerField()

    '''
        def get_runners_passed_by(self):
        Return the number of runners who started after this Result 
        and finished befor it.
        start_after = Result.objects.filter(start_time_of_day__gt=self.start_time_of_day)
        passed_by = start_after.filter(finish_time_of_day__lt=self.finish_time_of_day)
        return len(passed_by)
    '''




    def create_google_map(self):
      map = "https://maps.google.com/?q=" 
      map +=  str(self.street_number) + "+" + self.street_name + "+" + str(self.apartment_number) + ", " + "Newton, Massachusetts, " + self.zip_code
      return map
    
    
    def create_previous_page(self):

      voter_score=str(self.voter_score)
      party_affiliation=self.party_affiliation
      min_birthday=str(self.min_birthday.year)
      max_birthday=str(self.max_birthday.year)
      v20state=self.v20state
      v21town=self.v21town
      v21primary=self.v21primary
      v22general=self.v22general
      v23town=self.v23town
      link = "?page={{ page_obj.previous_page_number }}"
      
      link += "&voter_score={{ v.voter_score }}"
      link += "&party_affiliation={{ v.party_affiliation }}"
      link += "&min_birthday={{ v.min_birthday }}"
      link += "&max_birthday={{ v.max_birthday }}"
      link += "&v20state={{ v.v20state }}"
      link += "&v21town={{ v.v21town }}"
      link += "&v21primary={{ v.v21primary }}"
      link += "&v22general={{ v.v22general }}"
      link += "&v23town={{ v.v23town }}"

      return link

    def create_next_page(self):

      voter_score=str(self.voter_score)
      party_affiliation=self.party_affiliation
      min_birthday=str(self.min_birthday.year)
      max_birthday=str(self.max_birthday.year)
      v20state=self.v20state
      v21town=self.v21town
      v21primary=self.v21primary
      v22general=self.v22general
      v23town=self.v23town
      link = str("?page={{ page_obj.next_page_number }}")
      
      link += str("&voter_score={{ v.voter_score }}")
      link += str("&party_affiliation={{ v.party_affiliation }}")
      link += str("&min_birthday={{ v.min_birthday }}")
      link += str("&max_birthday={{ v.max_birthday }}")
      link += str("&v20state={{ v.v20state }}")
      link += str("&v21town={{ v.v21town }}")
      link += str("&v21primary={{ v.v21primary }}")
      link += str("&v22general={{ v.v22general }}")
      link += str("&v23town={{ v.v23town }}")

      return link
      
    
    def __str__(self):
        '''Return a string representation of this model instance.'''
        if self.party_affiliation == 'D ':
          return f'{self.first_name} {self.last_name} is a proud supporter of the Democratic Party.'
        elif self.party_affiliation == 'R ':
          return f'{self.first_name} {self.last_name} is a proud supporter of the Republican Party.'
        else:
          return f'{self.first_name} {self.last_name} is a proud supporter of one of the unimportant parties.'

def load_data():
    '''Load the data records from a CSV file, create Django model instances.'''

    # delete all records:
    Voter.objects.all().delete()
    
    # open the file for reading one line at a time
    filename = '/Users/DBeye/django-three/voter_analytics/csv_files/newton_voters.csv'
    f = open(filename) # open the file for reading
    headers = f.readline() # discard the first line containing headers

    # # read a single line:
    # line = f.readline().strip()
    # fields = line.split(',')
    # print(fields)
    # for i in range(len(fields)):
    #     print(f'fields[{i}] = {fields[i]}')

    # go through the entire filem one line at a time:
    for line in f:
        
        try:
            fields = line.strip().split(',')
            # "parsing": splitting some data into filelds, assign each to variable
            # create a new instance of Voter object with this record from CSV
            
            result = Voter(
              last_name = fields[1],
              first_name = fields[2],
              street_number = fields[3],
              street_name = fields[4],
              apartment_number = fields[5],
              zip_code = fields[6],
              birth_date = fields[7],
              register_date = fields[8],
              party_affiliation = fields[9],
              precient_number = fields[10],
              v20state = fields[11],
              v21town  = fields[12],
              v21primary = fields[13],
              v22general = fields[14],
              v23town = fields[15],
              voter_score = fields[16],
                        )
            #print(f'Created result: {result}')
            result.save() # saving/commiting to the database
        
        except:
            print(f"Exception occurred: {fields}.")

    # after the loop
    print("Done.")
