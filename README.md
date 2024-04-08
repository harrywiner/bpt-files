# British Pilgrimage Trust File Transfer
Downloads files from a standard sheet format and uploads to a specified Google Drive

## Setup
### Download
* First create a new Google project
* Add scope for Google Drive API and Google Sheets API
* Create a Service Account linked to the project
* Share the requisite spreadsheet with the Service Account
* Create credential json for the service account and add to the root directory of this project
  * you may have to edit line 8 in `download.py` to reflect the new filename

To use with another spreadsheet, edit line 11 in download.py to contain the ID of the spreadsheet, which you can find in the URL bar. 

Run `python3 download.py` and watch the photos flow into your computer

### Upload
* Change folder_id on line 21 of `upload.py` in order to change the Google Drive folder

Run `python3 upload.py`