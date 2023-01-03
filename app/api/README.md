<h1>Documentation</h1>

## Index
* [Documentation](#api-documentation)

## Api Documentation

### /getAUTH - GET
Get cookies to login in account through session.

<h3>Parameters</h3>

| Field  | Type | Required | Value |
| ------------- | ------------- | ------------- | ------------- |
| account_code | String | No | The account id |

<h3>Result</h3>

```
{
    "account_id": 2,
    "account_name": "@mytikaccount",
    "cookies": "Your cookies here"
}
```

<br>
<strong>Note:</strong> If nothing is sended, return a random account.

<h3>Possible erros</h3>

| Error | Description |
| ------------- | ------------- |
| NOT FOUND | The account_id doesn't exists |
<br>

### /getVideo - GET
Return the location of a specific video to be upload, if not parameter is sended, return random.

<h3>Parameters</h3>

| Field | Type | Required | Value |
| ------------- | ------------- | ------------- | ------------- |
| video_file | String | No | Video to be uploaded |

<h3>Result</h3>

```
"/home/tikbot/app/api/app/database/videos/video2.mp4"
```

<strong>Note:</strong>If no parameter is sended, return a random video.

<h3>Possible erros</h3>

| Error | Description |
| ------------- | ------------- |
| EMPTY PATH | The folder where is stored video is empty |

<br>

### /putCookies - PUT
Update cookies in file profile.

<h3>Parameters</h3>

| Field | Type | Required | Value |
| ------------- | ------------- | ------------- | ------------- |
| cookies | string | Yes | The cookies to be updated |
| account_code | String | Yes | Account code to authenticate |


<h3>Result</h3>

```
null 
```

<br>
<h3>Possible erros</h3>

| Error | Description |
| ------------- | ------------- |
| FileNotFoundError | The file called doesn't exists |

<br>

### /getVideo
Return the location of a specific video to be upload, if not parameter is sended, return random.

<h3>Parameters</h3>

| Field | Type | Required | Value |
| ------------- | ------------- | ------------- | ------------- |
| video_file | String | No | find the location, otherwise return a random video |

<h3>Result</h3>
"/home/tikbot/app/api/app/database/videos/video2.mp4"


<h3>Possible erros</h3>

| Error | Description |
| ------------- | ------------- |
| EMPTY PATH | The folder where is stored video is empty |
