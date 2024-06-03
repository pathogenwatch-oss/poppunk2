# Poppunk2 lineage assignment

## About

This tool takes a pre-built Poppunk2 cluster database and links novel genomes to the most similar cluster. Note that it
does not update or otherwise modify the clusters, and so provides a stable lineage assignment tool

## Supported species

| *Species*                  | *Creator*                                                              |    
|----------------------------|------------------------------------------------------------------------|
| _Vibrio cholerae_          | [Vibriowatch](https://vibriowatch.readthedocs.io/en/latest/index.html) |
| _Streptococcus pneumoniae_ | [GPS](https://www.pneumogen.net/gps/)                                  |

## How to build

1. NB. Update `versions.json` with the [current version of PopPUNK2 in anaconda](https://anaconda.org/bioconda/poppunk).
1. Update the scheme metadata if any files have changed.
1. Run docker build, specifying the library as a build argument, e.g for _V. cholerae_:

```
docker build --pull --rm --build-arg LIBRARY=vibriowatch -t registry.gitlab.com/cgps/pathogenwatch/analyses/poppunk2:v1.1.0-666
```

## How to add a new schema

1. Create a new set of clusters using poppunk2.
2. Place the required files in a directory - use gpsc_db as a template.
3. Create a new metadata.json file like one of the examples.

### Example scheme metadata file
```
{
  "email": "vibriowatch@sanger.ac.uk",
  "label": "VC",
  "source": "Vibriowatch clusters",
  "url": "https://vibriowatch.readthedocs.io/en/latest/mlst.html#how-to-view-poppunk-information-for-your-isolate",
  "versions": {
    "scheme": "v1"
  }
}
```

## Scheme-specific notes
### GPSC (Streptococcus pneumoniae)

- Releases are triggered on receipt of an email announcing an update from the GPS.
- Download links take the following formats:
  - https://gps-project.cog.sanger.ac.uk/GPS_v8_ref.tar.gz
  - https://gps-project.cog.sanger.ac.uk/GPS_v8_external_clusters.csv


