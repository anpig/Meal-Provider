# API Document
## Summary
- login
- POS Page
    - get menu
    - view order
    - add order
    - finish order
- main page (for worker)
    - get metadata of all restaurant
    - get info of a single restaurant
    - get history order
    - add review
- admin
    - add dish / upload dish picture
    - upload cover picture of a restaurant
    - get monthly report data
    - notify unpaid user
    - get all menu
    - update menu
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
> done
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
            "combo": 0,
            "price": 200,
            "rating": 4.5,
            "order_times": 0,
            "picture": "/static/dish/chicken.png",
            "available": 1
        },
        {
            "dish_id": 2,
            "name": "Hamburger",
            "description": "Delicious",
            "combo": 0,
            "price": 150,
            "rating": 4.5,
            "order_times": 0,
            "picture": "/static/dish/chicken.png",
            "available": 1
        }
    ]
}
```
### view order
> done
- endpoint: `/pos/get_order`
- only return today's order?
- method: GET
- response
```
{
    "order": 
    [
        {
            "order_id": ,
            "customer_id": ,
            "custumer_name": ,
            "order_time": "YYYY-MM-DD HH:MM:SS",
            "finish": ,
            "order_dish":
            [
                {
                    "dish_id": ,
                    "dish_name": ,
                    "price": 
                },
            ]
        },
    ]
}
```
### add order
> done
- endpoint: `/pos/add_order`
- method: POST
- request body
```
{
    "customer_id": ,
    "total_price": ,
    "dishes": 
    [
        "dish_id": ,
        "number": 
    ]
}
```
- response
```
{
    "status": "success|error",
    "error": "error_msg" // if status is error
    "order_id": // if status is success
}
```
### finish order
> done
- endpoint: `/pos/finish/<order-id>`
- method: POST
- response
```
{
    "status": "success|error",
    "error": "error_msg" // if status is error
}
```

## main page (for worker)
### get list of restaurants
> done
- endpoint: `/main/restaurant_list`
- method: GET
- response
```
{
    "restaurants":
    [
        {
            "id": ,
            "name": ,
            "rating": ,
            "picture": 
        },
    ]
}
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
        "phone": 0912345678,
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
                "combo": 0,
                "price": 200,
                "rating": 4.5,
                "order_times": 0,
                "picture": "/static/dish/chicken.png"
            },
            {
                "dish_id": 2,
                "name": "Hamburger",
                "description": "Delicious",
                "combo": 0,
                "price": 150,
                "rating": 4.5,
                "order_times": 0,
                "picture": "/static/dish/chicken.png"
            }
        ]
    }
    ```

### get history order
> done
- endpoint: `/main/history`
- method: GET
- only select the order of current month
- if the order hasn't been reviewed, set all rating to -1
- response
```
{
    "orders":
    [
        {
            "order_id": ,
            "order_time": "YYYY-MM-DD HH:MM:SS",
            "restaurant_id": ,
            "total_price": ,
            "finished": ,
            "reviewed": 1|0,
            "overall_rating": ,
            "dishes": 
            [
                {
                    "dish_id": ,
                    "dish_name": ,
                    "number": ,
                    "price": ,
                    "rating": ,
                }
            ]
        }
    ]
}
```
### add review
> done
- endpoint: `/main/review`
- method: POST
- request body
```
{
    "order_id": ,
    "overall_rating": , // 1 to 5
    "dishes_rating": 
    [
        {
            "dish_id": ,
            "rating": 
        }, 
        {
            "dish_id": ,
            "rating": 
        }
    ]
}
```
- response
```
{
    "status": "success|error",
    "error": "error_msg" // if status is error
}
```
## admin page
### add dish
> done
- endpoint: `/admin/add_dish`
- method: POST
- request body
```
{
    "restaurant_id": ,
    "name": ,
    "description": ,
    "combo": ,
    "picture_filename": , // upload picture first to get filename
    "price":
}
```
- response
```
{
    "status": "success|fail", 
    "error": // if status is fail
}
```

### upload picture of a dish
> done
- endpoint: `/admin/upload/dish`
- method: `POST`
- 看起來需要 `<input name='image'>` 才收的到 (name 要和後端收的 key 一樣)
- 這個應該一定得用表單上傳，方便的話順便送個 restaurant id (不行的話再看看可以怎麼做)
- accept file extension: png, jpg, jpeg
- response
```
{
    "status": "success|fail",
    "filename": "", // if status is success
    "error": "error msg" // if status is fail
}
```
### upload cover picture of the restaurant
> done
- endpoint: `/admin/upload/cover`
- method: `POST`
- 看起來需要 `<input name='image'>` 才收的到 (name 要和後端收的 key 一樣)
- 這個應該一定得用表單上傳，方便的話順便送個 restaurant id (不行的話再看看可以怎麼做)
- accept file extension: png, jpg, jpeg
- response
```
{
    "status": "success|fail",
    "filename": ""
}
```
### get monthly report
> to do
- endpoint: `/admin/monthly_report`
- method: `GET`
- response
```
```
### notify unpaid user
> to do
> how? To be discussed

### get all menu and reviews
> to do

### update menu
> to do
