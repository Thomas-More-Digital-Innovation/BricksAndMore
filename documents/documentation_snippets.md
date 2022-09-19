#
## Project structure
### Voting forms
- The voting forms are rendered by iterating over the creations because all the creations should have a voting form, whether or not there is a votingList, and thus a vote for that specific creation

- The voting forms can have an initial value when rendered automatically, but not when rendered manually, that's why the vote gets passed in the view too.