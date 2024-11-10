from django.db import models

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
    
    zip_code = models.IntegerField()
    birth_date = models.DateField()
    register_date = models.DateField()
    
    party_affiliation = models.CharField(max_length=1)
    
    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()
    
    voter_score = models.IntegerField()

    '''
    # gender/division
    gender = models.CharField(max_length=6)
    division = models.CharField(max_length=6)
    # result place
    place_overall = models.IntegerField()
    place_gender = models.IntegerField()
    place_division = models.IntegerField()
    # timing-related
    start_time_of_day = models.TimeField()
    finish_time_of_day = models.TimeField()
    time_finish = models.TimeField()
    time_half1 = models.TimeField()
    time_half2 = models.TimeField()
    '''

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

              zip_code = fields[6],
              birth_date = fields[7],
              register_date = fields[8],
              party_affiliation = fields[9],
              v20state = fields[11],
              v21town  = fields[12],
              v21primary = fields[13],
              v22general = fields[14],
              v23town = fields[15],
              voter_score = fields[16],
                        )
            print(f'Created result: {result}')
            result.save() # saving/commiting to the database
        
        except:
            print(f"Exception occurred: {fields}.")

    # after the loop
    print("Done.")