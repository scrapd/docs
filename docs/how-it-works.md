# How it works

The first objective of the ScrAPD tool set is to create a fully automated pipeline to collect traffic fatality data for the City of Austin.

The pipeline has 2 branches. The first branch (on the left) is for the data extracted from the APD reports and reflects the current data. The second one manages archived data provided by the City of Austin and the state of Texas via TxDoT.

The archived data are published between March and June of the following year (i.e.: CoA pusblished its 2018 data set in March 2019, TxDot dot is supposed to provide the 2018 data around June or July 2019).



![pipelines](img/scrapd-pipelines.svg)

## Current data (APD)

1. APD releases crash reports on the city website.
2. Every hour, ScrAPD checks for new reports.
3. If a new report is detected, it is extracted and stored in the `raw` data set of the current year.
4. Augmentations are generated and applied to the data set to add missing data (for instance the crash coordinates). This creates the `augmented` data set.
5. The `raw` and `augmented` data sets are stored on GitHub and data.world in `JSON` format.

## Archived data (CoA and TxDot)

1. CoA and TxDot release their data.
2. A tool is manually triggered (twice a year) to check for the new data sets.
3. The new data sets are downloaded.
4. They are processed and converted to the ScrAPD format.
5. The data sets are stored on GitHub in `JSON` format.

## FAQ

### Why do we need two pipelines?

The first reason is the difference of delay between sources. APD releases a report when a crash case is closed. CoA and TxDot release their information the year after.

The second reason is that the data sets do not contain exactly the same information and break the queries and graph generation.  That's why we have `scrapd` data sets and `archived` data sets.

### What are augmentations?

Augmentations are a mechanim to enhance data sets by adding information from other sources.

An example is the crash coordinates, which are not provided by APD. As a result, we generate an augmentation using an augmenter which converts the crash location to coordinates using the GeoCensus database.

The [augmenter specification](https://github.com/scrapd/datasets/wiki/Augmenter-Importer-specification) is defined in the [Datasets](https://github.com/scrapd/datasets) wiki.
