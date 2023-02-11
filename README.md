# Flask
# currency converter

## objective

This is a simple currency converter that converts from one currency to another

## endpoints

- `GET` `/api/to-usd` - converts from UZS (so'm) currency to USD
- `GET` `/api/to-uzs` - converts from USD to UZS (so'm) currency

## usage

- `GET` `/api/to-usd?amount=1000` - converts 1000 UZS to USD

### request
  
```http
GET /api/to-usd?amount=1000
```

parameters:

- `amount` (number) - amount of currency to convert

### response

```json
{
  "amount": 1000,
  "currency": "UZS",
  "converted": 0.11,
  "convertedCurrency": "USD"
}
```

- `GET` `/api/to-uzs?amount=1000` - converts 1000 USD to UZS (so'm)

### request
  
```http
GET /api/to-uzs?amount=1000
```

parameters:

- `amount` (number) - amount of currency to convert

### response

```json
{
  "amount": 1000,
  "currency": "USD",
  "converted": 89200,
  "convertedCurrency": "UZS"
}
```
