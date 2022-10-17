# ToDo

- make radio buttons into stars
- submit vote on change (get rid of submit buttons)
- fix creationId in forms

## Leftoff

- vote returns None, <https://stackoverflow.com/questions/46518908/django-forms-submit-radio-button-value-shows-up-as-none>

## Backlog

- write documentation snippet for myvotes view - model - template interaction and how  the correct vote is associated to the right creation
- create dashboard of all creations ordered by highest voted
- template cleanup (remove embedded and inline css where possible / make a css file (tailwind?))
- logging (<https://docs.djangoproject.com/en/4.1/topics/logging/>)

## Roadmap

10-16 october: Aggregations and dashboard
17-23 october: other development, logins (social auth), finishing up kanbanboard, image upload
24-30 october: styling (meeting?)
31 october - 6 november: deployment
7-13 november: extra time, documentation

### general

- logins
  - email + ticketnumber login? (is now just email and pass)

### voting

- validate actual vote in model (is number between 0 and 4 or 1 and 5?)
- staff only pages
  - overview of creations and how many votes they got in pretty dashboard (for admins / 'staff status' ? -> probably groups)
- templating
- reroute staff and admin users straight to dashboard, not votingHomepage
- make stars in star rating 'bricks'

### dashboard

- most voted
- least voted
- highest average
- lowest average
- bar chart sorted by lowest to highest average voted creations
- filters: sort by creation, sort by user, sort by time
- graphs: score of creation over time, score of user over time, ...
- (export to csv)
- most recent vote

## Maybe

- make an sql file to (create and) populate the database with dummy data (and admin account)

# Useful links

## aggregation (for votes)

<https://docs.djangoproject.com/en/4.0/topics/db/aggregation/>

# Far Future Ideas

- form for feedback -> results get shown in admin dashboard
- live feed on staff dashboard that displays 'abc just voted x stars on creation xyz'
- click on a creation to see the full description and the votes on it and stats, like average rating, minimum and maximum votes it got and how many people voted on it

## DONE

- voting models
- make page to add Creations (<https://stackoverflow.com/questions/24823294/django-accessible-url-pattern-only-for-certain-group-of-users>)
- add placeholders of current vote for each creation in the forms (<https://stackoverflow.com/questions/4270330/django-show-a-manytomanyfield-in-a-template>) -> using m2m in template (goal is to show the current vote for each creation, need to make sure each vote is linked to the correct creation_id)
- Changed Forms to ModelForms [TRIED & REVERTED]
- iterate over "creation" form fields, render a form per creation, and submit vote with that given creation.
  - figure out if you can even iterate over one specific form field.
  - doing it this way would make it so that each creation can be displayed in a list along with the amount of stars, while still using model forms
- fiddling with divs and ~ class="vote" ~ to get the stars css to work
    -try to get the stars to work with django form. I've been trying to use the "#vote_id'selector, and it aligns the stars better now, but the hovering effects don't work yet. See the test project in recently opened (/code/webdev/test) for the current progress.
- Css for the star forms works but the HMTL forms use the same vote_id's across forms which makes it so that only the forst form chagnes when voting (since all 'for' points to the same 'id'. Fix this by making the vote_id's unique.)
<https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#:~:text=%3D%22%7B%7B-,radio.id_for_label,-%7D%7D%22%3Es>
