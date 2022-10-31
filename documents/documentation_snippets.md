#

## Project structure

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

## Make Tailwind update the css on changes

<https://tailwindcss.com/blog/standalone-cli>

## Windows

 ```ps1
./tailwindcss.exe -i voting/static/voting/css/input.css  -o voting/static/voting/css/output.css --watch
 ```

## Linux

 ```shell
./tailwindcss-linux -i voting/static/voting/css/input.css -o voting/static/voting/css/output.css --watch
 ```
