# API Docs

> Base URL: https://boardgamebuddy-api-a3b5bf335532.herokuapp.com


| purpose | url | verb | request params | notes |
| --------| --- | ---- | -------------- | ----- |
| create a user | /users | POST | { “name”: “name”, “email”: “email@email.email” } | none |
| get all users | /users | GET | none | none  |
| get 1 user with data | /users/:id | GET | none | none | 
| edit a user’s data | /users/:id | PATCH | { “name”: “name”, “email”: “newemail@email.email” } | none | 
| delete user | /users/:id | DELETE | none | none | 
| get a user's favorites | /users/:id/favorites | GET | none |
| create/delete a user’s specific favorite boardgame | /users/:id/favorites | POST/DELETE | none | none |

## Sample Responses (happy path)
> **Create a user ⇒ POST /users**

**Request Body**

```

{
    "name": "reed",
    "email": "reed@reed.com"
}
```
**Response**
```
{
    "data": {
        "id": 3,
        "type": "user",
        "attributes": {
            "name": "reed",
            "email": "reed@reed.com"
        }
    }
}


```
> **Get a list of all users ⇒ GET /users**
```
[
    {
        "data": {
            "id": 1,
            "type": "user",
            "attributes": {
                "name": "Lane",
                "email": "lane@lane.com"
            }
        }
    },
    {
        "data": {
            "id": 2,
            "type": "user",
            "attributes": {
                "name": "noelle",
                "email": "noelle@noelle.com"
            }
        }
    },
    {
        "data": {
            "id": 3,
            "type": "user",
            "attributes": {
                "name": "reed",
                "email": "reed@reed.com"
            }
        }
    }
]

```

> **Get one users data ⇒ GET /users/2**
```
{
    "data": {
        "id": 2,
        "type": "user",
        "attributes": {
            "name": "noelle",
            "email": "noelle@noelle.com"
        }
    }
}

```

> **Edit a user ⇒ PATCH /users/2**

**Request Body**
```
{
    "name": "nowhale",
    "email": "noelle@nowhale.com"
}

```

**Response**
```
{
    "data": {
        "id": 2,
        "type": "user",
        "attributes": {
            "name": "nowhale",
            "email": "noelle@nowhale.com"
        }
    }
}
```

> **Delete a user ⇒ DELETE /users/2**
```
"User Deleted"
```

> **Get a list of all favorites for 1 user ⇒ /users/2/favorites**
```
[
    {
        "id": "210",
        "title": "Splendor",
        "image_path": "https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__original/img/Y2tUGY2nPTGd_epJYKQXPkQD8AM=/0x0/filters:format(jpeg)/pic1904079.jpg",
        "rank": "210"
    },
    {
        "id": "339",
        "title": "Above and Below",
        "image_path": "https://cf.geekdo-images.com/U0wpvRmBe65e4vwGf0Jbpg__original/img/gIlpowYQ7XzumYO0jZyVldxosBA=/0x0/filters:format(jpeg)/pic2398773.jpg",
        "rank": "339"
    },
    {
        "id": "2002",
        "title": "Taco Cat Goat Cheese Pizza",
        "image_path": "https://cf.geekdo-images.com/GHrnr-Khb0LvBU_QkrC_qA__original/img/1BR5aHWIz_v4ki-YB2IiMuS-uIs=/0x0/filters:format(png)/pic7192024.png",
        "rank": "2002"
    },
    {
        "id": "11545",
        "title": "Dominion",
        "image_path": "https://cf.geekdo-images.com/d3A6pTDGUh3xMM3aGSaEfw__original/img/_cX4OzC4S4XJBnOiOk-L8UhpN-k=/0x0/filters:format(jpeg)/pic7405387.jpg",
        "rank": "11545"
    },
    {
        "id": "103839",
        "title": "Sushi Go Party!: Sukeroku Promo",
        "image_path": "https://cf.geekdo-images.com/ftAziRJyG3S1XoVljLF1oA__original/img/68yY576G7miG3abFQYbyoll8gYI=/0x0/filters:format(png)/pic4167555.png",
        "rank": null
    }
]
```

> **Add a favorite board game to a user => POST /user/2/favorites?board_game_id=210**
```
{
    "id": 5,
    "board_game_id": 210,
    "user": 4
}
```

> **Delete a favorite board game to a user => DELETE /user/2/favorites?board_game_id=210**
```
"User Favorite Deleted"
```
