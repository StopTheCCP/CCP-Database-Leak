# CCP-Database-Leak
**Simple goal**: Translate the CCP leaked database into English and make all the data available, unfiltered, for everyone to see.

**Note**: GitHub has placed a bandwidth cap on the repository's CSV (LFS) files.  **As a result we have now moved our repository to [Codeberg.org](https://codeberg.org/StopTheCCP/CCP-Database-Leak).**

## Input Data:
- Original Data Source (removed): ~~https://gitlab.com/shanghai-ccp-member-db/shanghai-ccp-member-db/-/blob/master/shanghai-ccp-member.csv~~
- Mirror: https://git.rip/botayhard/shanghai-ccp-member-db/-/raw/master/shanghai-ccp-member.csv
- This repository: https://codeberg.org/StopTheCCP/CCP-Database-Leak/raw/branch/main/Data/shanghai-ccp-member.csv

## Pre-Processing:
1) The [leaked csv file](https://gitlab.com/shanghai-ccp-member-db/shanghai-ccp-member-db/-/blob/master/shanghai-ccp-member.csv) should be in the `/Data` directory.
2) Then `SplitFileIntoParts.py` is run to split the file into 40 separate files of 50,000 lines.

## Processing:
Run `TranslateCSVPartials.py` with python3.  You can change the input file range to target specific files to process.

Examples:
```
inputFileRange = [*range(1, 41)]  # all files from 1-40
inputFileRange = [1,2]  # specific files
```

## Post-Processing:
- TBD: Reference `MergeFiles.py`

## Status:
### 2020-12-18
- Migrated repository to Codeberg.org
- A few individuals have been running `TranslateCSVPartials.py` against the google translate service.  Google has been heavily throttling us.
So far we are only about halfway done.

## Future work:
### Analysis and Reporting
