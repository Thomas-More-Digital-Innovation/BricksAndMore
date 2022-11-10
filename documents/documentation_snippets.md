# Voting

project description

- made as a learning experince MVC / Django
- could be streamlined better, code is a bit messy
- tight deadline

## Running the project

- using docker:
  - run the container:
    - ```docker compose -f .\docker-compose.dev.yml up```
    or
    - ```docker compose -f .\docker-compose.dev.yml up --build```
  - open terminal in that container:
    - ```docker compose -f docker-compose.dev.yml exec web bash```

## Project structure

### Login

#### login providers

Only social auth is suported. This is done because of time constraints but also because users may use the webapp more if they can just sign in with one button and start voting straight away, instead of having to go through a register process.

Social auth is done using the Django all-auth package. Google, and Facebook are supported.
Google's auth configuration can be found at console.cloud.google.com
Facebook's auth configuration can be found at developers.facebook.com

#### groups

users can be assigned the 'helper' role. users with this role can access all the dashboard pages. These pages contain the stats page and pages to add, edit and remove creations.

### Voting forms

- The voting forms are rendered by iterating over the creations because all the creations should have a voting form, whether or not there is a votingList, and thus a vote for that specific creation

- The voting forms can have an initial value when rendered automatically, but not when rendered manually, that's why the vote gets passed in the view too.

## Voting page

The voting page contains a list of all the creations and the vote a user has given them (if they have voted, otherwise the stars will be empty). The Voting page uses manually rendered forms. The template for this page uses a list of all the creations associated with a dictionarry of the different categories with their respective forms and votes. Schematically it looks like this:

- Creation
  - Creativity
    - form
    - vote
  - Details
    - form
    - vote
  - Impressiveness
    - form
    - vote

Or in code:

```python
formlistItems = [
  {
    'creation': <Creation: firstCreation>, 
    'categoryForms': {
      'creativity': {
        'form': <VotingForm bound=False, valid=Unknown, fields=(vote;creationId;category)>,
        'vote': 4
          },
      'details': {
        'form': <VotingForm bound=False, valid=Unknown, fields=(vote;creationId;category)>,
        'vote': None
            },
      'impressiveness': {
        'form': <VotingForm bound=False, valid=Unknown, fields=(vote;creationId;category)>,
        'vote': None
      }
    }
  }
]     
```

```python
{'creation': creation, categoryForms: {creativity: {form: form(), vote}, uniqueness: {form: form(), vote: vote}, impressiveness: {form: form(), vote: vote}
```

## Requirements.txt

psycopg2-binary
django-unfold
django-allauth
gunicorn
Pillow

## Make Tailwind update the css on changes

Tailwind is added independently because no other Node packages are needed.

<https://tailwindcss.com/blog/standalone-cli>

## Windows

 ```ps1
./tailwindcss.exe -i voting/static/voting/css/input.css  -o voting/static/voting/css/output.css --watch
 ```

## Linux

 ```shell
./tailwindcss-linux -i voting/static/voting/css/input.css -o voting/static/voting/css/output.css --watch
 ```

## Future plans and optimizations

Some code is a bit messy because of time and knowledge constraints. Some things that could be improved:

- The way creations and their votes get sent to the view is a bit cluttered and might be done more effeciently
- If one person has multiple creations, a 'creator' model might be a good idea. Then stats can also be shown per creator or a small creator profile (for example name, country, list of creations, and total displayed bricks on the expo) can be made.
- a page per creation might be good too. The creations on the stats page can then be clicked to go straight to that page, containing more information about the creation.
- the way querysets are converted to lists on the stats page could be improved
- the app is styled for mobile devices but not at all for desktop.
