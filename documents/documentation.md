# Bricks and More voting Webapp

## About

This is a webapp for the Bricks and More Lego expo. It is a simple webapp that allows visitors to vote on which creations they like the most. Votes are cst by giving a creation one to five stars in three different categories. The webapp is built using the [Django](https://www.djangoproject.com/) microframework.

Django has been chosen because of the speed at which it can be developed, since the project had to be done within six to eight weeks and because it is a mature framework that handles a lot of security issues out of the box. It is also a framework that is easy to learn and has a lot of documentation.

Because the project had a very tight deadline, it has a lot of possible improvements. These are listed at "## Future plans and optimizations".

## pushing the code

when push add a tag:

git tag v1.0.0
git push --tags

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

#### Login providers

Only social auth is suported. This is done because of time constraints but also because users may use the webapp more if they can just sign in with one button and start voting straight away, instead of having to go through a register process.

Social auth is done using the Django all-auth package. Google, and Facebook are supported.
Google's auth configuration can be found at console.cloud.google.com
Facebook's auth configuration can be found at developers.facebook.com

#### groups

users can be assigned the 'helper' role. users with this role can access all the dashboard pages. These pages contain the stats page and pages to add, edit and remove creations.

### Voting forms

The voting should be as easy as possible for the visitors. After letting others test the voting, the refreshing of the page was annoying. This is why the voting is done using ajax. This way the page does not have to be refreshed after voting.

Testing also revealed that buttons should be big and easy to press.

Lastly scrolling all the way to the bottom was annoying. A search function was stickied to the top of the page so users can skip to any creation they want at all times

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

## Edition 2022

This project was first used during the 2022 expo. Around 60 people used the app. I suspect that most visitors are mostly interested in looking around a bit and not be bothered by an app while they walk around. Even though I tried to make the app as easy to use as possible.

Maybe just voting for a top three at the end of the expo or another way of voting might be used more. Other ways of making the expo more interactive might be explored too but a bit of market research beforehand might not be a bad idea.

## Future plans and optimizations

Some code is a bit messy because of time and knowledge constraints. Some things that could be improved:

- The way creations and their votes get sent to the view is a bit cluttered and might be done more effeciently
- If one person has multiple creations, a 'creator' model might be a good idea. Then stats can also be shown per creator or a small creator profile (for example name, country, list of creations, and total displayed bricks on the expo) can be made.
- a page per creation might be good too. The creations on the stats page can then be clicked to go straight to that page, containing more information about the creation.
- the way querysets are converted to lists on the stats page could be improved
- the app is styled for mobile devices but not at all for desktop.
- The 404 page is unstyled
