# Aggregation Notes

These are notes whil studying the django aggregation and annotation methods

## get average vote per creation

```python
# get creations and annotate them with the average vote (regardless of category)
In [51]: crs = Creation.objects.annotate(avgg=Avg("votinglist__vote"))

In [52]: crs[0]
Out[52]: <Creation: firstCreation>

In [53]: crs[0].avgg
Out[53]: 2.5

In [54]: crs[2]
Out[54]: <Creation: third creation>

In [55]: crs[2].avgg
Out[55]: 1.5

In [56]: 
```

## get average vote per category

```python

# creativity
In [60]: crsCrea = VotingList.objects.filter(category__startswith="crea").aggregate(Avg("vote"))

In [61]: print(crsCrea)
{'vote__avg': 3.2}
# impressiveness
In [62]: crsimpr = VotingList.objects.filter(category__startswith="impr").aggregate(Avg("vote"))

In [63]: print(crsimpr)
{'vote__avg': 3.5}

```

## Sort all creations by average vote

```python
In [77]: crs = Creation.objects.annotate(avgg=Avg("votinglist__vote")).order_by("avgg")

In [78]: for i in range(len(crs)):
    ...:     print(f"{crs[i].name} - {crs[i].avgg}")
    ...: 
UnvotedCreation - None
SecondCreation - 1.5
third creation - 1.5
Brents creation - 2.0
firstCreation - 2.5
adminPanelCreation - 4.0
creationSix - 5.0

In [79]: 
```
