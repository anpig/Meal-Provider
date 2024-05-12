# API Document
[toc]
## login
> done
- endpoint: `/login`
- method: POST
- request body
    ```
    {
        user_account: "",
        user_password: ""
    }
    ```
- response
    ```
    {
        "outh_token": "",
        "user_identity": "restaurant|worker|admin",
        "restaurant_id": "" // returned only when user_identity is restaurant 
    }
    ```

## POS page (for restaurant)
### get menu
> to do
- endpoint: `/pos/menu`
- method: GET
- response
```
{
    "meals": 
        [
            {
                "dish_id": 1,
                "name": "Fried Chicken",
                "description": "Delicious",
                "price": 200,
                "rating": 4.5,
                "order_times": 0,
                "picture": "/static/dish/chicken.png"
            },
            {
                "dish_id": 2,
                "name": "Hamburger",
                "description": "Delicious",
                "price": 150,
                "rating": 4.5,
                "order_times": 0,
                "picture": "/static/dish/chicken.png"
            }
        ]
}
```
### add dish
> to do
- endpoint: `/pos/add_dish`
- method: POST
- request body
- response

### upload picture of a dish
> to do
- endpoint: `/pos/upload/dish`
- method: `POST`
- accept file extension: png, jpg, jpeg
- response
```
{
    "status": "success|fail",
    "filename": ""
}
```
### upload cover picture of the restaurant
> to do
- endpoint: `/pos/upload/cover`
- method: `POST`
- accept file extension: png, jpg, jpeg
- response
```
{
    "status": "success|fail",
    "filename": ""
}
```
### get review
> to do
- endpoint: `/pos/review/<id>`
- method: GET
- response
```
```

## main page (for worker)
### get metadata for all restaurant
> to do
- endpoint: `/main/all`
- method: GET
- response
```
```
### get information of single restaurant
> done
- endpoint: `/main/restaurant/<id>`
- method: GET
- response example
    ```
    {
        "id": 1,
        "restaurant": "KFC",
        "phone": 912345678,
        "picture": "/static/restaurant/kfc.png",
        "description": "Fast Food Restaurant",
        "rating": 4.3,
        "open_time": "12:00:00",
        "close_time": "22:00:00",
        "meals": 
        [
            {
                "dish_id": 1,
                "name": "Fried Chicken",
                "description": "Delicious",
                "price": 200,
                "rating": 4.5,
                "order_times": 0,
                "picture": "/static/dish/chicken.png"
            },
            {
                "dish_id": 2,
                "name": "Hamburger",
                "description": "Delicious",
                "price": 150,
                "rating": 4.5,
                "order_times": 0,
                "picture": "/static/dish/chicken.png"
            }
        ]
    }
    ```
### order a meal
> to do
- endpoint: `/main/order`
- method: POST
- request body
```
```
- response
```
```

### get history order
> to do
- endpoint: `/main/history?onAccount=1|0`
    - onAccount = 1: filter out the order that has not been paid
- method: GET
- response
```
```
### add review
> to do
- endpoint: `/main/review`
- method: POST
- request body
```
```
- response
```
```
## admin page
### get monthly report
### notify unpaid user
### get all menu and reviews
### update menu