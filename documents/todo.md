# ToDo
## Leftoff
- add placeholders of current vote for each creation in the forms (https://stackoverflow.com/questions/4270330/django-show-a-manytomanyfield-in-a-template) -> using m2m in template (goal is to show the current vote for each creation, need to make sure each vote is linked to the correct creation_id)
## Backlog
 -  logins
    - email + ticketnumber login? (is now just email and pass)
    ### voting
    - validate actual vote in model (is number between 0 and 4 or 1 and 5?)
- staff only pages
    -   overview of creations and how many votes they got in pretty dashboard (for admins / 'staff status' ? -> probably groups)
-   templating
-   reroute staff and admin users straight to dashboard, not votingHomepage
-   make stars in star rating 'bricks'

## Maybe
-   make an sql file to (create and) populate the database with dummy data (and admin account)

# Useful links
## aggregation (for votes)
https://docs.djangoproject.com/en/4.0/topics/db/aggregation/

# Far Future Ideas
- form for feedback -> results get shown in admin dashboard
- live feed on staff dashboard that displays 'xyz just voted x stars on creation xyz'
- click on a creation to see the full description and the votes on it and stats, like average rating, minimum and maximum votes it got and how many people voted on it

## DONE
-   voting models
- make page to add Creations (https://stackoverflow.com/questions/24823294/django-accessible-url-pattern-only-for-certain-group-of-users)