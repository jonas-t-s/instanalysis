# instanalysis
Analyze your Instagram data with these scripts.
My goal with this repo is to occasionally add scripts when I have something interesting to add along with creating visually appealing results.

## How to get your Instagram data
1. Open a web browser
2. Login to instagram and go to your profile
3. Open your account settings
4. Go to privacy and security
5. Under data download hit "Request Download"
6. Enter your email and password
7. Wait up to 48 hours for your data (took ~5 minutes for me)

## Scripts
### Python
Scripts located in `scripts/python`

#### Who doesn't follow me back?
`<connections.json>` is a path to your connections.json file from your data download
Usage: `python no_followback.py <connections.json>`
#### Who stopped following me?
For this operation you need two JSON-Files. One file, that you downloader earlier before and one that is up to date. 
`<connections_old.json>`is the path to the out-dated `connections.json` file from your data download.
`<connections_new.json>` is the path to the newer `connections.json` file from your data download. 

Usage: 
`python missing_followers.py <connections_old.json> <connections_new.json>`

