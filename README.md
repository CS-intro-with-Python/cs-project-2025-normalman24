[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)
# CS_2024_project

## Description

BookHub is a web platform that allows users to share the books they have read.  
When someone finishes a book, they can upload it to the platform, including:

- Book cover  
- Author  
- Description  
- Year of publication  
- Number of pages

## Setup

Describe the steps to set up the environment and run the application. This can be a bash script or docker commands.

```
docker build -t bookhub .
docker run -p 5000:5000 bookhub
python app/main.py # The app will start at http://localhost:5000
```

## Requirements

```pip install -r requirements.txt```

## Features

Describe the main features the application performs.

The key feature is that users can add their impressions about the book.  
An impression includes:

- Text (review)
- Overall score (on a 1–10 scale)
- Period of reading (years, months, days, hours, or "less than 1 hour")

Additional planned features:

- Search by author, title, or year
- Rating aggregation

## Git

```git checkout origin main```

## Success Criteria

Describe the criteria by which the success of the project can be determined
(this will be updated in the future)

* Criteria 1

