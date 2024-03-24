```mermaid
sequenceDiagram
    autonumber
    People ->> Lodgingdays: $80 per night for stays of 3 nights or less
    People ->> Lodgingdays: $60 per night for 4 more or nights
    People ->> Lodgingdays: $50 per night for 10 more or nights 
    Lodgingdays ->> clearningCosts:  add 12%
    clearningCosts ->> combinedCost: multiply the number of people
    combinedCost ->> totalCost: add 8%
```
