[![Maintainability](https://api.codeclimate.com/v1/badges/305bbb9febbad4211861/maintainability)](https://codeclimate.com/github/NgachaIan/Challenge2-API/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/305bbb9febbad4211861/test_coverage)](https://codeclimate.com/github/NgachaIan/Challenge2-API/test_coverage)

[![Build Status](https://travis-ci.com/NgachaIan/Challenge2-API.svg?branch=develop)](https://travis-ci.com/NgachaIan/Challenge2-API)

[![Coverage Status](https://coveralls.io/repos/github/NgachaIan/Challenge2-API/badge.svg?branch=master)](https://coveralls.io/github/NgachaIan/Challenge2-API?branch=master)

# Challenge2-API
Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered.

The project is managed using [Pivotal Tracker](https://www.pivotaltracker.com). You can view the board [here](https://www.pivotaltracker.com/n/projects/2235836).

The repo for the frontend is available at [Questioner](https://github.com/NgachaIan/Questioner)

## Prerequisites

- [VS Code](https://code.visualstudio.com)
- [Python 3.6](https://www.python.org)
- [Postman](https://www.getpostman.com)

## Installation

- Clone the repo
```
$ git clone https://github.com/NgachaIan/Challenge2-API
```

- CD into the folder
```
$ cd Challenge2-API
```

- Create a virtual environment
```
$ python3 -m venv venv
```

- Activate the virtual environment
```
$ source venv/bin/activate
```

- Install dependencies
```
$ pip install -r requirements.txt
```

- Run the app 
```
$ python run.py or flask run
```

## API Endpoints (version1)

| **HTTP METHOD** | **URI** | **ACTION** |
| --- | --- | --- |
| **POST** | `/api/version1/user/post` | Register a new user |
| **GET** | `/api/version1/user/get` | Fetch a registered user |
| **POST** | `/api/version1/meetup/post` | Create a meetup |
| **GET** | `/api/version1/meetup/get` | Fetch all meetups |
| **POST** | `/api/version1/question/post` | Post a question to a specific meetup |
| **PATCH** | `/api/version1/question/upvote/<int:question_id>` | Upvote a question |
| **PATCH** | `/api/version1/question/downvote/<int:question_id>` | Downvote a question |
| **GET** | `/api/version1/question/get` | Fetch all questions for a meetup |
