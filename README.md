# mathboard
## What is mathboard?
Mathboard is a... tba
## Number API
### Access
The API is accessible through a `GET request` to `mathboard-io.herokuapp.com/<number>`.
As shown, the number is part of the path. No additional `GET` data is required.
A correct input returns the number, is_prime and divisors as JSON.

Returned data for the number 42 (`mathboard-io.herokuapp.com/42`):
```
{
  "number": 42,
  "is_prime": false,
  "divisors": [
    21,
    14,
    7,
    6,
    3,
    2
  ]
}
```
### Error messages
If the number is higher than 10 million (10,000,000), an error message gets returned:
```
{
  "message": "Too large number. Must be lower than 10,000,000 (TEN MILLION)"
}
```

If the path is not a number, the `404` status code gets returned. 
