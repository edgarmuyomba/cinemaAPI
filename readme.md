# Cinema-API
A simple api service used by the [Cinema-CLI]() tool. A tool used to download movies and series using the command line.

## Setup
1. Clone the repo
```bash
git clone <url>
```
2. Create a virtual environment in the base directory
```bash 
python3 -m venv env
```
3. Activate the virtual environment
```bash
env/scripts/activate # for windows
source env/bin/activate # for unix
```
4. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```
5. Run the server
```bash
python3 manage.py runserver
```

## Authentication
All request are governed by token-authentication and will require the authentication header in order to proceed

### Signup
`/accounts/signup/`

This expects a json object containing the username and password to be used
```json
{
    "username": "...",
    "password": "..."
}
```
If successful, it returns a json object with the user's token ( to be attached to all future requests ).
```json
{
    "message": "Account was created successfully",
    "token": "..."
}
```

### Login
`/accounts/login/`

This expects a json object containing the username and password to be used
```json
{
    "username": "...",
    "password": "..."
}
```
If successful, it returns a json object with the user's token ( to be attached to all future requests ).
```json
{
    "token": "..."
}
```

The Token is attached to the headers of all future requests using the key `Authorization` and value `Bearer <token>`

## Operations
### Latest
`/latest`

This simply returns the latest titles in the database
```json
[
    {
        "name": "Acrimony",
        "machine_name": "acrimony",
        "director": "Tyler Perry",
        "themes": "Drama, Horror, Romance",
        "year": 2018,
        "type": "movie"
    },
    {
        "name": "Severence",
        "machine_name": "severence",
        "director": "Dan Ercikson",
        "themes": "Drama, Mystery, Sci-Fi",
        "year": 2022,
        "type": "serie"
    }
]

```
### Search
`/search/?query=<query>`

This returns a list of titles with the specified *query term* in their title 
```json
[
    {
        "name": "Severence",
        "machine_name": "severence",
        "director": "Dan Ercikson",
        "themes": "Drama, Mystery, Sci-Fi",
        "year": 2022,
        "type": "serie"
    }
]
```
### Details
`/details/movie/<machine_name>`

This returns the details about the specified movie
```json
{
    "uuid": "8a46bad7-593a-4dbd-8a94-6075d63cb487",
    "name": "Acrimony",
    "machine_name": "acrimony",
    "director": "Tyler Perry",
    "cast": "Taraji P Henson, Lyriq Bent, Ajiona Alexus, Danielle Nicolet",
    "length": 150,
    "plot": "Melinda, a faithful and hardworking wife, gets tired of standing by her dishonest and unfaithful husband and begins to plan vengeance against him",
    "themes": "Drama, Horror, Romance",
    "year": 2018,
    "imdb_url": "https://www.imdb.com/title/tt6063050/",
    "file": "http://localhost:8000/mediafiles_cdn/movies/movie-1_XTUGcUf.mp4"
}
```

`/details/serie/<machine_name>`

This returns the details about the specified serie
```json
{
    "uuid": "fad0b9b3-df80-4239-b276-194747cbaa13",
    "name": "Severence",
    "machine_name": "severence",
    "director": "Dan Ercikson",
    "cast": "Adam Scott, Zach Cherry, Britt Lower",
    "length": 150,
    "plot": "Mark leads a team of office workers whose memories have been surgically divided between their work and personal lives. When a mysterious colleague appears outside of work, it begins a journey to discover the truth about their jobs",
    "themes": "Drama, Mystery, Sci-Fi",
    "year": 2022,
    "imdb_url": "https://www.imdb.com/title/tt11280740/?ref_=nv_sr_srsg_1_tt_4_nm_4_in_0_q_severence"
}
```
### Download
`/download/movie/<machine_name>`

This returns a stream used to download the movie file

`/download/serie/<machine_name>/?season=<season_number>&episode=<episode_number>`

This returns a stream used to download the specified episode of the serie
